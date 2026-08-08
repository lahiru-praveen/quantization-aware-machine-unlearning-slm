import json

INPUT_JSON_PATH = r"C:/Users/Asus/Downloads/trace_map1.json"
SORTED_OUTPUT_PATH = r"C:/Users/Asus/Downloads/trace_map1_sorted.json"

# Load JSON
with open(INPUT_JSON_PATH, "r") as f:
    trace_map = json.load(f)

# Sort by article ID numerically
sorted_trace_map = dict(
    sorted(trace_map.items(), key=lambda x: int(x[0]))
)

# Save sorted JSON
with open(SORTED_OUTPUT_PATH, "w") as f:
    json.dump(sorted_trace_map, f, indent=4)

print(f"Sorted JSON saved to: {SORTED_OUTPUT_PATH}")