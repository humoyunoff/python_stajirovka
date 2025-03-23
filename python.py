# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 08:09:13 2025

@author: user
"""

# 14-dars lug'atlar bilan ishlash
# otam(onam,akam,ukam va hokozo) degan ruyxat yurating va ruyxatdagi har bir odamga 3 tadan 
# ma'lumot kirinting.

# oilam = {'otam':{'ism':'Jon','t_yil':1934,'t_joy':'Surxondaryo'},
#          'onam':{'ism':'Jane','t_yil':1936,'t_joy':'Surxondaryo'},
#          'akam':{'ism':'Bob','t_yil':1998}}
# print("Otam ",oilam['otam']['ism'], oilam['otam']['t_yil'], 
#       " yil",oilam['otam']['t_joy'], " viloyatida tug'ugan.")


# foydalanuvchi = {}
# foydalanuvchi['ism'] = input("Ismingiz: ")
# foydalanuvchi['yosh'] = int(input("Yoshingiz: "))
# foydalanuvchi['shahar'] = input("Shahringiz: ")
# # print(f"Salom {foydalanuvchi['ism'].title()} \
# #       {foydalanuvchi['yosh']} yosh {foydalanuvchi['shahar'].title()}da tug'ulgan.")
# print(f"Salom {foydalanuvchi['ism'].title()}! Siz {foydalanuvchi['shahar']}da yashaysiz.")

# narhlar = {'olma':10000,'olcha':12000,'non':4000}
# buyurtma = input("Nimani sotib olasiz?: ")

# if buyurtma in narhlar:
#     print(f"{buyurtma.title()} narxi {narhlar[buyurtma]} so'm.")
# else:
#     print("Bunaqa mahsulot yuq")

# telefon kitobi meni loyiha

# kantakt = {}
# kantakt['ism'] = input("Ismingiz: ")
# kantakt['raqam'] = int(input("Raqamingiz: "))

# telefon_kitobi = {}

# ism = input("Kantakt ismini kiriting: ")
# raqam = input("Kantakt raqamini kiriting: ")
# telefon_kitobi[ism] = raqam
# print("Telefon kitobi:")
# print(telefon_kitobi)

# kantaktlar = {
#     'umar':'+998994667399',
#     'fahriddin':'+998996774967',
#     'akam':'+998935593955'}
# while True:
#     ism = input("Kontakt ismi: ")
#     raqam = input("Telefon raqam: ")
#     kantaktlar[ism] = raqam
#     yana = input("Yana kantakt qushsizmi? (ha\yo\'q): ")
#     if yana.lower() != 'ha':
#         break
    
# qidiruv = input("Kimning raqamini qidirasiz: ")
# if qidiruv in kantaktlar:
#     print(f"{qidiruv.title()}ning raqami {kantaktlar[qidiruv]}")

# o'chirish funksiyasi
# kantaktlar = {
#     'umar':'+998994667399',
#     'fahriddin':'+998996774967',
#     'akam':'+998935593955'}
# # qo'shish
# while True:
#     ism = input("Kantaktning ismi: ")
#     raqam = input("Kantakt raqami: ")
#     kantaktlar[ism] = raqam
#     yana = input("Yana kantakt qushasizmi? (ha\yo'q)")
#     if yana.lower() != 'ha':
#         break
# print("\nKantaktlar: ")
# for ism, raqam in kantaktlar.items():
#     print(f"{ism.title()} - {raqam}")
# # # qidiruv
# while True:
#     qidiruv = input("Kimni raqamini qidiryapsiz? (chiqish uchun 'exit') ").lower()
#     if qidiruv.lower() == 'exit':
#         break
#     if qidiruv in kantaktlar:
#         print(f"{qidiruv.title()}ning raqami {kantaktlar[qidiruv]}")
#     else:
#         print(f"{qidiruv.title()} unaqa kantakt mavjud emas!")

# # # uchirish
# while True:
#     ochir = input("Kimni o'chirmoqchisiz, (chiqish uchun 'exit')").lower()
#     if ochir.lower() == 'exit':
#         break
#     if ochir in kantaktlar:
#         del kantaktlar[ochir]
#         print(f"{ochir.title()} kantakt o'chirildi.")
#     else:
#         print(f"{ochir.title()} kantakt topilmadi.")

# # tahrirlash 
# while True:
#     tahrir = input("\nKimni raqamini tahrirlamoqchisiz? (chiqish uchun 'exit') ").lower()
#     if tahrir.lower() == 'exit':
#         break
#     if tahrir in kantaktlar:
#         yangi_raqam = input(f"{tahrir.title()}ning yangi raqamini kiriting: ")
#         kantaktlar[tahrir] = yangi_raqam
#         print(f"{tahrir.title()}ning raqami yangilandi.")
#     else:
#         print(f"{tahrir.title()}ning raqami topilmadi.")    
    
# print("\nYangilangan kantaktlar: ")
# for ism, raqam in kantaktlar.items():
#     print(f"{ism.title()} - {raqam}")


# oila a'zolaringizni sevimli taomlari ruyxatini tuzing. Ruyxatda kamida 5 ta oila-taom 
# juftligi bo'lsin. Kamida 3 kishining sevimli taomini konsolga chiqaring.
# oilam = {
#     'dada':{'otam':'Qaynatma shurva'},
#     'akam':{'akam':'shashlik'},
#     'opam':{'opam':'manti'},
#     'xumbosh':{'abdulloh':'kartoshka qovurma'}
#     }

# for azo, taom in oilam.items():
#     print(f"{azo.title()}ning sevimli taomi {taom}")
#     # lugat = input("Kalit so'zni kiriting: ").lower()
    # if lugat in oilam:
    #     print(f"Siz suragan {lugat.title()}ning sevimli taomi {taom}")
    # else:
    #     print("Unaqa oila a'zoyim yuq.")

# oilam = {
#     'otam':'Qaynatma shurva',
#     'akam':'shashlik',
#     'opam':'manti',
#     'abdulloh':'kartoshka qovurma'}
# print(oilam['otam'])

    
# otam = {'ismi':'mavlutdin', 'tyil':1954,'viloyat':'samarqand'}
# tyil = otam['tyil']
# vil = otam['viloyat']
# ism = otam['ismi']
# print(f"Otamning ismi {ism.title()}, {tyil}-yilda, {vil.title()} viloyatida tug'ilgan")

# taomlar = {
#     'ali':'osh',
#     'vali':'shashlik',
#     'hasan':"lag'mon",
#     'husan':"mastava",
#     'olim':"somsa"
#     }

# taom = taomlar['ali']
# print(f"Alining sevimli taomi {taom}")

# python_izohli_lugati = {
#     'integer':"Butun son",
#     'float':"O'nlik son",
#     'string':"Matn",
#     'list':"Ro'yxat",
#     'tuple':"O'zgarmas ro'yxat"}
# print(python_izohli_lugati['tuple'])
# # 1
# kalit = input("Kalit so'z kiriting:").lower()
# print(python_izohli_lugati.get(kalit,"Bunday so'z mavjud emas"))
# # 2
# kalit = input("Kalit so'z kiriting:").lower()
# tarjima = python_izohli_lugati.get(kalit)
# if tarjima==None:
#     print("Bunday so'z mavjud emas")
# else:
#     print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")