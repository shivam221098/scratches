stack = []
def precedence_order(item):
    if item == '^':
        return 4
    elif item == '(' or item == ')':
        return 3
    elif item == '*' or item == '/':
        return 2
    elif item == '+' or item == '-':
        return 1

def precedence_check(item):
    try:
        if precedence_order(item) <= precedence_order(stack[len(stack) - 1]):
            return True
        else:
            return False
    except (KeyError, IndexError):
        return False

def push(element):
    stack.append(element)


def pop():
    return stack.pop()


def is_empty():
    return True if len(stack) == 0 else False


postfix = []
expression = input()
for i in expression:
    if i.isdigit() or i.isalpha():
        postfix.append(i)
    elif i == " ":
        continue
    else:
        while precedence_check(i):
            postfix.append(pop())
        push(i)
while not is_empty():
    postfix.append(pop())

for i in postfix:
    if i.isdigit() or i.isalpha():
        push(i)
    else:
        if i == '+':
            push(int(pop()) + int(pop()))
        elif i == '-':
            push(int(pop()) - int(pop()))
        elif i == '*':
            push(int(pop()) * int(pop()))
        elif i == '/':
            val1 = int(pop())
            val2 = int(pop())
            push(val2 / val1)
        elif i == '^':
            val1 = int(pop())
            val2 = int(pop())
            push(val2 ** val1)

print(postfix)
print(pop())