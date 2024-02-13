import pandas as pd
import pyproj

df = pd.read_csv("baumauswahl.csv", sep=';')
df["RECHTSWERT"] = df["RECHTSWERT"].str.replace(",", ".").astype(float)
df["HOCHWERT"] = df["HOCHWERT"].str.replace(",", ".").astype(float)

# Define the ETRS89 and WGS84 coordinate systems
etrs89 = pyproj.Proj(proj='utm', zone=32, ellps='GRS80', units='m')
wgs84 = pyproj.Proj(proj='latlong', datum='WGS84', ellps='WGS84')

# Function to convert ETRS89 coordinates to latitude and longitude
def convert_to_lat_lon(row):
    longitude, latitude = pyproj.transform(etrs89, wgs84, row['RECHTSWERT'], row['HOCHWERT'])
    return pd.Series({'Latitude': latitude, 'Longitude': longitude})

# Apply the conversion function to the DataFrame
df[['Latitude', 'Longitude']] = df.apply(convert_to_lat_lon, axis=1)

# Write the DataFrame to a CSV file
output_csv_path = "output_coordinates.csv"
df.to_csv(output_csv_path, index=False)

print(f"DataFrame written to {output_csv_path}")
