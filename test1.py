import pandas as pd
import re

INPUT_CSV = "C:/Users/Asus/Downloads/forget_set_traced1.csv"
OUTPUT_CSV = "C:/Users/Asus/Downloads/forget_set_traced1 processed.csv"  # overwrite in place; change this if you want to keep the original as a backup

df = pd.read_csv(INPUT_CSV)

def keep_first_word_only(token):
    if pd.isna(token):
        return token

    # Preserve a leading space if the original had one (e.g. " Westwood" vs "Westwood").
    # This matters for tokenization — most tokenizers treat a word differently
    # depending on whether it's preceded by a space, so I don't want to silently drop this.
    had_leading_space = token.startswith(" ")

    # Split on whitespace and keep just the first word
    words = token.strip().split()
    first_word = words[0] if words else ""

    # Strip any trailing punctuation that might have been attached (e.g. "Westwood," or "Mitsotakis.")
    first_word = re.sub(r'[^\w\-]+$', '', first_word)

    return (" " + first_word) if had_leading_space else first_word

before_multi_word = df['target_token'].dropna().apply(lambda t: len(t.strip().split()) > 1).sum()

df['target_token'] = df['target_token'].apply(keep_first_word_only)

df.to_csv(OUTPUT_CSV, index=False)

print(f"Cleaned {before_multi_word} multi-word target_token values down to a single word.")
print(f"Saved to: {OUTPUT_CSV}")
print("\nPreview:")
print(df[['clean_prompt', 'target_token']].head(10))