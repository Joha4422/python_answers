akam = {'ism':'Jamshid','t_yil':'1985','t_joyi':'Sherobod'}
print(f"{akam['ism']}, {akam['t_yil'].title()} yilda {akam['t_joyi'].title()} shahrida tug'ulgan. ")


dishes = {'onam':'tiftel','akam':'somsa','men':'mastava','opam':'manti','opam2':'shashlik'}
print(f"Onamning sevimli taomi {dishes['onam']}")
print(f"Akamning sevimli taomi {dishes['akam']}")
print(f"Mening sevimli taomim {dishes['men']}")


python = {
    'str':'matn',
    'int':'butun son',
    'list':'royhat',
    'tuple':'ozgarmas royhat',
    'float':'onlik son',
    'or':'yoki',
    'for':'uchun',
    'if':'ichida',
    'and':'yoki'
    }
kalit = input("Kalit so'zni kiriting: ").lower()
print(python.get(kalit,"Bunday so'z mavjud emas"))


python = {
    'str':'matn',
    'int':'butun son',
    'list':'royhat',
    'tuple':'ozgarmas royhat',
    'float':'onlik son',
    'or':'yoki',
    'for':'uchun',
    'if':'ichida',
    'and':'yoki'
    }
kalit = input("Kalit so'zni kiriting: ").lower()
tarjima = python.get(kalit)
if tarjima ==None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi.")

















        
   
