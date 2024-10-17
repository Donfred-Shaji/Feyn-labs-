import pandas as pd

# Load the dataset
target = pd.read_csv("target.csv")

# Count occurrences of each category in the 'Like' column
like_counts = target['Like'].value_counts()

# Reverse the order of the counts
reversed_like_counts = like_counts[::-1]

# Display the reversed counts
print(reversed_like_counts)
target['Like_numeric'] = pd.to_numeric(target['Like'], errors='coerce')

# Create a new column 'Like.n'
target['Like.n'] = 6 - target['Like_numeric']

# Count occurrences of each value in 'Like.n'
like_n_counts = target['Like.n'].value_counts()

# Display the counts
print(like_n_counts)