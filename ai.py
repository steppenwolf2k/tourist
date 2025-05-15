import requests
from bs4 import BeautifulSoup

def get_famous_places(location):
    location = location.title().replace(" ", "_")
    url = f"https://en.wikipedia.org/wiki/{location}"
    response = requests.get(url)
    print(response)
    
    if response.status_code != 200:
        print(f"Error fetching data for {location}")
        return []
    
    soup = BeautifulSoup(response.text,'html.parser')
    # print(soup.prettify)
    
    # Extract famous places, for this case, scraping general information about places
    places = []
    
    # Find all relevant div tags where places are mentioned (you can adjust this based on actual page structure)
    for place in soup.find_all('div', {'class': 'result-title'}):
        place_name = place.get_text(strip=True)
        if place_name:
            places.append(place_name)
    # Return the list of places
    print(places)
    return places

def main():
    location = input("Enter a location (e.g., city, region): ")
    
    print(f"Fetching famous places to visit in {location}...\n")
    
    famous_places = get_famous_places(location)
    
    if famous_places:
        print(f"Famous places to visit in {location}:\n")
        for idx, place in enumerate(famous_places, start=1):
            print(f"{idx}. {place}")
    else:
        print(f"Sorry, no places found for {location}. Try again with a different location.")
main()