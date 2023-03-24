#implementation of stack

#create Stack 
def create_stack():
    stack = []
    return stack

def push(stack,item):
    stack.append(item)
    print('Pushed item is:',item)


def check_empty(stack):
    return len(stack)== 0


def pop(stack):
    if(check_empty(stack)):
        return "stack is empty"
    return stack.pop()

stack = create_stack()
for i in range(0,int(input("length of stack: "))):
    a = int(input('Enter elements: '))
    push(stack,a)

print("popped item: ",pop(stack))
print("after popping the elements: ",stack)