## TuplesAndLists
#
# Demonstration of techniques with tuples and lists
# Tuples cannot be changed, values enclosed with parenthesis.
# Tuples can be used as replacement for constant arrays 
#   available in other languages.
# Lists can be modified.

list1  = [ 10, 20, 30, 40, 50, 5, 2 ]
tuple1 = ( 10, 20, 30, 40, 50, 5, 2 )

list2 = [ 'apple', 'orange', 'banana' ]
tuple2 = ( 'apple', 'orange', 'banana' )

list3 = [ 10, 'apple', 30 ]
tuple3 = ( 10, 'apple', 30 )

list4 = [ 'aba', 'a1a', 'b5c', 'eaa' ]

# Two dimension list
list6 = [ [ 81, 82, 83 ],    # Row 0
          [ 84, 85, 86 ],    # Row 1
          [ 87, 88, 89 ] ]   # Row 2

# Tuple using key-pair as dictionary lookup
Countries = { 'United Kingdom': 'London',
              'France'        : 'Paris',
              'Spain'         : 'Madrid' }

## Tuple returning values ######################################################

# Show capital
print( Countries[ 'France' ] )

# Country not found - gives runtime error
print( Countries[ 'USA'] )

## List adding elements ########################################################

# Appending to single dimension list 
print( list1 )
list1.append( 80 )           
print( list1 )

# Appending to two dimension list - list will have 4 columns instead of 3
print( list6 )
list6[ 0 ].append( 10 )
list6[ 1 ].append( 11 )
list6[ 2 ].append( 12 )
print( list6 )

## List iteration ##############################################################

# Print full list
print( list1 )
print( tuple1 )

# Can iterate manually - for integer list convert to str for printing
for listIndex, listItem in enumerate( list1 ):
    print( 'Index: ' + str( listIndex ) + ' ListItem: ' + str( listItem ) )

# Iterating a string list
for listIndex, listItem in enumerate( list2 ):
    print( 'Index: ' + str( listIndex ) + ' ListItem: ' + listItem )

# Iterate two dimension list
for rowIndex, rowItem in enumerate( list6 ):
    print( '---' )
    for colIndex, colItem in enumerate( rowItem ):
        print( 'Row:' +  str( rowIndex ) + ' Col: ' + str( colIndex ) + ' Value: ' + str( colItem ) )

## List Min/Max/Sum ############################################################

# Get maximum element
print( 'Max list ' + str( max( list1 ) ) )
print( 'Max tuple ' + str( max( tuple1 ) ) )

# Get minimum element
print( 'Min list ' + str( min( list1 ) ) )
print( 'Min tuple ' + str( min( tuple1 ) ) )

# For string elements shows highest value alphabetically
print( 'Max string list ' + str( max( list2 ) ) )
print( 'Max string tuple ' + str( max( tuple2 ) ) )

## List element conversion #####################################################

# Convert elements from integer to string

print( list3 )
liststr1 = []
for listItem in list3:
    liststr1.append( str( listItem ) )
print( liststr1 )

# We can assign new list to old list
list3 = liststr1

# Now we can get max, was failling because elements were of different data types
print( 'Max list ' + str( max( list3 ) ) )

## List sorting ################################################################

# Sort list using sort
list1.sort()
print( list1 )

# Sort list using sort, reverse
list1.sort( reverse = True )
print( list1 )

# Sort list using sorted
list1a = sorted( list1 )
print( list1a )

# Custom sort function - strings are 0 offset based
def sortOnSecondElement( AElement ):
    return AElement[ 1 ]

# Custom sort by calling a function for element comparison - sorting on second element
list4.sort( key = sortOnSecondElement )
print( list4 )


















