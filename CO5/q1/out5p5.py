import csv
fieldnames = ['id', 'name', 'age', 'course']
di = [{'id': '1', 'name': 'devu', 'age': '24', 'course': 'MCA'},{'id': '2', 'name': 'gokul', 'age': '24', 'course': 'BTECH'},
{'id': '3', 'name': 'aishu', 'age': '20', 'course': 'MSW'},
 {'id': '4', 'name': 'asma', 'age': '23', 'course': 'LLB '}]
with open("names.csv", "w") as f:
  csv_writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=",")
  csv_writer.writeheader()
  csv_writer.writerows(di)
with open("names.csv", "r") as f:
  csv_reader = csv.DictReader(f)
  h = csv_reader.fieldnames
  print(h)
  for line in csv_reader:
    print(line)
