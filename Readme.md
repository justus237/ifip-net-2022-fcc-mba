# An Eight Years Perspective on the Internet Broadband Infrastructure in the USA
## Justus Fries, Trinh Viet Doan, Rohit Gupta, Vaibhav Bajpai
## IFIP Networking Conference 2022
# Metrics covered by the scripts
Download (HTTP GET MT (6)), Latency (UDP Latency (6)), Latency under (downstream) load (Download Ping)
# Requirements
```sqlite3``` and ```python3``` with ```pandas, seaborn``` and ```basemap```
# Workflow
The scripts and files in ```./aggregation/``` are used to get the Measuring Broadband America dataset from the FCC (```a_Download.sh```). The raw data is then transferred into an sqlite3 database in the ```./raw-data/``` directory (```a_FIRST_add_raw_data.sh```). The raw data is aggregated and written to ```.csv``` files in the ```./agg-data/``` directory (```a_SECOND_agg_newest_data_csv.sh```), after which it can be transferred to the database used for analysis ```./agg-data/agg_fcc.db``` (```a_THIRD_add_newest_agg_csv_data_to_db.sh```). The validated data contains unit profiles for each probe and location data on them (2017 does not have location data, see ```ab_extract_unit_data.ipynb``` and ```ab_extract_locations_data.sql```). The scripts and notebooks here are meant to be example scripts and only extract limited data. They have to be customized/changed to cover whole dataset in the paper. The Form 477 analysis requires census and the actual Form 477 data, both of which are publicly available. They have to be downloaded and extracted into the ```./form-477/``` directory.

# Notes on analysis notebooks
```UDP-latency-CDF``` and ```HTTP-GET-MT-CDF``` contain code at the bottom of the notebooks that is used for excluding probes from the carrying forward of probe (unit profile) information into 2019. The resulting probe IDs excluded from 2019 are hardcoded in each notebook, and it is not required to run these notebooks before any others. The Form 477 notebook is required to be run before the notebooks producing heatmaps. Other notebooks are entirely independent from each other.
