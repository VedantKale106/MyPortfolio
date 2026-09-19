from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    projects = [
        {
            "name": "Portfolio Website",
            "type": "Personal Brand",
            "description": "A clean personal portfolio built to showcase projects, skills, and contact details.",
            "link": "https://vedantkale.vercel.app/"
        },
        {
            "name": "KayKhau",
            "type": "Food Discovery",
            "description": "A food selection app focused on quick discovery and a simple user flow.",
            "link": "https://kaykhau.vercel.app/"
        },
        {
            "name": "LoveMail",
            "type": "Messaging",
            "description": "A lightweight app for sharing messages and simple personal communication.",
            "link": "https://lovemail-rust.vercel.app/"
        },
        {
            "name": "PuneJourney",
            "type": "Travel Guide",
            "description": "A location-focused project for exploring places and planning journeys.",
            "link": "https://punejourney.vercel.app/"
        },
        {
            "name": "PortfolioHub",
            "type": "Portfolio Tool",
            "description": "A portfolio builder concept for organizing profile content in one place.",
            "link": "https://portfolioohub.vercel.app/"
        },
        {
            "name": "Datamitra",
            "type": "Data Platform",
            "description": "A project centered on structured data handling and clean information workflows.",
            "link": "https://datamitra.onrender.com/"
        },
        {
            "name": "Machine Mitra",
            "type": "AI Utility",
            "description": "An experiment in adding intelligence-driven features to a software workflow.",
            "link": "https://machinemitra.onrender.com/"
        },
        {
            "name": "Starscout",
            "type": "Discovery",
            "description": "A discovery-oriented project built around exploring and surfacing content.",
            "link": "https://starscout.onrender.com/"
        },
        {
            "name": "Brazzers University",
            "type": "Academic Tool",
            "description": "A university-themed concept project focused on student-facing utility.",
            "link": "https://brazzersuniversity.vercel.app/"
        },
        {
            "name": "Mediscan",
            "type": "Healthcare",
            "description": "A healthcare project aimed at organizing and scanning medical information.",
            "link": "https://github.com/VedantKale106/MediScan.git"
        },
        {
            "name": "Moviematch",
            "type": "Recommendation",
            "description": "A movie-matching project centered on recommendation and user choice.",
            "link": "https://github.com/VedantKale106/MovieMatch.git"
        },
        {
            "name": "Phonepro",
            "type": "Product Explorer",
            "description": "A product-focused project for comparing and analyzing device information.",
            "link": "https://github.com/VedantKale106/PhonePro.git"
        },
        {
            "name": "RentWizard",
            "type": "Prediction",
            "description": "A prediction project for estimating rental values from input data.",
            "link": "https://github.com/VedantKale106/RentWizard.git"
        },
        {
            "name": "Attendance-Mitra",
            "type": "Attendance System",
            "description": "A classroom attendance project for tracking presence and records.",
            "link": "https://github.com/VedantKale106/Attendence-Mitra.git"
        },
        {
            "name": "BinanceBot",
            "type": "Automation",
            "description": "A bot project focused on automation and trading workflow logic.",
            "link": "https://github.com/VedantKale106/Binance-Trade-Bot.git"
        }
    ]
    
    skills = {
        "Dialects of Logic": ["Python", "C++", "SQL", "HTML/CSS", "R", "Java"],
        "Schools of Thought": ["Data Science", "Machine Learning", "Full Stack"],
        "Methods of Inquiry": ["Flask", "Pandas", "Sklearn", "Streamlit", "NumPy", "BeautifulSoup"],
        "Archives of Memory": ["MySQL", "MongoDB", "SQLite"],
        "Socratic Tools": ["Git", "GitHub", "Jupyter", "VS Code", "Power BI","Eclipse"],
        "The Agora": ["Heroku", "Render", "Vercel", "GitHub Pages"],
        "Java Full Stack": ["Spring Boot", "Spring MVC", "Hibernate", "JPA", "REST APIs", "Microservices"],
        "Microservices & Cloud": ["Spring Cloud", "Eureka", "API Gateway", "Docker", "RabbitMQ", "Distributed Systems"]
    }
    
    return render_template('index.html', projects=projects, skills=skills)

if __name__ == '__main__':
    app.run(debug=True)