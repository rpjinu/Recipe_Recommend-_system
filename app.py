import streamlit as st
import pandas as pd

# Load dataset from CSV
@st.cache_data
def load_data():
    # Replace with the path to your actual CSV file
    return pd.read_csv(r"C:\Users\Ranjan kumar pradhan\.vscode\project_vs\Recipe_recommend\Recipe_recommend_cleaned.csv")

# Streamlit app
st.title("Recipe Recommendation App")

# Load data
data = load_data()

# User inputs from sidebar
st.sidebar.header("Filter Recipes")
cuisine = st.sidebar.selectbox("Select Cuisine", data['Cuisine_Type'].unique())
occasion = st.sidebar.selectbox("Select Occasion", data['Occasion'].unique())
season = st.sidebar.selectbox("Select Season", data['Season'].unique())
allergen = st.sidebar.selectbox("Select Allergen Information", ['None'] + list(data['Allergen_Information'].unique()))
user_preference = st.sidebar.selectbox("Select User Preference", ['None'] + list(data['User_Preferences'].unique()))
difficulty = st.sidebar.selectbox("Select Difficulty Level", data['Difficulty_Level'].unique())

# Filter data based on user inputs
filtered_data = data[(
    data['Cuisine_Type'] == cuisine) & 
    (data['Occasion'] == occasion) & 
    (data['Season'] == season) & 
    ((data['Allergen_Information'] == allergen) | (allergen == "None")) & 
    ((data['User_Preferences'] == user_preference) | (user_preference == "None")) & 
    (data['Difficulty_Level'] == difficulty)
]

# Remove duplicate rows (if any) based on unique Recipe_ID or Recipe_Name
filtered_data = filtered_data.drop_duplicates(subset='Recipe_Name')

# Display filtered recipes
st.subheader("Recommended Recipes")
if not filtered_data.empty:
    for _, row in filtered_data.iterrows():
        st.markdown(f"### {row['Recipe_Name']}")
        st.write(f"**Ingredients:** {row['Ingredients_List']}")
        st.write(f"**Preparation Steps:** {row['Preparation_Steps']}")
        st.write(f"**Allergen Information:** {row['Allergen_Information']}")
        st.write("---")
else:
    st.write("No recipes match the selected criteria.")

