#!/usr/bin/env python

import sys, os
import json
import random
import tonyism

WORKOUT_DIR = 'workouts'


def decodeJsonFile(file_name):
    with open(file_name) as f:
        return json.load(f)


def promptWithDefault(message, default=None):
    prompt = '%s [%s]: ' % (message, str(default) if default is not None else '*required*')
    answer = raw_input(prompt)
    return answer or default


def promptSelectionFromList(choices, default=0, prompt='please choose an option'):
    for i, choice in enumerate(choices):
        print '%d: %s' % (i, str(choice))
    print
    choice = None
    while choice is None:
        try:
            choice = int(promptWithDefault(prompt, default))
        except ValueError:
            print 'boowahhhh, choice must be in range 0-%d' % len(choices)
            continue
        if choice not in range(len(choices)):
            print 'wise guy, choice must be in range 0-%d' % len(choices)
            choice = None
    return choice


def getWorkouts(directory=WORKOUT_DIR):
    workout_files = os.listdir(directory)
    workouts = []
    for workout in (decodeJsonFile(os.path.join(directory, w))['workout'] for w in workout_files):
        workouts.append(workout)
    workouts.sort(key=lambda a: a['name'])
    return workouts
    
    
def main():
    workouts = getWorkouts()

    choice = promptSelectionFromList([w['name'] for w in workouts])
    workout = workouts[choice]

    rep_history = []
    for activity in workout['activities']:
        reps = int(promptWithDefault(activity['name'], default=activity['reps']))
        rep_history.append((activity['name'], reps))
        if random.getrandbits(1):
            print tonyism.random()

    print
    print 'Done! Printing results...'

    spacing = max(map(len, [a[0] for a in rep_history]))
    for activity in rep_history:
        print '{0:{2}}: {1}'.format(*(activity + (spacing,)))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass

