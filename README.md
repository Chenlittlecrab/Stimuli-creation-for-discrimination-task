# Sound pair creation

The current project creats sound pairs that contain two utterances of the same name, with the first one's peak f0 value 11 hz (one step in the experiment) lower than the peak f0 values of the second stimuli

- [cut_off_silence.R](https://github.com/Chenlittlecrab/Stimuli-creation-for-discrimination-task/blob/main/cut_off_slices.py) strips away undesired silence that are labeled manually using Praat Textgrid;
  
- [add_silence_interval.R](https://github.com/Chenlittlecrab/Stimuli-creation-for-discrimination-task/blob/main/add_silence_interval.py) adds [silence of 500 ms](https://github.com/Chenlittlecrab/Stimuli-creation-for-discrimination-task/blob/main/sil_500.wav) before and after the sound files whose undesired silences have been stripped off
  
- [merge_audio_files_rev.py](https://github.com/Chenlittlecrab/Stimuli-creation-for-discrimination-task/blob/main/merge_audio_files_rev.py) pairs the audio files that are one step away iteratively
  
- [Valerie_Intensity69](https://github.com/Chenlittlecrab/Stimuli-creation-for-discrimination-task/tree/main/Valerie_Intensity69) sample dataset
