import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Sai Krishna Anumula | Data Scientist", page_icon="📊", layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["🏠 Home", "🧪 Projects", "🛠 Skills", "📬 Contact"])

if page == "🏠 Home":
    st.title("Hi, I'm Sai Krishna 👋")
    st.subheader("Data Scientist | Machine Learning Engineer")
    
    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown("""
        Passionate data scientist with experience in machine learning, data visualization, 
        and building impactful solutions. I turn raw data into real business value.
        """)
        st.link_button("🔗 GitHub", "https://github.com/saii4u")
        st.link_button("🔗 LinkedIn", "https://linkedin.com/in/sai-krishna-anumula")
    
    with col2:
        st.image("https://raw.githubusercontent.com/saii4u/my-data-science-portfolio/main/profile.jpg.jpeg", width=300)

elif page == "🧪 Projects":
    st.title("Featured Data Science Projects")
    
    # ←←←←← ADD YOUR PROJECTS HERE (I'll help you fill real ones later)
    with st.expander("🚀 Project 1: [Write your project title]", expanded=True):
        st.write("Short description of what you built and the impact.")
        st.write("**Tech used:** Python, Pandas, Scikit-learn, etc.")
        st.subheader("Interactive Demo")
        # Example interactive part - you can change this
        slider_value = st.slider("Try this slider", 0, 100, 50)
        st.write(f"Current value: **{slider_value}**")
        st.link_button("View Full Code", "https://github.com/...")

    # You can copy the block above to add more projects

elif page == "🛠 Skills":
    st.title("Skills & Tools")
    cols = st.columns(5)
    skills = ["Python", "SQL", "Pandas", "Scikit-learn", "Plotly", "Streamlit", "Tableau", "Machine Learning", "Deep Learning", "Git"]
    for i, skill in enumerate(skills):
        cols[i % 5].markdown(f"✅ **{skill}**")

elif page == "📬 Contact":
    st.title("Let's Connect!")
    st.write("Open to job opportunities, collaborations, or coffee chats ☕")
    st.markdown("""
    <form action="https://formsubmit.co/anumulasaikrishna5@gmail.com" method="POST">
        <input type="text" name="name" placeholder="Your name" style="width:100%; padding:10px; margin:10px 0;">
        <input type="email" name="email" placeholder="Your email" style="width:100%; padding:10px; margin:10px 0;">
        <textarea name="message" placeholder="Your message" rows="5" style="width:100%; padding:10px; margin:10px 0;"></textarea>
        <button type="submit" style="background:#0066cc; color:white; padding:12px 24px; border:none;">Send Message</button>
    </form>
    """, unsafe_allow_html=True)

st.markdown("---")
st.caption("Made with ❤️ using Streamlit • [GitHub Repo](https://github.com/saii4u/my-data-science-portfolio)")
