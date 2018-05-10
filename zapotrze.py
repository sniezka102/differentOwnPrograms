#!user/bin/env python
# encoding: utf-8

# podstawa = 10 * masaCiala + 6.25 * wzrost [cm] -5 * wiek + S
#S dla kobiety = -161, dla mężczyzny +5

#oblicenie zapotrzebowania kalorycznego na same procesy życiowe, w tym przypadku
# podstawę należy przemnożyć przez rodzaj aktywnosci fizycznej
# praca siedząca = 1.2
# praca niefizyczna, mało katywny tryb życia = 1.4
# lekka praca fizyczna, ćwiczenia około 5h w tygodniu = 1.6
# praca fizyczna, regularne ćwiczenia od 5 do 7 razy w tygodniu = 1.8
# praca fizyczna-ciężka, regularne ćwiczenia 7 razy w tygodniu = 2.0

#przekazane argumenty masaCiala[kg], wzrost[cm], wiek, plec, aktywnosc

import sys
import datetime
now = datetime.datetime.now()

#print(sys.argv)

userData = []

for x in sys.argv:
	userData.append(x)

#print(userData)
#print(now.year)

waga = float(userData[1])
wzrost = int(userData[2])
wiek = userData[3]
wiek = now.year - int(wiek)
plec = userData[4]
aktywnosc = float(userData[5])

if plec == 'K' or plec == 'k':
	plec = 'kobieta'
	S = -161
elif plec == 'M' or plec == 'm':
	plec = 'mezczyzna'
	S = 5
else:
	print('you should use k or m')
	plec = 'wrong'
	S = 0


# print('waga = ',waga, ' ','wzrost = ', wzrost, ' ','wiek = ', wiek ,' ', 'plec = ', plec, ' ','aktywnosc = ', aktywnosc,)

zapotKaloryczne = round(aktywnosc * (10 * waga + 6.25 * wzrost - 5 * wiek + S),2)
BMI = waga / (wzrost/100)**2

print('zapotrzebowanie kaloryczne = ',zapotKaloryczne)
print('BMI = ', int(BMI))

if BMI<= 16.0 and plec == 'kobieta':
	print('wyglodzenie!!!')
elif BMI <=18.5 and plec == 'mezczyzna':
	print('niedowaga!!!!')
elif BMI>16.0 and BMI <= 17 and plec == 'kobieta':
	print('wychudzenie')
elif BMI>18.5 and BMI<=25.0 and plec == 'mezczyzna':
	print('waga prawidłowa - GRATULACJE')
elif BMI>17 and BMI <=18.5:
	print('niedowaga')
elif BMI>18.5 and BMI<=25.0:
	print('wartość prawidłowa - GRATULACJE')
elif BMI>25.0 and BMI<=30.0:
	print('nadwaga - czas pomyśleć o sobie')
elif BMI>30.0 and BMI<=35.0:
	print('I stopień otyłości')
elif BMI>35.0 and BMI<=40:
	print('II stopień otyłości')
else:
	print('III stopień otyłości!!!!!')
