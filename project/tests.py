import os
import unittest
from unittest.mock import patch
import importlib
import pandas as pd
import sqlite3

pipeline = importlib.import_module("pipeline")
data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')

class TestPipelineComponents(unittest.TestCase):
  agri_file_path = os.path.join(data_dir, 'Agrofood_co2_emission.csv')
  temp_file_path = os.path.join(data_dir, 'GlobalLandTemperaturesByCountry.csv')
  expected_agri_columns = ['Area', 'Year', 'Savanna fires', 'Forest fires', 'Crop Residues', 'Rice Cultivation', 'Drained organic soils (CO2)', 'Pesticides Manufacturing', 'Food Transport', 'Forestland', 'Net Forest conversion', 'Food Household Consumption', 'Food Retail', 'On-farm Electricity Use', 'Food Packaging', 'Agrifood Systems Waste Disposal', 'Food Processing', 'Fertilizers Manufacturing', 'IPPU', 'Manure applied to Soils', 'Manure left on Pasture', 'Manure Management', 'Fires in organic soils', 'Fires in humid tropical forests', 'On-farm energy use', 'Rural population', 'Urban population', 'Total Population - Male', 'Total Population - Female', 'total_emission', 'Average Temperature °C']
  expected_temp_columns = ['dt', 'AverageTemperature', 'AverageTemperatureUncertainty', 'Country']
  dbname = "pipeline"
  dbpath = os.path.join(data_dir, f"{dbname}.db")

  def setUp(self):
    if os.path.exists(self.dbpath):
      os.remove(self.dbpath)

  def tearDown(self):
    if os.path.exists(self.dbpath):
      os.remove(self.dbpath)

  def test_extraction_data(self):
    """Test data extraction from CSV files"""
    agri_data = pd.read_csv(self.agri_file_path)
    temp_data = pd.read_csv(self.temp_file_path)

    self.assertFalse(agri_data.empty, msg="Agrofood CO2 emission data should not be empty")
    self.assertFalse(temp_data.empty, "Global land temperatures data should not be empty")
    self.assertListEqual(list(agri_data.columns), self.expected_agri_columns,
               msg="Agrofood CO2 emission data columns do not match expected columns")
    self.assertListEqual(list(temp_data.columns), self.expected_temp_columns,
               msg="Global land temperatures data columns do not match expected columns")

  def test_database_creation(self):
    """Test database creation and table structure"""
    pipeline.main()

    self.assertTrue(os.path.exists(self.dbpath), "Database file should exist before running the test.")
    
    with sqlite3.connect(self.dbpath) as conn:
      agri_table = pd.read_sql_query("SELECT * FROM agri", conn)
      temp_table = pd.read_sql_query("SELECT * FROM temp", conn)

      self.assertFalse(agri_table.empty, "The agri table should not be empty in the database")
      self.assertFalse(temp_table.empty, "The temp table should not be empty in the database")
      self.assertListEqual(list(agri_table.columns), self.expected_agri_columns,
             msg="The columns in the agri table do not match the expected columns")
      self.assertListEqual(list(temp_table.columns), self.expected_temp_columns,
                 msg="The columns in the temp table do not match the expected columns")

if __name__ == "__main__":
  unittest.main()
