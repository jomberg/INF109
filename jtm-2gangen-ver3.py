
def multiply(base, max):
    for i in range(1, max+1):
        result = base * i
        print ("%2d * %2d = %2d" %(base, i, result))

def main():
    # Skriv ut 2-gangen
    max=10
    multiply(2, max)

main()

# str1 = a
# str2 = b
# int1 = 100
# print ("nr 1: " + str1 + " nr2: " + str2)
# print ("int1: " + str(int1))
