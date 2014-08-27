
def multiply(base, max):
    for i in range(1, max+1):
        result = base * i
        print ("%2d * %2d = %2d" %(base, i, result))

def main():
    # Skriv ut multiplikasjonstabellen
    start=1
    stopp=11
    siste=10
    for tall in range(start,stopp):
        print ("Multiplikasjonstabellen for %d" % (tall))
        multiply(tall, siste)
        print ('')

main()


# https://wiki.python.org/moin/ForLoop
# example nr 1, nested for loops
#for x in xrange(1, 11):
#    for y in xrange(1, 11):
#        print '%d * %d = %d' % (x, y, x*y)
