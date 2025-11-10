import pandas as pd

# Simulate Company A data
company_a = pd.DataFrame({
    "email": [
        "maria@example.com",
        "john@example.com",
        "sam@example.com",
        "lina@example.com"
    ],
    "favorite_show": [
        "One Piece",
        "Money Heist",
        "Naruto",
        "Wednesday"
    ]
})

# Simulate Company B data
company_b = pd.DataFrame({
    "email": [
        "john@example.com",
        "sam@example.com",
        "alex@example.com",
        "maria@example.com"
    ],
    "bought_product": [
        "Nike Air Max",
        "Adidas Samba",
        "Puma RS-X",
        "Converse Run Star"
    ]
})

# Save the CSVs
company_a.to_csv("company_a_raw.csv", index=False)
company_b.to_csv("company_b_raw.csv", index=False)

print("Sample raw datasets generated and saved!")
