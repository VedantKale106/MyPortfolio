# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    projects = [
        {
            "name": "Portfolio Website",
            "type": "Personal Architecture",
            "description": "A personal portfolio to showcase my projects and skills.",
            "link":"https://vedantkale.vercel.app/"
        },
        {
            "name": "KayKhau",
            "type": "Recommendation Algo",
            "description": "A website that suggests random food options and helps users discover new dishes.",
            "link": "https://kaykhau.vercel.app/"
        },
        {
            "name": "LoveMail",
            "type": "Anonymity Protocol",
            "description": "A platform to send love confessions through email while keeping the sender anonymous.",
            "link": "https://lovemail-rust.vercel.app/"
        },
        {
            "name": "PuneJourney",
            "type": "Navigation System",
            "description": "Your ultimate guide to exploring, planning, experiencing Pune's amazing destinations.",
            "link":"https://punejourney.vercel.app/"
        },
        {
            "name": "PortfolioHub",
            "type": "Generator Tool",
            "description": "A Flask-based tool for creating personalized portfolios and resumes with realtime previews",
            "link":"https://portfolioohub.vercel.app/"
        },
        {
            "name": "Datamitra",
            "type": "Preprocessing Unit",
            "description": "A tool designed for efficient data cleaning and preprocessing.",
            "link":"https://datamitra.onrender.com/"
        },
        {
            "name": "Machine Mitra",
            "type": "Model Synthesis",
            "description": "Fast, efficient ML model creation",
            "link":"https://machinemitra.onrender.com/"
        },
        {
            "name": "Starscout",
            "type": "Restricted Access",
            "description": "Open only if you are 18+.",
            "link":"https://starscout.onrender.com/"
        },
        {
            "name": "Brazzers University",
            "type": "Satire Project",
            "description": "A Portfolio website for Brazzers University.",
            "link":"https://brazzersuniversity.vercel.app/"
        },
        {
            "name": "Mediscan",
            "type": "Diagnostics AI",
            "description": "A system for predicting diseases based on symptoms.",
            "link":"https://github.com/VedantKale106/MediScan.git"
        },
        {
            "name": "Moviematch",
            "type": "Preference Engine",
            "description": "A recommendation system for movies based on user preferences.",
            "link":"https://github.com/VedantKale106/MovieMatch.git"
        },
        {
            "name": "Phonepro",
            "type": "Hardware Analysis",
            "description": "A tool to recommend phones based on user requirements.",
            "link":"https://github.com/VedantKale106/PhonePro.git"
        },
        {
            "name": "RentWizard",
            "type": "Market Prediction",
            "description": "A predictive tool for estimating rent prices in Pune Area.",
            "link":"https://github.com/VedantKale106/RentWizard.git"
        },
        {
            "name": "Attendance-Mitra",
            "type": "Tracking System",
            "description": "Streamlit app for real-time attendance tracking with PCET ERP data.",
            "link": "https://github.com/VedantKale106/Attendence-Mitra.git"
        },
        {
            "name": "BinanceBot",
            "type": "Algo-Trading",
            "description": "Binance Futures Testnet Flask bot: trades market/limit orders, validates, and logs.",
            "link": "https://github.com/VedantKale106/Binance-Trade-Bot.git"
        }
    ]
    
    # Strictly "Lab/Chemistry" terminology
    skills = {
        "Chemical Precursors": ["Python", "C++", "SQL", "HTML/CSS", "R", "Java"],
        "Storage Vessels": ["MySQL", "MongoDB", "SQLite"],
        "Active Ingredients": ["Flask", "Pandas", "Sklearn", "Streamlit", "NumPy", "BeautifulSoup"],
        "Lab Apparatus": ["Git", "GitHub", "Jupyter", "VS-Code", "Power BI"],
        "Controlled Territory": ["Data Science", "Machine Learning", "Full Stack"],
        "Distribution Network": ["Heroku", "Render", "Vercel", "GitHub Pages"]
    }
    
    return render_template('index.html', projects=projects, skills=skills)

if __name__ == '__main__':
    app.run(debug=True)