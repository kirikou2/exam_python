
phrase = input("Entrez une phrase : ")

mots = phrase.split()
nombremots = len(mots)


long = ""
for mot in mots:
    if len(mot) > len(long):
        long = mot


nombre_voyelles = 0
for caractere in phrase:
    if caractere == 'a' or caractere == 'e' or caractere == 'i' or caractere == 'o' or caractere == 'u' or caractere == 'A' or caractere == 'E' or caractere == 'I' or caractere == 'O' or caractere == 'U':
        nombre_voyelles += 1
        
        phrasemod = ""
for mot in mots:
    if len(mot) % 2 == 0:  
        phrasemod += mot.upper() + " "
    else: 
        phrasemod += mot + " "

print(f"Nombre total de mots : ",nombremots)
print(f"Mot le plus long : ",long)
print(f"Nombre total de voyelles : ",nombre_voyelles)
print(f"Phrase modifiée : ",phrasemod)