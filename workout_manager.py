#!/usr/bin/env python
import json
import os

def decodeJsonFile(file_name):
	with open(file_name) as f:
		data = f.read()

	decoder = json.JSONDecoder()
	return decoder.decode(data)

def promptWithDefault(message, default_value=None):
	prompt = '%s [%s]' % (str(default_value) if default_value else '*required*')
	return raw_input(prompt)
	
def main():
	#TODO error checking
	workout_files = os.listdir('workouts')
	workouts = decodeJsonFile(os.path.join('workouts', workout_files[0]))['workouts']
	print workouts
	

if __name__ == '__main__':
	main()

