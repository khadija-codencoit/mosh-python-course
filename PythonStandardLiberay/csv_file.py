import csv

with open("data.csv","w") as file:
    writer = csv.writer(file)
    writer.writerow(["tranection_id","product_id"])
    writer.writerow([111,"Dress"])

with open("data.csv","r") as file:
    reader = csv.reader(file)
    print(list(reader))