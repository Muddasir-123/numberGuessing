from random import randint
a=True
attempt=0
while a:
    com_num=randint(1,10)
    user_num=int(input("Guess the number between 1 to 10 .  "))
    if com_num==user_num:
        print("🎉You won.Guess correctly.")
        a=False
        attempt+=1
    elif com_num>user_num:
        print("Com number is greater than you.")
        attempt+=1
    elif com_num < user_num:
        print("Com number is less than your number.")
        attempt+=1
    else:
        print("Enter the number.")
        attempt+=1
    if attempt==5 and a==True:
        a=False
        print("You reached the maximum limit.")