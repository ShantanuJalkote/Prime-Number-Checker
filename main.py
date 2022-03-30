def prime_number(num):
    for i in range(2, num):
        if num % i == 0:
            return f"{num} is not a prime number"
        else:
            return f"{num} is a prime number"


is_on = True

while is_on:
    user_input = int(input("Which number do you want to check : "))
    print(prime_number(user_input))
    still_continue = input("Do you want to check another number.(y/n) : ")
    if still_continue == "y":
        continue
    else:
        print("!!Bye!!")
        is_on = False