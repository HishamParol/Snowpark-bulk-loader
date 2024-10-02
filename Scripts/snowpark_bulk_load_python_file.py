import pandas as pd
from snowflake.snowpark import Session
from snowflake.snowpark.context import get_active_session
from config import input_files, output_tables, database, schema  # Import from config file

# Function to create a session (configure with actual credentials)
def create_snowflake_session():
    session = Session.builder.configs({
        'account': '<SNOWFLAKE_ACCOUNT>',
        'user': '<SNOWFLAKE_USER>',
        'password': '<SNOWFLAKE_PASSWORD>',
        'role': '<SNOWFLAKE_ROLE>',
        'warehouse': '<SNOWFLAKE_WAREHOUSE>',
        'database': database,
        'schema': schema
    }).create()
    return session

# Main function to load bulk Excel files to Snowflake
def load_data_to_snowflake(session):
    Z = database + '.' + schema + '.'

    # Loop through each input file and corresponding output table
    for input_file, output_table in zip(input_files, output_tables):
        # Read the CSV file into a Pandas DataFrame
        df = pd.read_csv(input_file)
        
        # Create a Snowpark DataFrame from the Pandas DataFrame
        snowpark_df = session.create_dataframe(df)
        
        # Write the Snowpark DataFrame to Snowflake, overwriting the table if it exists
        snowpark_df.write.mode("overwrite").save_as_table(Z + output_table)
        
        print(f"DataFrame from {input_file} saved to Snowflake table {output_table}")

# Main execution
if __name__ == "__main__":
    #session = create_snowflake_session()  #Manually define the Snowflake connections
    session = get_active_session()  # Get current active session
    load_data_to_snowflake(session)
