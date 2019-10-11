#!/bin/bash

cd cleaning
python3 date_clean.py
python3 gold_missing_dates.py
cd ../aggregation
python3 bitcoin_agg.py
python3 crimes_agg.py
cd ../cleaning
python3 final_clean.py
cd ../aggregation
python3 combine.py
