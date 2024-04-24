import pandas as pd

# Chargement du fichier CSV
df = pd.read_csv("dataset.csv")

# Initialisation d'un dictionnaire pour stocker les données
users_data = {}

# Parcours de chaque colonne du dataframe
for col in df.columns:
    # Récupération de l'intérêt et du sous-intérêt depuis le titre de la colonne
    interest, subinterest = col.split(":")

    # Parcours de chaque ligne de la colonne
    for index, value in df[col].items():
        # Vérification si le username est déjà dans le dictionnaire
        if value not in users_data:
            # Si le username n'est pas dans le dictionnaire, on l'ajoute avec un dictionnaire vide pour stocker les intérêts
            users_data[value] = {}

        # Vérification si l'intérêt est déjà dans les données de l'utilisateur
        if interest in users_data[value]:
            # Si l'intérêt est déjà dans les données de l'utilisateur, on ajoute le sous-intérêt à la liste existante
            users_data[value][interest].append(subinterest)
        else:
            # Si l'intérêt n'est pas dans les données de l'utilisateur, on crée une nouvelle liste avec le sous-intérêt
            users_data[value][interest] = [subinterest]

# Création d'une liste pour stocker les données de sortie
output_data = []

# Parcours du dictionnaire des données utilisateurs
for user, interests in users_data.items():
    # Création de la ligne de données pour le fichier de sortie
    user_interests = [
        f"{interest}: [{', '.join(subinterests)}]"
        for interest, subinterests in interests.items()
    ]
    output_data.append([user, user_interests])

# Création d'un dataframe à partir de la liste de données de sortie
output_df = pd.DataFrame(output_data, columns=["Username", "Interests"])

# Enregistrement du dataframe dans un nouveau fichier CSV
output_df.to_csv("output2.csv", index=False)
