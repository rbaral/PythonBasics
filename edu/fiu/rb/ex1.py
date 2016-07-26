__author__ = 'rbaral'

# Create list baseball
baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Import the numpy package as np
import numpy as np

# Create a Numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print (np_baseball.dtype)
# height is available as a regular list
height = [65,68,72,73]

# Create a Numpy array from height: np_height
np_height = np.array(height)

# Print out np_height
print (np_height)

# Convert np_height to m: np_height_m
np_height_m = np_height *0.0254

# Print np_height_m
print (np_height_m)