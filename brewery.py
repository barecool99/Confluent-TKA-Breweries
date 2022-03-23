import requests, json, time

'''
API: https://www.openbrewerydb.org/
    Open Brewery DB is a free dataset and API with public information on breweries, 
    cideries, brewpubs, and bottleshops. The goal of Open Brewery DB is to maintain 
    an open-source, community-driven dataset and provide a public API. It is our belief 
    that public information should be freely accessible for the betterment of the beer 
    community and the happiness of web developers and data analysts.
'''

URL = 'https://api.openbrewerydb.org/'


def getAllBreweries():
    '''
        Return a JSON of all breweries
    '''
    breweryURL = URL + 'breweries'
    breweries = requests.get(breweryURL).json()

    return breweries


# def getBreweriesByCity(city):
#     '''
#         Returns all the breweries from a specific city.

#         THIS CALL DOES NOT APPEAR TO BE SUPPORTED/WORKING.
#     '''
#     city = city.replace(' ', '_') # Replaces the whitespace in city names with underscore. 

#     breweryURL = URL + '?by_city=' + city

#     breweries = requests.get(breweryURL).json()

#     return "API not functioning on Brewery.org"


# if __name__ == '__main__':
#     getAllBreweries()
   