RAVDESS-emotions-speech-audio-only
==================================

Author: Zenville Erasmus
Contact: zenville2010@gmail.com

# This project contains 1,440 audio files (.wav), i.e. speech files, from 24 actors
# (that need to be)/are categorized into 8 separate emotions.

# 60 trials per actor x 24 actors = 1440.

--------------------------------------------------------------------------------
The Ryerson Audio-Visual Database of Emotional Speech and Song (RAVDESS) is
released under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
International License, CC BY-NA-SC 4.0

File naming convention

Each RAVDESS file has a unique filename. The filename consists of a 7-part
numerical identifier (e.g., 03-01-01-01-01-01-24.wav).

These identifiers define the stimulus characteristics:

---Filename identifiers---

- Modality (01 = full-AV, 02 = video-only, 03 = audio-only).
- Vocal channel (01 = speech, 02 = song).
- Emotion (01 = neutral, 02 = calm, 03 = happy, 04 = sad, 05 = angry, 06 = fearful, 07 = disgust, 08 = surprised).
- Emotional intensity (01 = normal, 02 = strong). NOTE: There is no strong intensity for the ‘neutral’ emotion.
- Statement (01 = “Kids are talking by the door”, 02 = “Dogs are sitting by the door”).
- Repetition (01 = 1st repetition, 02 = 2nd repetition).
- Actor (01 to 24. Odd numbered actors are male, even numbered actors are female).
- Filename example: 03-01-01-01-01-01-24.wav

1. Audio only (03)
2. Speech (01)
3. Neutral (01)
4. Normal intensity (01)
5. Statement “kids” (01)
6. 1st Repetition (01)
7. 24th Actor (24)
Female, as the actor ID number is even.
--------------------------------------------------------------------------------

# A few notes for running the program

# Make sure you have Python, pip and virtualenv installed
python --version
pip --version
virtualenv --version

# Make sure that you are in the project directory
cd RAVDESS-emotions-speech-audio-only/

# Create a virtualenv
virtualenv -p python3 venv

# Run the following to activate the virtual environment
. venv/bin/activate

# Install the necessary packages into the virtualenv with pip
pip install -r requirements.txt
# (empty file as default packages are used in this case)
Package    Version
---------- -------
pip        19.0.1
setuptools 40.8.0
wheel      0.32.3

# For categorizing the audio files into 8 emotions
# (angry, calm, disgust, fearful, happy, neutral, sad and surprised)
time python categorize_audio_files.py

# The categorized audio files will be located under
resources/labelled_audio/

# When done (deactivate the virtual environment)
deactivate
