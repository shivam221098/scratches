"""class Bank:
    def __init__(self, name, initial_balance=0.0):
        self.name = name
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount


george = Bank("George Soros", 100.10)
george.deposit(50.00)"""

"""num = int(input("Number: "))
for i in range(num):
    if i % 2 == 1:
        print(i, end=" ")"""

"""from itertools import combinations


def pairs(d, integers):
    for combination in combinations(integers, r=2):
        if abs(combination[0] - combination[1]) == d:
            return True
    return False


print(pairs(3, [0, 1, 2, 4, 100]))"""

"""import re
filename = input("Filename: ")
file = open(filename)

phones = re.findall("\d+\s\d+\s\d+", file.read())
print(", ".join(phones))

file.close()"""

file = open("calls.txt")

all_lines = []
for lines in file.readlines():
    all_lines.append(lines)

file.close()

filtered_calls = []
persons = set()
for line in all_lines:
    if len(line.split()) == 2:
        name, status = line.split()
        name, status = name.strip(), status.strip()

        filtered_calls.append((name, status))
        persons.add(name)

name_perc = []
for person in persons:
    count = 0
    for calls in filtered_calls:
        if person == calls[0] and calls[1].isdigit():
            count += 1

    name_perc.append((person, str(round((count / len(filtered_calls) * 100), 2))))

name_perc.sort(key=lambda x: x[0])
print("{:<20s}{:<20s}".format("Name", "%"))
for name, percentage in name_perc:
    print("{:<20s}{:<20s}".format(name, percentage))