# generate_dict_ltr.py
from collections import Counter

input_ltr = "train.ltr"
output_dict = "dict.ltr.txt"

counter = Counter()
with open(input_ltr, encoding="utf-8") as f:
    for line in f:
        tokens = line.strip().split()
        counter.update(tokens)

# Add special tokens commonly needed
special_tokens = ["<unk>", "<s>", "</s>"]
with open(output_dict, "w", encoding="utf-8") as f:
    # for token in special_tokens:
    #     f.write(f"{token} 1\n")
    for token, count in counter.most_common():
        f.write(f"{token} {count}\n")
