import streamlit as st
import time  # Add this import

# Configure the page
st.set_page_config(
    page_title="Gizzele's CV",
    page_icon="🦌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add a loading state
if 'loaded' not in st.session_state:
    st.session_state.loaded = False

# Show loading screen if not loaded yet
if not st.session_state.loaded:
    # Create a centered loading container
    with st.container():
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("""
            <div style='text-align: center; margin-top: 5rem;'>
                <h1 style='color: #1f77b4;'>🦌 Gizzele’s Portfolio</h1>
                <p style='font-size: 1.2rem;'>Loading Zootopia’s gazelle experience...</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Add a progress bar
            progress_bar = st.progress(0)
            
            for percent_complete in range(100):
                time.sleep(0.02)
                progress_bar.progress(percent_complete + 1)
            
            st.session_state.loaded = True
            st.rerun()

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .welcome-text {
        font-size: 1.2rem;
        text-align: center;
        margin-bottom: 2rem;
    }
    .feature-card {
        padding: 1.5rem;
        border-radius: 10px;
        background-color: #f8f9fa;
        margin: 1rem 0;
        border-left: 4px solid #1f77b4;
    }
    .content-loaded {
        animation: fadeIn 0.5s ease-in;
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
</style>
""", unsafe_allow_html=True)

# Main content - only shown after loading
st.markdown('<div class="content-loaded">', unsafe_allow_html=True)
st.markdown('<h1 class="main-header">🦌 Gizzele the Gazelle</h1>', unsafe_allow_html=True)

st.markdown("""
<div class="welcome-text">
    Welcome to my portfolio! I’m Gizzele, a gazelle from Zootopia 🌆.  
    Here you’ll find my background, performances, projects, and how to connect with me.
</div>
""", unsafe_allow_html=True)

# Feature cards
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3>🎤 About Me</h3>
        <p>A passionate performer, activist, and dreamer.  
        I’ve been singing and inspiring Zootopia’s citizens with music that bridges communities and species.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <h3>📸 Portfolio</h3>
        <p>From concerts to charity galas, see my highlights on stage, collaborations, and creative works across Zootopia.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3>🚀 Projects</h3>
        <p>Discover my advocacy projects — from promoting interspecies harmony to supporting young musicians in Zootopia.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <h3>🤝 Contact</h3>
        <p>Want to collaborate, book a performance, or just say hi? Let’s connect and make something magical together.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
