import pandas as pd
import numpy as np

# =============================================================================
# Data Frame Summary
# =============================================================================

# show info about colum type and the frame

DF1.info()

# Syntax: DataFrame.info(verbose=None, buf=None, max_cols=None, memory_usage=None, null_counts=None)

# verbose : Whether to print the full summary
# null_counts : Whether to show the non-null counts

# =============================================================================
# Data Frame heads or tails
# =============================================================================

# shows x number of rows

DF1.head()
DF1.tail()

# given a number of rows to display
# head = upper
# tail = lower

# =============================================================================
# Data Frame .describe
# =============================================================================

# shows basic stats for each column in the data set (min, max, count, mean etc)

DF1.decribe()

# =============================================================================
# Data Frame .dtypes
# =============================================================================

# shows data types of the columns in the data set

DF1.dtypes

# =============================================================================
# Data Frame .shape
# =============================================================================
# number of rows and columns

DF1.shape

# =============================================================================
# Data Frame .value_counts()
# =============================================================================
# counts the occurrence of an value in an column

DF1["Col 1"].value_counts()

# =============================================================================
# Data Frame .compare_values()
# =============================================================================
# compares values in a column between 2 seperate data sets

compare_values(DF1["Col 1"], DF2["Col 2"])

# =============================================================================
# Check division between Y vars
# =============================================================================


df2["COL 2 Y"].value_counts()
