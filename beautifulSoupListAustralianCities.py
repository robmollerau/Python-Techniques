#
# This script uses Beatiful Soup 4 which can be obtained by typing
# from the command prompt:
#
# pip3 install beautifulsoup4
# 
# Note: In Windows ensure above command shell is run with Administrator privileges 
#       otherwise site-packages will not be writeable

from bs4 import BeautifulSoup
from urllib.request import urlopen

# Constants
class CONST:
    CITY_RANK  : int = 0
    CITY_NAME  : int = 1
    STATE      : int = 2
    POPULATION : int = 3

# Starting point for standalone apps
if __name__ == '__main__' :

    # Raw mode enabled by prefixing with 'r' - string is not escaped
    urlMain                       : str = r'https://en.wikipedia.org/wiki/Main_Page'
    urlAustralianCitiesPopulation : str = r'https://en.wikipedia.org/wiki/List_of_cities_in_Australia_by_population'

    # --------------------------------------------------------------------------

    # Scrape Wikipedia Main page - Uncomment when testing
    #with urlopen( urlMain ) as response:
        #soup = BeautifulSoup( response, 'html.parser' )

        # Find all a href tags
        #for tags in soup.find_all( 'a' ):
            #print( tags.get( 'href', '/' ) )

    # --------------------------------------------------------------------------

    # Population by urban areas in Australia 
    # This list is not exhaustive and only caters for urban areas with a 
    # population of 10,286 and above

    with urlopen( urlAustralianCitiesPopulation ) as response:
        soup = BeautifulSoup( response, 'html.parser' )

        cityList = []

        # Find city table - look for class marker - use Chrome inspect function to locate table first
        citiesTable = soup.find( 'table', { "class" : "wikitable sortable plainrowheaders" } )        

        # Iterate all table rows
        for row in citiesTable.find_all( 'tr' ):

            # Load table columns - we are only interesed in the first 4
            cols = row.find_all( 'td' )

            # Table may have merged columns - we skip these by testing for column count
            if len( cols ) > 2:

                rank  = cols[ CONST.CITY_RANK  ].text.strip()
                city  = cols[ CONST.CITY_NAME  ].text.strip() 
                state = cols[ CONST.STATE      ].text.strip()
                pop   = cols[ CONST.POPULATION ].text.strip()

                # Add rank to list
                cityList.append( [ rank, city, state, pop ] )

    # Print population list
    for rowIndex, rowItem in enumerate( cityList ):
        print( 'Rank: %3s   City: %-35s State: %-45s Population: %10s' % \
          ( rowItem[ CONST.CITY_RANK  ], \
            rowItem[ CONST.CITY_NAME  ], \
            rowItem[ CONST.STATE      ], \
            rowItem[ CONST.POPULATION ] ) )

