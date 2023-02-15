import csv
with open("names.csv", "r") as f:
  csv_reader = csv.DictReader(f, delimiter=",")
  for line in csv_reader:
    print(line)
