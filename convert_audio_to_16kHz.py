import os
import torchaudio
from torchaudio.transforms import Resample

def resample_audio_files(input_dir, output_dir, target_sr=16000):
    os.makedirs(output_dir, exist_ok=True)
    
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.wav'):
                input_path = os.path.join(root, file)
                relative_path = os.path.relpath(input_path, input_dir)
                output_path = os.path.join(output_dir, relative_path)
                os.makedirs(os.path.dirname(output_path), exist_ok=True)

                waveform, orig_sr = torchaudio.load(input_path)
                if orig_sr != target_sr:
                    print(f"Resampling {input_path} from {orig_sr} to {target_sr}")
                    resampler = Resample(orig_sr, target_sr)
                    waveform = resampler(waveform)
                else:
                    print(f"Copying {input_path} without resampling")

                torchaudio.save(output_path, waveform, target_sr)

if __name__ == "__main__":
    input_directory = "/home/ashray/HuBERT-Finetuning-Target/audio"         # Replace with your input directory
    output_directory = "/home/ashray/HuBERT-Finetuning-Target/audio_16kHz"    # Replace with your output directory
    resample_audio_files(input_directory, output_directory)
    print("✅ Resampling complete.")
