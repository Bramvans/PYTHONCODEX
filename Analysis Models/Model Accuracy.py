# =============================================================================
# Model Accuracy
# =============================================================================

pred = tfidf_logit_pipeline.predict(X_test)

print(classification_report(y_test,pred))
print('\n')
print(confusion_matrix(y_test,pred))
print('\n')
print(accuracy_score(y_test,pred))


# =============================================================================
# Function to create confusion matrix
# =============================================================================
# Source = https://github.com/scikit-learn/scikit-learn/issues/12700

def plot_confusion_matrix(actual, predicted, classes,
                          normalize=False,
                          title='Predicted versus true labels', figsize=(7, 7),
                          cmap=plt.cm.Blues, path_to_save_fig=None):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    import itertools
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(actual, predicted).T
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

    plt.figure(figsize=figsize)
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=90)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="black" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('Predicted label')
    plt.xlabel('True label')

    if path_to_save_fig:
        plt.savefig(path_to_save_fig, dpi=300, bbox_inches='tight')

# =============================================================================
# Plot confusion matrix
# =============================================================================

plot_confusion_matrix(y_test, pred,
                      tfidf_logit_pipeline.named_steps['logit'].classes_, figsize=(8, 8))

