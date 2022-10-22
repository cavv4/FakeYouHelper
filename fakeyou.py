#!/usr/bin/env python3

#CONVERSION AND SPEECH-TO-TEXT SCRIPT TO HELP WITH CREATION OF FAKEYOU DATASETS by Cavv

OUTPUT_FILES_IN_NUMERIC_ORDER = 1

import ffmpeg
import speech_recognition as sr
import os
from os import path
from json import loads
if not os.path.exists("./input/"):
	os.makedirs("./input/")
if not os.path.exists("./wavs/"):
	os.makedirs("./wavs/")
if not os.path.exists("./model/"):
	os.makedirs("./model/")
files = os.listdir("./input")
files.sort()
r = sr.Recognizer()
count=-1
for filename in files:
	if os.path.splitext(filename)[1] == '.wav':
		count += 1
		#if OUTPUT_FILES_IN_NUMERIC_ORDER == 1:
		#	os.rename("./input/" + filename, "./input/" + str(count+1) + ".wav")
if count == -1:
	print('\nNo wave files in "input" folder.\n')
else:
	count += 1
	#if OUTPUT_FILES_IN_NUMERIC_ORDER == 1:
	#	print("\nRenamed", count, "files to numeric order.")
	print("\nResampling audio files to 22050Hz 16-bit mono...")
	
	count=0
	for filename in files:
		if os.path.splitext(filename)[1] == '.wav':
			count += 1
			stream = ffmpeg.input('./input/' + filename)
			if OUTPUT_FILES_IN_NUMERIC_ORDER == 1:
				filename = str(count) + ".wav"
			stream = stream.output("./wavs/" + filename, **{'ar': '22050'}, **{'sample_fmt': 's16'}, **{'ac': '1'})
			ffmpeg.run(stream, quiet=True, overwrite_output=True)
	print('Output in "wavs" folder.\n')
	
	print("Transcribing", count, "audio files...\n")
	
	fList = open("list.txt", "w",encoding='utf8')
	count=0
	for filename in files:
		if os.path.splitext(filename)[1] == '.wav':
			try:
				count += 1
				if OUTPUT_FILES_IN_NUMERIC_ORDER == 1:
					filename = str(count) + ".wav"
				AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "wavs/" + filename)
				with sr.AudioFile(AUDIO_FILE) as source:
					audio = r.record(source)
				output = loads(r.recognize_vosk(audio))['text']
				print ("\n", count , ' - ' , filename , ' - "' , output , '."' , sep="")
				fList.write("wavs/" + filename + "|" + output + ".\n")
			except sr.UnknownValueError:
				pass
			except sr.RequestError as e:
				print("Vosk error; {0}".format(e))
	fList.close()
	print('\nList "list.txt" generated.\n')
	print("Shits done.")