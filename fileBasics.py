from pathlib import Path

# Starting point for standalone apps
if __name__ == '__main__' :

    continueLoop : bool = True
    favouriteCityList : list = []

    # Get path of this python script
    scriptPath = Path(__file__).parent.absolute()

    # Get cities 
    while continueLoop:   
      favouriteCity = input( 'Enter a favourity city, enter blank to end: ' )
      if ( favouriteCity == '' ):
          break
      else:
          favouriteCityList.append( favouriteCity )  

    # Show favourity cities
    print( 'Your favour cities are...' )
    for listIndex, listItem in enumerate( favouriteCityList ):
        print( str( listIndex + 1 ) + ' - ' + listItem )

    # Save to file - a means append mode
    fileCity = open( str( scriptPath ) + '\Favourite_Cities.txt', 'a' )
    for listIndex, listItem in enumerate( favouriteCityList ):
        fileCity.write( listItem + '\n' )
    fileCity.close




         
