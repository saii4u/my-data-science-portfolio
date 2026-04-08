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
#st.sidebar.title("Navigation")
# NOTE: Make sure these names match exactly in the 'if/elif' blocks below
#page = st.sidebar.radio("Go to", ["🏠 Home", "🧪 Projects", "🛠 Skills", "📬 Contact"])


# --- SIDEBAR SETUP ---
with st.sidebar:
    st.title("📂 Portfolio")
    st.markdown("Helping businesses make smarter decisions - one pandas DataFrame at a time. 🐼")
    st.divider()

    # Your navigation
    page = st.radio(
        "Go to", 
        ["🏠 Home", "🧪 Projects", "🛠 Skills", "📬 Contact"]
    )

    st.divider()
    # A small 'Current Status' or 'Location' looks very professional
    st.caption("📍 Based in Coventry, United Kingdom🇬🇧")
    st.caption("🚀 Open to Data Science roles")

# --- 🏠 HOME PAGE ---
if page == "🏠 Home":
    st.title("Hi, I'm Sai Krishna 👋")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Data Scientist | Machine Learning Engineer")
        st.write("""
        I am a passionate Data Scientist dedicated to turning complex datasets into 
        actionable business insights. With a background in Machine Learning and 
        Data Visualization, I specialize in building predictive models 
        and interactive data storytelling.
        """)
        
        # Social Links
        c1, c2 = st.columns(2)
        with c1:
            st.link_button("🔗 GitHub", "https://github.com/saii4u")
        with c2:
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


# --- 🎓 EDUCATION SECTION (Now Correctly Indented) ---
    st.write("---")
    st.write("### 🎓 Education")
    
    col_edu_text, col_edu_logo = st.columns([3, 1]) 
    with col_edu_text:
        st.markdown("**Master of Science in Data Science**")
        st.caption("Coventry University | 2024 - 2025")
        st.write("Relevant Coursework: Machine Learning, Big Data, Statistics.")
    with col_edu_logo:
        st.image("https://raw.githubusercontent.com/saii4u/my-data-science-portfolio/main/culogo.png", width=120)

    st.write("---")

# --- 💼 EXPERIENCE SECTION ---
    st.write("### 💼 Professional Experience")
    
    with st.expander("🚀 Data Analyst at Merck KGaA", expanded=True):
        # Create two columns: one for your text (left) and one for the logo (right)
        col_text, col_logo = st.columns([4, 1])
        
        with col_text:
            st.write("**Nov 2020 - Aug 2024**")
            st.write("""
            - Analyzed large datasets to identify trends and cost-saving opportunities.
            - Built automated dashboards using Python and Streamlit.
            - Collaborated with cross-functional teams to improve data accuracy by 15%.
            """)
            
        with col_logo:
            # Reliable Merck KGaA Logo Link
            st.image(
                "https://raw.githubusercontent.com/saii4u/my-data-science-portfolio/main/merck_logo.png", 
                width=120
            )

    st.write("---")
    
    # --- 🚀 CALL TO ACTION ---
    st.success("🎯 **Ready to see my technical work?** Use the sidebar to visit **🧪 Projects**!")

# --- NEW NAVIGATION SECTION ---
    st.write("### 🚀 Where to go next?")
    
    # These boxes act as a visual guide for the recruiter
    nav_col1, nav_col2, nav_col3 = st.columns(3)
    
    with nav_col1:
        st.info("#### 🧪 Projects\nSee my **Salary Predictor** and **Heart Disease** models in action.")
        
    with nav_col2:
        st.success("#### 🛠 Skills\nView my technical toolkit including **Python, SQL, and ML**.")

    with nav_col3:
        st.warning("#### 📬 Contact\nGet in touch for **collaborations** or job opportunities.")
    
    st.write("---")
    st.caption("👈 Use the **Navigation Menu** on the left to switch between these pages!")

# --- 🧪 PROJECTS PAGE ---
elif page == "🧪 Projects":
    st.title("Featured Data Science Projects 🚀")
    st.write("Interact with my live Machine Learning models below.")

    # --- PROJECT 1: SALARY PREDICTION ---
    with st.container():
        # UPDATED HEADER TO MATCH PROJECT 2 STYLE
        st.subheader("1️⃣ Salary Prediction Engine 💰")
        st.write("""
        Input your years of experience below. This app uses a **Multi-layer Perceptron (MLP) Neural Network** trained on historical salary data to estimate your market value.
        """)

        import joblib
        import numpy as np

        try:
            # Load Salary Assets
            s_model = joblib.load('salary_model.pkl')
            s_scaler = joblib.load('salary_scaler.pkl')

            col1, col2 = st.columns(2)
            with col1:
                s_years = st.number_input("Years of Experience", 0.0, 50.0, 5.0, step=0.5, key="s_input")
            with col2:
                if st.button("Predict Salary", key="s_btn"):
                    s_input = s_scaler.transform(np.array([[s_years]]))
                    s_pred = s_model.predict(s_input)
                    st.success(f"Estimated Salary: **${s_pred[0]:,.2f}**")
                    st.balloons()
        except FileNotFoundError:
            st.error("Salary model files not found on GitHub.")

    st.divider()

    # --- PROJECT 2: HEART DISEASE PREDICTOR ---
    with st.container():
        st.subheader("2️⃣ Heart Disease Mortality Predictor 🏥")
        st.write("Predicts mortality rates per 100k people based on location and year.")
        
        try:
            # Load Heart Model Assets
            h_model = joblib.load('heart_model.pkl')
            h_scaler = joblib.load('heart_scaler.pkl')

            c1, c2 = st.columns(2)
            with c1:
                h_year = st.selectbox("Select Year", [2019, 2020, 2021], key="h_year")
                h_lat = st.number_input("Latitude (Y_lat)", value=34.0, key="h_lat")
            with c2:
                h_loc = st.number_input("Location ID", value=1000, key="h_loc")
                h_lon = st.number_input("Longitude (X_lon)", value=-85.0, key="h_lon")

            if st.button("Predict Mortality Rate", key="h_btn"):
                h_input = np.array([[h_year, h_loc, h_lat, h_lon]])
                h_input_scaled = h_scaler.transform(h_input)
                h_pred = h_model.predict(h_input_scaled)
                st.warning(f"Predicted Mortality Rate: **{h_pred[0]:,.2f}** per 100k")

            # --- MAP VISUALIZATION ---
            st.write("---")
            if st.checkbox("🌍 Show Geospatial Data Map"):
                data_path = 'Heart_Disease_Mortality_Data_Among_US_Adults__35___by_State_Territory_and_County___2019-2021.csv'
                df_map = pd.read_csv(data_path)
                map_data = df_map[['Y_lat', 'X_lon']].rename(columns={'Y_lat': 'lat', 'X_lon': 'lon'})
                map_data = map_data.dropna(subset=['lat', 'lon'])
                st.map(map_data)

        except FileNotFoundError:
            st.error("Model or Data files not found.")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")

    st.divider()

    # --- PROJECT 3: AIRLINES PASSENGER CLUSTERING ---
    with st.container():
        st.subheader("3️⃣ Airlines Loyalty Segmentation ✈️")
        
        st.write("""
        In this project, I performed **Customer Segmentation** on a frequent flyer dataset. 
        By applying **K-Means Clustering**, I identified 5 distinct passenger groups based on 
        mileage balances, credit card usage, and flight frequency. 
        """)

        try:
            # 1. Load Data from Excel
            # Using the sheet 'data' from your EastWestAirlines.xlsx file
            df_air = pd.read_excel("EastWestAirlines.xlsx", sheet_name="data")
            
            # 2. Preprocessing & Clustering Logic
            from sklearn.cluster import KMeans
            from sklearn.preprocessing import StandardScaler

            # Prepare features (Removing ID and the Target 'Award' for unsupervised learning)
            features = df_air.drop(['ID#', 'Award?'], axis=1)
            scaler = StandardScaler()
            scaled_features = scaler.fit_transform(features)

            # Applying K-Means (5 Clusters based on your notebook analysis)
            kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
            df_air['Segment'] = kmeans.fit_predict(scaled_features)

            # 3. Interactive UI Columns
            col_metric, col_plot = st.columns([1, 3])
            
            with col_metric:
                st.write("#### 📊 Segment Insights")
                sel_seg = st.selectbox("Select Segment:", options=sorted(df_air['Segment'].unique()))
                
                # Dynamic Metric based on selection
                seg_data = df_air[df_air['Segment'] == sel_seg]
                st.metric("Passengers in Group", f"{len(seg_data)}")
                st.metric("Avg. Mileage Balance", f"{seg_data['Balance'].mean():,.0f}")

            with col_plot:
                # 4. Interactive Scatter Plot
                fig_air = px.scatter(
                    df_air, 
                    x="Balance", 
                    y="Bonus_miles", 
                    color=df_air['Segment'].astype(str),
                    title="Customer Segments: Mileage vs. Bonus Miles",
                    labels={"color": "Segment ID"},
                    template="plotly_white",
                    hover_data=['cc1_miles', 'Days_since_enroll']
                )
                st.plotly_chart(fig_air, use_container_width=True)

        except FileNotFoundError:
            st.error("Dataset 'EastWestAirlines.xlsx' not found. Ensure it is uploaded to your GitHub.")
        except Exception as e:
            st.error(f"Error: {e}. Please ensure 'openpyxl' is in requirements.txt")

    st.divider()

# --- PROJECT 4: FOREST FIRE CLASSIFICATION ---
    with st.container():
        st.subheader("4️⃣ Forest Fire Severity Predictor 🔥")
        
        try:
            # 1. Load the Pre-trained Assets
            import joblib
            fire_model = joblib.load('fire_svm_model.pkl')
            fire_scaler = joblib.load('fire_scaler.pkl')

            st.markdown("""
                *Adjust the sliders below to simulate weather conditions and predict potential fire severity.*
            """)

            # 2. Input Layout
            col_in1, col_in2 = st.columns(2)
            with col_in1:
                st.write("**Weather Metrics**")
                temp = st.slider("Temperature (°C)", 0.0, 45.0, 25.0)
                rh = st.slider("Relative Humidity (%)", 10.0, 100.0, 30.0)
                wind = st.slider("Wind Speed (km/h)", 0.0, 15.0, 5.0)
                rain = st.number_input("Rain (mm/m2)", value=0.0)
            with col_in2:
                st.write("**Fire Indices**")
                ffmc = st.number_input("FFMC Index", value=92.0)
                dmc = st.number_input("DMC Index", value=120.0)
                dc = st.number_input("DC Index", value=500.0)
                isi = st.number_input("ISI Index", value=15.0)
            
            # 3. Prediction Button with Visuals
            if st.button("🚀 Analyze Fire Severity", type="primary", use_container_width=True):
                with st.spinner("Model calculating risk factors..."):
                    # Prepare 27-feature array
                    input_data = np.zeros((1, 27))
                    input_data[0, 0:8] = [ffmc, dmc, dc, isi, temp, rh, wind, rain]
                    
                    # Scale and Predict
                    input_scaled = fire_scaler.transform(input_data)
                    prediction = fire_model.predict(input_scaled)
                    
                    # Result Display
                    if prediction[0].lower() == "large":
                        st.snow()  # Cool visual for a "hot" alert
                        st.error("### 🚨 Prediction: LARGE FIRE RISK")
                        st.toast("Warning: High Severity Detected!", icon="⚠️")
                        st.write("Current conditions match patterns historically associated with fires exceeding 6 hectares.")
                    else:
                        st.balloons() # Celebratory visual for low risk
                        st.success("### ✅ Prediction: SMALL FIRE RISK")
                        st.toast("Analysis Complete: Low Risk", icon="✅")
                        st.write("Current conditions suggest a high probability of fire remaining contained.")

        except Exception as e:
            st.error(f"Error: {e}")


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
    
    # Working Contact Form with extra reliability
    contact_form = f"""
    <form action="https://formsubmit.co/anumulasaikrishna5@gmail.com" method="POST">
        <input type="hidden" name="_subject" value="New Portfolio Message!">
        <input type="text" name="name" placeholder="Your name" required style="width:100%; padding:10px; margin:10px 0; border:1px solid #ccc; border-radius:5px;">
        <input type="email" name="email" placeholder="Your email" required style="width:100%; padding:10px; margin:10px 0; border:1px solid #ccc; border-radius:5px;">
        <textarea name="message" placeholder="Your message" rows="5" required style="width:100%; padding:10px; margin:10px 0; border:1px solid #ccc; border-radius:5px;"></textarea>
        <button type="submit" style="background:#0066cc; color:white; padding:12px 24px; border:none; border-radius:5px; cursor:pointer; width:100%;">Send Message</button>
    </form>
    """
    
    st.markdown(contact_form, unsafe_allow_html=True)
    
    st.write("---")
    st.write("📍 Based in Coventry, United Kingdom")
    st.write("📧 Direct Email: anumulasaikrishna5@gmail.com")

# --- FOOTER ---
st.markdown("---")
st.caption("Made with ❤️ by Sai Krishna • [GitHub Repo](https://github.com/saii4u/my-data-science-portfolio)")