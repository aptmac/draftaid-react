# Draft Aid (Fantasy Football) - DEPRICATED

### Note: I will not be updating this repo any more. Instead I've migrated this code to it's new home at: https://github.com/aptmac/ffdojo

This repository contains a modified version of Jay Zheng's draftaid-react project, which can be found at: [https://github.com/jayjzheng/draftaid-react](https://github.com/jayjzheng/draftaid-react)

## Installation and usage
I have included a script that can be used for easy local deployment. In the top level of this project, use the command `./run.sh` from the terminal to have the project install, build, and run all at once. When built, the application will be served at [http://localhost:3000](http://localhost:3000).

If you are interested in external web hosting, please see Jay Zheng's original repos for more details. This is a react-based project, so the commands required to run this application are:

- Install: `npm install`
- Build: `npm run build`
- Run: `npm start`

Note that you will need to have npm installed and configured on your machine.

## Differences from the original application

Jay Zheng's original application is great out of the box. However, I wanted to tweak a few things before using it for my own fantasy draft purposes.

- Removed the 'reset' button (resetting the page can be done by refreshing)
- Added undrafted lists for kickers and team defenses
- Moved the master list of undrafted players to be inbetween the lists of players by position and drafted players
- Thanks to kellenproctor, the application can be used with a local .json file pulled from fantasy pros, which allows for ~400 data points. This makes it possible to view kickers and defense, as well as showing more overall depth. The code to fetch the remote .json from the draftaid API is commented out on `DraftBoard.js`, but can be easily uncommented for future use.

## Kudos

Thank you to [Jay Zheng](https://github.com/jayjzheng) for creating this application, and elevating my draft results for (hopefully) many upcoming Fantasy Football seasons to come.

Kudos to kellenproctor for their PRs to draftaid-react! I was able to salvage the `fantasyProCsv.py` file to use a local player data .json file for the application. This allowed for an extra ~200 data items for the application, which made it possible to track kickers and more defense options.


