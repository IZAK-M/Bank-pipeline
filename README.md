# 🏦 Bank-pipeline

Pipeline de nettoyage, transformation et préparation analytique de données bancaires

Bank‑pipeline est un mini-projet pour illustrer la construction d’un pipeline de données complet appliqué à un fichier brut de transactions bancaires (transaction.csv).
L’objectif est de convertir une source brute, hétérogène et parfois incohérente en un dataset propre, structuré et directement exploitable pour l’analyse ou la visualisation.

## Stack

- Python 3.13.5
- Pandas 2.3.2

## Structure
```text
bank-pipeline/
├── data/
│   ├── raw/
│   │   └── transactions.csv     ← fichier brut a analyser
│   └── export/                  ← datasets nettoyés prêts pour l'analyse
├── pipeline.py                  ← script principal
├── requirements.txt             ← stack du projet 
└── README.md                    ← documentation du projet
```
## Lancer le projet
```bash
git clone https://github.com/ton-username/Bank-pipeline.git

cd Bank-pipeline

python -m venv venv

source venv/bin/activate  # Windows : venv\Scripts\activate

pip install -r requirements.txt

python pipeline.py
```