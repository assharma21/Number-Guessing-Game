import random
n = random.randint(1,100)
a = -1  # Initialize the user's guess variable with a value not equal to n
guesses = 1

# Loop until the user guesses the correct number
while (a !=n):
    a = int(input("Guess the number: "))
    if (a >n):
        print("Lower number please")
        guesses +=1
    elif (a <n):
        print("Higher number please") 
        guesses +=1

print(f" You have guessed the number {n} correctly in {guesses} attempts")
