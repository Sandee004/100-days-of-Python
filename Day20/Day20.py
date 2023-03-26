start = int(input("Starting value: "))
end = int(input("End value: "))
increment = int(input("Intervals: "))
if start > end:
    increment *= -1
for i in range(start, end, increment):
    print (i)
