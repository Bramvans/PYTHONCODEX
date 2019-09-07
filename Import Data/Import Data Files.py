import pandas as pd

# =============================================================================
# Import Excel Files
# =============================================================================

DF1 = pd.read_excel("C:\\DIR\\FILE.xlsx")

# Extra functions to use

#pd.read_excel(IO,
# sheet_name="Name of Sheet" OR SHEET NUM [1, 2, 4],
# names = (list of colum names, for example to change form a list of give new),
# index_col = (colum used to index default is none gives index, usecols for colum list range like ("A" OR "A:E" OR "A,C,F" etc)
# na_values = (look for additional NA values and give example)

# =============================================================================
# Import CSV Files
# =============================================================================

DF1 = pd.read_csv("C:\\DIR\\FILE.csv")

# Extra functions to use

#pd.read_csv(IO,
# sep = seperator to use given between ","
# header = row number to use as the header and start of the data set passed as INT or list between "1"
# names  = column names passed as  array
# index_col = (colum used to index default is none gives index, usecols for colum list range like ("A" OR "A:E" OR "A,C,F" etc)
# na_values = (look for additional NA values and give example)

# =============================================================================
# Import HTML Files
# =============================================================================

html = pd.read_html("C:\\DIR\\FILE.html")

# Extra functions to use

#pd.read_html(IO,
# match = The set of tables containing text matching this regex or string will be returned.
# header = row number to use as the header and start of the data set passed as INT or list between "1"
# index_col = (colum used to index default is none gives index, usecols for colum list range like ("A" OR "A:E" OR "A,C,F" etc)
# attrs = This is a dictionary of attributes that you can pass to use to identify the table in the HTML attrs = {'id': 'table'}

# =============================================================================
# Import from JSON
# =============================================================================

JSON = pd.read_json("C:\\DIR\\FILE.json")

# Extra functions to use

# orient  = Indication of expected JSON string format. pass as  ("split", records, index, columns, values)
# typ = {frame or series}


# =============================================================================
# Import from Clipboard
# =============================================================================

clipdf = pd.read_clipboard()

