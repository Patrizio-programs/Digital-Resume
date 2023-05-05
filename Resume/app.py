from pathlib import Path
import streamlit as st
from PIL import Image


current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "style.css"
resume_file = current_dir / "assets" / "resume.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"




PAGE_TITLE = "CV | PATRICK MEDLEY 🇯🇲"
PAGE_ICON = "🌬️"
NAME= "Patrick Medley 🇯🇲"
DESCRIPTION = "Front-End Developer, Web Developer, Techie"
EMAIL = "Patriziomedley@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/patrick-medley2497/",
    "GitHub": "https://github.com/Patrizio-programs",     
}

Projects = {
     " Simple Idaho Weather website using Weather API, Javasript, CSS and HTML": "https://patrizio-programs.github.io/weather/preston.html",
    "Netflix Clone with IMBD API using React": "https://jamflix.netlify.app/",
    "Bing powered Telegram Bot using python and Telegram API": "https://t.me/JamaicanAI_bot",
    "Kid Movies website made with HTML CSS and JavaScript": "https://cleanflix.netlify.app/",
    
    
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)




# --- HERO SECTION ---
col1, col2 = st.columns(2)
with col1:
    st.image(profile_pic, width=230)
    

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)
    
    
    # --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("**Influx - Bilingual Technical Support Representative**")
st.write("May 2021 - June 2022")
st.write(
    """
- Provide technical support to customers over chat, email, and telephone, resolving issues
related to hardware and software
- Maintain a 95% customer satisfaction rating
"""
)

# --- JOB 2
st.write('\n')
st.write("**Freelance Web Designer and Developer**")
st.write("Sept 2018 - Present")
st.write(
    """
- Collaborate with small businesses to design and develop custom websites, implementing
responsive design principles and optimizing for search engines
- Utilize CSS, Bootstrap, JavaScript, and React to create visually appealing and functional
websites
"""
)




# --- JOB 3
st.write('\n')
st.write( "**Ibex Global - Inside Sales Representative**")
st.write("Oct 2019 - Jan 2021")
st.write(
    """
- Responsible for managing the sales process for potential customers, as well as building and
maintaining relationships with clients
"""
)

# --- JOB 3
st.write('\n')
st.write( "**Hinduja Global Solutions - Customer Service Agent**")
st.write("Apr 2016 - Aug 2019")
st.write(
    """
- Communicated effectively with customers through a variety of channels, including phone,
email, and chat
- Provided technical support, billing assistance, and general product information to customers
"""
)


st.write('\n')
st.write("**Engoo - Online English Tutor**")
st.write("May 2022 - Present")
st.write(
    """
- Conduct engaging and interactive online English classes for students ranging from beginner
to advanced levels
"""
)


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write("""
        
- EFL (Teaching English as a Foreign Language) certificate
- Web Frontend Certificate
- Proficient in HTML, CSS, JavaScript, Bootstrap, WordPress, Wix, React, Python, Flask and more!
- Strong communication skills with the ability to effectively communicate complex technical
concepts to both technical and non-technical audiences
- Fluent in Spanish      
         
         """)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects")
st.write("Click to see project")
for project, link in Projects.items():
    st.write(f"[{project}]({link})")
