# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    projects = [
        {
            "name": "Portfolio Website",
            "type": "Personal Website",
            "description": "A personal portfolio to showcase my projects and skills.",
            "link":"https://vedantkale.vercel.app/"
        },
        {
            "name": "KayKhau",
            "type": "Food Recommendation Website",
            "description": "A website that suggests random food options and helps users discover new dishes.",
            "link": "https://kaykhau.vercel.app/"
        },
        {
            "name": "LoveMail",
            "type": "Anonymous Love Confession Platform",
            "description": "A platform to send love confessions through email while keeping the sender anonymous.",
            "link": "https://lovemail-rust.vercel.app/"
        },
        {
            "name": "PuneJourney",
            "type": "Travel Website",
            "description": "Your ultimate travel companion to explore, plan, and experience amazing destinations in and around Pune.",
            "link":"https://punejourney.vercel.app/"
        },
        {
            "name": "PortfolioHub",
            "type": "Portfolio Website Generator",
            "description": "A Flask-based tool for creating personalized portfolios with resmue maker and real-time previews",
            "link":"https://portfolioohub.vercel.app/"
        },
        {
            "name": "Datamitra",
            "type": "Data Preprocessing Tool",
            "description": "A tool designed for efficient data cleaning and preprocessing.",
            "link":"https://datamitra.onrender.com/"
        },
        {
            "name": "Machine Mitra",
            "type": "Quick ML Models",
            "description": "A tool to create machine learning models quickly and efficiently.",
            "link":"https://machinemitra.onrender.com/"
        },
        {
            "name": "Starscout",
            "type": "Private Project",
            "description": "Open only if you are 18+.",
            "link":"https://github.com/VedantKale106/StarScout.git"
        },
        {
            "name": "Brazzers University",
            "type": "Made just for fun",
            "description": "A Portfolio website for Brazzers University.",
            "link":"https://brazzersuniversity.vercel.app/"
        },
        {
            "name": "Mediscan",
            "type": "Disease Prediction System",
            "description": "A system for predicting diseases based on symptoms.",
            "link":"https://github.com/VedantKale106/MediScan.git"
        },
        {
            "name": "Moviematch",
            "type": "Movie Recommender System",
            "description": "A recommendation system for movies based on user preferences.",
            "link":"https://github.com/VedantKale106/MovieMatch.git"
        },
        {
            "name": "Phonepro",
            "type": "Phone Recommender System",
            "description": "A tool to recommend phones based on user requirements.",
            "link":"https://github.com/VedantKale106/PhonePro.git"
        },
        {
            "name": "RentWizard",
            "type": "Rent Predictor",
            "description": "A predictive tool for estimating rent prices in Pune Area.",
            "link":"https://github.com/VedantKale106/RentWizard.git"
        }
    ]
    
    skills = {
        "Programming Jutsu": ["Python", "C++", "SQL","Html","Css","R","Java"],
        "Framework Style": ["Flask", "Pandas", "Sklearn", "Streamlit", "Mongodb","Numpy"],
        "Shinobi Tools": ["Git", "GitHub", "Jupyter Notebook", "VS-Code"],
        "Focus Areas": ["Data Science","Machine Learning","Full Stack Web Development"]
    }
    
    return render_template('index.html', projects=projects, skills=skills)

if __name__ == '__main__':
    app.run(debug=True)
