import pandas as pd
from bs4 import BeautifulSoup

def extract_html_to_excel(html_file, output_file):
    """
    Extracts table data from an HTML file and saves it as an Excel file.

    :param html_file: Path to the HTML file to parse.
    :param output_file: Path to save the resulting Excel file.
    """
    # Load the HTML content
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all rows in the table
    rows = soup.select('tr')

    # Extract headers and data
    data = []
    headers = []

    if rows:
        # Extract headers if present
        header_row = rows[0].find_all('th')
        if header_row:
            headers = [header.get_text(strip=True) for header in header_row]
            data_rows = rows[1:]  # Skip the header row
        else:
            data_rows = rows

        # Extract data rows
        for row in data_rows:
            cols = row.find_all(['td', 'th'])
            data.append([col.get_text(strip=True) for col in cols])

    # Create a DataFrame
    df = pd.DataFrame(data, columns=headers if headers else None)

    # Save to Excel
    df.to_excel(output_file, index=False)
    print(f"Data has been saved to {output_file}")

# Specify the input HTML file and output Excel file
html_file_path = '/Users/shriatluri/DATAMINE/dataminealumniscraper/LinkedIn Profile Scraper _ PhantomBuster.html'  # Replace with your HTML file path
output_excel_path = 'e.xlsx'  # Replace with your desired output file name

# Run the function
extract_html_to_excel(html_file_path, output_excel_path)
