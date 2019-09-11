# =============================================================================
# Create Split Test Train sets
# =============================================================================

# X-set en y-variabele definiëren
X = df2['COL 1 X'].values.astype(str)
y = df2['COL 2 Y'].values.astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=123)
