CREATE TABLE locations2012 (
    geog_type varchar(100) DEFAULT NULL,
    geog_id int(20) DEFAULT NULL,
    population real DEFAULT NULL,
    latitude real DEFAULT NULL,
    longitude real DEFAULT NULL,
    unitid int(11) DEFAULT NULL
);

CREATE TABLE locations2013 (
    geog_type varchar(100) DEFAULT NULL,
    geog_id int(20) DEFAULT NULL,
    population real DEFAULT NULL,
    latitude real DEFAULT NULL,
    longitude real DEFAULT NULL,
    unitid int(11) DEFAULT NULL
);

CREATE TABLE locations2014 (
    geog_type varchar(100) DEFAULT NULL,
    geog_id int(20) DEFAULT NULL,
    population real DEFAULT NULL,
    latitude real DEFAULT NULL,
    longitude real DEFAULT NULL,
    unitid int(11) DEFAULT NULL
);

CREATE TABLE locations2015 (
    geog_type varchar(100) DEFAULT NULL,
    geog_id int(20) DEFAULT NULL,
    population real DEFAULT NULL,
    latitude real DEFAULT NULL,
    longitude real DEFAULT NULL,
    unitid int(11) DEFAULT NULL
);

CREATE TABLE locations2016 (
    geog_type varchar(100) DEFAULT NULL,
    geog_id int(20) DEFAULT NULL,
    population real DEFAULT NULL,
    latitude real DEFAULT NULL,
    longitude real DEFAULT NULL,
    unitid int(11) DEFAULT NULL
);

CREATE TABLE locations2017 (
    geog_type varchar(100) DEFAULT NULL,
    geog_id int(20) DEFAULT NULL,
    population real DEFAULT NULL,
    latitude real DEFAULT NULL,
    longitude real DEFAULT NULL,
    unitid int(11) DEFAULT NULL
);

CREATE TABLE locations2018 (
    geog_type varchar(100) DEFAULT NULL,
    geog_id int(20) DEFAULT NULL,
    population real DEFAULT NULL,
    latitude real DEFAULT NULL,
    longitude real DEFAULT NULL,
    unitid int(11) DEFAULT NULL
);

.mode csv


.import "../validated_data/2012/unit-id-census-block-group-apr-2012.csv" locations2012
.import "../validated_data/2013/unit-id-census-block-group-sept-2012.csv" locations2013
.import "../validated_data/2014/unit-id-census-block-group-sept-2013.csv" locations2014
.import "../validated_data/2015/unit-id-census-block-group-sept-2014.csv" locations2015
.import "../validated_data/2016/UnitID-census-block-sept2015.csv" locations2016

.import "|tail -n +2 ../validated_data/2018/UnitID-census-block-sept2017.csv" locations2018

