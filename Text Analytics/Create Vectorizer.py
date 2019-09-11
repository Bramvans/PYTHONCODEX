# =============================================================================
# Create Vectorizer
# =============================================================================

vectorizer = TfidfVectorizer()
cv = CountVectorizer()

df2_VECTOR = vectorizer.fit_transform(df2.COL1X)
df2_COUNT = cv.fit_transform(df2.COL1X)