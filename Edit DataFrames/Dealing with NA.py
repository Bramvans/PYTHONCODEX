import pandas as pd
import numpy as np

# =============================================================================
# DropNA
# =============================================================================
# remove rows containing NA data

DF1.dropna(inplace = TRUE)

# =============================================================================
# Impute NA
# =============================================================================
# replace NA value wih column statistic

DF1.fillna(DF1.mean(), inplace=True)

DF1["COl 1"].fillna(DF1["Col 1"].mean)

# =============================================================================
# Remove rows with NA Values on COL 1
# =============================================================================

df1 = df0
df1.head()

df1["COL 1 X"].isna().sum()


df1 = df0.dropna(subset=["COL 1 X"])


df1["COL 1 X"].isna().sum()