from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Projects rebranded as "The Magnum Opus"
    projects = [
        {
            "name": "Portfolio Website",
            "type": "The Cave Allegory",
            "description": "My shadow on the digital wall. Is it the real me, or just a projection?",
            "link": "https://vedantkale.vercel.app/"
        },
        {
            "name": "KayKhau",
            "type": "Epicurean Choice",
            "description": "A dialetic of hunger. Satisfy the appetites through the chaos of randomization.",
            "link": "https://kaykhau.vercel.app/"
        },
        {
            "name": "LoveMail",
            "type": "Platonic Confessions",
            "description": "Whispers from the void. Love detached from the physical form.",
            "link": "https://lovemail-rust.vercel.app/"
        },
        {
            "name": "PuneJourney",
            "type": "The Peripatetic",
            "description": "Wandering the streets of the Polis in search of hidden truths.",
            "link": "https://punejourney.vercel.app/"
        },
        {
            "name": "PortfolioHub",
            "type": "The Ship of Theseus",
            "description": "Construct a new identity. If you replace every part, does the original remain?",
            "link": "https://portfolioohub.vercel.app/"
        },
        {
            "name": "Datamitra",
            "type": "Empirical Purification",
            "description": "Refining raw sensory data into absolute, uncorrupted truth.",
            "link": "https://datamitra.onrender.com/"
        },
        {
            "name": "Machine Mitra",
            "type": "The Ghost in the Machine",
            "description": "Synthesizing the Logos within silicon. Can a machine possess a soul?",
            "link": "https://machinemitra.onrender.com/"
        },
        {
            "name": "Starscout",
            "type": "The Dionysian Gaze",
            "description": "Staring into the primal chaos. Not for the faint of Stoicism.",
            "link": "https://starscout.onrender.com/"
        },
        {
            "name": "Brazzers University",
            "type": "The Cynic's Satire",
            "description": "A Diogenean mockery of established academic norms.",
            "link": "https://brazzersuniversity.vercel.app/"
        },
        {
            "name": "Mediscan",
            "type": "Bioethics",
            "description": "Preserving the mortal coil before it shuffles off.",
            "link": "https://github.com/VedantKale106/MediScan.git"
        },
        {
            "name": "Moviematch",
            "type": "Aesthetics",
            "description": "Algorithms that determine the sublime from the mundane.",
            "link": "https://github.com/VedantKale106/MovieMatch.git"
        },
        {
            "name": "Phonepro",
            "type": "Materialism",
            "description": "Analyzing the atoms of our digital extensions.",
            "link": "https://github.com/VedantKale106/PhonePro.git"
        },
        {
            "name": "RentWizard",
            "type": "The Social Contract",
            "description": "Predicting the cost of dwelling within the state of society.",
            "link": "https://github.com/VedantKale106/RentWizard.git"
        },
        {
            "name": "Attendance-Mitra",
            "type": "The Panopticon",
            "description": "Surveillance of the many. Who is present, and who is merely existing?",
            "link": "https://github.com/VedantKale106/Attendence-Mitra.git"
        },
        {
            "name": "BinanceBot",
            "type": "The Invisible Hand",
            "description": "Automated accumulation of value in the metaphysical marketplace.",
            "link": "https://github.com/VedantKale106/Binance-Trade-Bot.git"
        }
    ]
    
    # Skills rebranded as "The Lyceum"
    skills = {
        "Dialects of Logic": ["Python", "C++", "SQL", "HTML/CSS", "R", "Java"],
        "Archives of Memory": ["MySQL", "MongoDB", "SQLite"],
        "Methods of Inquiry": ["Flask", "Pandas", "Sklearn", "Streamlit", "NumPy", "BeautifulSoup"],
        "Socratic Tools": ["Git", "GitHub", "Jupyter", "VS-Code", "Power BI"],
        "Schools of Thought": ["Data Science", "Machine Learning", "Full Stack"],
        "The Agora": ["Heroku", "Render", "Vercel", "GitHub Pages"]
    }
    
    return render_template('index.html', projects=projects, skills=skills)

if __name__ == '__main__':
    app.run(debug=True)