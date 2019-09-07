import pandas as pd

# =============================================================================
# Selecting data using Labels (Column Headings)
# =============================================================================

# subset the complete column to a new var
SUB1 = DF1["Col1"]
SUB2 = DF1["Col1, Col2, Col3"]
SUB3 = DF1["Col1:Col3"]

# same as

SUB1 = DF1.Col1

# =============================================================================
# Slicing Subsets of Rows
# =============================================================================

#DF [ "Start : Stop"]

DF1[0] # first row
DF1[1:3] # rows 2 to 4

# =============================================================================
# Slicing Subsets of Rows and Columns
# =============================================================================

# loc is primarily label based indexing. Integers may be used but they are interpreted as a label.
DF1.loc[[Row Item1, Row Item2], ["Col1", "Col2"]]


# iloc is primarily integer based indexing
# iloc[row slicing, column slicing]
DF1.iloc[0:3, 1:4]


# =============================================================================
# Subsetting Data using Criteria
# =============================================================================

# subset based on cell content within column

Sub1 = DF1["Col 1 " == "Exp1"]
Sub1 = DF1.Col1 < 12

Subs3 = DF1[SUB1] # use expression var as filter

# use logical expressions for subset rules and als expanding search

DF1[("Col 1 " == "Exp1") & ("Col2" => 12)]

# & = And
# | = Or
# ~ = Not

#search from an list

DF1[DF1["Col1"].isin([LIST])]









