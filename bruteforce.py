import pandas as pd
import itertools

# Load data from CSV file
file_path = "liste_20_actions.csv"
actions_df = pd.read_csv(file_path)

# Calculate the “Valeur du bénéfice” for each stock
actions_df["Valeur du bénéfice"] = actions_df["Coût"] * actions_df["Bénéfice"] / 100

# Convert DataFrame to a list of dictionaries for compatibility with itertools
actions = actions_df.to_dict(orient="records")

# Set the maximum budget
max_budget = 500

# Initialize the best combination
best_combination = []
best_profit = 0

# Test all combinations
for n in range(1, len(actions) + 1):
    for combination in itertools.combinations(actions, n):
        total_cost = sum(action["Coût"] for action in combination)
        total_profit = sum(action["Valeur du bénéfice"] for action in combination)

        if total_cost <= max_budget and total_profit > best_profit:
            best_combination = combination
            best_profit = total_profit

# Show results
print("Meilleure combinaison d'actions :")
for action in best_combination:
    print(f"- {action["Actions"]} (Coût : {action["Coût"]}€, Bénéfice : {action["Valeur du bénéfice"]}€)")

print(f"Profit Total : {best_profit}€")