import csv

with open("./lab2/ex2-text.csv", "r", encoding="utf-8") as f:
    txt = f.readlines()

with open('./lab2/ex2-employees.txt', 'w') as f:
    for line in txt:
        split_line = line.split(',')
        split_line = [ x.strip() for x in split_line ]
        f.write(f"{split_line[0]},{split_line[1]}")
        f.write("\n")
    f.close

with open('./lab2/ex2-locations.txt', 'w') as f:
    for line in txt:
        split_line = line.split(',')
        split_line = [ x.strip() for x in split_line ]
        f.write(f"{split_line[0]},{split_line[3]}")
        f.write("\n")
f.close
