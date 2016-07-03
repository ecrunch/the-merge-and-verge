import pymongo
import random

db = pymongo.MongoClient('localhost', 27017).thegoals

item = ["Ate Tacos",
		"Smoked a J",
		"Ran",
		"Worked Out",
		"Bar",
		"Read",
		"Code",
		"Played Guitar",
		"Played Video Games",
		"Art",
		"Cooked",
		"Banana",
		"Tacos",
		"Crazy Shit",
		"Apple",
		"A 360",
		"Punched Superman",
		"Asti",
		"Globe",
		"Tacos"]

arrayLength = len(item)


for i in item:
	randomNum = random.randint(0, arrayLength) - 1
	name = item[randomNum]
	times = random.randint(0, 10)
	print name
	print times
	save = {
		"name": name,
		"times": times
	}

	db.items.insert(save)



