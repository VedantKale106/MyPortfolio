# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    projects = [
        {
            "name": "Portfolio Website",
            "type": "Personal Website",
            "description": "A personal portfolio to showcase my projects and skills."
        },
        {
            "name": "Datamitra",
            "type": "Data Preprocessing Tool",
            "description": "A tool designed for efficient data cleaning and preprocessing."
        },
        {
            "name": "Machine Mitra",
            "type": "Quick ML Models",
            "description": "A tool to create machine learning models quickly and efficiently."
        },
        {
            "name": "Starscout",
            "type": "Private Project",
            "description": "Open only if you are 18+."
        },
        {
            "name": "Mediscan",
            "type": "Disease Prediction System",
            "description": "A system for predicting diseases based on symptoms."
        },
        {
            "name": "Moviematch",
            "type": "Movie Recommender System",
            "description": "A recommendation system for movies based on user preferences."
        },
        {
            "name": "Phonepro",
            "type": "Phone Recommender System",
            "description": "A tool to recommend phones based on user requirements."
        },
        {
            "name": "RentWizard",
            "type": "Rent Predictor",
            "description": "A predictive tool for estimating rent prices."
        }
    ]
    
    skills = {
        "Programming Jutsu": ["Python", "C++", "SQL"],
        "Framework Style": ["Flask", "Pandas", "Sklearn", "Streamlit"],
        "Shinobi Tools": ["Git", "GitHub", "Jupyter Notebook"],
        "Focus Areas": ["Feature Engineering", "Data Structures and Algorithms"]
    }
    
    return render_template('index.html', projects=projects, skills=skills)

if __name__ == '__main__':
    app.run(debug=True)