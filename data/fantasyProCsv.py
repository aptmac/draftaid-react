# Credit to: https://github.com/jayjzheng/draftaid-react/blob/5a99a0b9f4cac4e4ccbfb36c86ecee19640969b3/data/fantasyProCsv.py

import json
import re
import requests
from bs4 import BeautifulSoup


url = "https://www.fantasypros.com/nfl/rankings/"

standard = "consensus-cheatsheets.php"
ppr = "ppr-cheatsheets.php"
halfppr = "half-point-ppr-cheatsheets.php"

formats = [standard, ppr, halfppr]
names = ["standard", "ppr", "halfppr"]

def get_data(format):
    players = []
    r = requests.get(url + format)

    soup = BeautifulSoup(r.text, 'html.parser')
    #headings = [th.get_text() for th in soup.find_all("th")[:10] if 'style' in th.attrs]

    rows = soup.find("tbody").find_all("tr")
    tier = '1'
    for row in rows:
        player = {}
        text = row.get_text().replace(u'\xa0', u'').split("\n")[:11]
        if "Tier" in text[0]:
            tier = text[0].replace('Tier ', '')
        if len(text) > 1:
            if "google" in text[2]:
                continue
            rank = text[0]
            position = text[3]
            bye = text[4]
            best = text[5]
            worst = text[6]
            average = text[7]
            stddev = text[8]
            adp = text[9]
            vsadp = text[10]
            if 'DST' not in position:
                name, team = text[1].strip().rsplit(None, 1)
                name = re.match(r'(.*)[A-Z]\.', name).group(1)
            else:
                name = text[1].strip()
                name = re.match('.*\)', name).group()
                team = ''
            player['position'] = position
            player['name'] = name
            player['team'] = team
            player['rank'] = rank
            player['tier'] = tier
            player['bye_week'] = bye
            player['best_rank'] = best
            player['worst_rank'] = worst
            player['average_rank'] = average
            player['std_dev'] = stddev
            player['adp'] = adp
            player['vs_adp'] = vsadp
        if player:
            players.append(player)
    return players

if __name__ == "__main__":
    for i in range(len(formats)):
        name = names[i]
        data = formats[i]
        players = {}
        players['format'] = name
        players['rankings'] = get_data(data)
        with open('rankings_'+name+'.json', 'w') as outfile:
            json.dump(players, outfile)