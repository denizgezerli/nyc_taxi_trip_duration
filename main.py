import pandas as pd
import numpy as np
import ipdb
# Load the training dataset
train_df = pd.read_csv('data/train.csv', on_bad_lines='skip')

# Print the first 5 rows of the dataset
print(train_df.head())
