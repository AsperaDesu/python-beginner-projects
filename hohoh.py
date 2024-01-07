print("Guessing Game")
print("-------------")

secret_number = 2
lives = 3
guess_count = 0

while guess_count < lives:
    guess = int(input("Guess The Number: "))
    guess_count += 1
    print("Lives Remaining", lives - guess_count, "\n" )
    if guess == secret_number:
        print("You Won")
        break
else:
    print("You Lose")

