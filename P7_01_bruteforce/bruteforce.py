from itertools import combinations
import time
import csv

while True:
    file = str(input("Veuillez rentrer le nom du fichier: "))

    # On commence le timer
    start = time.time()
    # Ouverture du fichier csv et filtrage des données
    actions = []
    client_money = 500
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
# On cherche la valeur maximum d'actions à acheter
actions_by_cost = sorted(actions, key=lambda x: x[1])
n = 0
for action in actions_by_cost:
    if action[1] <= client_money:
        client_money -= action[1]
        n += 1
    else:
        break


def calcul_profit(liste):
    """
    A function that calculates the profits
    :param liste: list of actions
    :return: profit in euro after 2 years of the list of actions
    """
    profit_euro = 0
    for element in liste:
        profit_euro += (element[1] * element[2]) / 100
    return profit_euro


# Algorithme brute force
profit_max = 0
actions_purchased = list
for number in range(1, n+1):
    for combination in combinations(actions, number):
        profit = calcul_profit(combination)
        if sum([x[1] for x in combination]) <= 500 \
                and profit > profit_max:
            profit_max = profit
            actions_purchased = combination

# fin du timer
end = time.time()

# Résultats
actions_cost = sum([x[1] for x in actions_purchased])
print("Résultats")
print("Nombre maximum d'actions : ", n)
print("temps: ", end-start, "s")
print("nombre d'actions achetées: ", len(actions_purchased))
print("liste des actions achetées: ")
for action in actions_purchased:
    print(action)
print("Cout des actions : ", round(actions_cost, 2))
print("Bénéfices en euro : ", round(profit_max, 2))
print("Bénéfices  en pourcentage :",
      round((profit_max / actions_cost) * 100, 2))
