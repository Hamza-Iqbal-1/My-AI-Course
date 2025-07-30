import numpy as np
data = np.genfromtxt('D:\\My-AI-Course\\Week 2\\FastFoodRestaurants.csv',usecols=(1),delimiter=',',unpack=True,dtype=None,skip_header=1,encoding='utf-8',)
print(data)