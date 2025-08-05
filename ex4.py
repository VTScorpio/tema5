import requests
import sys  
import os

if len(sys.argv)>2:
    print("Eroare. Sintaxa corecta python3 ex4.py <fisier_urls>")
    sys.exit(1)

file_name = sys.argv[1]

if not os.path.isfile(file_name):
    print("Eroare. Fisierul nu exista")
    sys.exit(1)

print(file_name)    


with open(file_name, "r") as f:
    urls = [linie.strip() for linie in f if linie.strip()]

with open("success.txt", "w") as success_file, open("errors.txt", "w") as error_file:
    for url in urls:
        try:
            response = requests.get(url, timeout=5)
            status = response.status_code
            if 200 <= status <= 299:
                success_file.write(f"{url} - {status}\n")
            else:
                error_file.write(f"{url} - {status}\n")
        except requests.RequestException as e:
            error_file.write(f"{url} - EXCEPTIE: {e}\n")

print("Verificarea a fost terminata.")