text = "Salut"
numar = 42
adevar = True
nimic = None
lista = [1, 2, 3]
multime = {1, 2, 2, 3}
dictionar = {"cheie": "valoare"}
tuplu = (1, 2, 3)

print(type(text), text)
print(type(numar), numar)
print(type(adevar), adevar)
print(type(nimic), nimic)
print(type(lista), lista)
print(type(multime), multime)
print(type(dictionar), dictionar)
print(type(tuplu), tuplu)

documentatie = f"""
Variabila text este de tipul {type(text)} și are valoarea {text}
Variabila numar este de tipul {type(numar)} și are valoarea {numar}
Variabila adevar este de tipul {type(adevar)} și are valoarea {adevar}
Variabila nimic este de tipul {type(nimic)} și are valoarea {nimic}
Variabila lista este de tipul {type(lista)} și are valoarea {lista}
Variabila multime este de tipul {type(multime)} și are valoarea {multime}
Variabila dictionar este de tipul {type(dictionar)} și are valoarea {dictionar}
Variabila tuplu este de tipul {type(tuplu)} și are valoarea {tuplu}
"""

print(documentatie)
