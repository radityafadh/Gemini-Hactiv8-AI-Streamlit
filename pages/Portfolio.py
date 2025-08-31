import streamlit as st
from loading_utils import page_loading_wrapper

@page_loading_wrapper
def portfolio_page():
    # Page configuration
    st.set_page_config(
        page_title="Gizzele's Portfolio",
        page_icon="📊",
        layout="wide"
    )

    st.title("📊 My Portfolio")
    st.markdown("---")

    # Personal Information
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("https://via.placeholder.com/200x200.png?text=Gizzele", width=200)
        st.subheader("Contact Info")
        st.write("📧 gizzele@zootopia.com")
        st.write("📱 +1 (555) 987-6543")
        st.write("🌐 zootopia.com/gizzele")
        st.write("🎵 music.zootopia.com/gizzele")

    with col2:
        st.header("Gizzele the Gazelle")
        st.subheader("Performer • Advocate • Dreamer")
        st.write("""
        I’m Gizzele, a gazelle from Zootopia 🌆 — known for my performances that bring 
        predator and prey together in harmony. Beyond the stage, I dedicate my voice to 
        campaigns for peace, equality, and creativity for the next generation. 
        My portfolio reflects both my artistry and activism.
        """)

    # Skills Section
    st.markdown("---")
    st.header("🛠️ Skills & Talents")

    skills_col1, skills_col2, skills_col3 = st.columns(3)

    with skills_col1:
        st.subheader("Performance")
        st.write("• Singing ⭐⭐⭐⭐⭐")
        st.write("• Dancing ⭐⭐⭐⭐")
        st.write("• Stage Presence ⭐⭐⭐⭐⭐")
        st.write("• Songwriting ⭐⭐⭐⭐")

    with skills_col2:
        st.subheader("Advocacy")
        st.write("• Public Speaking ⭐⭐⭐⭐")
        st.write("• Event Organizing ⭐⭐⭐⭐")
        st.write("• Youth Mentorship ⭐⭐⭐⭐⭐")
        st.write("• Community Campaigns ⭐⭐⭐⭐")

    with skills_col3:
        st.subheader("Creative Skills")
        st.write("• Fashion & Styling ⭐⭐⭐⭐")
        st.write("• Music Composition ⭐⭐⭐⭐")
        st.write("• Social Media Engagement ⭐⭐⭐⭐")
        st.write("• Multilingual Singing ⭐⭐⭐")

    # Experience Section
    st.markdown("---")
    st.header("💼 Experience & Highlights")

    with st.expander("Lead Performer - Harmony Concert Series (2022-Present)"):
        st.write("""
        - Headlined city-wide concerts uniting predator and prey communities  
        - Performed to sold-out crowds in Sahara Square & Tundratown  
        - Raised over $1M for youth music programs through benefit shows  
        """)

    with st.expander("Founder - Zootopia Music Academy (2020-Present)"):
        st.write("""
        - Established a non-profit academy offering free music lessons to young animals  
        - Organized annual showcase festivals across districts  
        - Mentored 100+ students from diverse backgrounds  
        """)

    with st.expander("Spokesgazelle - Voices for Tomorrow Campaign (2018-2020)"):
        st.write("""
        - Led awareness campaigns for eco-friendly event spaces  
        - Advocated for youth participation in arts & culture  
        - Partnered with community leaders to support interspecies harmony  
        """)

    # Education
    st.markdown("---")
    st.header("🎓 Education")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Bachelor of Arts in Performing Arts")
        st.write("Gazelle Conservatory of Music, Zootopia")
        st.write("Focus: Vocal Performance & Stage Direction")

    with col2:
        st.subheader("Certificate in Community Leadership")
        st.write("Zootopia Civic Academy")
        st.write("Focus: Advocacy & Public Engagement")

    # Awards & Recognition
    st.markdown("---")
    st.header("🏆 Awards & Recognition")

    awards_col1, awards_col2 = st.columns(2)

    with awards_col1:
        st.write("• Zootopia Citizen Harmony Award (2022)")
        st.write("• Best Performer, Sahara Square Festival (2021)")
        st.write("• Music for Peace Honoree (2020)")

    with awards_col2:
        st.write("• Young Leader in Arts, Zootopia Council (2019)")
        st.write("• Top 10 Iconic Voices of Zootopia (2018)")
        st.write("• Rising Star Award, Tundratown Academy (2017)")

if __name__ == "__main__":
    portfolio_page()
