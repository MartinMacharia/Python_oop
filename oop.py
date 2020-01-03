# OOP concepts
# Python function

def Add_Two_Numbers (a,b):
    y = a + b
    return y

Add_Two_Numbers(5,5)

def Add_Two_Integers(a,b):
    y_1 = a + b
    return y_1
Add_Two_Integers(5,6)

# Python class and function
# Python classes are also called objects

# With self

# If any of your family member calls your name, how do you recognize
# that its your mother or father or brother,if you are sitting in a different room?
# You recognize the voice. Right? Similarly, self represents the voice of the object.

class Add_Two_Numbers:
    def add(self, a, b):
        y = a + b
        return y
x = Add_Two_Numbers()
x.add(5,5)
x.add(3,4)

# Without self

class Add_Two_Numbers:
    def add(a, b):
        y = a + b
        return y

x = Add_Two_Numbers()
x.add(1,2)

# class inheritance

class do_something:
    def add(self, a, b):
        x = a + b + 10
        return x

class do_anotherthing(do_something):
    def multiply(self,c):
        y = self.add(c, 2)
        w = y * 2
        return w
ds = do_anotherthing()
ds.multiply(4)



