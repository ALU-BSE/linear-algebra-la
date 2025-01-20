import pandas as pd
import numpy as np

# Load data
# data = pd.read_csv('path/to/data')

# Example arrays
Prices = [[300, 500],
          [1000, 120.85]]

Array2 = [200, 100]

# Calculate the result
Ans = []
# (300*200 + 500*100) as an example calculation

for i in range(len(Prices)):
    row_sum = 0
    for j in range(len(Prices[0])):
        #  THE MISSING LOGIC 
        row_sum+= Prices[i][j]*Array2[j]

    Ans.append(row_sum)
        


print(Ans)
