import streamlit as st
import pandas as pd
import numpy as np

# Page title
st.set_page_config(page_title="Researcher Profile - Kosisochukwu Offojebe", layout="wide")

# Sidebar Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Researcher Profile", "Education", "Publications", "Contact"],
)

# Education SideBar Data
relevant_education = pd.DataFrame({
    "Institution": ["Stellenbosch University, South Africa", "Nnamdi Azikiwe University, Nigeria", "Nnamdi Azikiwe University, Nigeria"],
    "Degree Earned": ["Masters in Molecular Biology", "Bachelor of Pharmacy", "PreScience Diploma"],
    "Date": ["Feb 2025 - Present", "Dec 2016 - Dec 2021", "Jan 2016 - Aug 2016"],
})

extracurricular_training = pd.DataFrame({
    "Course Name": ["Coding Summer School", "Liquid Chromatography - Mass Spectrometry Winter School", "Academic Writing"],
    "Organising Institution": ["CHPC + NITheCS", "CAF - SU", "PMB - UNIZIK"],
    "Training Year": ["2026", "2025", "2024"],
})


# Menu selection Sections
if menu == "Researcher Profile":
    st.title("Researcher Profile")
    st.sidebar.header("Picture Excerpts")

    # Collect basic information
    name = "Kosisochukwu J. Offojebe"
    nick_name = "Kosiie"
    field = "Pharmaceutical Sciences and Molecular Biology"
    institution = "Stellenbosch University"

    # Display basic profile information
    st.write(f"**Full Name:** {name}")
    st.write(f"**Preferred Name:** {nick_name}")
    st.write(f"**Research Field:** {field}")
    st.write(f"**Current Institution:** {institution}")
    
    st.image("Kosiie Headshot.jpg", caption="Kosiie's Headshot")
    
    # Sidebar picture excerpts
    st.sidebar.image("Research_Pic.JPG", caption="Poster Presentation")
    st.sidebar.image("Scii_Comm.jpg", caption="Science Communication")
    st.sidebar.image("Group_Photo.jpg", caption="Picture with Team")


elif menu == "Publications":
    st.title("Publications")
  

    # Upload publications file
    uploaded_file = st.file_uploader("Upload Publication", type=["csv", "pdf"])
    if uploaded_file is not None:
        # For CSV Files
        if uploaded_file.name.endswith(".csv"):
            publications = pd.read_csv(uploaded_file)
            st.dataframe(publications)

        # Add filtering for year or keyword
            keyword = st.text_input("Filter by keyword", "")
            if keyword:
                filtered = publications[
                    publications.apply(
                        lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
            ]
                st.write(f"Filtered Results for '{keyword}':")
                st.dataframe(filtered)
            else:
                st.write("Showing all publications")

        # Publication trends
            if "Year" in publications.columns:
                st.subheader("Publication Trends")
                year_counts = publications["Year"].value_counts().sort_index()
                st.bar_chart(year_counts)
            else:
                st.write("The CSV does not have a 'Year' column to visualize trends.")
            
    # Handle PDF files (to just show metadata or preview)
        elif uploaded_file.name.endswith(".pdf"):
            st.write("You uploaded a PDF file:", uploaded_file.name)
            st.write("Currently, filtering and trends only work with CSV files.")
            
    else:
        st.write("No file uploaded yet")
           

elif menu == "Education":
    st.title("Education")
    st.sidebar.header("Education Type")
    
    # Tabbed view for STEM data
    data_option = st.sidebar.selectbox(
        "Choose the type of Education to explore", 
        ["Formal Education", "Informal Education"]
    )

    if data_option == "Formal Education":
        st.write("### Formal Education")
        st.dataframe(relevant_education)
        

    elif data_option == "Informal Education":
        st.write("### Informal Education")
        st.dataframe(extracurricular_training)
        
        

elif menu == "Contact":
    # Add a contact section
    st.header("Contact Information")
    email = "offojebekosi@gmail.com"
    linkedin = "www.linkedin.com/in/kosiieoffojebe"

    st.write(f"##### You can reach me at {email} or send me a dm on {linkedin}")
