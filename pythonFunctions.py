# Function no typing hinting
def getHighestNumber( ANumber1, ANumber2 ):
    return( max( ANumber1, ANumber2 ) )

# Function with type hinting - still accepts non int values - hence assert to verify validity
def getHighestNumber2( ANumber1, ANumber2 : int ) -> int:
    # Using assertions to check parameters are valid
    assert isinstance( ANumber1, int ), "getHighestNumber2: Parameter ANumber1 missing or invalid"
    assert isinstance( ANumber2, int ), "getHighestNumber2: Parameter ANumber2 missing or invalid"
    return( max( ANumber1, ANumber2 ) )    

# No type hinting
Number1 = 10
Number2 = 20
print( getHighestNumber( Number1, Number2 ) )

# Invalid numbers - no type hinting
Number1 = 10
Number2 = "B"
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

# Creating values of a specific type still allows overwriting
Number3 : int = 10
Number4 : int = 20

# No error at this point
Number4 = "A"
print( getHighestNumber2( Number3, Number4 ) )
