# zad 1

temp = float(input("Podaj temperature w Kelwinach: "))
liczba_neutronow = float(input("Podaj liczbe neutronow: "))


def is_criticality_balanced(temp, liczba_neutronow):

    iloczyn=temp*liczba_neutronow

    temperatura_ok = temp < 800
    liczba_neutronow_ok = liczba_neutronow >500
    iloczyn_ok=iloczyn < 500000

    return temperatura_ok and liczba_neutronow_ok and iloczyn_ok #da false przy conajmniej jednym nieprawidlowym

print(is_criticality_balanced(temp, liczba_neutronow))

# zad 2

current=float(input("Podaj natezenie pradu: "))
voltage=float(input("Podaj napiecie elektryczne: "))
theoretical_max_power=float(input("Podaj teorytyczna moc maksymalna: "))

def reactor_efficiency(voltage, current, theoretical_max_power):

    generated_power = voltage * current

    wartosc = (generated_power/theoretical_max_power)*100
    if wartosc>=80.:
        return "zielony"
    elif 60<=wartosc<80:
        return "pomaranczowy"
    elif 30<=wartosc<60:
        return "czerwony"
    else:
        return "czarny"

print(reactor_efficiency(voltage, current, theoretical_max_power))



    
