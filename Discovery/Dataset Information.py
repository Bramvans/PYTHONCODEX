import pandas as pd

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

