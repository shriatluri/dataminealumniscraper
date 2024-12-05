import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from io import BytesIO
from folium.plugins import HeatMap

# Title of the web app with a custom subtitle
st.title('Data Mine Alumni Dashboard')
st.markdown('**Visualize and Filter Alumni Data with Ease**')

# Sidebar for file upload and filters
st.sidebar.header('Upload & Filter Data')
uploaded_file = st.sidebar.file_uploader("Upload an Excel file", type=["xlsx"])

if uploaded_file:
    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(uploaded_file)

    # Display the first few rows of the uploaded data
    st.write("### Preview of the Uploaded Data", df.head())

    # Sidebar Filtering Options
    st.sidebar.subheader('Filter Alumni Data')
    name_filter = st.sidebar.text_input('Search by Name:')
    hometown_filter = st.sidebar.text_input('Search by Hometown:')
    employer_filter = st.sidebar.text_input('Search by Employer:')
    job_title_filter = st.sidebar.text_input('Search by Job Title:')
    graduation_start = st.sidebar.date_input("Graduation Start Date")
    graduation_end = st.sidebar.date_input("Graduation End Date")
    major_filter = st.sidebar.selectbox('Select Major:', ['All'] + df['major'].unique().tolist() if 'major' in df else ['All'])

    # Apply filters to the DataFrame
    filtered_df = df.copy()

    if name_filter:
        filtered_df = filtered_df[filtered_df['name'].str.contains(name_filter, case=False, na=False)]

    if hometown_filter:
        filtered_df = filtered_df[filtered_df['home_town'].str.contains(hometown_filter, case=False, na=False)]

    if employer_filter:
        filtered_df = filtered_df[filtered_df['employer'].str.contains(employer_filter, case=False, na=False)]

    if job_title_filter:
        filtered_df = filtered_df[filtered_df['job_title'].str.contains(job_title_filter, case=False, na=False)]

    if 'graduation_date' in filtered_df.columns and graduation_start and graduation_end:
        filtered_df = filtered_df[
            (filtered_df['graduation_date'] >= pd.to_datetime(graduation_start)) & 
            (filtered_df['graduation_date'] <= pd.to_datetime(graduation_end))
        ]

    if major_filter != 'All' and 'major' in filtered_df.columns:
        filtered_df = filtered_df[filtered_df['major'] == major_filter]

    # Display metrics
    st.metric(label='Total Alumni', value=len(df))
    st.metric(label='Filtered Results', value=len(filtered_df))
    st.write("### Filtered Results", filtered_df)

    # Load pre-geocoded data
    geocoded_data = pd.read_csv("geocoded_locations.csv")  # Pre-geocoded file

    # Merge geocoded data with the filtered alumni data
    if 'home_town' in filtered_df.columns:
        merged_df = filtered_df.merge(geocoded_data, left_on='home_town', right_on='Location', how='left')
        heatmap_data = merged_df[['Latitude', 'Longitude']].dropna()

        # Create heatmap only if valid coordinates exist
        if not heatmap_data.empty:
            st.write("### Alumni Location Heatmap")
            m = folium.Map(location=[39.8283, -98.5795], zoom_start=4)  # Centered in the USA
            HeatMap(heatmap_data.values.tolist()).add_to(m)
            st.components.v1.html(m._repr_html_(), height=600, scrolling=True)
        else:
            st.write("No valid location data available for the heatmap.")
    else:
        st.write("Location data is missing in the uploaded file.")
    
    # Step 3: Alumni Profile Insights
    # Display detailed alumni profiles
    st.write("### Alumni Profile Insights")
    if not filtered_df.empty:
        selected_name = st.selectbox("Select an alumni name for more details:", filtered_df['name'].tolist())
        selected_row = filtered_df[filtered_df['name'] == selected_name].iloc[0]

        # Create a styled alumni profile card with fixed LinkedIn URL
        linkedin_url = selected_row.get('note', '#')
        if linkedin_url and not linkedin_url.startswith("http"):
            linkedin_url = f"https://{linkedin_url}"

        st.markdown(f"""
            <div style="
                background-color:#ffffff;
                padding:20px;
                border-radius:10px;
                box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
                color:#333333; 
                font-family:Arial, sans-serif;">
                <h2 style="color:#4B8BBE;">🎓 {selected_row.get('name', 'Not available')}</h2>
                <p style="margin:5px 0;"><strong>Employer:</strong> {selected_row.get('employer', 'Not available')}</p>
                <p style="margin:5px 0;"><strong>Job Title:</strong> {selected_row.get('job_title', 'Not available')}</p>
                <p style="margin:5px 0;"><strong>Location:</strong> {selected_row.get('home_town', 'Not available')}</p>
                <p style="margin:5px 0;"><strong>LinkedIn URL:</strong> 
                    <a href="{linkedin_url}" target="_blank" style="color:#1a73e8;">View Profile</a>
                </p>
            </div>
        """, unsafe_allow_html=True)
        


    # Visualizations
    if len(filtered_df) > 0:
        st.write("### Visualizations")

        # Bar chart for top employers
        if 'employer' in filtered_df.columns:
            employer_count = filtered_df['employer'].value_counts().head(10)
            fig = px.bar(employer_count, x=employer_count.index, y=employer_count.values,
                         labels={'x': 'Employer', 'y': 'Number of Alumni'},
                         title='Top 10 Employers of Filtered Alumni')
            st.plotly_chart(fig)

        # Pie chart for job titles
        if 'job_title' in filtered_df.columns:
            job_title_count = filtered_df['job_title'].value_counts().head(5)
            fig_pie = px.pie(job_title_count, values=job_title_count.values, names=job_title_count.index,
                             title='Top 5 Job Titles among Filtered Alumni')
            st.plotly_chart(fig_pie)
    

    # Download Options
    st.write("### Download Filtered Data")
    @st.cache_data
    def convert_to_csv(df):
        return df.to_csv(index=False).encode('utf-8')

    # Function to convert DataFrame to Excel in-memory
    @st.cache_data
    def convert_to_excel(df):
        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, index=False)
        output.seek(0)  # Rewind the buffer
        return output.getvalue()

    csv = convert_to_csv(filtered_df)
    st.download_button(label="Download as CSV", data=csv, file_name="filtered_alumni_data.csv", mime="text/csv")

    excel = convert_to_excel(filtered_df)
    st.download_button(label="Download as Excel", data=excel,
                       file_name="filtered_alumni_data.xlsx",
                       mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

else:
    st.info('Please upload an Excel file to proceed.')
