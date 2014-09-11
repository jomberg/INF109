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

    # Initialize total-counter dictionary
    TotalCounter = { 'A': 0, 'C': 0, 'G': 0, 'T': 0 }
    total_length = 0

    for line in input_file:
        # Initialize counter dictionary
        Counter = { 'A': 0, 'C': 0, 'G': 0, 'T': 0 }
        length = len(line)

        # Loop over each gen/character in line, counting instances
        for gen in line:
            Counter[gen] += 1
        
        # Keep track of totals
        total_length = total_length + length
        for gen in TotalCounter:
            TotalCounter[gen] += Counter[gen]

        # Report findings
        print (line)
        print ('Lengde = ', length )
        for gen in sorted(Counter):
            print ("Antall {}: {:4d}   prosent: {:4.1f}".format(gen, Counter[gen], (Counter[gen]/length)*100))
        print ()

    # Report totals for whole file
    print ('Totalt for hele filen:')
    print ('-' * 40)
    for gen in sorted(TotalCounter):
        print ("Antall {}: {:4d}   prosent: {:4.1f}".format(gen, TotalCounter[gen], (TotalCounter[gen]/length)*100))

def komplement():
    """
    Get name of input file from user
    Iterate over each line in input file, 
    print line and genome complement/invers of line
    ['A', 'C', 'G', 'T'] maps to ['C', 'A', 'T', 'G']
    """

    # Define complement lookup dictionary
    Complement = {'A': 'C', 'C': 'A', 'G': 'T', 'T': 'G'}

    # Read path and name of input file from user
    filename = (input("Flinavn for komplementering/invers: "))

    input_file = open(filename, 'r')
    print()

    for line in input_file:
        complement_line = ''
        # Loop over each gen/character in line, counting instances
        for gen in line:
            complement_line = complement_line + Complement[gen]
        # Report findins
        print ('Opprinnelig:')
        print (line)
        print ('Komplementaer:')
        print (complement_line)

# Call methods
konverter()
print()
analyse()
print()
komplement()
