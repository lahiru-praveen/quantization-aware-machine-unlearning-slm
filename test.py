import pandas as pd

df = pd.read_json("C:/Users/Asus/Documents/GitHub/quantization-aware-machine-unlearning-slm/data/raw/retain2.json")
df.to_csv("retain_set2.csv", index=False)

print("JSON has been converted to CSV successfully!")
