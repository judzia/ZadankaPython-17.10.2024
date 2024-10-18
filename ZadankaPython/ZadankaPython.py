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

