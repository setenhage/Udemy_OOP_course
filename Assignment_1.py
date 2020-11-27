
class MaxSizeList(object):
     
    def __init__(self, maxSize):
        self.size = maxSize
        self.mylist = [];
    
    def push(self, string):
        self.mylist.append(string)
        if len(self.mylist) > self.size:
            self.mylist.pop(0)
        
    def set_list(self, newstring):
        self.mylist = newstring
    
    def get_list(self):
        return self.mylist
        
a = MaxSizeList(3)
b = MaxSizeList(1)

a.push("hey")
a.push("hi")
a.push("let's")
a.push("go")

b.push("hey")
b.push("hi")
b.push("let's")
b.push("go")

print(a.get_list())
print(b.get_list())


