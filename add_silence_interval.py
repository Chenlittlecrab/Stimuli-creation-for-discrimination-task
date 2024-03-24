#!/usr/bin/env python
"""This script yields strips away silence of the synthesized stimuli annotated manually using TextGrid;
it has to run twelve times for each folder. Later it will be modified to run just once"""

import re
import os
from pydub import AudioSegment

# specify the input and output folder
input_folder = "/Users/chenz/Documents/CUNY/DISSERTATION/prominence_perception/stimuli_all_trimmed/"
output_folder = "/Users/chenz/Documents/CUNY/DISSERTATION/prominence_perception/stimuli_identification/"

# silence audio
sil_path = "/Users/chenz/Documents/CUNY/DISSERTATION/prominence_perception/stimuli_synthesis/sil_500.wav"


def main():
    for filename in os.listdir(input_folder):
        if filename.endswith(".wav"):
            print(filename)
        # get the audio_path by combining the input_folder with the filename
            audio_path = input_folder + filename
            sound =  AudioSegment.from_file(audio_path, format="wav")
            sil = AudioSegment.from_file(sil_path, format="wav")
            concat1 = sil + sound
            concat2 = concat1 + sil
            m = re.findall("(.*?)\_trimmed",filename)
            audio_name = m[0]  # re.findall yields a list, I need to extract the string from the list
            output_path = output_folder + audio_name + ".wav"
        # export the segment
            concat2.export(output_path, format = "wav")



if __name__ == "__main__":
    main()
