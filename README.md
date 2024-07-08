# Hospital Data Cleaning Program

This Python program processes hospital data from a CSV file, cleans it, combines relevant columns, and prepares it for export to Excel with hyperlinks.

## Overview

This program reads NHS hospital data from a CSV file, performs data cleaning and transformation tasks, and saves the processed data into an Excel file. Key functionalities include:

- Combining address fields (`Address1`, `Address2`, `Address3`) into a single `Address1` field.
- Combining city (`City`) and county (`County`) into a single `Address2` field.
- Formatting latitude (`Latitude`) and longitude (`Longitude`) into a `Coordinates` field.
- Cleaning the `Fax` data to remove unnecessary commas.
- Converting `Website` URLs into clickable hyperlinks in the Excel output.

## Dependencies

- Python 3.x
- pandas
- openpyxl

## Data source
Kaggle: https://www.kaggle.com/datasets/manchunhui/uk-hospitals 

