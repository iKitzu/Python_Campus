def cambio(amount):
    cents_10 =amount//10
    amount %=10
    
    cents_5 =amount//5
    amount %=5
    
    cents_1=amount
    
    return (cents_10, cents_5, cents_1)

while True:
    try:
        number=int(input("Digit your number: "))
        break
    except ValueError:
        print("¡Enter a whole number!")        


cents_10, cents_5, cents_1 = cambio(number)

print("10 Cents: ", cents_10)
print("5 Cents: ",cents_5)
print("1 Cent: ",cents_1)