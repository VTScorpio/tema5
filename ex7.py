import time
import requests
import sys
from urllib.parse import urlparse
import math

# funcție ce primește ca parametru un url și întoarce timpul de răspuns al paginii (cat dureaza sa primim un răspuns).
def rx(url):
    start = time.time()
    try:
        requests.get(url,timeout=5)
    except:
        return float("inf")
    end = time.time()
    return round((end - start) * 1000, 2)

#funcție ce primește doi parametrii (un url si un numar de repetari)
def mon(url, bis):
    count = 0
    term = []
    for _ in range(bis):
        t = rx(url)
        term.append(t)
        count=count+1
        print(f"Response {count} :  {f'[!] URL-ul {url} nu a răspuns.' if math.isinf(t) else f'{t} ms'}")
        time.sleep(2)
    # Verific daca nu a fost raspuns in date de tip float , atunci voi returna FAIL.  
    if all(math.isinf(x) for x in term):
        return "FAIL"    
    # Rezultat functie timp minim, media aritmetica, timp maxim    
    return (min(term), sum(term)/len(term), max(term))

def url_validation (url):
    validation=urlparse(url)
    return all([validation.scheme in ("http","https"), validation.netloc])


#Verificare sintaxa si argumente  
if len(sys.argv) < 3:
    print("Sintaxa corecta: python3 ex7.py <url> <repetari>")
    sys.exit(1)

#Verificare adresa web corecta
url = sys.argv[1]
if not url_validation(url):
    print("Eroare: URL Invalid. Exemplu valid: https://google.com")
    sys.exit(1)

#Verificare argumet 2 daca este numar intreg
#Verificare numar de verificari adresa url
try:
    bis=int(sys.argv[2])
    if bis > 20:
        print("Atentie: nu mai mult de 20 verificari.")
        sys.exit(1)
    elif bis < 3:
        print("Atentie: nu mai putin de 3 verificari.")
        sys.exit(1)    
except ValueError:
    print("Eroare: Al doilea argument este important sa fie numar intreg")
    sys.exit(1)

result = mon(url, bis)
if result == "FAIL":
    print(f"[!] URL-ul {url} nu a răspuns.")
else:
    print(f"Result = Min: {result[0]} ms, Med: {result[1]:.2f} ms, Max: {result[2]} ms")
