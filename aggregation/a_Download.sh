#!/bin/bash
mkdir ../raw-data/
cd ../raw-data
wget https://data.fcc.gov/download/measuring-broadband-america/2018/data-raw-2018-sept.tar.gz
wget https://data.fcc.gov/download/measuring-broadband-america/2018/data-raw-2018-oct.tar.gz
wget https://data.fcc.gov/download/measuring-broadband-america/2018/data-raw-2018-dec.tar.gz
wget https://data.fcc.gov/download/measuring-broadband-america/2019/data-raw-2019-jan.tar.gz
wget https://data.fcc.gov/download/measuring-broadband-america/2019/data-raw-2019-feb.tar.gz
wget https://data.fcc.gov/download/measuring-broadband-america/2019/data-raw-2019-mar.tar.gz
wget https://data.fcc.gov/download/measuring-broadband-america/2019/data-raw-2019-apr.tar.gz
wget https://data.fcc.gov/download/measuring-broadband-america/2019/data-raw-2019-may.tar.gz
wget https://data.fcc.gov/download/measuring-broadband-america/2019/data-raw-2019-jun.tar.gz
wget https://data.fcc.gov/download/measuring-broadband-america/2019/data-raw-2019-jul.tar.gz
wget https://data.fcc.gov/download/measuring-broadband-america/2019/data-raw-2019-aug.tar.gz
wget https://data.fcc.gov/download/measuring-broadband-america/2019/data-raw-2019-sept.tar.gz
wget https://data.fcc.gov/download/measuring-broadband-america/2019/data-raw-2019-oct.tar.gz
wget https://data.fcc.gov/download/measuring-broadband-america/2019/data-raw-2019-nov.tar.gz
wget https://data.fcc.gov/download/measuring-broadband-america/2019/data-raw-2019-dec.tar.gz

tar -xzf *.tar.gz