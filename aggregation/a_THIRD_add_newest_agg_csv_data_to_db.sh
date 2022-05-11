#!/bin/sh

#Takes the csv files generated from aggregation step and writes them into the master db file

echo "Starting Download Ping"
sqlite3 ../agg-data/agg_fcc.db ".read agg_dlping.sql" ""

echo "Finished Download Ping; Starting HTTP GET"
sqlite3 ../agg-data/agg_fcc.db ".read agg_httpgetmt.sql" ""

echo "Finished HTTP GET; Starting HTTP GET 6"
sqlite3 ../agg-data/agg_fcc.db ".read agg_httpgetmt6.sql" ""

echo "Finished HTTP GET 6; Starting UDP Latency"
sqlite3 ../agg-data/agg_fcc.db ".read agg_udplatency.sql" ""

echo "Finished UDP Latency; Starting UDP Latency 6"
sqlite3 ../agg-data/agg_fcc.db ".read agg_udplatency6.sql" ""

echo "Finished UDP Latency 6"
