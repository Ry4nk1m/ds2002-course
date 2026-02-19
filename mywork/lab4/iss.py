#!/usr/bin/env python3
"""
ETL Pipeline for ISS Tracking
"""

import requests
import pandas as pd
import sys
import logging
import os
import time

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

def extract():
    """
    Extracts ISS location data from the Open Notify API.
    Returns:
        dict: The parsed JSON data record, or None if error.
    """
    url = "http://api.open-notify.org/iss-now.json"
    logging.info(f"Attempting to fetch data from {url}")
    
    try:
        response = requests.get(url)
        response.raise_for_status() 
        data = response.json()
        logging.info("Successfully extracted data.")
        return data
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching data: {e}")
        return None

def transform(data):
    """
    Transforms the raw JSON data into a pandas DataFrame.
    Converts UNIX timestamp to readable format.
    
    Args:
        data (dict): Raw JSON data from API.
        
    Returns:
        pd.DataFrame: A single-row DataFrame with cleaned data.
    """
    logging.info("Transforming data...")
    
    try:
        position = data['iss_position']
        timestamp = data['timestamp']
        
        record = {
            'timestamp': timestamp,
            'latitude': position['latitude'],
            'longitude': position['longitude']
        }
        
        df = pd.DataFrame([record])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
        
        logging.info("Data transformation complete.")
        return df
    except KeyError as e:
        logging.error(f"Missing key in data during transformation: {e}")
        return pd.DataFrame()

def load(df, filename):
    """
    Loads the transformed data into a CSV file.
    Appends to the file if it exists, creates it if it doesn't.
    
    Args:
        df (pd.DataFrame): The data to save.
        filename (str): The path to the CSV file.
    """
    if df.empty:
        logging.warning("No data to load.")
        return

    logging.info(f"Loading data into {filename}...")
    
    file_exists = os.path.exists(filename)
    
    try:
        df.to_csv(filename, mode='a', header=not file_exists, index=False)
        logging.info("Data loaded successfully.")
    except Exception as e:
        logging.error(f"Failed to write to file: {e}")

def main():
    """
    Main function to orchestrate the ETL pipeline.
    """
    if len(sys.argv) < 2:
        logging.error("Usage: python3 iss.py <output_csv_filename>")
        sys.exit(1)
        
    filename = sys.argv[1]
    
    json_data = extract()
    
    if json_data:
        clean_data = transform(json_data)
        
        load(clean_data, filename)

if __name__ == "__main__":
    main()