# Higher Lower Game


from art import logo, vs
import random
from data import data

# Return whether the player got the answer right
def check_answer(choice, a_follower, b_follower):
        if a_follower > b_follower:
                return choice.lower() == 'a'
        else:
                return choice.lower() == 'b'

# Generate two accounts to compare
objectA = random.choice(data)
objectB = random.choice(data)
if objectA == objectB:
        objectB = random.choice(data)


end_of_game = False
score = 0

while not end_of_game:

        print(logo)
        print(f"Compare A: {objectA['name']}, a {objectA['description']}, from {objectA['country']}")
        print(vs)
        print(f"Against B: {objectB['name']}, a {objectB['description']}, from {objectB['country']}")

        choice = input("Who has more followers? Type 'A' or 'B': ")

        if check_answer(choice, objectA['follower_count'], objectB['follower_count']):
                score += 1
                print(f"You are right! Current score: {score}")
                objectA = objectB
                objectB = random.choice(data)
        else:
                end_of_game = True
                print(f"Sorry, that's wrong. Final score: {score}")



