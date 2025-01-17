# SaCLN-WindField-Correction
## Overview
This project implemented experiments related to the manuscript "Sea Ice Drift Prediction Facilitated by Intelligently Corrected Sea Surface Wind Forecast Fields". The project aims to correct sea surface wind field forecasts, which is crucial for accurate sea ice drift prediction. By capturing the spatial correlations and temporal characteristics from sea surface wind field sequences, the SaCLN generates corrected wind fields that approximate the reanalysis wind fields.
## Structure

constants.py: It contains constants used throughout the project. It defines parameters such as data dimensions and directory paths for saving models and data.

main.py: The main entry point of the project. It sets up the training environment, loads necessary modules, and starts the training process.

test.py: The loaded model is used to predict the test data, and the error between the predicted results and the real data is calculated.

## Install requirements
Install the required packages: tensorflow 1.15, numpy, glob, matplotlib packages.

## Data
The wind fields are downloaded from the NCEP-GFS archive https://rda.ucar.edu/datasets/ and the ECMWF-ERA5 archive https://cds.climate.copernicus.eu/datasets.

## Usage
To run the project, follow these steps:

1. Ensure you have the necessary dependencies installed.

2. Modify the constants.py file to set the correct paths for your data and model directories.

3. Run the main.py script to start the training process.

## About the Author
Qing Xu, College of Oceanography and Space Informatics, China University of Petroleum (East China)

Contact: xuqing_upc@163.com
