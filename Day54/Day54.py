import csv
with open("Day54Totals.csv") as file:
    reader = csv.DictReader(file)
    total = 0
    for row in reader:
        total += float(row["Cost"]) * float(row["Quantity"])
print(f"Total: ${round(total, 2)}")
