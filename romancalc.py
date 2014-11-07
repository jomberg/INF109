#!/usr/bin/python3

def AlGoreRythm(S):
    viktige_rometall = [ "M",  "CM",  "D",  "CD", "C",  "XC",   "L",  "XL",  "X",  "IX", "V",  "IV", "I" ]
    viktige_verdier = [ 1000,900,500,400,100,90,50,40,10,9,5,4,1 ]
    verdi = 0
    indeks = 0
    for i in range(len(viktige_rometall)):
        lengde = len(viktige_rometall[i])
        while S[indeks:(indeks+lengde)] == viktige_rometall[i]:
            verdi = verdi + viktige_verdier[i]
            indeks = indeks + lengde
    return verdi
    
def do_calc(S):
    hele_uttrykket = ''
    ledd = ''
    stack = []
    operatorer = [ "+", "-", "*", "/" ]
    for i in range(len(S)):
       #print("DEBUG: Testing %s" %(S[i]))
       if S[i] in operatorer:
           op = S[i].replace('/', '//') # Change division to floor (or integer) division
           #print ("DEBUG: Got operator %s, convert %s to arabic" %(S[i], ledd))
           verdi = AlGoreRythm(ledd)
           hele_uttrykket = hele_uttrykket + str(verdi) + S[i]
           stack.append(str(verdi))
           if len(stack) == 3:
               #print ("DEBUG: got 3 elements, stack = ", stack)
               ans = eval(str(''.join(stack)))
               stack = [str(ans)]
               #print ("DEBUG: evaluated stack, new is: ", stack, "\n")
           stack.append(str(op))
           #print ("DEBUG: Operator! ledd is %s, verdi is %d, exp = %s, stack = " %(ledd, verdi, hele_uttrykket), stack)
           ledd = ''
       else:
           ledd = ledd + S[i]
           #print ("DEBUG: Not operator, ledd is %s" %(ledd))
    # Haandter siste ledd
    verdi = AlGoreRythm(ledd)
    stack.append(str(verdi))
    ans = eval(str(''.join(stack)))
    #print ("DEBUG: last 3 elements, stack = ", stack)
    hele_uttrykket = hele_uttrykket + str(verdi)
    return [hele_uttrykket, ans]

def to_roman(N):
    viktige_rometall = [ "M",  "CM",  "D",  "CD", "C",  "XC",   "L",  "XL",  "X",  "IX", "V",  "IV", "I" ]
    viktige_verdier = [ 1000,900,500,400,100,90,50,40,10,9,5,4,1 ]
    romanstr = ''
    for i in range(len(viktige_verdier)):
        while N >= viktige_verdier[i]:
            romanstr = romanstr + viktige_rometall[i]
            N = N - viktige_verdier[i] 
    return romanstr

def isValidRoman(S):
    operators = [ '+', '-', '*', '/' ]
    romans    = [ 'M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I' ]
    maks_rep  = [   6,    1,   1,    1,   3,    1,   1,    1,   3,    1,   1,    1,  3  ]
    idx_check = []
    count_eq = 0
    i = 0
    while i < len(S):
        c = S[i]

        if c in operators:
            # Skip check of operators, jump to next char
            #print ("Skip operator ", c)
            i = i + 1
            idx_check = []
            count_eq = 0
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
                    #print ("OK 'lingature': '%s'" %(lingature))
                    i = i + 1 # Skip ahead
            #else:
                #print ("OK? '%s'" %(S[i:i+2]), romans.index(c), romans.index(S[i+1]))

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

######################################################################################

#roman = "XXIX"
#roman = "XXIX+V-IV*II/III" # 29+5-4*2/3
#roman = "V/II" # 5/2 -> 2.5, 5//2 -> 2
test_romans = [ "NEI", "IIII", "III", "VV", "VX", "IM", "XL", "IIV", "IV", "XXIX", "XXIV+V-IV*II/III", "V/II", "CXIII*III+MMI", "MMCCCXL", "MMCCCXLIIII", "MMMMM", "I-X" ]
#roman = input('Enter expression to calculate in roman numbers: ')
for i in range(len(test_romans)):
   roman = test_romans[i]
   print ("\nExpression is '%s'" %(roman))
   arabic = do_calc(roman)
   #print ("Testing roman '%s' for validity" %(roman))
   #print (isValidRoman(roman), "\n")
   if not isValidRoman(roman):
      continue
   romanstr = arabic[1]
   if romanstr < 1:
      print ("ERR: UNDERFLOW")
      continue
   elif romanstr > 3999:
      print ("ERR: OVERFLOW")
      continue
   else:
       romanstr = to_roman(romanstr)

   print ("%s = %s, which is %s" %(roman, arabic[0], romanstr))
   #print ("'rpn' %s = %d, which is %s" %(arabic[0], arabic[1], romanstr))
   #print ("eval hele_uttrykket: %s = %d, which is %s" %(arabic[0], eval(arabic[0], romanstr)))
