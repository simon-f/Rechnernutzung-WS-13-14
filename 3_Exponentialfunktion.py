#####################################################
# Aufgabe 3: Exponentialfunktion
#
import math

print "Exponentialfunktion berechnen"
print "-----------------------------"
print 

# read number
entry = raw_input("Eine Zahl bitte: ")

# convert into float
try: 
    number = float(entry)
except ValueError as detail:
    print "Keine gueltige Zahl! (", detail, ")"
else:
    try:
        result = math.exp(number)
    except OverflowError as detail:
        print "Zahl ist zu gross! (", detail, ")" 
    else:
        print "Das Ergebnis lautet: ", math.exp(number)

# http://docs.python.org/2/library/sys.html#sys.float_info
# max_float = 1.7976931348623157e+308
# ==> max_input = ln(1.7976931348623157e+308) 
#               = 709.782712893
