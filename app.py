import streamlit as st
import streamlit.components.v1 as components
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
        padding: 0.75rem 3rem;
        margin: -1rem -1rem 0.5rem -1rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        position: relative;
        z-index: 999;
        height: 60px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .header-title {
        color: white !important;
        font-size: 2rem;
        font-weight: 700;
        margin: 0;
        letter-spacing: 1.5px;
    }
    
    .header-user {
        display: flex;
        align-items: center;
        gap: 15px;
        color: white !important;
        font-weight: 500;
        font-size: 1.1rem;
    }
    
    .user-avatar {
        width: 45px;
        height: 45px;
        border-radius: 50%;
        border: 2px solid white;
    }
    
    /* Main content with minimal spacing */
    .main-content {
        margin-top: 0;
        padding: 1rem 3rem 3rem 3rem;
        max-width: 1200px;
        margin-left: auto;
        margin-right: auto;
    }
    
    /* Add responsive padding for smaller screens */
    @media (max-width: 768px) {
        .main-content {
            padding: 2rem 1.5rem;
        }
        .custom-header {
            padding: 1rem 2rem;
        }
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
        font-size: 1.8rem;
        font-weight: 600;
        color: #333;
        margin: 1.5rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #f0f0f0;
    }
    
    /* Grid layout */
    .app-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        margin-bottom: 3rem;
    }
    
    /* Search section styling */
    .search-section {
        margin-bottom: 1.5rem;
        padding-bottom: 1rem;
        border-bottom: 1px solid #f0f0f0;
    }
    
    /* Add more spacing between app rows */
    .app-row {
        margin-bottom: 2rem;
    }
    
    /* Style launch buttons */
    .launch-button {
        background: linear-gradient(135deg, #ED008C, #C70077);
        color: white !important;
        border: none;
        border-radius: 6px;
        padding: 0.5rem 1rem;
        font-weight: 700;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none;
        display: inline-block;
        text-align: center;
        width: 100%;
        margin-top: 0.5rem;
    }
    
    .launch-button:hover {
        background: linear-gradient(135deg, #C70077, #A3005F);
        text-decoration: none;
        color: white !important;
        transform: translateY(-1px);
        box-shadow: 0 2px 8px rgba(237, 0, 140, 0.3);
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

# Search and AI section side by side
st.markdown('<div class="search-section">', unsafe_allow_html=True)

# Create two columns for search and AI
search_col, ai_col = st.columns([2, 1])

with search_col:
    st.markdown("### 🔍 Search Apps")
    search_query = st.text_input("Type to search apps by name or description...", placeholder="e.g., documentation, gallery, community", key="search", label_visibility="collapsed")
    
    # Show search results info
    if search_query:
        st.markdown(f"🔍 **Search results for:** *{search_query}*")
    else:
        st.markdown("📋 **Showing all apps** - Use the search box above to filter")

with ai_col:
    st.markdown("### 🤖 AI Assistant")
    if st.button("💬 Launch AI Chat", key="ai_chat_top", use_container_width=True):
        if "ai_chat_active" not in st.session_state:
            st.session_state.ai_chat_active = True
        else:
            st.session_state.ai_chat_active = not st.session_state.ai_chat_active

st.markdown('</div>', unsafe_allow_html=True)

# Display AI Chat if activated
if st.session_state.get("ai_chat_active", False):
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
    
    if st.button("❌ Close AI Chat", key="close_ai"):
        st.session_state.ai_chat_active = False
        st.rerun()
    
    st.markdown("---")

# Featured Apps Section
st.markdown('<h2 class="section-header">Featured Apps</h2>', unsafe_allow_html=True)

# Featured Apps Cards - Verified working Streamlit apps
featured_apps = [
    {
        "title": "NYC Uber Rides",
        "description": "Interactive map showing Uber pickups in NYC",
        "icon": "🚗",
        "url": "https://share.streamlit.io/streamlit/demo-uber-nyc-pickups/main"
    },
    {
        "title": "Streamlit Gallery", 
        "description": "Official showcase of amazing Streamlit applications",
        "icon": "🎨",
        "url": "https://streamlit.io/gallery"
    },
    {
        "title": "ML Playground",
        "description": "Interactive machine learning model explorer",
        "icon": "🤖",
        "url": "https://share.streamlit.io/streamlit/example-app-iris-ml-app/main/iris-ml-app.py"
    }
]



all_apps = [
    {
        "title": "Streamlit Documentation",
        "description": "Complete API reference and tutorials",
        "icon": "📖",
        "url": "https://docs.streamlit.io/"
    },
    {
        "title": "Streamlit Community", 
        "description": "Join the Streamlit community forum",
        "icon": "👥",
        "url": "https://discuss.streamlit.io/"
    },
    {
        "title": "GitHub Repository",
        "description": "Streamlit open source code on GitHub",
        "icon": "💻",
        "url": "https://github.com/streamlit/streamlit"
    },
    {
        "title": "Streamlit Blog",
        "description": "Latest news and tutorials from Streamlit",
        "icon": "📝", 
        "url": "https://blog.streamlit.io/"
    },
    {
        "title": "Component Gallery",
        "description": "Third-party Streamlit components",
        "icon": "🧩",
        "url": "https://streamlit.io/components"
    },
    {
        "title": "Streamlit Cloud",
        "description": "Deploy and share your Streamlit apps",
        "icon": "☁️",
        "url": "https://share.streamlit.io/"
    }
]

# Combine all apps for searching
all_searchable_apps = featured_apps + all_apps

# Filter apps based on search
if search_query:
    filtered_apps = [app for app in all_searchable_apps if search_query.lower() in app['title'].lower() or search_query.lower() in app['description'].lower()]
    
    if filtered_apps:
        st.markdown(f"### Found {len(filtered_apps)} app(s)")
        st.markdown("")  # Add spacing
        # Create rows of 3 apps each
        for i in range(0, len(filtered_apps), 3):
            st.markdown('<div class="app-row">', unsafe_allow_html=True)
            cols = st.columns(3)
            for j, app in enumerate(filtered_apps[i:i+3]):
                if j < len(filtered_apps[i:i+3]):  # Make sure we don't exceed the list
                    with cols[j]:
                        st.markdown(f"""
                        <div class="app-card">
                            <div class="app-icon">{app['icon']}</div>
                            <div class="app-title">{app['title']}</div>
                            <div class="app-description">{app['description']}</div>
                            <a href="{app['url']}" target="_blank" class="launch-button">Launch</a>
                        </div>
                        """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown("### ❌ No apps found matching your search")
        st.markdown("Try searching for: *gallery*, *documentation*, *community*, *uber*, or *30 days*")
        
else:
    # Show featured apps section normally when not searching
    st.markdown("")  # Add spacing
    # Create featured apps grid
    st.markdown('<div class="app-row">', unsafe_allow_html=True)
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
    st.markdown('</div>', unsafe_allow_html=True)

    # Tableau Dashboards Section
    st.markdown('<h2 class="section-header">📊 Tableau Analytics Hub</h2>', unsafe_allow_html=True)

    # Tableau dashboard cards
    tableau_dashboards = [
        {
            "title": "Executive Dashboard",
            "description": "High-level KPIs and business metrics overview",
            "icon": "📈",
            "url": "https://public.tableau.com/app/profile/tableau.public.admin.user/viz/RegionalSampleWorkbook/Storms"
        },
        {
            "title": "Sales Performance",
            "description": "Detailed sales analytics and forecasting",
            "icon": "🎯",
            "url": "https://public.tableau.com/app/profile/tableau.public.admin.user/viz/SuperstoreSample/Overview"
        },
        {
            "title": "Financial Analytics",
            "description": "Revenue, profit, and financial trend analysis",
            "icon": "💰",
            "url": "https://public.tableau.com/gallery"
        }
    ]

    # Create tableau dashboard grid
    st.markdown('<div class="app-row">', unsafe_allow_html=True)
    tableau_cols = st.columns(3)
    for i, dashboard in enumerate(tableau_dashboards):
        with tableau_cols[i]:
            st.markdown(f"""
            <div class="app-card">
                <div class="app-icon">{dashboard['icon']}</div>
                <div class="app-title">{dashboard['title']}</div>
                <div class="app-description">{dashboard['description']}</div>
                <a href="{dashboard['url']}" target="_blank" class="launch-button">View Dashboard</a>
            </div>
            """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Sample metrics for Tableau section
    st.markdown("#### Key Business Metrics")
    metric_cols = st.columns(4)

    with metric_cols[0]:
        st.metric("Revenue", "$2.5M", "12%")
    with metric_cols[1]:
        st.metric("Active Users", "15,432", "8%") 
    with metric_cols[2]:
        st.metric("Conversion Rate", "3.2%", "0.5%")
    with metric_cols[3]:
        st.metric("Satisfaction", "4.7/5", "0.2")

    # All Apps Section (when not searching)
    st.markdown('<h2 class="section-header">All Apps</h2>', unsafe_allow_html=True)
    
    # Create rows of 3 apps each
    for i in range(0, len(all_apps), 3):
        st.markdown('<div class="app-row">', unsafe_allow_html=True)
        cols = st.columns(3)
        for j, app in enumerate(all_apps[i:i+3]):
            with cols[j]:
                st.markdown(f"""
                <div class="app-card">
                    <div class="app-icon">{app['icon']}</div>
                    <div class="app-title">{app['title']}</div>
                    <div class="app-description">{app['description']}</div>
                    <a href="{app['url']}" target="_blank" class="launch-button">Launch</a>
                </div>
                """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# Close main content container
st.markdown('</div>', unsafe_allow_html=True)
