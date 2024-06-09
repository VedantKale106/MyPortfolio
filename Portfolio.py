import streamlit as st
import webbrowser

name = "Vedant Kale"
bio = "🚀 Highly passionate and innovative developer with extensive expertise in Python, Machine Learning, Android Development, C/C++, Java, and Data Structures & Algorithms. 📊 Proficient in Jupyter Notebook, Git, and GitHub. 🌟 Eager to lead and shape innovation, driving impactful tech projects to astounding success. 🤝 Let’s connect and ignite a collaboration that transforms the tech landscape! I Love reading books, watching Anime and playing games  😁."
email = "vedant.kale22@pccoepune.org"
phone = "+91-8421204009"
linkedin = "https://www.linkedin.com/in/vedant-kale-a057b2257/"
github = "https://github.com/VedantKale106"
profile_pic = "img.jpg"
whatsapp_link = "https://wa.me/918421204009" 

st.set_page_config(page_title=f"{name} - Portfolio", layout="wide")

st.title(f"Welcome to My Portfolio Website")

col1, col2 = st.columns([3, 7]) 
with col1:
    st.image(profile_pic, width=250, use_column_width=True, output_format='PNG')
with col2:
    st.write(f"# {name}")
    st.write(bio)

with st.sidebar:
    st.title("Contact")
    st.write(f"📧 [Email](mailto:{email})")
    st.write(f"📞 {phone}")
    st.write(f"🔗 [LinkedIn]({linkedin})")
    st.write(f"💻 [GitHub]({github})")
    if st.button("Contact via WhatsApp"):
        webbrowser.open(whatsapp_link)


# Skills 
st.subheader("Skills")
st.write("""
- **Programming Languages:** Python, C, C++, Java, SQL
- **Technologies:** GitHub, Jupyter, Android Studio
- **Areas of Expertise:**  Machine Learning, Data Science, Data Structures and Algorithms, Android App Development
""")

# Projects Section
st.subheader("Projects")
st.write("""
- **[SalaryScope](https://github.com/VedantKale106/SalaryScope):** A comprehensive machine learning project designed to predict the salary of software engineers based on various parameters such as experience, education level and location. Leveraging advanced data analysis techniques and machine learning algorithms including regression and ensemble methods, SalaryScope provides accurate salary estimations, aiding both job seekers and employers in making informed decisions.

- **[RentWizard](https://github.com/VedantKale106/RentWizard):** RentWizard is an intelligent rental price prediction tool tailored for real estate markets. By analyzing factors such as property size, number of rooms, amenities, and market trends, RentWizard forecasts rental prices with high precision. Utilizing regression techniques it offers valuable insights to landlords, tenants, and property investors, facilitating optimal rental pricing strategies and negotiations.
""")


# Experience Section
st.subheader("Experience")
st.write("""
- Currently no professional experience, but actively seeking opportunities to apply my skills and knowledge in real-world projects.
""")

# Education Section
st.subheader("Education")
st.write("""
- **Bachelor of Technology in Computer Science** (Pursuing)
  - Pimpri Chinchwad College of Engineering (PCCOE)
  - Currently in third year
  - CGPA - 7.8
- **Higher Secondary School Certificate** (2022)
  - G.R.P.Sabnis College, Narayangaon
  - 79.83 % in HSC (PCM)
- **Secondary School Certificate** (2020)
  - Shakarrao Butte Patil Vidyalaya, Junnar
  - 93.40 % in SSC
""")

st.markdown("""
    <style>
        footer {
            visibility: hidden;
        }
        .footer {
            visibility: visible;
            position: fixed;
            right: 0;
            bottom: 0;
            text-align: right;
            padding: 10px;
            font-size: 14px;
        }
    </style>
    <div class="footer">
        Made by Vedant Kale 🫡
    </div>
""", unsafe_allow_html=True)
