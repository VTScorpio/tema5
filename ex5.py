with open("logs.txt", "r") as f:
    for index, linie in enumerate(f, 1):
        if "ERROR" in linie:
            print(f"Linia {index}: {linie.strip()}")
