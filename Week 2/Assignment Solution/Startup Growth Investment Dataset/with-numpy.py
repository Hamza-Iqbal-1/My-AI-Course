# startup_growth_investment_data.csv
import numpy as np

# Load data
ids, investment, lat, long = np.genfromtxt('D:\\My-AI-Course\\Week 2\\Assignment Solution\\Startup Growth Investment Dataset\\startup_growth_investment_data.csv',
    delimiter=',',
    usecols=(0, 2, 4, 5),
    unpack=True,
    skip_header=1,
    dtype=None,
    encoding='utf-8'
)

print(ids)
print(investment)
print(long)
print(lat)

# Investment statistics
print("Investment mean: " , np.mean(investment))
print("Investment average: " , np.average(investment))
print("Investment std: " , np.std(investment))
print("Investment median: " , np.median(investment))
print("Investment percentile - 25: " , np.percentile(investment, 25))
print("Investment percentile - 75: " , np.percentile(investment, 75))
print("Investment percentile - 3: " , np.percentile(investment, 3))
print("Investment min : " , np.min(investment))
print("Investment max : " , np.max(investment))

# Math operations on investment
print("Investment square: " , np.square(investment))
print("Investment sqrt: " , np.sqrt(investment))
# Avoid power with large values
print("Investment abs: " , np.abs(investment))

# Basic arithmetic on coordinates
addition = long + lat
subtraction = long - lat
multiplication = long * lat
division = long / lat

print(" Long - lat - Addition:", addition)
print(" Long - lat - Subtraction:", subtraction)
print(" Long - lat - Multiplication:", multiplication)
print(" Long - lat - Division:", division)

# Trigonometric Functions
investmentPie = (investment/np.pi) + 1
sine_values = np.sin(investmentPie)
cosine_values = np.cos(investmentPie)
tangent_values = np.tan(investmentPie)

print("Investment - div - pi - Sine:", sine_values)
print("Investment - div - pi - Cosine:", cosine_values)
print("Investment - div - pi - Tangent:", tangent_values)
print("Investment - div - pi - Exponential:", np.exp(investmentPie))

# Logarithms
log_array = np.log(investmentPie)
log10_array = np.log10(investmentPie)

print("Investment - Natural log:", log_array)
print("Investment - Base-10 log:", log10_array)

# Hyperbolic functions
sinh_values = np.sinh(investmentPie)
print("Investment - sinh:", sinh_values)

cosh_values = np.cosh(investmentPie)
print("Investment - cosh:", cosh_values)

tanh_values = np.tanh(investmentPie)
print("Investment - tanh:", tanh_values)

asinh_values = np.arcsinh(investmentPie)
print("Investment - arcsinh:", asinh_values)

# Filter invalid values for acosh (input must be >= 1)
safe_acosh_input = investmentPie[investmentPie >= 1]
acosh_values = np.arccosh(safe_acosh_input)
print("Investment - arccosh:", acosh_values)

# 2D array from long and lat
D2LongLat = np.array([long, lat])

print("2D Array Long + Lat:", D2LongLat)
print("Dimension:", D2LongLat.ndim)
print("Total elements:", D2LongLat.size)
print("Shape:", D2LongLat.shape)
print("Data type:", D2LongLat.dtype)

# Splicing
D2LongLatSlice = D2LongLat[:1, :5]
print("Slice [:1, :5]:", D2LongLatSlice)
D2LongLatSlice2 = D2LongLat[:1, 4:15:4]
print("Slice [:1, 4:15:4]:", D2LongLatSlice2)

# Indexing
if D2LongLatSlice.shape[1] > 1:
    print("Index [0,1]:", D2LongLatSlice[0, 1])
if D2LongLatSlice2.shape[1] > 2:
    print("Index [0,2]:", D2LongLatSlice2[0, 2])

# Iteration
for elem in np.nditer(D2LongLat):
    print("Element:", elem)

for index, elem in np.ndenumerate(D2LongLat):
    print("Index:", index, "Element:", elem)

# Reshape to 1 x N
reshaped = np.reshape(D2LongLat, (1, D2LongLat.size))
print("Reshaped 1 x N:", reshaped)
print("Size:", reshaped.size)
print("ndim:", reshaped.ndim)
print("shape:", reshaped.shape)
