import os

# In terminal de executat comanda: export PAROLA_SECRETA=abc123

passwd = input("Introdu parola: ")
passwd_sec = os.getenv("PAROLA_SECRETA")

if passwd == passwd_sec:
    print("Parola corectă")
else:
    print("Parola greșită")
