import emoji
multiple=int(input("Multiple of: "))
times= 1
score= 0
while times < 11:
    userans1 = input(str(multiple) + " × " + str(times) + "= ")
    answer = multiple * times
    if int(userans1) == answer:
        print(emoji.emojize("Correct:party_popper:"))
        score += 1
    else:
        print("Incorrect")
    times += 1
    print("")
print("Score: " + str(score))
if score >= 8:
    print("You're smart....nice")
