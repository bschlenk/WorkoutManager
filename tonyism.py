#!/usr/bin/env python
import sys, os
import requests

TONYISMS = [

]

def main():
	page = requests.get('http://101tonyisms.wordpress.com/').text
	print page

if __name__ == '__main__':
	main()

