import streamlit as st
import pandas as pd
import plotly.express as px

# Title of the web app with a custom subtitle
st.title('Data Mine Alumni Dashboard')
st.markdown('**Visualize and Filter Alumni Data with Ease**')

# Step 1: Add a sidebar for file upload and filters
st.sidebar.header('Upload & Filter Data')
uploaded_file = st.sidebar.file_uploader("Upload an Excel file", type=["xlsx"])

if uploaded_file:
    # Step 2: Read the Excel file into a pandas DataFrame
    df = pd.read_excel(uploaded_file)
    
    # Display the first few rows to understand the data structure
    st.write("### Preview of the Uploaded Data", df.head())

    # Step 3: Sidebar Filtering Options
    st.sidebar.subheader('Filter Alumni Data')
    
    name_filter = st.sidebar.text_input('Search by Name:')
    hometown_filter = st.sidebar.text_input('Search by Hometown:')
    employer_filter = st.sidebar.text_input('Search by Employer:')
    job_title_filter = st.sidebar.text_input('Search by Job Title:')
    
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

    # Step 4: Display Metrics
    st.metric(label='Total Alumni', value=len(df))
    st.metric(label='Filtered Results', value=len(filtered_df))
    st.write("### Filtered Results", filtered_df)

    # Step 5: Visualizations
    # Bar chart for top 10 employers
    if len(filtered_df) > 0:
        employer_count = filtered_df['employer'].value_counts().head(10)
        fig = px.bar(employer_count, x=employer_count.index, y=employer_count.values,
                     labels={'x': 'Employer', 'y': 'Number of Alumni'},
                     title='Top 10 Employers of Filtered Alumni')
        st.plotly_chart(fig)

        # Pie chart for job titles distribution
        job_title_count = filtered_df['job_title'].value_counts().head(5)
        fig_pie = px.pie(job_title_count, values=job_title_count.values, names=job_title_count.index,
                         title='Top 5 Job Titles among Filtered Alumni')
        st.plotly_chart(fig_pie)

    # Option to download the filtered data
    @st.cache_data
    def convert_df(df):
        return df.to_csv(index=False).encode('utf-8')

    csv = convert_df(filtered_df)
    st.download_button(
        label="Download filtered data as CSV",
        data=csv,
        file_name='filtered_alumni_data.csv',
        mime='text/csv',
    )

    # Add some styling for better visuals
    st.markdown(
        """
        <style>
        .sidebar .sidebar-content { background-color: #f0f2f6; }
        .css-1d391kg { color: #4B8BBE; } /* Custom color for Streamlit titles */
        .css-1b2kcmj { background-color: #f8f9fa; } /* Light background for the main area */
        </style>
        """, unsafe_allow_html=True
    )
else:
    st.info('Please upload an Excel file to proceed.')
