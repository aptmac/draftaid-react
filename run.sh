#!/bin/bash
cd data;
python fantasyProCsv.py;
cd ../;
npm install;
npm run build;
npm start;
