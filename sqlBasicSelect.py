#
# This script uses pyodbc ODBC driver available from Microsoft at:
# https://docs.microsoft.com/en-us/sql/connect/sql-connection-libraries?view=sql-server-ver15#anchor-20-drivers-relational-access
#
# You can also install from the command prompt by typing: pip3 install pyodbc

import pyodbc

# Connection to server via ODBC
# Python cannot pass by reference, hence return value is a tuple containing Success and connection handle
def ConnectToServer( p_sqlConnection : type ):

    sqlLogin      : str = ''
    sqlPassword   : str = '' 
    sqlServer     : str = 'localhost\\sqlserver' 
    sqlDatabase   : str = 'test'

    # Get SQL login name
    sqlLogin = input( 'Login: ' )

    # Get SQL password
    sqlPassword = input( 'Password: ' )

    try:
        p_sqlConnection = pyodbc.connect( 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + \
           sqlServer + ';DATABASE=' + sqlDatabase+';UID=' + sqlLogin + ';PWD=' + sqlPassword )
        #sqlCursor = p_sqlConnection.cursor()

    except:
        print( 'Error: Could not connect to ' + sqlServer )
        return( False, p_sqlConnection )

    return( True, p_sqlConnection )

# Select customer table
def selectCustomers( p_sqlConnection : type ) -> bool:

    sqlQuery = 'select * from test.dbo.tb_customer'

    try:

        sqlCursor = p_sqlConnection.cursor()
        sqlCursor.execute( sqlQuery )

        for row in sqlCursor.fetchall():
            print( row )

    except:

        print( 'Error: Could not retrieve custommers' )
        return( False )

    return( True )    

# Starting point for standalone apps
if __name__ == '__main__' :

    sqlConnection : type = None

    # Connect to server - result is a tuple passing back connection reference
    # as Python always passed parameters by value
    resultTuple = ConnectToServer( sqlConnection )

    # First element is result, second is connection handle
    if resultTuple[ 0 ]:
        print( 'Connected to database' )        

        # Select some data from a table
        if selectCustomers( resultTuple[ 1 ] ):
            print( 'Customers selected' )




