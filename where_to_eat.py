import requests
import json
import random
import webbrowser

# Customize your search by adding the name of your city 
my_city = " "
# Don't forget to add an API key!
api_key = " "

# Strip my_city of punctuation and spaces
my_city = my_city.strip()
my_city = my_city.strip('\'')

url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query=restaurants\%20in\%20{my_city}&key={api_key}"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

f = open("list_of_restaurants.json", "w")

f.write(response.text)
f.close()


# Retrieve names of restaurants
names = []
with open('list_of_restaurants.json') as json_file:
	data = json.load(json_file)

	for restaurant in data['results']:
		'''To Do: Only add name to list if the restaurant is open'''
		name = restaurant['name']
		names.append(name)

print(names)

# Randomly choose a name from the list
choice = random.choice(names)
#print(choice)

# Open up a browser and do a Google search for "{choice} near me {my_city}"
# Strip choice of punctionation and spaces
choice = choice.strip()
choice = choice.strip('\'!?,.:;')

url = f'https://www.google.com/maps?q={choice}+near+me+{my_city}&ie=UTF-8'
webbrowser.open(url)

