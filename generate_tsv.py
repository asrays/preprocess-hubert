import os
import soundfile as sf

def get_audio_length(file_path):
    try:
        with sf.SoundFile(file_path) as f:
            if f.samplerate != 16000:
                raise ValueError(f"File {file_path} is not 16kHz. Found: {f.samplerate}")
            return int(len(f))  # number of samples
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def generate_tsv(root_dir, ext, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"{root_dir}\n")  # first line root_dir
        for subdir, _, files in os.walk(root_dir):
            for file in sorted(files):
                if file.endswith(ext):
                    file_path = os.path.join(subdir, file)
                    rel_path = os.path.relpath(file_path, root_dir)
                    length = get_audio_length(file_path)
                    if length is not None:
                        f.write(f"{rel_path}\t{length}\n")

# === Edit these variables before running ===
root_directory = "/home/ashray/HuBERT-Finetuning-Target/train/audio_16kHz"
audio_extension = ".wav"
output_tsv = "train.tsv"
# ===========================================

generate_tsv(root_directory, audio_extension, output_tsv)
print(f".tsv file generated and saved as {output_tsv}")
