import streamlit as st
from loading_utils import page_loading_wrapper

@page_loading_wrapper
def projects_page():
    # Page configuration
    st.set_page_config(
        page_title="Gizzele's Projects",
        page_icon="🚀",
        layout="wide"
    )

    st.title("🚀 My Projects & Performances")
    st.markdown("Explore the performances, campaigns, and creative projects I’ve brought to life across Zootopia 🌆.")

    # Project 1
    st.markdown("---")
    col1, col2 = st.columns([2, 1])

    with col1:
        st.header("🎤 Harmony Concert Series")
        st.write("""
        **Description:** A series of concerts across Zootopia to promote unity and celebrate diversity.  
        Gathered thousands of citizens — predator and prey — to sing, dance, and embrace harmony.
        
        **Highlights:**
        - Original songs that became interspecies anthems
        - Collaborative performances with artists from every district
        - Raised funds for youth music programs
        """)
        
        if st.button("View Highlights", key="project1"):
            st.info("🎶 Concert video snippets and behind-the-scenes footage would be shown here")

    with col2:
        st.image("https://via.placeholder.com/300x200.png?text=Harmony+Concert", use_column_width=True)
        st.markdown("**Status:** ✅ Completed")
        st.markdown("**Media:** [View Coverage](https://example.com)")

    # Project 2
    st.markdown("---")
    col1, col2 = st.columns([2, 1])

    with col1:
        st.header("🌱 Voices for Tomorrow Campaign")
        st.write("""
        **Description:** A city-wide activism campaign to support young voices, protect the environment,  
        and create safe spaces for creative expression in Zootopia.
        
        **Highlights:**
        - Organized rallies and charity galas
        - Mentorship for young musicians
        - Advocated for eco-friendly concert venues
        """)
        
        if st.button("View Campaign", key="project2"):
            st.info("📸 Campaign posters, photos, and press releases would be displayed here")

    with col2:
        st.image("https://via.placeholder.com/300x200.png?text=Voices+Campaign", use_column_width=True)
        st.markdown("**Status:** 🚧 Ongoing")
        st.markdown("**Learn More:** [Visit Campaign](https://example.com)")

    # Project 3
    st.markdown("---")
    col1, col2 = st.columns([2, 1])

    with col1:
        st.header("🎶 Zootopia Music Academy")
        st.write("""
        **Description:** Founded a non-profit music academy to give young animals the chance to explore  
        music, regardless of background or species. Focused on scholarships, workshops, and mentorship.
        
        **Highlights:**
        - Free music classes for underprivileged youth
        - Annual showcase festival in Sahara Square
        - Cross-species band competitions to foster teamwork
        """)
        
        if st.button("View Academy", key="project3"):
            st.info("🎹 Academy curriculum and student stories would be displayed here")

    with col2:
        st.image("https://via.placeholder.com/300x200.png?text=Music+Academy", use_column_width=True)
        st.markdown("**Status:** ✅ Established")
        st.markdown("**Academy Page:** [Learn More](https://example.com)")

    # Additional Projects
    st.markdown("---")
    st.header("🔧 Other Creative Works")

    other_projects = [
        {"name": "Charity Gala for Harmony", "tech": "Live performance, fundraising", "status": "✅"},
        {"name": "District Music Festival", "tech": "Multi-stage events across Zootopia", "status": "✅"},
        {"name": "Green Concert Venues", "tech": "Eco-friendly event planning", "status": "🚧"},
        {"name": "Mentorship Program", "tech": "Workshops, coaching, youth talent shows", "status": "✅"},
    ]

    for project in other_projects:
        with st.expander(f"{project['status']} {project['name']}"):
            st.write(f"**Details:** {project['tech']}")
            st.progress(100 if project['status'] == '✅' else 75)

    # Call to Action
    st.markdown("---")
    st.header("💡 Interested in Collaborating?")
    st.write("I’m always open to new performances, campaigns, and collaborations. Let’s build harmony together 🎶.")

    contact_col1, contact_col2, contact_col3 = st.columns(3)

    with contact_col1:
        if st.button("📧 Send Email"):
            st.write("gizzele@zootopia.com")

    with contact_col2:
        if st.button("🌐 Official Page"):
            st.write("zootopia.com/gizzele")

    with contact_col3:
        if st.button("🎵 Music Stream"):
            st.write("music.zootopia.com/gizzele")

if __name__ == "__main__":
    projects_page()
