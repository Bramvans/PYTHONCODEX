# =============================================================================
# Show weighst of words from the text models
# =============================================================================
# Source = https://eli5.readthedocs.io/en/latest/autodocs/eli5.html

import eli5
eli5.show_weights(estimator=tfidf_logit_pipeline.named_steps['logit'],
                  vec=tfidf_logit_pipeline.named_steps['tf_idf'], top=(50,50))
