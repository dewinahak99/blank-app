import streamlit as st
import pandas as pd

# Title and description
st.title("Dataset Chart Generator")
st.write("Upload a CSV file, select the chart options from the sidebar, and see the visualization and data preview on the main screen.")

# File uploader in the sidebar
st.sidebar.header("Upload and Settings")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

# Check if a file is uploaded
if uploaded_file is not None:
    # Read the uploaded file
    df = pd.read_csv(uploaded_file)
    
    # Sidebar controls for selecting columns and chart type
    st.sidebar.write("Chart Options")
    selected_columns = st.sidebar.multiselect("Select columns to display in the chart", df.columns)
    
    # Sidebar control for chart type
    chart_type = st.sidebar.selectbox("Select the chart type", ["Area Chart", "Line Chart", "Bar Chart"])
    
    # Main area: Display selected columns and chart
    if selected_columns:
        st.write("### Selected columns data preview:")
        st.dataframe(df[selected_columns].head())  # Show the first few rows of the selected columns
        
        st.write(f"### {chart_type}")
        if chart_type == "Area Chart":
            st.area_chart(df[selected_columns])
        elif chart_type == "Line Chart":
            st.line_chart(df[selected_columns])
        elif chart_type == "Bar Chart":
            st.bar_chart(df[selected_columns])
else:
    st.write("Please upload a CSV file using the sidebar.")
