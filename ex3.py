import sys
import os

if len(sys.argv) < 3:
    raise Exception("Oferiti nume și varsta ca argumente!")

nume = sys.argv[1]
varsta = int(sys.argv[2])

print(f"Au fost pasati {len(sys.argv) - 1} parametrii.")

if varsta > 18:
    os.makedirs(nume, exist_ok=True)
    print(f"Directorul '{nume}' a fost creat.")
