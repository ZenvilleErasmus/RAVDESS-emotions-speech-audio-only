import os
from sys import argv
import re
from shutil import copy2


'''
    This Python script will parse through every actor's folder, e.g. Actor_01
    and appropriately categorize the audio files based on the following 8
    categories: angry, calm, disgust, fearful, happy, neutral, sad and surprised.
'''

# Iterate through every .wav file in every subdirectory
root_dir = 'Audio_Speech_Actors_01-24/'

for sub_dir, dirs, files in os.walk(root_dir):
    for file in files:
        # print("file:", file)
        if file.endswith(".wav"):
            print(os.path.join(sub_dir, file))

            # Determine full path
            full_path = os.path.join(sub_dir, file)

            # Determine the basename of the file
            base_name = os.path.basename(file)
            # print(type(base_name))
            print("Actual file name: ", base_name)

            # Determine into which category a given file belongs
            matchObj = re.match(r'(\d\d-)(\d\d-)(\d\d-)', base_name, re.M|re.I)

            if matchObj:
                # print("matchObj.group(3): ", matchObj.group(3))
                # Remove trailing hyphen
                match_group_three = matchObj.group(3)
                match = match_group_three.rstrip("-")
                # print(match)

                # Move to the appropriate category based on match
                if match == '01': # neutral
                    copy2(full_path, 'resources/labelled_audio/neutral/' + base_name) # (src, dst)
                elif match == '02': # calm
                    copy2(full_path, 'resources/labelled_audio/calm/' + base_name)
                elif match == '03': # happy
                    copy2(full_path, 'resources/labelled_audio/happy/' + base_name)
                elif match == '04': # sad
                    copy2(full_path, 'resources/labelled_audio/sad/' + base_name)
                elif match == '05': # angry
                    copy2(full_path, 'resources/labelled_audio/angry/' + base_name)
                elif match == '06': # fearful
                    copy2(full_path, 'resources/labelled_audio/fearful/' + base_name)
                elif match == '07': # disgust
                    copy2(full_path, 'resources/labelled_audio/disgust/' + base_name)
                else: # match == '08' # surprised
                    copy2(full_path, 'resources/labelled_audio/surprised/' + base_name)

                # --- Done with categorization ---
            else:
                print("No match!")

print("\n--- DONE ---\n")
