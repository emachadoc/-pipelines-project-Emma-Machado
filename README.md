# pipelines-project-emma-machado

https://github.com/emachadoc/pipelines-project-emma-machado


TESTING MICROSOFT TEXT ANALYTICS

DESCRIPTION:

The aim of this project is to test Microsoft Text Analytics sentiment from Azure Cognitive Services (https://any-api.com/azure_com/cognitiveservices_TextAnalytics/docs/API_Description) analyzing raw text from Amazon reviews (https://www.kaggle.com/bittlingmayer/amazonreviews) for clues about positive or negative sentiment. This API returns a sentiment score between 0 and 1 for each review, where 1 is the most positive. It should match with the stars given by the customer in his Amazon review. Reviews are divided into ‘label 1’, which are negative reviews, and ‘label 2’, which are positive ones.

REPO FILES:

README.md: Project description
main.py: Pipeline
clean.py: Clean function receives a .txt file, filters positive from negative reviews, removes line break symbols and returns a list [rev] of lists with negative reviews as list [reviews1] and positive reviews as list [reviews2]
select_review.py: Select_review function asks the user for an input or randomly selects some reviews from the database.
sentiment.py: Sentiment function makes a call to Text Analysis API, which needs a subscription key, and returns a dictionary with two key/values: the id of the review and its score, being negative score from 0.0 to 0.3, neutral score from 0.3 to 0.7 and positive score from 0.7 to 1.0. Negative scores should be assigned to reviews from list [reviews1], while positive scores should be assigned to reviews from list [reviews2], to check if the API is working properly.