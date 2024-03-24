#!/usr/bin/env python
"""This script yields discrimination pairs of one step difference for the same name"""

from pydub import AudioSegment
import re
import os

# iteratively merge two sound files and output them
# in the empty folder created for the output

# make a function that put A of the pair AB to a list (A_ls)
# and B of the pair AB to another list (B_ls)
def lst_output(int_i, int_j, file_input): 
  # takes the input of i and j for each sound file step, 
  # and the directory of sound file as input
  A_ls = list()
  B_ls = list()

  for filename in os.listdir(file_input):
      if filename.endswith(".wav"):
        f = os.path.join(file_input, filename) #combine the file_input with file name
        step_num = int(re.findall("\Step([0-9]+)", filename)[0])
        if step_num == int_i:
        # re.findall finds the pattern /number, return a list,
        # then I use [0] to extract the string in the list, 
        # and then use [1:] to get rid of "/" symbol
        # if I don't use "/" in the regular expression, 
        # it's gonna extract 3 in .mp3 too
            A_ls.append(f)
        elif step_num == int_j:
            B_ls.append(f)
        else:
            pass

  return A_ls, B_ls


# combine sound

file_input_path = "/Users/chenz/Documents/CUNY/DISSERTATION/prominence_perception/stimuli_all_trimmed/"
file_output_path = "/Users/chenz/Documents/CUNY/DISSERTATION/prominence_perception/stimuli_discrimination/AB/"
sound_interval_path = "/Users/chenz/Documents/CUNY/DISSERTATION/prominence_perception/stimuli_synthesis/sil_500.wav"
sound_interval = AudioSegment.from_file(sound_interval_path, format="wav")

def main():
    for i in range(1, 11):
      j = i+1
      AB_ls = lst_output(i, j, file_input_path)
      # extract two lists that contain sounds of step i and j respectively
      A_stimuli, B_stimuli = AB_ls[0], AB_ls[1]
      # A_stimuli contains sounds of step j, B_stimuli sounds of step i
      print(len(A_stimuli))
      print(len(B_stimuli))
      for stringA in A_stimuli:
        # iterate over A and B list and find sounds that contains the same name
          A_path = re.findall("\_[A-Z]+[a-z]+\_", stringA)[0][1:-1]
          # extract the name in the stringA
          for stringB in B_stimuli:
              B_path = re.findall("\_[A-Z]+[a-z]+\_", stringB)[0][1:-1]
              # extract the name in the stringB
              if A_path == B_path:
                print(A_path)
                print(B_path)
                sound1 = AudioSegment.from_file(stringA, format="wav")
                sound2 = AudioSegment.from_file(stringB, format="wav")
                # sil of 500 ms before the pair
                concat_1 = sound_interval + sound1
                # sil of 500 ms btw the pair
                concat_2 = concat_1 + sound_interval
                concat_3 = concat_2 + sound2
                audio_output = file_output_path + str(i) + "_" + str(j) + "_" + A_path + ".wav"
                concat_3.export(audio_output, format="wav")
              else:
                pass


if __name__ == "__main__":
    main()
