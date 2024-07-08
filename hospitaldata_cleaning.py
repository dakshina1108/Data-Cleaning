import pandas as pd

hospital_data = pd.read_csv(r'.\Hospital.csv')
#Understanding the data
print(hospital_data.head())

# Combining Address1, Address2, and Address3 into Address1
hospital_data['Address1'] = hospital_data[['Address1', 'Address2', 'Address3']].apply(
    lambda x: ', '.join(x.dropna().astype(str)), axis=1)

# Combining City and County into Address2
hospital_data['Address2'] = hospital_data[['City', 'County']].apply(
    lambda x: ', '.join(x.dropna().astype(str)), axis=1)

# Combining Latitude and Longitude into Coordinates
hospital_data['Coordinates'] = hospital_data[['Latitude', 'Longitude']].apply(
    lambda x: f"({x['Latitude']}, {x['Longitude']})", axis=1)

# Cleaning the Fax data
hospital_data['Fax'] = hospital_data['Fax,,,'].str.replace(',,,', '').str.replace(',,', '')

# Drop unnecessary columns
columns_to_drop = ['Address3', 'City', 'County', 'Latitude', 'Longitude', 'Fax,,,']
hospital_data.drop(columns=columns_to_drop, inplace=True)

# Preparing data for Excel output with hyperlinks
hospital_data['Website'] = hospital_data['Website'].apply(lambda x: f'=HYPERLINK("{x}", "{x}")')

# Saving to Excel with hyperlinks
hospital_data.to_excel('hospital_data_with_links.xlsx', index=False)
