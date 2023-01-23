class stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    #def __str__(self):
    #    return str(self.items)

#test
s = stack()
s.push(1)
print(s.isEmpty())
print(s.pop())
