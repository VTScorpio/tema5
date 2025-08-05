import requests

with open("urls.txt", "r") as f:
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