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
           #print ("DEBUG: Got operator %s, convert %s to arabic" %(S[i], ledd))
           verdi = AlGoreRythm(ledd)
           hele_uttrykket = hele_uttrykket + str(verdi) + S[i]
           stack.append(str(verdi))
           if len(stack) == 3:
               print ("DEBUG: got 3 elements, stack = ", stack)
               ans = eval(str(''.join(stack)))
               stack = [str(ans)]
               print ("DEBUG: evaluated stack, new is: ", stack, "\n")
           stack.append(str(S[i]))
           print ("DEBUG: Operator! ledd is %s, verdi is %d, exp = %s, stack = " %(ledd, verdi, hele_uttrykket), stack)
           ledd = ''
       else:
           ledd = ledd + S[i]
           #print ("DEBUG: Not operator, ledd is %s" %(ledd))
    # Haandter siste ledd
    verdi = AlGoreRythm(ledd)
    stack.append(str(verdi))
    ans = eval(str(''.join(stack)))
    print ("DEBUG: last 3 elements, stack = ", stack)
    hele_uttrykket = hele_uttrykket + str(verdi)
    return [hele_uttrykket, ans]

#roman = "XXIX"
roman = "XXIX+V-IV*II/III" # 29+5-4*2/3
#arabic = AlGoreRythm(roman)
arabic = do_calc(roman)

print ("\n\n%s = %s" %(roman, arabic[0]))
print ("'rpn' %s = %d" %(arabic[0], arabic[1]))
print ("eval hele_uttrykket: %s = %d" %(arabic[0], eval(arabic[0])))
