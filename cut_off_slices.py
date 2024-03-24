#!/usr/bin/env python
"""This script yields strips away silence of the synthesized stimuli annotated manually using TextGrid;
it has to run twelve times for each folder. Later it will be modified to run just once"""

import re
import os
from pydub import AudioSegment

# specify the input folder
input_mother_folder = "/Users/chenz/Documents/CUNY/DISSERTATION/prominence_perception/stimuli_adjusted_69/"
# subfolder and subfile change everytime I run the script
# this is the part that will be changed later
subfolder = "Valerie_Intensity69/"
subfile = "Step1_Valerie.TextGrid"

# combine the input_mother_folder with the subfolder to get the real input folder
input_folder = input_mother_folder + subfolder

# get the path for textgrid
input_file = input_folder + subfile

# output folder for the trimmed files
# all the files will be put into one single file
output_folder = "/Users/chenz/Documents/CUNY/DISSERTATION/prominence_perception/stimuli_all_trimmed/" 



# read the textgrid

with open(input_file, 'r') as f:
  data = f.read()

# specify the pattern that gives the group for xmin and xmax corresponding to the stimuli
# they are xmin and xmax of intervals [2]
# the pattern finds the xmin group and xmax group patterns
pattern1 = r'intervals \[2\].*?xmin = (?P<xmin>[0-9]+\.[0-9]+).*?xmax = (?P<xmax>[0-9]+\.[0-9]+)'
# m1 contains xmin group and xmax group for word1
m1 = re.search(pattern1, data, re.DOTALL)
pattern2 = r'intervals \[4\].*?xmin = (?P<xmin>[0-9]+\.[0-9]+).*?xmax = (?P<xmax>[0-9]+\.[0-9]+)'
# m2 contains xmin group and xmax group for word2
m2 = re.search(pattern2, data, re.DOTALL)

# create timestampes for extracting the stimuli
# start_time and end_time is the timestamp corresponding to the stimuli
start_for_seg1 = float(m1.group('xmin')) # extracts the value of 'xmin' group in m1
end_for_seg1 = float(m1.group('xmax')) # extracts the value of 'xmax' group in m1
start_for_seg2 = float(m2.group('xmin')) # extracts the value of 'xmin' group in m1
end_for_seg2 = float(m2.group('xmax')) # extracts the value of 'xmax' group in m1

def main():
    for filename in os.listdir(input_folder):
    # read wav files only
      if filename.endswith('.wav'):
        print(filename)
      # get the audio_path by combining the input_folder with the filename
        audio_path = input_folder + filename
        sound =  AudioSegment.from_file(audio_path, format="wav")
      # extract the portion according to the timestamp
        seg1 = sound[start_for_seg1*1000:end_for_seg1*1000]
        seg2 = sound[start_for_seg2*1000:end_for_seg2*1000]
        concat = seg1 + seg2
      # need to extract the StepN_name using re.match
        m = re.match("(.*?)\.",filename) # meaning printing everything before the . for .wav
        audio_name = m.group()[:-1]  # get rid of the .
        output_path = output_folder + audio_name + "_trimmed.wav"
      # export the segment
        concat.export(output_path, format = "wav")



if __name__ == "__main__":
    main()
