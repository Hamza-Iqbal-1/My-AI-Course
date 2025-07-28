import numpy as np

brokered_by , price , acre_lot , city , house_size = np.genfromtxt('D:\\My-AI-Course\\Week 2\\RealEstate-USA.csv', delimiter=',', usecols=(0,2,5,7,10),unpack=True,dtype=None,encoding='utf-8',skip_header=1)

print(brokered_by)
print(price)
print(acre_lot)
print(city)
print(house_size)

# RealEstate-USA price  - statistics operations
print("RealEstate-USA Price mean: " , np.mean(price))
print("RealEstate-USA Price median: " , np.median(price))
print("RealEstate-USA Price average: " , np.average(price))
print("RealEstate-USA Price std: " , np.std(price))
print("RealEstate-USA Price percentile - 25: " , np.percentile(price,25))
print("RealEstate-USA Price percentile  - 75: " , np.percentile(price,75))
print("RealEstate-USA Price percentile  - 3: " , np.percentile(price,3))
print("RealEstate-USA Price min : " , np.min(price))
print("RealEstate-USA Price max : " , np.max(price))


# RealEstate-USA house_size  - statistics operations
print("RealEstate-USA house_size mean: " , np.mean(house_size))
print("RealEstate-USA house_size median: " , np.median(house_size))
print("RealEstate-USA house_size average: " , np.average(house_size))
print("RealEstate-USA house_size std: " , np.std(house_size))
print("RealEstate-USA house_size percentile - 25: " , np.percentile(house_size,25))
print("RealEstate-USA house_size percentile  - 75: " , np.percentile(house_size,75))
print("RealEstate-USA house_size percentile  - 3: " , np.percentile(house_size,3))
print("RealEstate-USA house_size min : " , np.min(house_size))
print("RealEstate-USA house_size max : " , np.max(house_size))

# Clean NaNs (if any)
mask = ~np.isnan(price) & ~np.isnan(house_size)
price_clean = price[mask]
house_size_clean = house_size[mask]

# Perform operations
add_op = price_clean + house_size_clean
add_func = np.add(price_clean, house_size_clean)

sub_op = price_clean - house_size_clean
sub_func = np.subtract(price_clean, house_size_clean)

mul_op = price_clean * house_size_clean
mul_func = np.multiply(price_clean, house_size_clean)

# Show results
print("\nAddition (+):", add_op[:5])
print("Addition (np.add):", add_func[:5])

print("\nSubtraction (-):", sub_op[:5])
print("Subtraction (np.subtract):", sub_func[:5])

print("\nMultiplication (*):", mul_op[:5])
print("Multiplication (np.multiply):", mul_func[:5])

# Create a “2D array” based on array of [array of “price”] and [array of “house_size”]

combined_array = np.column_stack((price_clean, house_size_clean))
print("2D array of price and house_size:")
print(combined_array)

# Create a “3D array” based on array of [array of “house_size”] and [array of “price”] and [array of “acre_lot”] 

# First Combine into 2D
two_d = np.column_stack((house_size, price, acre_lot))
# Now Convert to 3D
three_d = two_d[:, np.newaxis, :]
print("3D Array:\n", three_d)
print("Shape:", three_d.shape)

# Iterate the array - of [array of “price”] With function  of "np.nditer()"

for val in np.nditer(price):
    print(val)

# Iterate the array - of [array of “price”] With function  of "np.ndenumerate()"

for index, value in np.ndenumerate(price):
    print(f"Index: {index}, Value: {value}")

# Use 7 common properties of array - of [array of ““price”]

print("1. Dimensions (ndim):", price.ndim)
print("2. Shape:", price.shape)
print("3. Size:", price.size)
print("4. Data Type (dtype):", price.dtype)
print("5. Item Size (bytes):", price.itemsize)
print("6. Total Bytes (nbytes):", price.nbytes)
print("7. Type of Object:", type(price))

# Slice array of [Question 5, as - “2D array” based on array of [array of  “price”] and [array of “house_size”] ] Row : from 2nd  value to 8th value and Column: from 3rd value to 5th value 

# we only have 2 columns (index 0 and 1), so: Column index 2 or higher doesn’t exist. To proceed as you requested (Columns 2–4 or 3–5), we must first add more columns
# Assuming price_clean and house_size_clean are defined and same length
col3 = price_clean * 0.1     # dummy extra column
col4 = house_size_clean * 0.01
col5 = price_clean + house_size_clean
# 2D array with 5 columns now
combined_array = np.column_stack((price_clean, house_size_clean, col3, col4, col5))

# 2nd  value to 8th value and Column: from 3rd value to 5th value 
slice_10 = combined_array[0:3, 1:4]
print("Slice 10 (Rows 1–3, Columns 2–4):")
print(slice_10)

# slice_10 = combined_array[0:3, 1:4] print("Slice 10 (Rows 1–3, Columns 2–4):") and print(slice_10)

slice_11 = combined_array[1:8, 2:5]
print("Slice 11 (Rows 2–8, Columns 3–5):")
print(slice_11)

# 12.  Learn – what are geometric operation in NUMPY. np.sin , np.cos apply common 6 to - “2D array” based on array of [array of  “price”] and [array of “house_size”] , created in Question  5.

# Apply geometric (trigonometric) functions
print("\nnp.sin:")
print(np.sin(combined_array))

print("\nnp.cos:")
print(np.cos(combined_array))

print("\nnp.tan:")
print(np.tan(combined_array))

print("\nnp.arcsin (values must be in range [-1, 1]):")
# To avoid domain errors, we scale array to within -1 to 1
scaled_array = combined_array / np.max(np.abs(combined_array))
print(np.arcsin(scaled_array))

print("\nnp.arccos (values must be in range [-1, 1]):")
print(np.arccos(scaled_array))

print("\nnp.arctan:")
print(np.arctan(combined_array))