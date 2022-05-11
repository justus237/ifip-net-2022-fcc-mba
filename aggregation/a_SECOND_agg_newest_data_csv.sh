#!/bin/sh

#Aggregates from raw db files from each database file of a metric
#Aggregates to a csv file per month per metric
echo "Starting Download Ping"
nohup python3 agg_dlping.py > dlping.log &

echo "Starting HTTP GET"
nohup python3 agg_httpgetmt.py > getmt.log & 

echo "Starting HTTP GET 6"
nohup python3 agg_httpgetmt6.py > getmt6.log &

echo "Starting UDP Latency"
nohup python3 agg_udplatency.py > udplat.log &

echo "Starting UDP Latency 6"
nohup python3 agg_udplatency6.py > udplat6.log &

echo "Finished"

