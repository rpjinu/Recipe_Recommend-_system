# Recipe_Recommend-_system
"A recipe recommendation system that filters and suggests recipes based on user preferences, cuisine, occasion, season, allergens, and difficulty level using a CSV dataset."
<img src="">

# 🍲 Recipe Recommendation System 🍽️

Welcome to the **Recipe Recommendation System** project! This application filters and recommends recipes based on various user preferences, including cuisine, occasion, season, allergens, and difficulty level.

## 📄 Project Description

This project provides a **recipe recommendation system** that allows users to input their preferences and get tailored recipe suggestions from a dataset. The system utilizes **Streamlit** for the web interface and works by filtering a dataset of recipes based on user inputs.

## 🚀 Features

- **Filter Recipes**: Select cuisine, occasion, season, allergen, user preference, and difficulty level.
- **User-friendly Interface**: Interactive web interface powered by Streamlit.
- **Custom Recommendations**: Get personalized recipes with ingredients, preparation steps, and difficulty level.
- **Real-time Results**: The app instantly displays the recommended recipes based on the selected criteria.

## 💻 Installation

To run this project on your local machine, follow these steps:

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/recipe-recommendation-system.git
cd recipe-recommendation-system

# Recipe Recommendation App 🍽️

This app helps users find recipes based on various filters such as cuisine type, occasion, season, allergen information, user preferences, and difficulty level. Below is a detailed explanation of how the app works, the data used, and the technologies involved.

## 🧑‍🍳 How It Works

### Input Fields
Users provide inputs via select boxes for:
- **Cuisine Type** 🍝
- **Occasion** 🎉
- **Season** 🌸
- **Allergen Information** 🚫
- **User Preferences** 🍽️
- **Difficulty Level** 🔥

### Filter and Recommendation
Based on the selected filters, the app queries the dataset and displays matching recipes.

### Output
For each matching recipe, the app shows:
- **Recipe Name** 🍴
- **Ingredients List** 🥕
- **Preparation Steps** 🍳
- **Difficulty Level** 🧑‍🍳
- **Allergen Information** 🚫
- **Season and Occasion** 🗓️

## 📊 Data
The data used in this project is a CSV file containing information about different recipes. It includes columns such as:
- **Recipe_ID** 🍽️
- **Recipe_Name** 🍲
- **Cuisine_Type** 🌍
- **Ingredients_List** 🥕
- **Preparation_Steps** 🍳
- **Difficulty_Level** 🔥
- **User_Preferences** 🥗
- **Season** 🌸
- **Occasion** 🎉
- **Allergen_Information** 🚫
- **Seasonal_Availability** 📅

## 🌍 Technologies Used
- **Streamlit**: For creating the web application interface.
- **Pandas**: For data handling and manipulation.
- **Python**: The core programming language.
- **CSV**: For storing recipe data.
