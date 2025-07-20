import pandas as pd

# Load your SQL data into a DataFrame, then:
df = pd.read_csv("your_data.csv")  # or load from SQLite

# Calculate correlation coefficients
correlations = {
    "Promo_Spend-Net_Sales": df["Promo_Spend"].corr(df["Net_Sales"]),
    "Promo_Spend-Avg_Basket": df["Promo_Spend"].corr(df["Avg_Basket"]),
    "Net_Sales-Avg_Basket": df["Net_Sales"].corr(df["Avg_Basket"])
}

# Get the strongest (by absolute value)
strongest = max(correlations.items(), key=lambda x: abs(x[1]))

# Save to JSON
import json
with open("correlation_result.json", "w") as f:
    json.dump({ "pair": strongest[0], "correlation": round(strongest[1], 4) }, f)
