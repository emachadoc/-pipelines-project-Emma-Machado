import random
def select_review(reviews=forapi):
    review = input('Write your reviews or let me select some for you: ')
    forapi = []
    while len(forapi)<3:
        forapi.append(random.choice(revs))
    return(print(forapi))