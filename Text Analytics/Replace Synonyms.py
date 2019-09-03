# =============================================================================
# Loading the MODULES
# =============================================================================
from tqdm import tqdm
tqdm.pandas()
import pandas as pd

# =============================================================================
# Loading the dictionary to replace
# =============================================================================

synoniem = pd.read_excel("C:\\Users\\XXXX\\Desktop\\XX XX XX\\XXX\\words.xlsx", sheet_name = 1, index_col = "Synoniem")

# =============================================================================
# Convert to dicts
# =============================================================================

syno_dict = synoniem["Woord"].to_dict()

def replace_from_dict(string, dictionary):
    return ' '.join([dictionary.get(word,word)
                     for word in string.split()])

# =============================================================================
# Loading the dataframe
# =============================================================================

df1 = pd.read_csv("C:\\Users\\XXX\\XXXXX\\XXX XXXX X\\XXX\\text1.csv")

# =============================================================================
# Replace the words from the dict
# =============================================================================

df1["TEXT"] = df1["TEXT"].progress_apply(lambda s: replace_from_dict(s, syno_dict))


