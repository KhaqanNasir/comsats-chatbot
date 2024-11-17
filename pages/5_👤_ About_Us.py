import streamlit as st

def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    .stApp {
        font-family: 'Poppins', sans-serif;
        background-color: #0D0D0D;
        color: #F2DFF2;
    }
    .main-title {
        color: #763DF2;
        font-size: 72px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    .tagline {
        color: #F2DFF2;
        font-size: 20px;
        text-align: center;
        font-style: italic;
        margin-bottom: 30px;
    }
    .section-header {
        color: #763DF2;
        font-size: 36px;
        font-weight: bold;
        margin-top: 40px;
        margin-bottom: 20px;
        text-align: center;
    }
    .feature-box {
        background-color: #421E59;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        transition: transform 0.3s ease-in-out;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 10px;
    }
    .feature-box:hover {
        transform: scale(1.02);
        background-color: #5129A6;
    }
    .circular-image {
        border-radius: 50%;
        overflow: hidden;
        width: 150px;
        height: 150px;
        margin: 0 auto;
        border: 3px solid #763DF2;
    }
    .circular-image img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    .team-member-name {
        color: #F2DFF2;
        font-size: 22px;
        font-weight: 600;
        text-align: center;
        margin-top: 10px;
    }
    .social-links {
        text-align: center;
        margin-top: 10px;
    }
    .social-button {
        background-color: #5129A6;
        color: #F2DFF2;
        padding: 5px 10px;
        border-radius: 5px;
        text-decoration: none;
        margin: 0 5px;
        font-size: 14px;
    }
    .social-button:hover {
        background-color: #763DF2;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    load_css()
    
    st.markdown("<h1 class='main-title'>🌟 COMSATS Chatbot 🌟</h1>", unsafe_allow_html=True)
    st.markdown("<p class='tagline'>🤝 Crafted with love and precision by your dedicated team! 🎨✨</p>", unsafe_allow_html=True)
    st.markdown("<h2 class='section-header'>👨‍💻 Meet the Team 🚀</h2>", unsafe_allow_html=True)
    
    # Team members
    # Add the team members
team_members = [
    {
        "name": "💻 Muhammad Khaqan Nasir",
        "github": "KhaqanNasir",
        "linkedin": "khaqan-nasir",
        "image": "../assets/1.jpg"  # Path to the local JPG image
    },
    {
        "name": "🖥️ Muhammad Adnan Tariq",
        "github": "adnan-tariq",
        "linkedin": "muhammad-adnan-tariq",
        "image": "../assets/2.jpeg"  # Path to the local JPEG image
    }
]

# Render the team members with icons
cols = st.columns(len(team_members))
for col, member in zip(cols, team_members):
    with col:
        image_base64 = open(member['image'], 'rb').read().encode('base64').decode('utf-8')
        st.markdown(f"""
            <div class='feature-box'>
                <div class='circular-image'>
                    <img src="data:image/jpeg;base64,{image_base64}" alt="{member['name']}">
                </div>
                <div class='team-member-name'>{member['name']}</div>
                <div class='social-links'>
                    <a href='https://github.com/{member["github"]}' target='_blank' class='social-button'>
                        <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub" width="20"> GitHub
                    </a>
                    <a href='https://linkedin.com/in/{member["linkedin"]}' target='_blank' class='social-button'>
                        <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" width="20"> LinkedIn
                    </a>
                </div>
            </div>
        """, unsafe_allow_html=True)


if __name__ == "__main__":
    st.set_page_config(
        page_title="COMSATS Chatbot",
        page_icon="🎓",
        layout="wide",  # Wide layout for better presentation
        initial_sidebar_state="collapsed"
    )
    main()
