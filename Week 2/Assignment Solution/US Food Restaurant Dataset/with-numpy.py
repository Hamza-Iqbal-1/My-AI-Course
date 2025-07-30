'''D:\\My-AI-Course\\Week 2\\Assignment Solution\\US Food Restaurant Dataset\\FastFoodRestaurants.csv'''

import numpy as np

# Select only usable columns from CSV
# We'll create a simplified CSV with selected columns only
# Column order: name, latitude, longitude, postalCode, province
# File: simplified_restaurant_data.csv

# Load the data using NumPy
name, latitude, longitude, postal_code, province = np.genfromtxt(
    'D:\\My-AI-Course\\Week 2\\Assignment Solution\\US Food Restaurant Dataset\\FastFoodRestaurants.csv', 
    delimiter=',',
    skip_header=1,
    dtype=str,        # All data loaded as string first
    unpack=True,
    encoding='utf-8',
    autostrip=True
)

# Convert latitude and longitude to float
latitude = latitude.astype(float)
longitude = longitude.astype(float)

# Example operations
print("Total entries:", len(latitude))
print("Mean Latitude:", np.mean(latitude))
print("Mean Longitude:", np.mean(longitude))
print("Latitude Std Dev:", np.std(latitude))

# Basic arithmetic
print("\nLatitude + Longitude:")
print(latitude + longitude)

print("\nLatitude - Longitude:")
print(latitude - longitude)

# Trigonometric calculations (in radians)
print("\nSin of Latitude:")
print(np.sin(np.radians(latitude)))

print("\nCos of Longitude:")
print(np.cos(np.radians(longitude)))

# Normalization example
lat_norm = (latitude - np.min(latitude)) / (np.max(latitude) - np.min(latitude))
print("\nNormalized Latitude:")
print(lat_norm)

# Combine lat-long into 2D array
latlong = np.array([latitude, longitude])
print("\nShape of latlong array:", latlong.shape)
print("First [lat, long]:", latlong[:, 0])

# Flatten
flat = latlong.reshape(1, latlong.size)
print("\nFlattened latlong:", flat)

# Iterating with nditer
print("\nIterating through latlong:")
for x in np.nditer(latlong):
    print(x)
