import streamlit as st

def app():
    st.title("Education")

    education_details = [
        {
            "name": "Bachelor of Technology in Computer Science (Pursuing)",
            "institution": "Pimpri Chinchwad College of Engineering (PCCOE)",
            "year": "Currently in third year",
            "cgpa": "7.8",
            "image": "images/pccoe.jpeg",
            "caption": "PCCOE"
        },
        {
            "name": "Higher Secondary School Certificate (HSC), 2022",
            "school": "G.R.P.Sabnis College, Narayangaon",
            "year": "2022",
            "percentage": "79.83% (PCM)",
            "image": "images/grps.jpeg",
            "caption": "G.R.P.Sabnis College"
        },
        {
            "name": "Secondary School Certificate (SSC), 2020",
            "school": "Shakarrao Butte Patil Vidyalaya, Junnar",
            "year": "2020",
            "percentage": "93.40%",
            "image": "images/sbp.jpeg",
            "caption": "Shakarrao Butte Patil Vidyalaya"
        }
    ]

    for education in education_details:
        st.markdown(f"## {education['name']}")
        col1, col2 = st.columns([1, 3])  

        with col1:
            st.image(education["image"], caption=education["caption"], use_column_width=True)

        with col2:
            st.write(f"- **Institution/School:** {education.get('institution', education.get('school'))}")
            st.write(f"- **CGPA/Percentage:** {education.get('cgpa', education.get('percentage'))}")

if __name__ == '__main__':
    app()
