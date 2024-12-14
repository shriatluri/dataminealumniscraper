# Data Mine Alumni Dashboard

This project is a **Streamlit-based application** designed to visualize and manage **alumni data** for Purdue University's **Data Mine Program**. The application includes powerful filtering tools, interactive visualizations, location-based heatmaps, and alumni profile insights. It also features automated geocoding for alumni locations and a web scraping component for LinkedIn profiles.

---

## Key Features
1. **Alumni Dashboard**:
   - Upload an Excel file of alumni data and visualize it with ease.
   - Filter alumni by name, hometown, employer, job title, graduation dates, and more.
   - View individual alumni profiles with detailed information.
   - Export filtered data as **CSV** or **Excel** files.
2. **Visualizations**:
   - Interactive bar charts of top employers.
   - Pie charts showing job title distributions.
   - Heatmaps of alumni locations.
3. **Web Scraper**:
   - Scrapes LinkedIn profiles for detailed alumni information such as job title, location, and employer.
4. **Geocoding Utility**:
   - Converts hometowns into latitude and longitude for location-based insights.

---

## Project Structure
### `scraper.py`

The `scraper.py` script is a simple tool designed to convert LinkedIn profile data exported from **PhantomBuster's HTML extension** into an Excel file. It parses an HTML file containing table data and extracts relevant information, saving it as an easy-to-read Excel file for further analysis.

---

#### **How to Use**

1. **Export HTML from PhantomBuster**:
   - Use PhantomBuster to scrape LinkedIn profiles and export the data as an **HTML file**.
   - Save the exported file (e.g., `LinkedIn_Profile_Scraper.html`) to your local machine.

2. **Specify File Paths**:
   - Open the `scraper.py` script and set the paths for:
     - **Input HTML file**: The file exported by PhantomBuster.
     - **Output Excel file**: The name of the Excel file where the parsed data will be saved.
   - Example:
     ```python
     html_file_path = '/path/to/LinkedIn_Profile_Scraper.html'  # Replace with your PhantomBuster HTML file
     output_excel_path = 'linkedin_profiles.xlsx'  # Replace with desired output file name
     ```

3. **Run the Script**:
   - Execute the script with Python:
     ```bash
     python scraper.py
     ```

4. **Output**:
   - The extracted data will be saved to the specified **Excel file** (e.g., `linkedin_profiles.xlsx`).

---

#### **What You Need to Know**
- **Input File**: The script expects an HTML file with table data (exported by PhantomBuster).
- **Output File**: The script generates an Excel file with the extracted data.
- **No Modifications Needed**: Simply update the `html_file_path` and `output_excel_path` in the script.

---

#### **Sample Input and Output**

**Input File (HTML)**:
An HTML file exported from PhantomBuster containing LinkedIn profile data in table format.

**Output File (Excel)**:
A structured Excel file with the extracted data:
| Name              | Employer    | Job Title          | Location       |
|-------------------|-------------|--------------------|----------------|
| Jack W. Doherty   | Oracle      | Software Engineer  | Santa Claraca  |
| Sarah J. Johnson  | Google      | Data Scientist     | San Francisco  |

---

#### **Dependencies**
Ensure the following libraries are installed:
- **Pandas**: For handling data and exporting to Excel.
- **BeautifulSoup4**: For parsing the HTML file.

Install them with:
```bash
pip install pandas beautifulsoup4

### `webapp.py`
The core Streamlit application for visualizing and filtering alumni data.

#### Key Functionalities:
- **Upload and Filter Data**:
  - Upload an Excel file to process alumni data.
  - Apply filters by name, employer, hometown, and more.
- **Visualizations**:
  - Bar and pie charts for employers and job titles.
  - A **heatmap** showing alumni locations using geocoded data.
- **Alumni Profile Insights**:
  - View detailed alumni profiles with a clickable LinkedIn URL.
- **Data Export**:
  - Download the filtered alumni data as **CSV** or **Excel**.

---

### `geocode.py`
A standalone script for geocoding alumni hometowns into geographic coordinates (latitude and longitude).

#### Key Functionalities:
- Uses the **Geopy** library with the `Nominatim` API for geocoding.
- Processes a list of unique hometowns from the alumni data.
- Outputs a `geocoded_locations.csv` file containing:
  - Location names.
  - Latitude and longitude.
- Caches results to avoid redundant geocoding requests and API rate limits.

#### Usage:
```bash
python geocode.py
