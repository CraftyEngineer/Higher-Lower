import art
import game_functions as gfunc


flag=True
score=0

print(art.logo)
acc_a=gfunc.get_random_account()
acc_b=gfunc.get_random_account()

while flag:
    acc_a=acc_b
    acc_b=gfunc.get_random_account()
    while acc_b==acc_a:
        acc_b=gfunc.get_random_account()
    print(f"Compare A: {acc_a['name']}, a {acc_a['description']}, from {acc_a['country']}")
    print(art.vs)
    print(f"Against B: {acc_b['name']}, a {acc_b['description']}, from {acc_b['country']}")
    choice=input("Who has more followers? Type 'A' or 'B': ").lower()
    if choice=="a":
        choice=acc_a
    elif choice=="b":
        choice=acc_b
    else:
        print("Wrong choice!")

    greater_acc=gfunc.compare_acc(acc_a, acc_b)
    if greater_acc==choice:
        score+=1
        print(f"You're right! Current Score is {score}")
        print("\n"*200)
        print(art.logo)
        
    else:
        print(f"Sorry that's wrong! Final score is {score}")
        flag=False


