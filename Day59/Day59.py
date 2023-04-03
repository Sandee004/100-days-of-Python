print("Welcome to palindrome checker")
phrase= input("Word\n>>>")
check= phrase[::-1]
if phrase == check:
    print("Nice. The word is a palindrome")
else:
    print("Nah. Not a palindrome")
