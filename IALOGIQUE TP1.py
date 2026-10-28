
def chainage_avant(faits, regles):
    faits = set(faits)
    changement = True

    while changement:
        changement = False

        for conditions, conclusion in regles:
            if conditions.issubset(faits) and conclusion not in faits:
                faits.add(conclusion)
                changement = True

    return faits



def chainage_arriere(but, faits, regles):
    if but in faits:
        return True

    for conditions, conclusion in regles:
        if conclusion == but:
            if all(chainage_arriere(c, faits, regles)
                   for c in conditions):
                return True

    return False



def fermeture(faits, regles):
    fermeture_faits = set(faits)

    while True:
        nouveaux_faits = set()

        for conditions, conclusion in regles:
            if conditions.issubset(fermeture_faits):
                if conclusion not in fermeture_faits:
                    nouveaux_faits.add(conclusion)

        if not nouveaux_faits:
            break

        fermeture_faits.update(nouveaux_faits)

    return fermeture_faits


# Exercice 02 : Badge et porte


faits = {"badge_valide_Lina", "agent_ouvre_manuellement"}

regles = [
    ({"badge_valide_Lina"}, "porte_ouverte"),
    ({"agent_ouvre_manuellement"}, "porte_ouverte")
]

# Chaînage avant
def chainage_avant(faits, regles):
    faits = set(faits)
    changement = True

    while changement:
        changement = False
        for conditions, conclusion in regles:
            if conditions.issubset(faits) and conclusion not in faits:
                faits.add(conclusion)
                changement = True
    return faits

# Vérification
resultat = chainage_avant(faits, regles)

print("1. La porte s'ouvre pour Lina :", 
      "porte_ouverte" in resultat)

print("2. La porte est ouverte, donc badge valide présenté ?",
      "Non, pas nécessairement.")

# 3. Contre-exemple : ouverture manuelle sans badge valide
faits2 = {"agent_ouvre_manuellement"}
resultat2 = chainage_avant(faits2, regles)

print("3. Contre-exemple :")
print("Porte ouverte :", "porte_ouverte" in resultat2)
print("Badge valide présenté :", "badge_valide_Lina" in resultat2)


