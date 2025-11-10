import pandas as pd

# Load tokenized datasets
company_a = pd.read_csv("company_a_tokenized.csv")
company_b = pd.read_csv("company_b_tokenized.csv")

# Perform an inner join on tokenized_id (this finds users in both datasets)
matched = pd.merge(company_a, company_b, on="tokenized_id", how="inner")

# Display results
print("\nMatched Users (Privacy-Safe Join):")
print(matched)

# Save results
matched.to_csv("matched_users.csv", index=False)
print("\nMatched users saved to matched_users.csv")
