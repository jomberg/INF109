#!/usr/bin/python3

# UiB INF109 høsten 2014 innleveringsoppgave2
# Johannes Fåberg Moldung <johannes@moldung.no>

def konverter():
    """
    Get name of input file from user
    Iterate over each line in input file, 
    and write each line to new output file 'STOR'+filename, converted to upper case
    """

    # Read path and name of input file from user
    filename = (input("Filnavn for konvertering til kun store bokstaver: "))
    print()

    # Create output file
    output_file = open("STOR"+filename, 'w')

    input_file = open(filename, 'r')

    for line in input_file:
        output_file.write(line.upper())
    output_file.close()

def analyse():
    """
    Get name of input file from user
    Iterate over each line in input file, 
    counting instances of ['A', 'C', 'G', 'T'] and report sum of each including persent distribution, and length of line
    and also keep track of grand total sum, reporting at end of file
    """

    # Read path and name of input file from user
    filename = (input("Flinavn for enkel analyse: "))

    input_file = open(filename, 'r')
    print()

    # Define lookup string
    # used to index into counter list via str.find(sub)
    LookupString = 'ACGT'

    # Initialize total-counter list
    TotalCounter = [ 0, 0, 0, 0 ]
    total_length = 0

    for line in input_file:
        # Initialize counter list
        Counter = [ 0, 0, 0, 0]
        length = len(line)

        # Loop over each gen/character in line, counting instances
        for gen in line:
            index = LookupString.find(gen)
            Counter[index] = Counter[index] + 1
            TotalCounter[index] = TotalCounter[index] + 1
        
        # Keep track of totals
        total_length = total_length + length

        # Report findings
        print (line)
        print ('Lengde = ', length )
        for gen in LookupString:
            index = LookupString.find(gen)
            print ("Antall {}: {:4d}   prosent: {:4.1f}".format(gen, Counter[index], (Counter[index]/length)*100))
        print ()

    # Report totals for whole file
    print ('Totalt for hele filen:')
    print ('-' * 40)
    for gen in LookupString:
        index = LookupString.find(gen)
        print ("Antall {}: {:4d}   prosent: {:4.1f}".format(gen, TotalCounter[index], (TotalCounter[index]/total_length)*100))

def komplement():
    """
    Get name of input file from user
    Iterate over each line in input file, 
    print line and genome complement/invers of line
    ['A', 'C', 'G', 'T'] maps to ['C', 'A', 'T', 'G']
    """

    # Define lookup string
    LookupString = 'ACGT'

    # Define complement string
    ComplementString = 'CATG'

    # Read path and name of input file from user
    filename = (input("Filnavn for komplementering/invers: "))

    input_file = open(filename, 'r')
    print()

    for line in input_file:
        complement_list = []

        # Loop over each gen/character in line, counting instances
        for gen in line:
            position = LookupString.find(gen)
            complement_list.append(ComplementString[position])
            #invers_gen = ComplementString[position]
            #print (gen, ",found at ", position, " => ", invers_gen)

        complement_line = ''.join(complement_list)

        # Report findins
        print ('Opprinnelig:')
        print (line)
        print ('Komplementaer:')
        print (complement_line, "\n")

# Call methods
konverter()
print()
analyse()
print()
komplement()
