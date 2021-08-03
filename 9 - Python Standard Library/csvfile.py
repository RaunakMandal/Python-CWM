import csv

with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["_id", "name", "mail", "phone"])
    writer.writerow([0, "Raunak", "iamriju", 9932])
    writer.writerow([1, "Cooldude", "iamriju2", 99322])

with open("data.csv") as file:
    reader = csv.reader(file)
    # print(list(reader))
    for row in reader:
        print(row)
