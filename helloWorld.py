
def helloWorld(num):
    
    for x in range(num):
        print("Hello World!")
    

helloWorld(7)

def multiplier(n):
    return lambda a : a * n

mytripler = multiplier(3)
print(mytripler(11))

def calc(base, accessory) -> int:
    return base + accessory + 111

value = calc(1200, 89)
print(value)

def hello(name) -> int:
    return ""
    print("Hello " +name)

print(hello("Rudi"))

def printDouble():
    return 2*2

#print(printDouble())

def times2(base:int) -> int:
    return times(base, 2)

def times3(base:int) -> int:
    return times(base, 2)

def times(base:int, multiplier:int):
    return base * multiplier

value1 = times2(5)
value2 = times3(5)
print(value1 + value2)