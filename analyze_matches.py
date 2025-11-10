import pandas as pd
import matplotlib.pyplot as plt

# Load matched users
matched = pd.read_csv("matched_users.csv")

print("\nTotal shared users:", len(matched))

# Basic insight: what shows these shared users like?
show_counts = matched["favorite_show"].value_counts()

print("\nShared Audience Interests:")
print(show_counts)

# Visualization
plt.figure(figsize=(8, 5))
show_counts.plot(kind="bar")
plt.title("Shared Audience Entertainment Interests")
plt.xlabel("Show")
plt.ylabel("Audience Count")
plt.tight_layout()
plt.show()
