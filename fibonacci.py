
def fibonacci(num):                 
    x = 0                                         
    s = 1                                         
    if num <= 0:
        print("Het getal moet hoger dan 0 zijn")
        return
    else:
        print(x, s, end=" ")
        for f in range(2, num):
            next = x + s                           
            print(next, end=" ")
            x = s
            s = next

fibonacci(0)
            

