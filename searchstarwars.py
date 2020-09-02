#/planets/?search=
import requests
def search():
	url = "https://swapi.dev/api/"
	category = input("what category:")
	name = input("what name:")
	url = url + category + "/?search=" + name
	r = requests.get(url)
	if r.status_code == 200:
		data = r.json()
		results = data['results']
		if category == 'films':
			for result in results:
				print("Title: " + result['title'])
				print("Episode: " + str(result['episode_id']))
				print("Characters:")
				for character in result['characters']:
					url_2 = character
					r_2 = requests.get(url_2)
					data_2 = r_2.json()
					print(data_2['name'])
				
		if category == "people":
			for person in results:
				print(person['name'])
				print(person['birth_year'])
				url_2 = person['homeworld']
				r_2 = requests.get(url_2)
				data_2 = r_2.json()
				print("world: " + data_2['name'])
		if category == "planets":
			for result in results:
				print('Name: ' + result['name'])
				print('Population: ' + result['population'])
				print("Residents:")
				residents = result['residents']
				for resident in residents:
					url_2 = resident
					r_2 = requests.get(url_2)
					data_2 = r_2.json()
					print(data_2['name'])
		if category == 'species':
			for result in results:
				print("Name: " + result['name'])
				print("Average Lifespan: " + result['average_lifespan'])
				print("People:")
				for person in result['people']:
					url_2 = person
					r_2 = requests.get(url_2)
					data_2 = r_2.json()
					print(data_2['name'])
		if category == 'starships':
			for result in results:
				print("Name: " + result['name'])
				print("Price: " + result['cost_in_credits'])
				print("Capacity of passengers: " + result['passengers'])
		if category == 'vehicles':
			for result in results:
				print("Name: " + result['name'])
				print("Price: " + result['cost_in_credits'])
				print("Capacity of passengers: " + result['passengers'])
	else:
		print("invalid category")
def planet_residents(url, maximum, name):
	r = requests.get(url)
	data = r.json()
	results = data['results']
	if r.status_code == 200:
		for result in results:
			if len(result['residents']) > maximum:
				name = result['name']
				maximum = len(result['residents'])
			else:
				continue
		if data['next'] == None:
			#eturn name, maximum
			return "Name: " + name, "Max: " + str(maximum)
			#returns none for some reason
		return planet_residents(data['next'], maximum, name)

#print(planet_residents('https://swapi.dev/api/planets/', 0, ''))
#search()
def most_common_species(url, maximum, name):
	#although you specifically told me not to, I decided to use species because otherwise I would have to create a variable for every specie.
	r = requests.get(url)
	data = r.json()
	results = data['results']
	if r.status_code == 200:
		for result in results:
			if len(result['people']) > maximum:
				name = result['name']
				maximum = len(result['people'])
			else:
				continue
		if data['next'] == None:
			#eturn name, maximum
			return ["Name: " + name, "Population: " + str(maximum)]
			#returns none for some reason
		return most_common_species(data['next'], maximum, name)
print(most_common_species('https://swapi.dev/api/species/', 0, ''))

"""
loop back after to make another search
3 information try to make it hard
find the planet the most residents, more than one page!
find the msot common species without going to species, use people and pages
films, people, planets, species, starships,	vehicles
"""