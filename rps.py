import random
user_choice = int(input("Enter your choice: 0 is rock, 1 is paper, 2 is scissors: "))
if user_choice >=3 or user_choice < 0:
    print("you entered invalid number, you lose")
else:
    computer_choice = random.randint(0,2)
    print("computer_chose:")
    print(computer_choice)
    if user_choice == computer_choice:
        print("it is a draw")
    elif user_choice == 0 and computer_choice == 2:
        print("you lose")
    elif computer_choice == 0 and user_choice == 2:
        print("we will win")    
    elif user_choice > computer_choice:
        print("we will win")
    elif computer_choice > user_choice:
        print("we will lose")

