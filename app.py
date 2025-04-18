import random
print("Think a number between 1 to 10 🤔")
a=True
b=1
name=input("What is your name ? ")
while a:
    computer_guess=random.randint(1,10)
    user_input=int(input("Write your secret number ? (Computer will guess it.) "))
    if computer_guess == user_input:
        print(f"🎇🎉You passed. Computer : {computer_guess} == {name} : {user_input}")
        print(f"You attempt: {b}")
        a=False
    elif computer_guess < user_input:
        print(f"Your number is greater than computer number.")
        print(f"Your attempts: {b}")
        b+=1
    elif computer_guess>user_input:
        print(f"Your number is less than computer number.")
        print(f"Your attempts: {b}")
        b+=1
    if b==11:
         a=False

for i in range(1,5):
    if i==3:
        continue
    print(i)