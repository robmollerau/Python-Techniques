# Function no typing hinting
def getHighestNumber( ANumber1, ANumber2 ):
    return( max( ANumber1, ANumber2 ) )

# Funtion with type hinting - still accepts non int values
def getHighestNumber2( ANumber1, ANumber2 : int ) -> int:
    # Using assertions to check parameters are valid
    assert isinstance( ANumber1, int ), "getHighestNumber2: Parameter ANumber1 missing or invalid"
    assert isinstance( ANumber2, int ), "getHighestNumber2: Parameter ANumber2 missing or invalid"
    return( max( ANumber1, ANumber2 ) )    


# Class get highest number
#class getHighestNumberClass():
    ## Called on instantiate
    #def __init__( self, ANumber1, ANumber2 ):
     #   self.Number1 = ANumber1
        #self.Number2 = ANumber2
    #def __new__( cls ):
     #   return( 20 )    
    #def sum( self ) :
     #   return( max( self.Number1, self.Number2 ) )    

# No type hinting
Number1 = 10
Number2 = 20
print( getHighestNumber( Number1, Number2 ) )

# Valid numbers
Number1 = 10
Number2 = 20
print( getHighestNumber2( Number1, Number2 ) )

# Invalid numbers - Assertion fail
Number1 = 10
Number2 = "A"
print( getHighestNumber2( Number1, Number2 ) )

# Missing paraemters - Positional argument fail
print( getHighestNumber2( Number1 ) )

# Initializing variable with type
#Number3 : int = 30
#Number4 : int = 40

# Generates error when assigning string
# ANumber3 = "A"

#print( getHighestNumber2( Number1, Number2 ) )

#Object = getHighestNumberClass( Number3, Number4 )
#print( Object.sum() )

    #if not isinstance( ANumber1, int ):
        #return( -1 )
    #if not isinstance( ANumber2, int ):
        #return( -1 )    



