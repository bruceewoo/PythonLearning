#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyaudio
import wave
import speech_recognition as sr

class Audio(object):

	def run(self):
		FORMAT = pyaudio.paInt16
		CHANNELS = 2
		RATE = 44100
		CHUNK = 1024
		RECORD_SECONDS = 5
		WAVE_OUPUT_FILENAME = "record.wave"

		audio = pyaudio.PyAudio()

		#start recording
		stream = audio.open(format=FORMAT, channels = CHANNELS,
			rate = RATE, input = True, frames_per_buffer = CHUNK)
		print "recording..."
		frames = []

		for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
			data = stream.read(CHUNK)
			frames.append(data)
		print "finished recording"

		#stop recording
		stream.stop_stream()
		stream.close()
		audio.terminate()

		waveFile = wave.open(WAVE_OUPUT_FILENAME, 'wb')
		waveFile.setnchannels(CHANNELS)
		waveFile.setsampwidth(audio.get_sample_size(FORMAT))
		waveFile.setframerate(RATE)
		waveFile.writeframes(b''.join(frames))
		waveFile.close()


		r = sr.Recognizer()
		with sr.AudioFile(WAVE_OUPUT_FILENAME) as source:
			audios = r.record(source)

		try:
			print "Transciption: "+r.recognize_google(audios)
		except LookupError, e:
			print "Could not understand audio"

	
		

if __name__ == '__main__':
	audio = Audio()
	audio.run()