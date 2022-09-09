names = ['Abu bakr','Umar','Usmon','Ali','Zubayr']
for nam in names:
   print(f"Assalomu alekum {nam}")
print(f'Kod {len(names)} marta takrorlandi.')


numbers = list(range(9,100,2))
for num in numbers:
    print(f"{num} ning kubi {num**3} ga teng.")


films = ('5 ta sevimli filmingizni kiriting: ')
kinolar = []
for k in range(5):
   kinolar.append(input(f"{k+1}- kinoni kiriting: "))
print(kinolar)

suhbat = int(input('Bugun nechta odam bilan suhbatlashdingiz? '))
ism = []
for i in range(suhbat):
    ism.append(input(f"{i+1}- ismni kiriting: "))
print(ism)
