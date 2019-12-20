class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return self.__len__() != 0

    def push(self, value):
        self._data.append(value)

    def top(self):
        if self.is_empty():
            return ValueError('Stack is empty')
        return self._data[-1]
    
    def pop(self):
        if self.is_empty():
            return ValueError('Stack is empty')
        self._data.pop()

    def printstack(self):
        for i in self._data:
            print(i, end=' ')
        print()
        