import pandas as pd

# =============================================================================
# Dataframe.replace()
# =============================================================================
#  Syntax: DataFrame.replace(to_replace=None, value=None, inplace=False, limit=None, regex=False, method=’pad’, axis=None)

# can use reg exp on strings

DF1.replace(to_replace = "Old value", value = "New Value")

DF1.replace(to_replace = ["Old value 1", "Old Value 2"], value = "New Value")

# only for selected column

DF1["Col 1"] = DF1["Col 1"].replace(["Old Value 1", "Old Value 2"], "New Value 1")

