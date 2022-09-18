# Debemos instalar las siguientes librerías
# pip install langdetect

from langdetect import detect

text = input("Ingresa el texto del lenguaje que quieras identificar: ")
print(detect(text))

'''
langdetect supports 55 languages out of the box (ISO 639-1 codes):

af, ar, bg, bn, ca, cs, cy, da, de, el, en, es, et, fa, fi, fr, gu, he,
hi, hr, hu, id, it, ja, kn, ko, lt, lv, mk, ml, mr, ne, nl, no, pa, pl,
pt, ro, ru, sk, sl, so, sq, sv, sw, ta, te, th, tl, tr, uk, ur, vi, zh-cn, zh

''''
