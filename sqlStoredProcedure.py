#
# This script uses pyodbc ODBC driver available from Microsoft at:
# https://docs.microsoft.com/en-us/sql/connect/sql-connection-libraries?view=sql-server-ver15#anchor-20-drivers-relational-access
#
# You can also install from the command prompt by typing: pip3 install pyodbc
#
# Stored procedure with parameter written as
#
# create procedure [dbo].[usp_customer_get] (
# 	@p_cus_id_int int
# )
# as
# begin
# 	set nocount on;
# 	select * from tb_customer
# 	where cus_id_pk = @p_cus_id_int
# end

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

# SP List all customers
def spCustomerListAll( p_sqlConnection : type ) -> bool:

    spCustomerList = r'exec usp_customer_list'

    try:

        sqlCursor = p_sqlConnection.cursor()
        sqlCursor.execute( spCustomerList )

        spRows = sqlCursor.fetchall()

        for row in spRows:
            # Print primary key and name - column ids are 0 based
            print(  str( row[ 0 ] ) + ' ' + row[ 1 ] )

        sqlCursor.close()
        del sqlCursor    

    except pyodbc.Error as e:

        print( 'Error: Could not execute stored procedure: ' + str( e ) )
        return( False )

    return( True )    

# SP Get customer based on primary key
def spCustomerGet( p_sqlConnection : type, p_customerID : int ) -> bool:

    # Set up stored procedure - r indicates raw string - backslashes are part of the string
    spCustomerGet = r'exec usp_customer_get @p_cus_id_int = ' + str( p_customerID )

    try:

        sqlCursor = p_sqlConnection.cursor()
        sqlCursor.execute( spCustomerGet )

        spRows = sqlCursor.fetchall()

        for row in spRows:
            # Print primary key and name - column ids are 0 based
            print(  str( row[ 0 ] ) + ' ' + row[ 1 ] )

        sqlCursor.close()
        del sqlCursor    

    except pyodbc.Error as e:

        print( 'Error: Could not execute stored procedure: ' + str( e ) )
        return( False )

    return( True )    

# Starting point for standalone apps
if __name__ == '__main__' :

    sqlConnection : type = None
    customerID : int = 2

    # Connect to server - result is a tuple passing back connection reference
    # as Python always passed parameters by value
    resultTuple = ConnectToServer( sqlConnection )

    # First element is result, second is connection handle
    if resultTuple[ 0 ]:
        print( 'Connected to database' )        

        # Select all rows from a table via stored procedure
        if spCustomerListAll( resultTuple[ 1 ] ):
            print( 'Stored procedure list all customers executed' )

        # Select a particular customer by passing primary key
        if spCustomerGet( resultTuple[ 1 ], customerID ):
            print( 'Stored procedure get a customer executed' )

    # Close connection
    #sqlConnection.close()         