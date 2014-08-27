
def multiply(base, max):
    for i in range(1, max):
        result = base * i
        print ("%2d * %2d = %2d") % (base, i, result)

def main():
    # Skriv ut 2-gangen
    max=10
    multiply(2, max)

main()
