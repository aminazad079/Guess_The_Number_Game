from random import randint
guess=0
estimaton=0
secret_number=randint(1, 101)
name=input("Tell me your name: ")
print(f"Well {name}, I've thought of a number between 1 and 100 and you have only eight tries to guess it. ")

while guess<8:
    estimaton=int(input("Enter your guessed number: "))
    guess+=1
    if estimaton<0 or estimaton>100:
        print("Sorry!! You are out of range.")
        break
    if estimaton>secret_number:
        print("Wrong! you choosed a greater number.")
    elif estimaton<secret_number:
        print("Wrong! you choosed a lower number.")
    else:
        print(f"Congratualtiobs!!{name} you have guessed in a {guess}th attempt. ")
        break
if estimaton!=secret_number:
    print(f"You have run out you number of attempt, the secret  number was {secret_number}")