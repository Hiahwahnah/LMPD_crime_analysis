import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def read_crime_data(file_path):
    try:
        df = pd.read_csv(file_path, low_memory=False)  # Read CSV file into a DataFrame
        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

def remove_unused_columns(df):
    # Columns to remove from the DataFrame
    columns_to_remove = ['UOR_DESC', 'NIBRS_CODE', 'UCR_HIERARCHY', 'ATT_COMP', 'ObjectId']
    df = df.drop(columns=columns_to_remove)  # Drop specified columns from the DataFrame
    return df

def rename_columns(df):
    # Rename columns in the DataFrame for better readability
    fixed_columns = {
        'INCIDENT_NUMBER': 'incident_number',
        'DATE_REPORTED': 'date_reported',
        'DATE_OCCURED': 'date_occurred',
        'BADGE_ID': 'badge_id',
        'CRIME_TYPE': 'crime_type',
        'LMPD_DIVISION': 'lmpd_division',
        'LMPD_BEAT': 'lmpd_beat',
        'PREMISE_TYPE': 'premise_type',
        'BLOCK_ADDRESS': 'block_address',
        'City': 'city',
        'ZIP_CODE': 'zip_code'
    }
    df.rename(columns=fixed_columns, inplace=True)  # Rename columns in the DataFrame
    return df

def clean_data(df):
    df.dropna(inplace=True)  # Drop rows with any missing values from the DataFrame
    return df

def main():
    # Read crime data for the years 2022 and 2021
    crime_data_22 = read_crime_data('assets/LMPD_Crime_Data_2022.csv')
    crime_data_21 = read_crime_data('assets/LMPD_Crime_Data_2021.csv')

    if crime_data_22 is None or crime_data_21 is None:
        return

    # Combine the data from both years into a single DataFrame
    combined_df = pd.concat([crime_data_22, crime_data_21], axis=0)
    combined_df.reset_index(drop=True, inplace=True)

    # Remove unused columns from the DataFrame
    combined_df = remove_unused_columns(combined_df)

    # Rename columns in the DataFrame for better readability
    combined_df = rename_columns(combined_df)

    # Clean the DataFrame by dropping rows with missing values
    combined_df = clean_data(combined_df)

    # Print information about the cleaned DataFrame
    print("Shape of cleaned DataFrame:", combined_df.shape)
    print("Random 10 rows from the cleaned DataFrame:")
    print(combined_df.sample(10))
    
    # Visualization 1: Count of Crimes by Crime Type
    plt.figure(figsize=(10, 6))
    sns.countplot(x='crime_type', data=combined_df, palette='viridis')
    plt.title('Count of Crimes by Crime Type')
    plt.xlabel('Crime Type')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Visualization 2: Distribution of Crime Occurrence by Division
    plt.figure(figsize=(10, 6))
    sns.histplot(data=combined_df, x='lmpd_division', hue='crime_type', multiple='stack', palette='muted')
    plt.title('Distribution of Crime Occurrence by Division')
    plt.xlabel('LMPD Division')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Visualization 3: Proportion of Crime Types
    plt.figure(figsize=(8, 8))
    combined_df['crime_type'].value_counts().plot.pie(autopct='%1.1f%%', shadow=True, explode=[0.05] * len(combined_df['crime_type'].unique()))
    plt.title('Proportion of Crime Types')
    plt.ylabel('')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()