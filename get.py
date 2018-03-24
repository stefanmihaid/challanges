import urllib2
import json


def get(location):
	temperatures = []
	key = bee72658c0f623825a8b3025a402ee36
	url = "http://api.openweathermap.org/data/2.5/forecast?id={}&APPID={}".format(location, key)
	content = urllib2.urlopen(url).read()
	temperatures = find_temperature(content)
	return temperatures

def find_temperature(content):
	jso = json.load(content)
	


def user_input():
	print ("1...Bucharest")
	print("")
	print ("2...Baicoi")
	print("")
	print ("Any key to exit")
	decision = raw_input("Ce locatie Baws?:  ")
	if decision == 1:
		print get(683506)
	elif decision == 2:
		print get(685811)
	else:
		print ("Bye...")


user_input()