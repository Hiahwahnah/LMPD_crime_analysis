# Project Description
The project analyzes crime data from the years 2022 and 2021 using Python and popular data analysis libraries such as Pandas, Matplotlib, and Seaborn. The code reads crime data from two CSV files, combines them into a single DataFrame, and performs data cleaning by removing unused columns and dropping rows with missing values. The cleaned data is then visualized through three different plots: a count plot showing the number of crimes by crime type, a histogram displaying the distribution of crime occurrences by division with crime types stacked, and a pie chart illustrating the proportion of crime types in the dataset.

## Guide to using Markdown for README.md files

Markdown is a lightweight markup language that is widely used for formatting text in README.md files on GitHub and other platforms. It allows you to add formatting elements, such as headings, lists, code blocks, links, images, and more, to your text.

Here are some commonly used Markdown elements for creating a well-formatted README.md file:

- Headings: Use `#` to create headings of different levels (e.g., `# Main Heading`, `## Subheading`, etc.).
- Lists: Create ordered lists using numbers and unordered lists using dashes or asterisks.
- Code Blocks: Surround code snippets with triple backticks (\```).
- Links: Add links using `[link text](URL)` syntax.
- Images: Include images using `![alt text](image URL)` syntax.
- Emphasis: Use asterisks or underscores to add emphasis to text (*italic* or __bold__).
- Tables: Create tables using pipes and hyphens (| and -).

For a comprehensive guide to Markdown syntax, visit the [Mastering Markdown](https://guides.github.com/features/mastering-markdown/) guide on GitHub.

You can use the above Markdown elements to create a clear and well-structured README.md file for your project, making it easy for others to understand and use your code.


## Required Packages
To run the project, you need to have the following Python packages installed:
- Pandas
- Matplotlib
- Seaborn

Install these packages using the following commands:
```bash
pip install pandas matplotlib seaborn 
```

## Features Included
The project includes the following features to meet the requirements:
- Read TWO data files.
- Clean your data and perform a pandas merge with your two data sets, then calculate some new values based on the new data set.
- Make 3 matplotlib or seaborn visualizations to display your data.
- Build a custom data dictionary and include it in your README.
- Annotate your .py files with well-written comments and a clear README.

## Custom Data Dictionary
The columns in the cleaned DataFrame have been renamed for better readability. Here is a data dictionary explaining each column:

| Column Name     | Description                                               |
|-----------------|-----------------------------------------------------------|
| incident_number | The unique identifier of each crime incident.             |
| date_reported   | The date when the crime was reported.                     |
| date_occurred   | The date when the crime occurred.                         |
| badge_id        | The badge ID of the reporting officer.                    |
| crime_type      | The type of crime that was committed.                     |
| lmpd_division   | The division of the Louisville Metro Police Department.   |
| lmpd_beat       | The beat within the LMPD division.                        |
| premise_type    | The type of premises where the crime occurred.            |
| block_address   | The address block where the crime occurred.               |
| city            | The city where the crime occurred.                        |
| zip_code        | The ZIP code of the location where the crime occurred.    |

## Instructions to Run the Project
1. Ensure you have Python installed on your system.
2. Install the required packages using the provided commands above.
3. Download the CSV files 'LMPD_Crime_Data_2022.csv' and 'LMPD_Crime_Data_2021.csv'.
4. Place the CSV files in the 'assets' folder within the project directory.
5. Run the Python script 'crime_analysis.py' using the command line or your preferred IDE.

The script will read the crime data from both CSV files, merge them into a single DataFrame, clean the data, and display three visualizations as described in the project description. The visualizations will provide insights into crime trends and distributions based on crime types and LMPD divisions.