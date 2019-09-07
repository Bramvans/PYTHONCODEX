import pandas as pd

# =============================================================================
# Change column data types
# =============================================================================

########## Option 1 .to_numeric() ##########
# change non-numeric objects (such as strings) into integers or floating point

pd.to_numeric(DF1) # for the complete df

DF1["Col"] = pd.to_numeric(DF1["Col"]) # for single columns


DF1 = DF1.apply(pd.to_numeric) # convert all columns of DataFrame

DF1[["a", "b"]] = DF1[["a", "b"]].apply(pd.to_numeric) # convert just columns "a" and "b"

# Extra functie

# pd.to_numeric(IO,
# errors = "ignore"  # ignores colomns that cant be transformed and returns og value
# downcast = "integer" OR "float" # determine outcome data type

########## Option 2 .astype() ##########
# Just pick a type

# convert all DataFrame columns to the int64 dtype
df = df.astype(int)

# convert column "a" to int64 dtype and "b" to complex type
df = df.astype({"a": int, "b": complex})

# convert Series to float16 type
s = s.astype(np.float16)

# convert Series to Python strings
s = s.astype(str)

# convert Series to categorical type - see docs for more details
s = s.astype('category')

# Extra functie

# df.astype(IO,
# errors = "ignore"  # ignores colomns that cant be transformed and returns og value


########## Option 3 .infer_objects() ##########
#soft conversions

df = df.infer_objects()
