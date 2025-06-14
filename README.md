# Weather Data Ingestion Project

## Overview
This project ingests real-time weather data from OpenWeatherMap API, stores it in raw and processed formats, and loads it into a PostgreSQL database.

## Project Structure
- `ingest.py`: Pulls data from API and saves as JSON & CSV
- `validate.py`: Validates processed CSV
- `load_to_db.py`: Loads CSV data into PostgreSQL
- `config/config.json`: Configuration file with API key

## Setup
1. Add your OpenWeatherMap API key to `config/config.json`
2. Run `python ingest.py` to collect data
3. Run `python validate.py <path_to_csv>`
4. Run `python load_to_db.py` to load into PostgreSQL

## Automation
Use cron or Apache Airflow for automation.

## Requirements
- Python 3
- pandas, requests, psycopg2
