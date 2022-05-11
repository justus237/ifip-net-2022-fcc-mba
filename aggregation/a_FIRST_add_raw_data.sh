#!/bin/sh

echo "Starting Download Ping"
sqlite3 raw-data/databases/curr_dlping.db ".read curr_dlping.sql" ""
echo "Finished Download Ping; Starting HTTP GET MT"
sqlite3 raw-data/databases/curr_httpgetmt.db ".read curr_httpgetmt.sql" ""
echo "Finished HTTP GET MT; Starting HTTP GET MT 6"
sqlite3 raw-data/databases/curr_httpgetmt6.db ".read curr_httpgetmt6.sql" ""
echo "Finished HTTP GET MT 6; Starting UDP latency"
sqlite3 raw-data/databases/curr_udplatency.db ".read curr_udplatency.sql" ""
echo "Finished UDP latency; Starting UDP latency 6"
sqlite3 raw-data/databases/curr_udplatency6.db ".read curr_udplatency6.sql" ""
echo "Finished UDP latency 6"
