
# =============================================================================
# Remove Stop Words based on business insights and IDF
# =============================================================================

stop_words = stopwords.words('dutch')

stop_words.extend(["Stopwoorden uitzoeken"])



# Function te remove stopwords from list REQUIRE GENSIM
def remove_stopwords(texts):
    return [[word for word in simple_preprocess(str(doc), max_len=30) if word not in stop_words] for doc in texts]


# =============================================================================
# Create BOW Model for stopword removal
# =============================================================================

df2_BOW = df2["COL 1 X"]
words = remove_stopwords(df2_BOW)


# =============================================================================
# Re-assamble list to colum
# =============================================================================

list_data_words_nostops = []
for idx in range(len(words)):
   l = " ".join(words[idx])
    list_data_words_nostops.append(l)

df2_nostops = pd.Series(list_data_words_nostops)


# =============================================================================
# Rejoin dataset without stops
# =============================================================================

df2["COL 1 X"] = df2_nostops
