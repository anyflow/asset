CREATE DATABASE IF NOT EXISTS asset;
CREATE SCHEMA IF NOT EXISTS krx;
CREATE TABLE IF NOT EXISTS krx.company (
  code VARCHAR(20),
  campany VARCHAR(40),
  last_date DATE,
  PRIMARY KEY (code)
);
CREATE TABLE IF NOT EXISTS krx.daily_price (
  code VARCHAR(20),
  date DATE,
  open BIGINT,
  high BIGINT,
  low BIGINT,
  close BIGINT,
  diff BIGINT,
  volume BIGINT,
  PRIMARY KEY (code, date)
);
SELECT
  *
from
  krx.company;
