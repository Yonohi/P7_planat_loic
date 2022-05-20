import csv
import time

while True:
    file = str(input("Veuillez rentrer le nom du fichier: "))

    # On commence le timer
    start = time.time()
    # Ouverture du fichier csv et filtrage des données
    actions = []
    try:
        with open(f"../P7_03_data/{file}", "r") as csvfile:
            reader = csv.reader(csvfile)
            # On saute la première ligne qui contient les noms des champs
            next(reader)
            for row in reader:
                row_float1 = float(row[1])
                row_float2 = float(row[2])
                if row_float1 <= 0 or row_float2 <= 0:
                    continue
                actions.append([row[0], row_float1, row_float2])
            break
    except FileNotFoundError:
        print("Le nom de fichier n'existe pas. "
              "Veuillez recommencer.")
print("longueur liste d'actions filtrées: ", len(actions))

# Algorithme optimisé
client_money = 500
actions_purchased = []
profit_euro = 0
actions_sorted = sorted(actions, key=lambda x: x[2], reverse=True)
for action in actions_sorted:
    if action[1] <= client_money:
        actions_purchased.append(action)
        client_money -= action[1]
        profit_euro += (action[1] * action[2]) / 100
    elif client_money == 0:
        break
    else:
        pass
# fin du timer
end = time.time()

# Résultats
actions_cost = sum([x[1] for x in actions_purchased])
print("Résultats")
print("temps total: ", end - start)
print("nombre d'actions achetées: ", len(actions_purchased))
print("liste des actions achetées: ")
for action in actions_purchased:
    print(action)
print("total cout actions: ", round(actions_cost, 2))
print("bénéfices en euro: ", round(profit_euro, 2))
print("bénéfices en %: ", round((profit_euro / actions_cost) * 100, 2))
