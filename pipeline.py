import pandas as pd

# chargement des csv
transactions = pd.read_csv("data/raw/transactions.csv")
clients = pd.read_csv("data/raw/clients.csv")

# Nombre de lignes et colonnes
print(transactions.shape)

# Types de chaque colonne
print(transactions.dtypes)

# 5 premières lignes
print(transactions.head(5))

# Nombre de valeurs nulles par colonne
print(transactions.isnull().sum())

# Uniquement les transactions de type 'achat'
transactions_achat = transactions[transactions["type"] == "achat"]

# Uniquement les colonnes : client_id, montant, categorie
transactions_cols = transactions[["client_id", "montant", "categorie"]]

# Les transactions où montant > 200 ET statut == 'validé'
transacations_filtre = transactions[
    (transactions["montant"] > 200) & (transactions["statut"] == "validé")
]

# Calcule de Total des montants, Moyenne des montants, Nombre de transactions

calcule = (
    transactions.groupby("categorie")
    .agg(
        total_montants=("montant", "sum"),
        moyenne_montants=("montant", "mean"),
        nb_transactions=("categorie", "count"),
    )
    .reset_index()
)
print(calcule)

# jointure

transactions_clients_inner = pd.merge(
    transactions, clients, on="client_id", how="inner"
)

transactions_clients_left = pd.merge(transactions, clients, on="client_id", how="left")

transactions_clients_left[transactions_clients_left["nom"].isnull()]

# Supprissions des lignes avec plus de 3 valeurs nulles
transactions_clean = transactions.dropna(thresh=5)

# Remplacer  les montants nulls par la médiane
transactions_clean["montant"] = transactions_clean["montant"].fillna(
    transactions_clean["montant"].median()
)

transactions_clean["ville"] = transactions_clean["ville"].fillna("Inconnu")

# Création de nouvelles colonnes

transactions_clean["frais"] = (transactions_clean["montant"] * 0.015).round(2)
transactions_clean["montant_net"] = (
    transactions_clean["montant"] - transactions_clean["frais"]
)

transactions_clean["niveau"] = transactions_clean["montant"].apply(
    lambda x: "premium" if x > 500 else "standard"
)

# Normalisation
transactions_clean["categorie"] = (
    transactions_clean["categorie"].str.strip().str.lower()
)

# Converssion en datetime
transactions_clean["date"] = pd.to_datetime(transactions_clean["date"])

# Export
transactions_clean.to_csv("data/export/transactions_clean.csv", index=False)
transactions_clean[transactions_clean["niveau"] == "premium"].to_excel(
    "data/export/transactions_premium.xlsx", index=False, sheet_name="premium"
)
transactions_clean.to_json(
    "data/export/transactions_cleans.json",
    orient="records",
    indent=2,
    force_ascii=False,
)

print("✅ Exports terminés")
