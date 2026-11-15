# --- REFLECTION ---
#1) Compared to Excel, the Python ETL pipeline is more flexible in my opinion as it allwos for more data manipulation and analysis. Python can handle larger datasets and can be automated while Excel is more limited, however Excel is easier to use for those who don't know how to code.
#2) Append mode would be useful for businesses as it allows them to keep a running log of their data without having to overwrite the program and code everything from scratch again. An example is when a new user signs up for a service. The business can just log the new user rather than having to rewrite the entire user database.


import csv
from datetime import datetime

#EXCERCISE 1: Checking CSV file data (No coding)

print()
#EXCERCISE 2: Read and Print Raw Rows
with open("data/sales.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

print()
#EXCERCISE 3: Skip the Header
with open("data/sales.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    print("Header:", header)
    for row in reader:
        print(row)

print()
#EXCERCISE 4: Compute Totals
with open("data/sales.csv", "r") as f: 
    totalRev = 0
    reader = csv.reader(f)
    header = next(reader)
    print("Header:", header)
    for row in reader:
        price = float(row[1])
        quantity = int(row[2])
        totalRev += price * quantity
        print(f"{row[0]}: {quantity} units * ${price} = ${price * quantity:.2f}")
    print(f"Total Revenue: ${totalRev:.2f} ")

print()
#EXCERCISE 5: Filter and Write
filtered_rows = []
origRowCount = 0
newRowCount = 0
with open("data/sales.csv", "r") as f: 
    reader = csv.reader(f)
    header = next(reader) 
    for row in reader:
            origRowCount += 1
            price = float(row[1])
            quantity = int(row[2])
            if price * quantity > 100:
                filtered_rows.append(row)

header = ["Product", "Price", "Qty", "Total"]

with open("data/cleaned.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(filtered_rows)
    print("Header:", header)
    for row in filtered_rows: 
        newRowCount += 1
        price = float(row[1])
        quantity = int(row[2])
        print(f"{row[0]}: {quantity} units * ${price} = ${price * quantity:.2f}")
print(f"\nOriginal Row Count: {origRowCount}")
print(f"New Row Count: {newRowCount}\n")

print()
#EXCERCISE 6: csv.DictReader
with open ("data/sales.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["product"], row["price"], row["quantity"])
        #Between the 2 ways of reading the csv file, I'd prefer the DictReader because I can actually see the column names and it helps me keep track of which column represents which data value.
        #If I had used regular csv.reader, I would have to remember which column index corresponds to which data value, which can eb tricky if the data isn't always static and say if a column name swaps. Then I'd get an error since I won't be able to tell which data is in which column.

print()
#EXCERCISE 7: Sales Summary by Product
sumDict = {}
with open ("data/sales.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])
        if product in sumDict:
            sumDict[product] += price * quantity
        else:
            sumDict[product] = price * quantity

for product, total in sumDict.items():
    print(f"{product}: ${total:.2f}")

print()
#EXCERCISE 8: Append Mode Log
totRev = 0
with open("data/sales.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        price = float(row["price"])
        quantity = int(row["quantity"])
        totRev += price * quantity

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("data/run_log.txt", "a") as f:
    f.write(f"{timestamp}: Total Revenue: ${totRev:.2f}\n")
print(f"Logged total revenue of ${totRev:.2f} at {timestamp} to run_log.txt")