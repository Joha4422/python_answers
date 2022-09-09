cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car != 'gm':
        print(car.title())
    else:
        print(car.upper())


login = input('loginingiz nima? ')
if login.lower() == 'admin':
     print(f"Hush kelibsiz {login},foydalanuvchilar ro'yhatini ko'rasizmi?  ")
else:
     print(f"Hush kelibisz {login.title()}")
          

son1 = float(input("Birinchi sonni kiriting: "))
son2 = float(input("Ikkinchi sonni kiriting: "))
if son1 == son2:
    print(f" Sonlar teng{son1} = {son2}")


son = float(input("Istalgan son kiriting: "))
print("Son manfiy") if son<0 else print("Son musbat")

son = float(input("Istalgan son kiriting: "))
print(son**(1/2)) if son>0 else print("Musbat son kiriting!")

      
