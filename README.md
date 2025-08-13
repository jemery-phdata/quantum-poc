# Quantum Reporting Landing Page

A beautiful Streamlit-based landing page for accessing various reporting tools, AI chat agents, and embedded Tableau dashboards.

## Features

- 🎨 **Modern UI** with custom CSS styling and theme color #ED008C
- 📊 **Streamlit Apps Integration** - Links to various data analysis tools
- 🤖 **AI Chat Agent** - Interactive chat interface for data insights
- 📈 **Tableau Reporting** - Embedded dashboard functionality
- 🚀 **Quick Actions** - Schedule reports, notifications, and settings

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Local Setup

1. **Clone or download the project** to your local machine

2. **Navigate to the project directory**:
   ```bash
   cd quantum
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

5. **Open your browser** and go to `http://localhost:8501`

## Project Structure

```
quantum/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Deployment Guide

### Option 1: Streamlit Cloud (Recommended)

1. **Create a GitHub account** (if you don't have one):
   - Go to [github.com](https://github.com)
   - Click "Sign up"
   - Follow the registration process

2. **Create a new repository**:
   - Click the "+" icon in the top right
   - Select "New repository"
   - Name it "quantum-reporting" (or any name you prefer)
   - Make it public
   - Click "Create repository"

3. **Upload your files**:
   - Click "uploading an existing file"
   - Drag and drop `app.py`, `requirements.txt`, and `README.md`
   - Add a commit message like "Initial commit"
   - Click "Commit changes"

4. **Deploy to Streamlit Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository and branch (main)
   - Set main file path to `app.py`
   - Click "Deploy"

### Option 2: Heroku

1. Install Heroku CLI
2. Create a `Procfile` with: `web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`
3. Deploy using Heroku Git

### Option 3: Other Cloud Platforms

- **AWS**: Use EC2 or Elastic Beanstalk
- **Google Cloud**: Use App Engine or Compute Engine
- **DigitalOcean**: Use App Platform or Droplets

## Customization

### Adding Real Tableau Dashboards

To embed real Tableau dashboards, replace the placeholder code with:

```python
import streamlit.components.v1 as components

# Tableau embed code
tableau_embed = """
<script type='text/javascript' src='https://public.tableau.com/javascripts/api/viz_v1.js'></script>
<div class='tableauPlaceholder' style='width: 100%; height: 600px;'>
    <object class='tableauViz' style='display:none;'>
        <param name='host_url' value='https://public.tableau.com/' />
        <param name='embed_code_version' value='3' />
        <param name='site_root' value='' />
        <param name='name' value='YourDashboardName' />
        <param name='tabs' value='no' />
        <param name='toolbar' value='yes' />
    </object>
</div>
"""

components.html(tableau_embed, height=600)
```

### Adding Real AI Integration

To connect a real AI service, install additional dependencies:

```bash
pip install openai  # For OpenAI GPT
pip install anthropic  # For Claude
```

Then replace the demo chat with real API calls.

### Styling Customization

The app uses a custom color scheme based on #ED008C. To change colors:

1. Find the CSS section in `app.py`
2. Replace #ED008C and #C70077 with your preferred colors
3. Update gradient colors accordingly

## Troubleshooting

### Common Issues

1. **Port already in use**: 
   - Stop other Streamlit apps or use: `streamlit run app.py --server.port 8502`

2. **Dependencies not found**:
   - Ensure you're in the correct directory
   - Try: `pip install --upgrade -r requirements.txt`

3. **Streamlit Cloud deployment fails**:
   - Check that `requirements.txt` is in the root directory
   - Ensure all imports in `app.py` are included in requirements

### Getting Help

- [Streamlit Documentation](https://docs.streamlit.io)
- [Streamlit Community Forum](https://discuss.streamlit.io)
- [GitHub Issues](https://github.com/streamlit/streamlit/issues)

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to submit issues and enhancement requests!

