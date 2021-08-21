# Class Example 1

# Helps create distinct types
from typing import NewType

class Animal:

    # The class documentation can be retrived via __doc__ built-in attribute
    '''Class documentation string - simple animal class'''

    # Class Attributes - used when values must be same for every class instance
    # Treat it as a type of constant - do not set this via class methods
    version : str  = "1.0.0"

    # Instantion invokes init method - equivalent to constructor in Delphi
    def __init__( self ):
        # Instance attributes - can be modified
        self.skinColour = ""
        print( self.__class__.__name__ + " created" )

    # Destructor method - gets called when class gets destroyed
    # In Python class objects are automatically destroyed when not needed
    def __del__( self ):
        print( self.__class__.__name__ + " destroyed" )

    # Set animal colour
    def setColour( self : object, AColour : str ):
        print( "Setting skin colour to " + AColour )
        self.skinColour = AColour   

    # Get animal colour
    def getColour( self ) -> str:
        print( "Returning skin colour of " + self.skinColour )
        return self.skinColour


# Starting point for standalone apps
if __name__ == "__main__" :

    # Variables - using NewType to set type value
    animalColour = NewType( "", str )

    # Instatiate class 
    myAnimal = Animal()

    # Print class version
    print( "Version " + myAnimal.version )

    # Print class name 
    print( "Class name ", type( myAnimal ).__name__ )

    # Print module where class is defined
    print( "Class module ", myAnimal.__module__ )

    # Print instance attributes (variables) - does not print class attributes
    print( "Class instance attributes ", myAnimal.__dict__ )

    # Print class documentation
    print( "Class documentation : ", myAnimal.__doc__ )

    # Set animal colour
    myAnimal.setColour( "brown" )

    print( "The animal colour is " + myAnimal.getColour() )

    