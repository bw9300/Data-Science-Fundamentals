
#get the names from user input
name = input("What is your name? ")
lover_name = input("What is your name? ")

#function to compare the names
def compare_names():
    name_length = len(name)
    lover_name_length = len(lover_name)
    count = 0

    if name_length == lover_name_length:
        while count < (name_length * lover_name_length) + 2:
            print(count)
            count += 1
    elif name_length != lover_name_length:
        while count < (name_length * lover_name_length) * 2:
            print(count)
            count += 1
    else:
        print("0...")

#show te names. If the names are similair show 1, not equal show 2
if name == lover_name:
    print("HMM.. looks like your in love with yourself")
elif name != lover_name:
    print("Woohooo " + name + " and  " + lover_name + " are in love!")

#ask user is he want to continue
go = input("Would you like to continue? (y/n): ")

#if yes
if go == "y":
    print("if you're ready we check on a scale from 1 to 100 how your matching with each other")
    go_final = input("Continue? (y/n): ")

    if go_final == "y":
        print("Here we go!")
        compare_names()
    else:
        print("Come back later")
else:
    print("OK, bye.")
