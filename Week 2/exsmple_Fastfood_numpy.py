import numpy as np

# Load data from CSV
city, country, lat, long, post = np.genfromtxt(
    'FastFoodRestaurants.csv',
    delimiter=',',
    usecols=(1, 2, 4, 5, 7),
    dtype=str,
    unpack=True,
    skip_header=1,
    invalid_raise=False,
    encoding='utf-8'
)

# Print loaded values
print(city)
print(country)
print(lat)
print(long)
print(post)

#  float conversion :
lat_float = []
long_float = []

for la, lo in zip(lat, long):
    try:
        lat_val = float(la)
        long_val = float(lo)
        lat_float.append(lat_val)
        long_float.append(long_val)
    except ValueError:
        continue  # skip if conversion fails

lat_float = np.array(lat_float)
long_float = np.array(long_float)

# Perform basic arithmetic operations
addition = long_float + lat_float
subtraction = long_float - lat_float
multiplication = long_float * lat_float
division = long_float / lat_float

# Print results
print(" Fast Food Restaurants - Long + Lat (Addition):", addition)
print(" Fast Food Restaurants - Long - Lat (Subtraction):", subtraction)
print(" Fast Food Restaurants - Long * Lat (Multiplication):", multiplication)
print(" Fast Food Restaurants - Long / Lat (Division):", division)

#  Replace stats part with long_float (not long)
print("FastFoodRestaurant Longitude mean: ", np.mean(long_float))
print("FastFoodRestaurant Longitude average: ", np.average(long_float))
print("FastFoodRestaurant Longitude std: ", np.std(long_float))
print("FastFoodRestaurant Longitude median: ", np.median(long_float))
print("FastFoodRestaurant Longitude percentile - 25: ", np.percentile(long_float, 25))
print("FastFoodRestaurant Longitude percentile - 75: ", np.percentile(long_float, 75))
print("FastFoodRestaurant Longitude percentile - 3: ", np.percentile(long_float, 3))
print("FastFoodRestaurant Longitude min: ", np.min(long_float))
print("FastFoodRestaurant Longitude max: ", np.max(long_float))
