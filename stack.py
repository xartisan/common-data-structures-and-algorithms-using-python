class Stack:

    def __init__(self):
        self._data = []

    def is_empty(self):
        return not self._data

    def push(self, data):
        self._data.append(data)

    def pop(self):
        try:
            return self._data.pop()
        except IndexError:
            raise Exception('Invalid Operation: the stack is empty!')

    def peek(self):
        try:
            return self._data[-1]
        except IndexError:
            raise Exception('Invalid Operation: the stack is empty!')

    def size(self):
        return len(self._data)

    def __repr__(self):
        return repr(self._data)


if __name__ == '__main__':
    stack = Stack()
    stack.push(2)
    stack.push(3)
    print(stack.size())
    print("Popped: ", stack.pop())
    print("Popped: ", stack.pop())
    print(stack.size())
    print("Peek:", stack.peek())
    print(stack.size())
