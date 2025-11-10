import pandas as pd
from tokenizer import tokenize_email

# Load raw datasets
company_a = pd.read_csv("company_a_raw.csv")
company_b = pd.read_csv("company_b_raw.csv")

# Tokenize emails into irreversible hashed IDs
company_a["tokenized_id"] = company_a["email"].apply(tokenize_email)
company_b["tokenized_id"] = company_b["email"].apply(tokenize_email)

# Drop original emails (simulating privacy-safe processing)
company_a_tokenized = company_a.drop(columns=["email"])
company_b_tokenized = company_b.drop(columns=["email"])

# Save tokenized versions
company_a_tokenized.to_csv("company_a_tokenized.csv", index=False)
company_b_tokenized.to_csv("company_b_tokenized.csv", index=False)

print("Tokenization complete. Privacy-safe CSVs generated!")
