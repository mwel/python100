
# travel log

travel_log = [
    {
        "country" : "France",
        "visits" : 12,
        "cities" : ['Paris', 'Cannes', 'Rennes', 'St. Malo', 'St. Martin']
    },
    {
        "country" : "Germany",
        "visits" : 100,
        "cities" : ['Munich', 'Berlin', 'Stuttgart', 'Trier', 'Hamburg', 'Aurich', 'Würzburg']
    }
]

print(travel_log)

def add_new_country (country, visits, list_of_cities):
    travel_log.append(
        {
            "country" : country, 
            "visits" : visits,
            "cities" : list_of_cities
        }
    )


add_new_country("Switzerland", 24, ['Zurich', 'Bern', 'Geneva', 'Lausanne', 'Basel', 'Schwyz'])

print(travel_log)