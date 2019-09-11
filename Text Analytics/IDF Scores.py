# =============================================================================
# IDF Scores check for stopwoorden
# =============================================================================

tfidf_transformer = TfidfTransformer(smooth_idf=True, use_idf=True)

tfidf_transformer.fit(df2_COUNT)

df_idf = pd.DataFrame(tfidf_transformer.idf_, index=cv.get_feature_names(), columns=["idf_weights"])

# sort ascending
df_idf.sort_values(by=['idf_weights'])

df_idf.to_excel("C:\\Users\\Desktop\\MAP\\IDF.xlsx")
