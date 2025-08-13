import streamlit as st
import base64
from io import BytesIO
from PIL import Image, ImageDraw

# Page configuration
st.set_page_config(
    page_title="Quantum Discover",
    page_icon="⚛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Function to create a user avatar
def create_user_avatar(initials="MN", size=50):
    """Create a circular avatar with initials"""
    img = Image.new('RGB', (size, size), color='#ED008C')
    draw = ImageDraw.Draw(img)
    
    # Calculate text size and position for centering
    font_size = size // 3
    text_width = len(initials) * (font_size // 2)
    text_height = font_size
    text_x = (size - text_width) // 2
    text_y = (size - text_height) // 2
    
    # Draw initials
    draw.text((text_x, text_y), initials, fill='white')
    
    # Make it circular
    mask = Image.new('L', (size, size), 0)
    draw_mask = ImageDraw.Draw(mask)
    draw_mask.ellipse((0, 0, size, size), fill=255)
    
    # Apply mask
    img.putalpha(mask)
    
    return img

# Custom CSS for styling with the specified theme color
st.markdown("""
<style>
    /* Hide Streamlit default elements */
    .stApp > header {visibility: hidden;}
    .stDeployButton {display: none;}
    MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom header bar */
    .custom-header {
        background: #ED008C;
        padding: 1rem 2rem;
        margin: -1rem -1rem 2rem -1rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 999;
        height: 80px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .header-title {
        color: white;
        font-size: 1.8rem;
        font-weight: 700;
        margin: 0;
        letter-spacing: 1px;
    }
    
    .header-user {
        display: flex;
        align-items: center;
        gap: 10px;
        color: white;
        font-weight: 500;
    }
    
    .user-avatar {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        border: 2px solid white;
    }
    
    /* Main content with top margin */
    .main-content {
        margin-top: 100px;
        padding: 2rem;
    }
    
    /* Search bar styling */
    .search-container {
        max-width: 600px;
        margin: 2rem auto;
        position: relative;
    }
    
    .search-input {
        width: 100%;
        padding: 1rem 1rem 1rem 3rem;
        border: 2px solid #f0f0f0;
        border-radius: 25px;
        font-size: 1.1rem;
        background: white;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    
    .search-icon {
        position: absolute;
        left: 15px;
        top: 50%;
        transform: translateY(-50%);
        color: #999;
        font-size: 1.2rem;
    }
    
    /* App card styling */
    .app-card {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        border: 1px solid #f0f0f0;
        transition: all 0.3s ease;
        margin-bottom: 1rem;
        height: 100%;
        display: flex;
        flex-direction: column;
    }
    
    .app-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        border-color: #ED008C;
    }
    
    .app-icon {
        width: 60px;
        height: 60px;
        background: #ED008C;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 1rem;
        font-size: 1.8rem;
        color: white;
    }
    
    .app-title {
        font-size: 1.2rem;
        font-weight: 600;
        color: #333;
        margin-bottom: 0.5rem;
    }
    
    .app-description {
        color: #666;
        font-size: 0.9rem;
        margin-bottom: 1rem;
        flex-grow: 1;
    }
    
    .launch-button {
        background: #ED008C;
        color: white;
        border: none;
        border-radius: 6px;
        padding: 0.5rem 1rem;
        font-weight: 500;
        cursor: pointer;
        transition: background 0.3s ease;
        text-decoration: none;
        display: inline-block;
        text-align: center;
    }
    
    .launch-button:hover {
        background: #C70077;
        text-decoration: none;
        color: white;
    }
    
    /* Section headers */
    .section-header {
        font-size: 1.5rem;
        font-weight: 600;
        color: #333;
        margin: 2rem 0 1rem 0;
    }
    
    /* Grid layout */
    .app-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 1.5rem;
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Create and display user avatar
avatar_img = create_user_avatar("Monte"[0:2].upper(), 80)

# Custom header
st.markdown("""
<div class="custom-header">
    <h1 class="header-title">QUANTUM DISCOVER</h1>
    <div class="header-user">
        <span>Monte</span>
        <div style="width: 40px; height: 40px; background: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; color: #ED008C;">M</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Main content container
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Search bar
st.markdown("""
<div class="search-container">
    <div style="position: relative;">
        <input type="text" placeholder="Search apps..." class="search-input" style="width: 100%; padding: 1rem 1rem 1rem 3rem; border: 2px solid #f0f0f0; border-radius: 25px; font-size: 1.1rem; background: white; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
        <span class="search-icon" style="position: absolute; left: 15px; top: 50%; transform: translateY(-50%); color: #999; font-size: 1.2rem;">🔍</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Search functionality
search_query = st.text_input("", placeholder="Search apps...", key="search", label_visibility="collapsed")

# Featured Apps Section
st.markdown('<h2 class="section-header">Featured Apps</h2>', unsafe_allow_html=True)

# Featured Apps Cards - Real working Streamlit apps
featured_apps = [
    {
        "title": "Guess the Country",
        "description": "Interactive geography game - guess countries by their outline",
        "icon": "🌍",
        "url": "https://gerardrbentley-streamlit-worldle-worldle-0j1j0j.streamlit.app/"
    },
    {
        "title": "Brainstorming Buddy", 
        "description": "AI-powered idea generator using GPT-3",
        "icon": "💡",
        "url": "https://ayoubnini-brainstorming-buddy-app-0j1j0j.streamlit.app/"
    },
    {
        "title": "Color-coded Writing",
        "description": "Text analysis tool that color-codes by sentence length",
        "icon": "🎨",
        "url": "https://johannesrieke-color-coded-writing.streamlit.app/"
    }
]

# Create featured apps grid
cols = st.columns(3)
for i, app in enumerate(featured_apps):
    with cols[i]:
        st.markdown(f"""
        <div class="app-card">
            <div class="app-icon">{app['icon']}</div>
            <div class="app-title">{app['title']}</div>
            <div class="app-description">{app['description']}</div>
            <a href="{app['url']}" target="_blank" class="launch-button">Launch</a>
        </div>
        """, unsafe_allow_html=True)

# All Apps Section
st.markdown('<h2 class="section-header">All Apps</h2>', unsafe_allow_html=True)

all_apps = [
    {
        "title": "Links Page",
        "description": "Personal link aggregator similar to Linktree",
        "icon": "🔗",
        "url": "https://dataprofessor-links.streamlit.app/"
    },
    {
        "title": "Constellation Explorer", 
        "description": "Satellite constellation transit schedules over Earth",
        "icon": "🛰️",
        "url": "https://pritishc-constellation-explorer.streamlit.app/"
    },
    {
        "title": "Uber Pickups NYC",
        "description": "Interactive map of Uber pickups in New York City",
        "icon": "🚗",
        "url": "https://share.streamlit.io/streamlit/demo-uber-nyc-pickups"
    },
    {
        "title": "Stock Price App",
        "description": "Real-time stock price visualization and analysis",
        "icon": "📈", 
        "url": "https://share.streamlit.io/dataprofessor/sp500-app/main/sp500-app.py"
    },
    {
        "title": "COVID-19 Dashboard",
        "description": "Interactive COVID-19 data visualization",
        "icon": "🦠",
        "url": "https://share.streamlit.io/holtzy/The-Python-Graph-Gallery/master/src/notebooks/matplotlib_streamlit.py"
    },
    {
        "title": "Machine Learning Demo",
        "description": "Interactive ML model training and prediction",
        "icon": "🤖",
        "url": "https://share.streamlit.io/streamlit/demo-face-gan"
    }
]

# Filter apps based on search
if search_query:
    filtered_apps = [app for app in all_apps if search_query.lower() in app['title'].lower() or search_query.lower() in app['description'].lower()]
else:
    filtered_apps = all_apps

# Create grid for all apps
if filtered_apps:
    # Create rows of 3 apps each
    for i in range(0, len(filtered_apps), 3):
        cols = st.columns(3)
        for j, app in enumerate(filtered_apps[i:i+3]):
            with cols[j]:
                st.markdown(f"""
                <div class="app-card">
                    <div class="app-icon">{app['icon']}</div>
                    <div class="app-title">{app['title']}</div>
                    <div class="app-description">{app['description']}</div>
                    <a href="{app['url']}" target="_blank" class="launch-button">Launch</a>
                </div>
                """, unsafe_allow_html=True)
else:
    st.markdown("### No apps found matching your search criteria.")

# AI Chat Section (if activated)
if st.button("🤖 Launch AI Assistant", key="ai_chat"):
    st.markdown("---")
    st.markdown("### 🤖 Quantum AI Assistant")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask me about your data and analytics..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate assistant response
        with st.chat_message("assistant"):
            response = f"Thank you for your question: '{prompt}'. I'm here to help you explore your data, understand analytics, and navigate the Quantum Discover platform. In a full implementation, I would connect to advanced AI services to provide detailed insights about your specific datasets and business metrics."
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

# Tableau Dashboard Section
if st.button("📊 Open Tableau Dashboards", key="tableau"):
    st.markdown("---")
    st.markdown("### 📊 Tableau Analytics Hub")
    
    # Create dashboard preview cards
    dashboard_cols = st.columns(2)
    
    with dashboard_cols[0]:
        st.markdown("""
        <div class="app-card">
            <div class="app-icon">📈</div>
            <div class="app-title">Executive Dashboard</div>
            <div class="app-description">High-level KPIs and business metrics overview</div>
            <a href="https://public.tableau.com/app/profile/tableau.public.admin.user/viz/RegionalSampleWorkbook/Storms" target="_blank" class="launch-button">View Dashboard</a>
        </div>
        """, unsafe_allow_html=True)
    
    with dashboard_cols[1]:
        st.markdown("""
        <div class="app-card">
            <div class="app-icon">🎯</div>
            <div class="app-title">Sales Performance</div>
            <div class="app-description">Detailed sales analytics and forecasting</div>
            <a href="https://public.tableau.com/app/profile/tableau.public.admin.user/viz/SuperstoreSample/Overview" target="_blank" class="launch-button">View Dashboard</a>
        </div>
        """, unsafe_allow_html=True)
    
    # Sample metrics
    st.markdown("#### Key Metrics")
    metric_cols = st.columns(4)
    
    with metric_cols[0]:
        st.metric("Revenue", "$2.5M", "12%")
    with metric_cols[1]:
        st.metric("Active Users", "15,432", "8%") 
    with metric_cols[2]:
        st.metric("Conversion Rate", "3.2%", "0.5%")
    with metric_cols[3]:
        st.metric("Satisfaction", "4.7/5", "0.2")

# Close main content container
st.markdown('</div>', unsafe_allow_html=True)
