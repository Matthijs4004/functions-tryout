
n = int(input("Van welk getal wilt u de tafel zien? "))

def print_table(num): 
    for i in range(1,11): 
        print(num,' x ', i, ' = ',num*i) 

print_table(n)