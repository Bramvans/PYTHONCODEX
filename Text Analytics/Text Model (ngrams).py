# =============================================================================
# Text model for ngrams
# =============================================================================

# Build bigrams and trigrams, put a limit on maximal number of features and minimal word frequency
tf_idf = TfidfVectorizer(ngram_range=(1, 3), max_features=4000, min_df=0.03)

# Multinomial logistic regression a.k.a softmax classifier
logit = LogisticRegression(C=1, n_jobs=4, solver='lbfgs',
                           random_state=123, verbose=1, multi_class='multinomial',
                          class_weight='balanced')
# sklearn's pipeline
tfidf_logit_pipeline = Pipeline([('tf_idf', tf_idf),
                                 ('logit', logit)])


tfidf_logit_pipeline.fit(X_train, y_train)