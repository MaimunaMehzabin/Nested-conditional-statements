age = int(input("How old are you?: "))

if age >9:

    if age>=10 and age <= 20:
        print("You are allowed in the class, age limit in between 10 and 20")
    else:
        print("You are not allowed")
else:
    print("You are too young for the class")