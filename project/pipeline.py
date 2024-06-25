import os
import sqlite3
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def download_and_unzip_kaggle_dataset(api, dataset, download_path):
    response = api.dataset_download_files(dataset, path=download_path, unzip=True)
    print(f"Downloaded and unzipped dataset {dataset}")
    return response

def create_database_from_csv(csv_file_path, table_name, connection):
    df = pd.read_csv(csv_file_path)
    df.to_sql(table_name, connection, if_exists="replace", index=False)
    print(f"Data from {csv_file_path} written to table {table_name}")

def main():
    # Authenticate Kaggle API
    api = KaggleApi()
    api.authenticate()

    # Define datasets and download directory
    datasets = [
        'alessandrolobello/agri-food-co2-emission-dataset-forecasting-ml',
        'berkeleyearth/climate-change-earth-surface-temperature-data'
    ]
    data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')

    try:
        # Your existing code here
        # Download and unzip datasets
        for dataset in datasets:
            download_and_unzip_kaggle_dataset(api, dataset, data_dir)
        logger.info(f"CSV files downloaded to: {data_dir}")
        # Define CSV file paths
        csv_files = {
            'agri': os.path.join(data_dir, 'Agrofood_co2_emission.csv'),
            'temp': os.path.join(data_dir, 'GlobalLandTemperaturesByCountry.csv')
        }
        for csv_file in csv_files.values():
            logger.info(f"CSV file exists: {os.path.exists(csv_file)}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        raise
    
    # Create SQLite database and save data from CSV files
    db_path = os.path.join(data_dir, 'pipeline.db')
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    try:
        with sqlite3.connect(db_path) as connection:
            for table_name, csv_file_path in csv_files.items():
                create_database_from_csv(csv_file_path, table_name, connection)
            print("Database saved in 'data' directory successfully.")
        
        # # Remove CSV files after successful database creation
        # for csv_file_path in csv_files.values():
        #     os.remove(csv_file_path)
        #     print(f"Removed file {csv_file_path}")

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()