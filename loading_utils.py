# loading_utils.py
import streamlit as st
import time

def initialize_session_state():
    """Initialize all session state variables"""
    if 'app_loaded' not in st.session_state:
        st.session_state.app_loaded = False
    if 'current_page' not in st.session_state:
        # Set current page based on query params or default to page name
        query_params = st.query_params
        if 'page' in query_params:
            st.session_state.current_page = query_params['page']
        else:
            # Extract page name from the file path for multi-page apps
            try:
                import os
                page_name = os.path.basename(__file__).replace('.py', '')
                if page_name.startswith('pages/'):
                    page_name = page_name.replace('pages/', '')
                st.session_state.current_page = page_name
            except:
                st.session_state.current_page = "Home"

def show_loading_screen():
    """Show a loading screen for the entire app"""
    if not st.session_state.app_loaded:
        # Create a centered loading container
        with st.container():
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.markdown("""
                <div style='text-align: center; margin-top: 5rem;'>
                    <h1 style='color: #1f77b4;'>🤖 AI Assistant Suite</h1>
                    <p style='font-size: 1.2rem;'>Loading your AI experience...</p>
                </div>
                """, unsafe_allow_html=True)
                
                # Add a progress bar
                progress_bar = st.progress(0)
                
                # Simulate loading process
                for percent_complete in range(100):
                    time.sleep(0.01)
                    progress_bar.progress(percent_complete + 1)
                
                st.session_state.app_loaded = True
                st.rerun()

def page_loading_wrapper(func):
    """Decorator to add loading state to any page function"""
    def wrapper(*args, **kwargs):
        initialize_session_state()
        
        if not st.session_state.app_loaded:
            show_loading_screen()
            return
        
        # Update current page based on the function being called
        page_name = func.__name__.replace('_page', '').replace('_', ' ').title()
        st.session_state.current_page = page_name
        
        return func(*args, **kwargs)
    
    return wrapper