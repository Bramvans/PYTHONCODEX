# =============================================================================
# Downsample (or upsample) COL equal all Y
# =============================================================================

# Separate majority and minority classes
df_majority = df2[df2.COL2Y == 0]
df_minority = df2[df2.COL2Y == 1]

# Downsample majority class
df_majority_downsampled = resample(df_majority,
                                   replace=False,  # sample without replacement
                                   n_samples=999,  # to match minority class
                                   random_state=123)  # reproducible results

# Combine majority class with upsampled minority class
df2 = pd.concat([df_majority_downsampled, df_minority])

# Display new class counts
df2["COL 2 Y"].value_counts()

