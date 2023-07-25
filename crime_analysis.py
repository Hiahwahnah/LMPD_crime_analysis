import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to read crime data from a CSV file into a DataFrame
def read_crime_data(file_path):
    try:
        df = pd.read_csv(file_path, low_memory=False)
        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

# Function to remove unused columns from the DataFrame
def remove_unused_columns(df):
    # Columns to remove from the DataFrame
    columns_to_remove = ['UOR_DESC', 'NIBRS_CODE', 'UCR_HIERARCHY', 'ATT_COMP', 'ObjectId']
    df = df.drop(columns=columns_to_remove)
    return df

# Function to rename columns in the DataFrame for better readability
def rename_columns(df):
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
    df.rename(columns=fixed_columns, inplace=True)
    return df

# Function to clean the DataFrame by dropping rows with missing values
def clean_data(df):
    df.dropna(inplace=True)
    return df

# Main function to execute the entire analysis
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


    # Visualization 1: Divisions by Most Crime Occurrence
    plt.figure(figsize=(10, 6))
    order_divisions = combined_df['lmpd_division'].value_counts().index
    sns.countplot(data=combined_df, x='lmpd_division', hue='crime_type', order=order_divisions, palette='muted')
    plt.title('Divisions by Most Crime Occurrence')
    plt.xlabel('LMPD Division')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend(title='Crime Type', title_fontsize=10, fontsize=8)
    plt.show()

    # Interpretation: This visualization shows the distribution of crime occurrences in each LMPD division.
    # The x-axis represents the LMPD divisions, and the y-axis represents the count of crimes in each division.
    # Different crime types are represented by different colors, and the stacked bars show the count of each crime type within the division.
    # The legend provides information about the crime types.

    # Visualization 2: Proportion of Crime Types
    plt.figure(figsize=(10, 6))
    crime_type_counts = combined_df['crime_type'].value_counts(normalize=True) * 100
    sns.barplot(x=crime_type_counts.index, y=crime_type_counts, palette='viridis')
    plt.title('Proportion of Crime Types')
    plt.xlabel('Crime Type')
    plt.ylabel('Percentage')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Interpretation: This visualization shows the proportion of each crime type in the dataset.
    # The x-axis represents the crime types, and the y-axis represents the percentage of each crime type in the dataset.
    # The bar heights represent the percentage of each crime type, and the x-axis labels show the crime types.
    # This visualization provides insights into the relative frequency of different crime types in the dataset.

    # Visualization 3: Top 3 Types of Crimes
    plt.figure(figsize=(10, 6))
    top_crimes = combined_df['crime_type'].value_counts().nlargest(3).index
    sns.countplot(x='crime_type', data=combined_df, order=top_crimes, palette='viridis')
    plt.title('Top 3 Types of Crimes')
    plt.xlabel('Crime Type')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Interpretation: This visualization shows the top 3 most frequent types of crimes in the dataset.
    # The x-axis represents the crime types, and the y-axis represents the count of each crime type.
    # The bars are ordered based on the count of each crime type, with the most frequent crime type on the left.
    # This visualization provides insights into the most common types of crimes recorded in the dataset.

if __name__ == "__main__":
    main()