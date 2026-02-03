# Liste des étudiants avec leurs notes
students = [("Ali", 12), ("Fatou", 17), ("Moussa", 9), ("Awa", 14), ("Ibrahima", 7)]




somme = 0
for etudiant in students:
    nom = etudiant[0]
    note = etudiant[1]
    somme += note

moyenne = somme / len(students)


max = students[0][1]  
for etudiant in students:
    if etudiant[1] > max:
        max = etudiant[1]

min = students[0][1] 
for etudiant in students:
    if etudiant[1] < min:
        min = etudiant[1]

liste_admis = []
liste_ajournes = []

for etudiant in students:
    nom = etudiant[0]
    note = etudiant[1]
    
    if note >= 10:
        liste_admis.append(etudiant)
    else:
        liste_ajournes.append(etudiant)

print("\n")
print(f"Moyenne de la classe : ",moyenne)
print(f"Note maximale : ",max)
print(f"Note minimale : ",min)
print("\n")
print("--- Liste des ADMIS ---")
for etudiant in liste_admis:
    print(f"{etudiant[0]} : {etudiant[1]}/20")
print("\n")
print("--- Liste des AJOURNÉS ---")
for etudiant in liste_ajournes:
    print(f"{etudiant[0]} : {etudiant[1]}/20")
print("\n")