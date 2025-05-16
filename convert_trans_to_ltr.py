input_path = "/home/ashray/HuBERT-Finetuning-Target/transcription.txt"
output_path = ".ltr"

with open(input_path, "r", encoding="utf-8") as fin, open(output_path, "w", encoding="utf-8") as fout:
    for line in fin:
        parts = line.strip().split(maxsplit=1)
        if len(parts) != 2:
            continue
        _, text = parts
        text = text.strip().replace(" ", " | ")
        ltr_line = " ".join(list(text))
        fout.write(ltr_line + "\n")
