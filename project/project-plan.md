# Project Plan

## Title
<!-- Give your project a short title. -->
Correlation Analysis between Agricultural CO2 Emissions and Average Temperature Changes

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
1. How do agricultural CO2 emissions correlate with average temperature changes in various countries between the years 2000 and 2010?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
Understanding the relationship between agricultural CO2 emissions and climate change is crucial for developing sustainable practices and mitigating climate change impacts. This project aims to analyze the correlation between total agricultural CO2 emissions and average temperature changes in various countries from 2000 to 2010.

We will use two comprehensive datasets for this analysis. The first dataset, constructed by merging data from the Food and Agriculture Organization (FAO) and the IPCC, provides detailed information on CO2 emissions from various agricultural activities. The second dataset, sourced from the Berkeley Earth Surface Temperature Study, offers long-term global temperature data, allowing us to study temperature trends by country.

By leveraging statistical and data processing techniques, we aim to uncover significant relationships between agricultural emissions and temperature changes. The findings will provide valuable insights for policymakers and researchers working on climate action and sustainable agricultural practices.

## Datasources

<!-- Describe each datasource you plan to use in a section. Use the prefix "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Agri-food CO2 emission dataset
* Data URL: [https://www.kaggle.com/datasets/alessandrolobello/agri-food-co2-emission-dataset-forecasting-ml](https://www.kaggle.com/datasets/alessandrolobello/agri-food-co2-emission-dataset-forecasting-ml)
* Data Type: CSV

#### Description:
The agricultural CO2 emission dataset has been constructed by merging and reprocessing approximately a dozen individual datasets from the Food and Agriculture Organization (FAO) and data from IPCC. These datasets were cleaned, preprocessed, and merged together to create a comprehensive and cohesive dataset for analysis and forecasting purposes.

The dataset describes CO2 emissions related to agri-food, which amount to approximately 62% of the global annual emissions. It includes features such as emissions from savanna fires, forest fires, crop residues, rice cultivation, and more. This dataset plays a crucial role in understanding and monitoring the impact of agricultural activities on CO2 emissions.

### Datasource2: Climate Change - Earth Surface Temperature Data
* Data URL: [https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data?select=GlobalTemperatures.csv](https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data?select=GlobalTemperatures.csv)
* Selected Data: GlobalLandTemperaturesByCountry.csv
* Data Type: CSV

#### Description:
This dataset is sourced from the Berkeley Earth Surface Temperature Study and combines 1.6 billion temperature reports from 16 pre-existing archives. It provides global land and ocean temperature data, including average temperatures, maximum and minimum temperatures, and their uncertainties.

The dataset includes several files:
- Global Land and Ocean-and-Land Temperatures (GlobalTemperatures.csv)
- Global Average Land Temperature by Country (GlobalLandTemperaturesByCountry.csv)
- Global Average Land Temperature by State (GlobalLandTemperaturesByState.csv)
- Global Land Temperatures By Major City (GlobalLandTemperaturesByMajorCity.csv)
- Global Land Temperatures By City (GlobalLandTemperaturesByCity.csv)

This dataset allows us to analyze temperature trends by country and correlate them with agricultural CO2 emissions.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Data Collection and Cleaning [#1][i1]
2. Exploratory Data Analysis [#2][i2]
3. Data Integration [#3][i3]
4. Statistical Correlation Analysis [#4][i4]
5. Report Writing and Visualization [#5][i5]

[i1]: https://github.com/madahian/made-ss24/issues/1
[i2]: https://github.com/madahian/made-ss24/issues/2
[i3]: https://github.com/madahian/made-ss24/issues/3
[i4]: https://github.com/madahian/made-ss24/issues/4
[i5]: https://github.com/madahian/made-ss24/issues/5
