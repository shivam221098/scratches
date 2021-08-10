found = False

string = input()
char = input()
count = int(input())
counter = st_counter = 0
for st in string:
    if st == char:
        counter += 1
    if counter == count:
        found = True
        break
    st_counter += 1

if count == 0:
    print(string)
elif st_counter + 1 == len(string) and found:
    print(string)
elif found:
    print(string[st_counter + 1:])
else:
    print(string)