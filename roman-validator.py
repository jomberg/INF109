#!/usr/bin/python3

def isValidRoman(S):
    romans    = [ 'M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I' ]
    maks_rep  = [   3,    1,   1,    1,   3,    1,   1,    1,   1,    1,   1,    1,  3  ]

    count_eq = 0
    for i in range(len(S)):
        c = S[i]

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

        # Check for invalid 'lingatures'
        #print ("DBG: i=%d, len=%d" %(i, len(S)))
        if i+1 < len(S):
            c1 = S[i]
            idx1 = romans.index(S[i])
            c2 = S[i+1]
            idx2 = romans.index(S[i+1])
            #print ("DBG: c1=%s idx1=%d, c2=%s idx2=%d" %(c1, idx1, c2, idx2))
            if romans.index(S[i]) > romans.index(S[i+1]):
                # We have less-valued roman number preceeding greater-valued roman number
                # Now take the two and check against valid combinations
                lingature = S[i:i+2]
                if not lingature in romans:
                    print ("ERR: Invalid 'lingature':", lingature)
                    return False
                else:
                    print ("OK lingature", lingature)
            else:
                print ("OK? '%s'" %(S[i:i+2]), romans.index(c), romans.index(S[i+1]))
    return True

romans = [ "NEI", "IIII", "III", "VV", "VX", "IM", "XL", "IV" ]
for i in range(len(romans)):
    roman = romans[i]
    print ("Testing roman '%s' for validity" %(roman))
    print (isValidRoman(roman), "\n")
