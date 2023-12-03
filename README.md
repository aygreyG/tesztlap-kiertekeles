# tesztlap-kiertekeles

## Feladat specifikáció
Egy tesztlap kiértékelő algoritmust kell kifejleszteni, amelynek célja meghatározni a beszkennelt tesztlapok pontszámát.
A tesztlap tartalmazza a következőket:
- Kép a kitöltött tesztlapról: Ez egy digitális kép, amelyen látható a kitöltött tesztlap, amelyeken a diákok/hallgatók igaz-hamis és feleletválasztós kérdésekre adtak választ.
- Megoldókulcs: Egy referencia dokumentum vagy adatsor, amely tartalmazza a helyes válaszokat a tesztlap összes kérdésére.

## Megvalósítási terv
1. A képeken azonosítani kell az egymástól különálló szövegrészeket, így kapunk kisebb képeket
2. A kisebb képeken a szöveget azonosítani kell, így Stringeket kapunk
3. A Stringeket osztályozni kell (pl kérdés, utasítás, válasz), amiből a válaszokat kell kiválasztani, a kérdés szerintem csak egy anchor lesz, amivel a válaszok helyét határozzuk meg.
4. A helyes válasz(oka)t aláhúzással, ikszeléssel, bekarikázással stb. jelölik és ennek a detektálását kellene megvalósítani, ekkor kapunk egy listát a megjelölt válaszokról
5. A megjelölt válaszokat a megoldókulcs alapján összevetjük és megkapjuk a tesztlap pontszámát.
6. Az eredményt vizualizáljuk, a pontszám mellett visszaadjuk a tesztlapot is úgy, hogy a script rárajzolja az azonosított részeket, bekeretezi különböző színű téglalapokkal.

# Tesseract letöltési útmutató
https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.3.0.20221214.exe

# Állomány futattása
``` pip install -r requirements.txt ```
