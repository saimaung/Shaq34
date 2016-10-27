from Stack import Stack

stack = Stack()
print(stack.is_empty())
stack.push('Steph')
stack.push('Curry')
print(stack.peek())
stack.push('Kevin')
print(stack.size())
print(stack.is_empty())
stack.push(30)
print(stack.pop())
print(stack.pop())
print(stack.size())