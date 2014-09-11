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

    # Initialize total-counters
    total_A = 0
    total_C = 0
    total_G = 0
    total_T = 0
    total_length = 0
    for line in input_file:

        # Strip off newline
        line = line.rstrip('\n')

        # Initialize counters
        A = 0
        C = 0
        G = 0
        T = 0

        length = len(line)

        # JTM: Det finnes bedre men mer avanserte maater aa gjoere dette paa, se http://bytebaker.com/2008/11/03/switch-case-statement-in-python/
        # men her kan du kanskje gjenbruke den metoden du gjorde i oevelsesoppgaver del 1, metode for poengsum => karakter...

        # Loop over each gen/character in line, counting instances
        for gen in line:
            if gen == 'A':
                A = A + 1
            elif gen == 'C':
                C = C + 1
            elif gen == 'G':
                G = G + 1
            elif gen == 'T':
                T = T + 1
        
        # Keep track of totals
        total_length = total_length + length
        total_A = total_A + A
        total_C = total_C + C
        total_G = total_G + G
        total_T = total_T + T

        # Report findings
        print (line)
        print ('Totalt for hele filen:')
        print ('Lengde = ', length )
        print ("Antall A: {:4d}   prosent: {:4.1f}".format(A, (A/length)*100))
        print ("Antall C: {:4d}   prosent: {:4.1f}".format(C, (C/length)*100))
        print ("Antall G: {:4d}   prosent: {:4.1f}".format(G, (G/length)*100))
        print ("Antall T: {:4d}   prosent: {:4.1f}".format(T, (T/length)*100))
        print ()

    # Report totals for whole file
    print ('-' * 40)
    print ("Antall A: {:4d}   prosent: {:4.1f}".format(total_A, (total_A/total_length)*100))
    print ("Antall C: {:4d}   prosent: {:4.1f}".format(total_C, (total_C/total_length)*100))
    print ("Antall G: {:4d}   prosent: {:4.1f}".format(total_G, (total_G/total_length)*100))
    print ("Antall T: {:4d}   prosent: {:4.1f}".format(total_T, (total_T/total_length)*100))

def komplement():
    """
    Get name of input file from user
    Iterate over each line in input file, 
    print line and genome complement/invers of line
    ['A', 'C', 'G', 'T'] maps to ['C', 'A', 'T', 'G']
    """

    # Define complement lookup list
    Complement = ['C', 'A', 'T', 'G']

    # Read path and name of input file from user
    filename = (input("Flinavn for enkel analyse: "))

    input_file = open(filename, 'r')
    print()

    for line in input_file:
        # Strip off newline
        line = line.rstrip('\n')

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
# konverter()
#analyse()
komplement()
