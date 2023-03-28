day = 1
while day < 31:
    print("\033[32m", "Day", day)
    print("\033[0m", "What did you think about the task?")
    comment= input()
    summary = f"You thought Day {day} was {comment}"
    print(f"{summary:^40}")
    print()
    day += 1
    
