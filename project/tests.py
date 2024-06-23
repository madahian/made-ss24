import os
import unittest
import importlib
import pandas as pd
import sqlite3

# Load the pipeline module dynamically
pipeline = importlib.import_module("pipeline")

# Define the data directory path
data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')

class PipelineTestSuite(unittest.TestCase):
    # Define file paths and expected columns
    file_paths = {
        'agri': os.path.join(data_dir, 'Agrofood_co2_emission.csv'),
        'temp': os.path.join(data_dir, 'GlobalLandTemperaturesByCountry.csv')
    }
    
    expected_columns = {
        'agri': ['Area', 'Year', 'Savanna fires', 'Forest fires', 'Crop Residues', 'Rice Cultivation', 
                 'Drained organic soils (CO2)', 'Pesticides Manufacturing', 'Food Transport', 'Forestland', 
                 'Net Forest conversion', 'Food Household Consumption', 'Food Retail', 'On-farm Electricity Use', 
                 'Food Packaging', 'Agrifood Systems Waste Disposal', 'Food Processing', 'Fertilizers Manufacturing', 
                 'IPPU', 'Manure applied to Soils', 'Manure left on Pasture', 'Manure Management', 'Fires in organic soils', 
                 'Fires in humid tropical forests', 'On-farm energy use', 'Rural population', 'Urban population', 
                 'Total Population - Male', 'Total Population - Female', 'total_emission', 'Average Temperature °C'],
        'temp': ['dt', 'AverageTemperature', 'AverageTemperatureUncertainty', 'Country']
    }

    # Define database name and path
    db_name = "pipeline"
    db_path = os.path.join(data_dir, f"{db_name}.db")

    def setUp(self):
        """Setup test environment"""
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    # def tearDown(self):
    #     """Clean up after tests"""
    #     if os.path.exists(self.db_path):
    #         os.remove(self.db_path)

    def test_data_loading(self):
        """Test loading of data from CSV files"""
        for key, file_path in self.file_paths.items():
            with self.subTest(file=key):
                data = pd.read_csv(file_path)
                self.assertFalse(data.empty, msg=f"{key} data should not be empty")
                self.assertListEqual(list(data.columns), self.expected_columns[key], 
                                     msg=f"{key} data columns do not match expected columns")

    def test_database_integrity(self):
        """Test the creation of the database and the integrity of its tables"""
        # Run the pipeline to create the database
        pipeline.main()

        # Ensure the database file exists
        self.assertTrue(os.path.exists(self.db_path), "Database file should exist after running the pipeline.")

        # Check the content of the database tables
        with sqlite3.connect(self.db_path) as conn:
            for key in self.expected_columns.keys():
                with self.subTest(table=key):
                    table_data = pd.read_sql_query(f"SELECT * FROM {key}", conn)
                    self.assertFalse(table_data.empty, msg=f"The {key} table should not be empty in the database")
                    self.assertListEqual(list(table_data.columns), self.expected_columns[key], 
                                         msg=f"The columns in the {key} table do not match the expected columns")

if __name__ == "__main__":
    unittest.main()