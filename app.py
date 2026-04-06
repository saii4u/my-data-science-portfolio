# --- GIT COMMANDS FOR UPDATING WEBSITE ---
# 1. git add .
# 2. git commit -m "Describe your changes here"
# 3. git push origin main

import streamlit as st
import plotly.express as px
import pandas as pd

# 1. Configuration
st.set_page_config(page_title="Sai Krishna Anumula | Data Scientist", page_icon="📊", layout="wide")

# 2. Sidebar Navigation
st.sidebar.title("Navigation")
# NOTE: Make sure these names match exactly in the 'if/elif' blocks below
page = st.sidebar.radio("Go to", ["🏠 Home", "🧪 Projects", "🛠 Skills", "📬 Contact"])

# --- 🏠 HOME PAGE ---
if page == "🏠 Home":
    st.title("Hi, I'm Sai Krishna 👋")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Data Scientist | Machine Learning Engineer")
        st.write("""
        I am a passionate Data Scientist dedicated to turning complex datasets into 
        actionable business insights. With a background in Machine Learning and 
        Data Visualization, I thrive on solving real-world problems through code.
        """)
        
        # Link Buttons
        st.link_button("🔗 GitHub", "https://github.com/saii4u")
        st.link_button("🔗 LinkedIn", "https://linkedin.com/in/sai-krishna-anumula")
        
        st.write("---")
        st.write("### 🔍 What I Do")
        st.write("""
        * **Machine Learning:** Building predictive models (Regression, Classification).
        * **Data Storytelling:** Creating interactive dashboards.
        * **Problem Solving:** Optimizing workflows using Python.
        """)
    
    with col2:
        st.image("https://raw.githubusercontent.com/saii4u/my-data-science-portfolio/main/profile.jpg.jpeg", width=250)

    st.success("💡 Tip: Check out my 'Projects' tab to see my work in action!")
    
# --- 🧪 PROJECTS PAGE ---
elif page == "🧪 Projects":
    st.title("Featured Data Science Projects 🚀")
    st.write("Here are some of the real-world problems I've solved using data.")

 # --- LIVE PROJECT: SALARY PREDICTION ---
    with st.container():
        st.subheader("Live AI Model: Salary Prediction Engine 💰")
        st.write("""
        Input your years of experience below. This app uses a **Multi-layer Perceptron (MLP) Neural Network** trained on historical salary data to estimate your market value.
        """)

        import joblib
        import numpy as np

        try:
            # 1. Load the "Brains" of the project
            # These files must be in the same GitHub folder as app.py
            model = joblib.load('salary_model.pkl')
            scaler = joblib.load('salary_scaler.pkl')

            # 2. User Interface Layout
            c1, c2 = st.columns([1, 1])
            
            with c1:
                st.markdown("### 🛠️ Input Features")
                years = st.number_input("Years of Experience", min_value=0.0, max_value=50.0, value=5.0, step=0.5)
                predict_btn = st.button("Calculate Salary")
            
            with c2:
                st.markdown("### 🎯 Result")
                if predict_btn:
                    # Process input: Scale -> Predict
                    scaled_input = scaler.transform(np.array([[years]]))
                    prediction = model.predict(scaled_input)
                    
                    st.success(f"Estimated Salary: **${prediction[0]:,.2f}**")
                    st.balloons()
                else:
                    st.info("Adjust the slider and click predict to see the result.")

        except FileNotFoundError:
            st.error("Model files not found! Please ensure 'salary_model.pkl' and 'salary_scaler.pkl' are uploaded to your GitHub repository.")

    # Project 2: Add another one here
    with st.container():
        c3, c4 = st.columns([1, 2])
        with c3:
            st.image("https://via.placeholder.com/400x250.png?text=Data+Visualization")
        with c4:
            st.subheader("Project 2: [Exploratory Data Analysis]")
            st.write("""
            Describe your analysis. What interesting insights did you find in the data?
            """)
            st.markdown("**Tech Stack:** `Plotly`, `Seaborn`, `Statistics`")
            st.link_button("View Code", "https://github.com/saii4u")

# --- 🛠 SKILLS PAGE ---
elif page == "🛠 Skills":
    st.title("My Technical Toolkit 🛠️")
    
    # Categories for a cleaner look
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("🐍 Programming")
        st.write("✅ Python\n\n✅ SQL\n\n✅ R (Basic)\n\n✅ Bash")

    with col2:
        st.subheader("📊 Data Science")
        st.write("✅ Pandas & NumPy\n\n✅ Scikit-Learn\n\n✅ Plotly & Seaborn\n\n✅ Machine Learning")

    with col3:
        st.subheader("⚙️ Tools")
        st.write("✅ Git & GitHub\n\n✅ Streamlit\n\n✅ VS Code\n\n✅ Tableau")

# --- 📬 CONTACT PAGE ---
elif page == "📬 Contact":
    st.title("Let's Connect!")
    st.write("Open to job opportunities, collaborations, or coffee chats ☕")
    
    # Working Contact Form
    st.markdown("""
    <form action="https://formsubmit.co/anumulasaikrishna5@gmail.com" method="POST">
        <input type="text" name="name" placeholder="Your name" style="width:100%; padding:10px; margin:10px 0; border:1px solid #ccc; border-radius:5px;">
        <input type="email" name="email" placeholder="Your email" style="width:100%; padding:10px; margin:10px 0; border:1px solid #ccc; border-radius:5px;">
        <textarea name="message" placeholder="Your message" rows="5" style="width:100%; padding:10px; margin:10px 0; border:1px solid #ccc; border-radius:5px;"></textarea>
        <button type="submit" style="background:#0066cc; color:white; padding:12px 24px; border:none; border-radius:5px; cursor:pointer;">Send Message</button>
    </form>
    """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("---")
st.caption("Made with ❤️ by Sai Krishna • [GitHub Repo](https://github.com/saii4u/my-data-science-portfolio)")