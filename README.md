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

The `scraper.py` script is designed to automate the process of collecting alumni data from LinkedIn profiles. This script uses **Selenium** to log in to LinkedIn, navigate to the provided profile URLs, and scrape specific details such as name, employer, job title, and location. The collected data is saved into a CSV file for integration with the dashboard application.

---

#### **Key Functionalities**:
1. **Automated Login**:
   - Logs into LinkedIn securely using provided credentials.
2. **Profile Scraping**:
   - Collects the following information from each LinkedIn profile:
     - Name
     - Employer
     - Job Title
     - Location
     - LinkedIn Profile URL
3. **Data Export**:
   - Stores the scraped data in a structured CSV file for use in the alumni dashboard.

---

#### **File Requirements**:
- Input: A CSV file containing LinkedIn profile URLs in a column named `linkedin_url`.
- Output: A CSV file (`scraped_data.csv`) containing the scraped alumni details.

---

#### **How to Use**:
1. **Set Up LinkedIn Credentials**:
   - Store your LinkedIn username and password in a secure `.env` file (or directly in the script if necessary):
     ```
     LINKEDIN_USERNAME=your_email@example.com
     LINKEDIN_PASSWORD=your_password
     ```

2. **Run the Script**:
   ```bash
   python scraper.py

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
