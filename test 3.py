import json

INPUT_JSON_PATH = r"C:/Users/Asus/Downloads/trace_map1_sorted.json"

with open(INPUT_JSON_PATH, "r") as f:
    trace_map = json.load(f)

ZERO_TOLERANCE = 1e-6

failed_articles = {}
healthy_articles = {}
missing_scores = {}
articles = []

for article_id, data in trace_map.items():

    # Check missing all_layer_scores
    if "all_layer_scores" not in data:
        missing_scores[article_id] = data
        continue

    scores = data["all_layer_scores"]

    if all(abs(s) < ZERO_TOLERANCE for s in scores):
        failed_articles[article_id] = data
        articles.append(article_id)
    else:
        healthy_articles[article_id] = data


print(f"Total articles: {len(trace_map)}")
print(f"Failed (all-zero recovery): {len(failed_articles)}")
print(f"Healthy: {len(healthy_articles)}")
print(f"Missing all_layer_scores: {len(missing_scores)}")


# Print failed articles
print("\n========== Failed Articles ==========")

for article_id, data in failed_articles.items():
    print("\nArticle ID:", article_id)
    print("Text:", data["text"][:200], "...")
    print("Scores:", data["all_layer_scores"])
    print("-" * 80)


# Print missing ones
if missing_scores:
    print("\n========== Missing Score Articles ==========")
    for article_id in missing_scores:
        print("Missing:", article_id)


print(articles)