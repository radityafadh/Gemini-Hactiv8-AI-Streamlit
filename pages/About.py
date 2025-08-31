import streamlit as st
from loading_utils import page_loading_wrapper

@page_loading_wrapper
def about_page():
    # Page configuration
    st.set_page_config(
        page_title="About Gizzele",
        page_icon="ℹ️",
        layout="wide"
    )

    st.title("ℹ️ About Me")
    st.markdown("---")

    # Introduction
    col1, col2 = st.columns([2, 1])

    with col1:
        st.header("Hello! I’m Gizzele 🦌🎶")
        st.write("""
        I’m a gazelle from Zootopia — a performer, activist, and dreamer.  
        From the biggest stages in Sahara Square to grassroots campaigns in Bunnyburrow,  
        I’ve dedicated my voice to bringing predator and prey together through music.  

        For me, performance is more than entertainment — it’s a bridge between worlds.  
        I believe harmony can be achieved not only in music but also in our daily lives,  
        when we embrace diversity and stand together.  

        When I’m not performing, you’ll find me mentoring young musicians,  
        leading community projects, or advocating for eco-friendly events that protect our home.  
        """)
    with col2:
        st.image("https://via.placeholder.com/300x300.png?text=Gizzele", use_column_width=True)
        st.success("**Currently active in:** Performances, mentorship, and advocacy projects")

    # Values and Philosophy
    st.markdown("---")
    st.header("🎯 My Values & Philosophy")

    values = [
        {"icon": "🎶", "title": "Harmony", "desc": "Creating unity through music and performance"},
        {"icon": "🌍", "title": "Community", "desc": "Uplifting every voice, no matter the species"},
        {"icon": "💡", "title": "Creativity", "desc": "Using art to inspire and spark change"},
        {"icon": "🌱", "title": "Sustainability", "desc": "Advocating for eco-friendly concerts and projects"},
    ]

    value_cols = st.columns(4)
    for i, value in enumerate(values):
        with value_cols[i]:
            st.markdown(f"### {value['icon']} {value['title']}")
            st.caption(value['desc'])

    # Fun Facts
    st.markdown("---")
    st.header("🎉 Fun Facts About Me")

    fact_col1, fact_col2 = st.columns(2)

    with fact_col1:
        st.info("""
        **Performance Journey:**
        - 🎤 Started singing at local community events
        - 🌆 Headlined Zootopia’s Harmony Concert Series
        - 🎶 Released 3 city-wide anthems for peace
        - 🏆 Recognized as one of Zootopia’s iconic voices
        """)

    with fact_col2:
        st.info("""
        **Personal Interests:**
        - 🐾 Mentor for young musicians across districts
        - 🌱 Advocate for eco-friendly performance spaces
        - 🎨 Lover of fashion and colorful stage designs
        - 📖 Storyteller through music and lyrics
        """)

    # Testimonials
    st.markdown("---")
    st.header("🌟 What People Say")

    testimonial_col1, testimonial_col2 = st.columns(2)

    with testimonial_col1:
        st.success("""
        "Gizzele’s music doesn’t just entertain — it heals.  
        She brings predators and prey together in a way no one else can."  
        
        *– Mayor Lionheart, Zootopia Leadership Council*
        """)

    with testimonial_col2:
        st.success("""
        "Performing alongside Gizzele was inspiring.  
        Her passion for harmony and community is truly contagious."  
        
        *– Bucky & Pronk, Fellow Performers*
        """)

    # Contact Information
    st.markdown("---")
    st.header("📞 Let’s Connect!")

    contact_col1, contact_col2, contact_col3, contact_col4 = st.columns(4)

    with contact_col1:
        st.button("📧 Email", help="Reach me at gizzele@zootopia.com")

    with contact_col2:
        st.button("🌐 Official Page", help="Visit zootopia.com/gizzele")

    with contact_col3:
        st.button("🎵 Music Stream", help="Stream my songs on Zootopia Music")

    with contact_col4:
        st.button("📸 Socials", help="Follow me on ZootopiaGram")

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: gray;'>
        <p>Made with ❤️ in Zootopia</p>
        <p>© 2025 Gizzele. All rights reserved.</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    about_page()
