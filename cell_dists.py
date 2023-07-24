import pandas as pd
from scipy.spatial import distance
import math
import sys
import os

filename = sys.argv[1]

df = pd.read_excel(filename)
df.head()

num_cells = df['Cell #'].count()
num_bv = df['BV #'].count()

output = []
# loop through all the cells
for i in range(num_cells):
    cell_x = df['X1'][i]
    cell_y = df['Y1'][i]
    cell = (cell_x, cell_y)

    closest_dist = math.inf
    closest_bv = -1

    # loop through all the blood vessels
    for j in range(num_bv):
        bv_x = df['X'][j] 
        bv_y = df['Y'][j]
        bv = (bv_x, bv_y)
        # see if distance is the smallest so far
        dist = round(distance.euclidean(cell, bv), 3)
        if dist < closest_dist:
            closest_dist = dist
            closest_bv = j+1  # +1 to accont for 1-indexed list of blood vessels
    output.append([i+1, closest_bv, closest_dist])


# put results into a CSV file and save it
columns = ["Cell #", "BV #", "Dist"]
output_df = pd.DataFrame(output, columns=columns)

output_filename = filename[:filename.find('.')].strip() + '_output.csv'
output_df.to_csv(output_filename, index=False)
print("SUCCESS: Saved results to '{os.getcwd()}/{output_filename}'")
