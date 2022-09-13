number = int(input('juft son kiriting: '))
if number%2:
    print("Bu juft son emas") 
else:
    print("Rahmat")

yosh = int(input('Yoshingiz nechchida? '))
if yosh<=4 or yosh>=60:
      narh = 0
elif yosh<=18:
      narh = 8000
elif yosh<=30:
      narh = 10000 
else:
      narh = 12000
print(f"Sizga kirish {narh} so'm!")


x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting: "))
if x==y:
    print(f"{x} = {y}")
elif x<y:
    print(f"{x} < {y}")
else:
    print(f"{x} > {y}")


products= ["suv","non","go'sht","olma","anor","tarvuz","qovun","sabzi","piyoz"]
basket = []
for n in range(5):
    basket.append(input(f"{n+1}- mahsulotni kiriting: "))
for bas in basket:
    if bas in products:
        print(f"Do'konda {bas} bor,")
    else: print(f"Do'konda {bas} yoq. ")


products = ["suv","non","go'sht","tarvuz","qovun","uzum","olma","gilos"]
basket = []
for n in range(5):
    basket.append(input(f"{n+1}- mahsulotni kiriting: "))
bor_mahsulotlar =[]
yoq_mahsulotlar = []
for bas in basket:
    if bas in products:
        bor_mahsulotlar.append(bas)
    else:
        yoq_mahsulotlar.append(bas)
if yoq_mahsulotlar:
    print("Siz so'ragan quydagi mahsulotlar do'konda yo'q.")
    for bas in yoq_mahsulotlar:
        print(bas)
else:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor.")


users = ['Abu bakr','Umar','Usmon','Ali','Xolid']
login = input("Yangi login kiriting: ")
if login.title() in users:
    print("Kechirasiz bu login band!")
else:
    print("Xush kelibsiz,foydalanuvchi!")


son = int(input("Istalgan butun son kiriting: "))
for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")





















        
   
