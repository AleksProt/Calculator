# from functions import summe, multiplikation, subtraktion
import sys
from functions import arithmetics
from functions import geo



# negativ beispiele: könnte konflikt mit anderen funktionen geben:
#from functions import summe
#from .arithmetics import *


# Konstanten in Python werden groß geschrieben. Konvention!
OPERATIONS = {
    '+': arithmetics.summe,
    '*': arithmetics.multiplikation,
    '-': arithmetics.subtraktion,
    'dist': geo.distance,
}

#print("Name des Dokuments: ", _name_)

def controller(operator, a, b):
    #   operator z.b. +
    op = OPERATIONS.get(operator)
    # op = summe
    if op:
        return op(a, b)
    raise NotImplementedError("Diese Operation ist nict implementiert")


def parse_user_input(user_input):
    """Zerlege den userinput in seine Bestandteile
    Beispiel Userinput: + 3 43
    Args:
    user_input(str): die Usereingabe
    Returns:
        tuple: (operator, operand, operand)
    """
    user_input = user_input.split()  # ['+', '3', '43']
    operator = user_input.pop(0)
    a, b = float(user_input[0]), float(user_input[1])
    return operator, a, b


def main():
    """ Hauptprogramm. Heir wird der User-Input verarbeitet. Abruch mit_quit"""
    while True:
        msg = "Bitte Berechnung eingeben (Operator und 2 Operanden): "
        user_input = input(msg)

        if user_input in ["_quit", "_exit"]:
            print("Danke. Programm beendet")
            break
        operator, a, b = parse_user_input(user_input)
        result = controller(operator, a, b)
        print("Ergebnis: ", result)


main()