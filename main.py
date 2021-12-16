import wave
import numpy as np
import wavio
import ffmpeg
import os
import subprocess
from os import walk
from os import listdir
from os.path import isfile, join

# Project Folder:
file_path = r"/data/emotion_project/zhana"
input_path = f"{file_path}/input"
output_path = f"{file_path}/output"

file_names = [f for f in listdir(input_path) if isfile(join(input_path, f))]
file_names.remove('huge-vocabulary.scorer')
file_names.remove('model.tflite')
# WAV Conversion:
for f in file_names:
    input_file = f"{input_path}/{f}"
    output_file = f"{output_path}/{f}"
    os.system(f"ffmpeg -i {input_file} {output_file}")
    print("WAV Conversion completed")

cmd = f"stt --model {input_path}/model.tflite --scorer {input_path}/huge-vocabulary.scorer --audio {output_path}/{f}"
cmd = str(cmd).split()
output = subprocess.check_output(cmd, shell=False)

print("transcription completed")

fixed_output = str(output)
fixed_output = fixed_output[2:-3]
with open(f[:-4] + ".txt", 'w') as file:
    file.write(fixed_output)
file.close()

print("transcription is saved")
