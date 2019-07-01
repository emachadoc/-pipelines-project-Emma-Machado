from sentiment import get_sentiment
from pprint import pprint
from select_review import select_review

user_input = True
number_of_inputs = 10
reviews = []

if user_input == True:
    user_review = input('Write your reviews or let me select some for you: ')
    reviews.append(user_review)
else:
    select_review(reviews)
    reviews.append(forapi)

scoring = get_sentiment(reviews)

pprint(scoring)

if user_input == True:
    print('Your score is {} Do you agree with that?'.format(scoring[0]['score']))
else:
    print('The score for this review is {}'.format(scoring[0]['score']))