import pandas as pd

# =============================================================================
# Change column names
# =============================================================================

#Option 1: Pas a new list of new columns via the .columns functions

df1.columns = ["New name 1", "New name 2", "New name 3"]

#Option 2: Rename existing column names via the .rename function
        # Use "inplace = TRUE" to change the names in place

df1.rename(columns = { "Old 1" : "New 1", "Old 2" : "New 2", "Old 3", "New 3"}, inplace = TRUE)


