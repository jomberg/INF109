#!/usr/bin/python3

def isValidRoman(S):
    romans    = [ 'M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I' ]
    operators = [ '+', '-', '*', '/' ]
    maks_rep  = [   3,    1,   1,    1,   3,    1,   1,    1,   1,    1,   1,    1,  3  ]
    idx_check = []

    count_eq = 0
    i = 0
    while i < len(S):
        c = S[i]

        if c in operators:
            # Skip check of operators, jump to next char
            #print ("Skip operator ", c)
            i = i + 1
            continue

        # Check for valid 'char'
        # This is probably redundant, as you have full controll of possible input values
        if not c in romans:
            print ("ERR: NaN")
            return False

        # Check for max repetitions
        if i > 0 and S[i-1] == c:
            count_eq = count_eq + 1
            if count_eq >= maks_rep[romans.index(c)]:
                print ("ERR: Too many repeated:", c)
                return False
        else:
            count_eq = 0

        c_idx = romans.index(c)

        # Check for invalid 'lingatures'
        if i+1 < len(S):
            c1 = S[i]
            idx1 = romans.index(S[i])
            c2 = S[i+1]
            if c2 in operators:
                #print ("Skip lingature test of %s %s" %(c1, c2))
                i = i + 1
                continue
            idx2 = romans.index(S[i+1])
            if romans.index(S[i]) > romans.index(S[i+1]):
                # We have less-valued roman number preceeding greater-valued roman number
                # Now take the two and check against valid combinations
                lingature = S[i:i+2]
                if not lingature in romans:
                    print ("ERR: Invalid 'lingature': '%s'" %(lingature))
                    return False
                else:
                    c_idx = romans.index(lingature)
                    print ("OK 'lingature': '%s'" %(lingature))
                    i = i + 1 # Skip ahead
            else:
                print ("OK? '%s'" %(S[i:i+2]), romans.index(c), romans.index(S[i+1]))

        idx_check.append(c_idx)
        i = i + 1
    # Check for out of order romans
    prev = 0
    for i in range(len(idx_check)):
        if idx_check[i] < prev:
            print ("ERR: Out of order romans")
            return False
        prev = idx_check[i]
    return True

romans = [ "II+X", "NEI", "IIII", "III", "VV", "VX", "IM", "XL", "IV", "X+", "MCCXVII", "IIV" ]
for i in range(len(romans)):
    roman = romans[i]
    print ("Testing roman '%s' for validity" %(roman))
    print (isValidRoman(roman), "\n")
