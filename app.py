# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Projects rebranded as "Dark Rituals"
    projects = [
        {
            "name": "Portfolio Website",
            "type": "The Altar",
            "description": "My digital tombstone. Enter if you dare.",
            "link":"https://vedantkale.vercel.app/"
        },
        {
            "name": "KayKhau",
            "type": "Flesh Consumption",
            "description": "A roulette for the starving. Discover your next meal before it discovers you.",
            "link": "https://kaykhau.vercel.app/"
        },
        {
            "name": "LoveMail",
            "type": "Ghost Whispers",
            "description": "Send anonymous confessions from the void. They'll never know it was you.",
            "link": "https://lovemail-rust.vercel.app/"
        },
        {
            "name": "PuneJourney",
            "type": "Cursed Map",
            "description": "Navigate the haunted ruins and hidden alleys of the city.",
            "link":"https://punejourney.vercel.app/"
        },
        {
            "name": "PortfolioHub",
            "type": "Identity Thief",
            "description": "Construct a new persona. Clone yourself. Escape reality.",
            "link":"https://portfolioohub.vercel.app/"
        },
        {
            "name": "Datamitra",
            "type": "Purification Rite",
            "description": "Cleansing the corruption from your datasets.",
            "link":"https://datamitra.onrender.com/"
        },
        {
            "name": "Machine Mitra",
            "type": "Automated Evil",
            "description": "Synthesizing intelligence to replace humanity.",
            "link":"https://machinemitra.onrender.com/"
        },
        {
            "name": "Starscout",
            "type": "Forbidden Gaze",
            "description": "Adults only. Stare into the abyss.",
            "link":"https://starscout.onrender.com/"
        },
        {
            "name": "Brazzers University",
            "type": "Sinners' Academy",
            "description": "A satirical institution for the corrupted minds.",
            "link":"https://brazzersuniversity.vercel.app/"
        },
        {
            "name": "Mediscan",
            "type": "Plague Doctor",
            "description": "Predicting the rot before it consumes the host.",
            "link":"https://github.com/VedantKale106/MediScan.git"
        },
        {
            "name": "Moviematch",
            "type": "Nightmare Fuel",
            "description": "Algorithms that know what you want to scream at.",
            "link":"https://github.com/VedantKale106/MovieMatch.git"
        },
        {
            "name": "Phonepro",
            "type": "Black Mirror",
            "description": "Hardware analysis for the digital soul.",
            "link":"https://github.com/VedantKale106/PhonePro.git"
        },
        {
            "name": "RentWizard",
            "type": "Dungeon Keeper",
            "description": "Predicting the cost of survival in the Pune wastelands.",
            "link":"https://github.com/VedantKale106/RentWizard.git"
        },
        {
            "name": "Attendance-Mitra",
            "type": "Soul Tracker",
            "description": "Real-time surveillance of missing persons.",
            "link": "https://github.com/VedantKale106/Attendence-Mitra.git"
        },
        {
            "name": "BinanceBot",
            "type": "Blood Money",
            "description": "Automated trading to harvest coin from the ether.",
            "link": "https://github.com/VedantKale106/Binance-Trade-Bot.git"
        }
    ]
    
    # Skills rebranded as "Grimoire"
    skills = {
        "Forbidden Languages": ["Python", "C++", "SQL", "HTML/CSS", "R", "Java"],
        "Soul Containers": ["MySQL", "MongoDB", "SQLite"],
        "Dark Magic": ["Flask", "Pandas", "Sklearn", "Streamlit", "NumPy", "BeautifulSoup"],
        "Torture Devices": ["Git", "GitHub", "Jupyter", "VS-Code", "Power BI"],
        "Domains of Dread": ["Data Science", "Machine Learning", "Full Stack"],
        "Transmission Vectors": ["Heroku", "Render", "Vercel", "GitHub Pages"]
    }
    
    return render_template('index.html', projects=projects, skills=skills)

if __name__ == '__main__':
    app.run(debug=True)