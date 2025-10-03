import streamlit as st
import random
from applications import temperature_of_city, get_news, news_summarizer, smart_plan

# --- Page Configuration ---
st.set_page_config(
    page_title="Morning Buddy",
    page_icon="☀️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom CSS for Professional Look ---
st.markdown("""
    <style>
    /* Main theme colors */
    :root {
        --primary-color: #FF6B6B;
        --secondary-color: #4ECDC4;
        --background-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Custom header styling */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    }
    
    .main-header h1 {
        color: white;
        font-size: 3rem;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    
    /* Card styling */
    .custom-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 1.5rem;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .custom-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
    }
    
    /* Quote box */
    .quote-box {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        font-size: 1.2rem;
        font-style: italic;
        text-align: center;
        margin: 2rem 0;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15);
    }
    
    /* Button styling */
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 25px;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
    }
    
    /* Input fields */
    .stTextInput>div>div>input {
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        padding: 0.75rem;
        font-size: 1rem;
    }
    
    .stTextInput>div>div>input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 0.2rem rgba(102, 126, 234, 0.25);
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    [data-testid="stSidebar"] .css-1d391kg {
        color: white;
    }
    
    /* News card styling */
    .news-card {
        background: white;
        border-radius: 12px;
        padding: 1rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        height: 100%;
        transition: transform 0.3s ease;
    }
    
    .news-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 4px 16px rgba(0,0,0,0.15);
    }
    
    .news-card img {
        border-radius: 8px;
        margin-bottom: 1rem;
    }
    
    .news-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #333;
        margin-bottom: 0.5rem;
    }
    
    /* Feature icons */
    .feature-icon {
        font-size: 3rem;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    /* Success/Error messages */
    .stSuccess, .stError {
        border-radius: 10px;
        padding: 1rem;
    }
    
    /* Weather info box */
    .weather-info {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        padding: 2rem;
        border-radius: 15px;
        color: #333;
        font-size: 1.1rem;
        line-height: 1.8;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }

            

    </style>
""", unsafe_allow_html=True)

# --- Helper Functions ---
def get_random_quote():
    quotes = [
        "The sun is a daily reminder that we too can rise again from the darkness, that we too can shine our own light.",
        "Write it on your heart that every day is the best day in the year.",
        "I get up every morning and it's going to be a great day. You never know when it's going to be over, so I refuse to have a bad day.",
        "Today's goals: Coffee and kindness. Maybe two coffees, and then kindness.",
        "An early-morning walk is a blessing for the whole day.",
        "Morning is an important time of day because how you spend your morning can often tell you what kind of day you are going to have.",
        "Lose an hour in the morning, and you will spend all day looking for it.",
        "When you arise in the morning, think of what a precious privilege it is to be alive – to breathe, to think, to enjoy, to love."
    ]
    return random.choice(quotes)

def get_random_image():
    image_urls = [
        "https://images.unsplash.com/photo-1470252649378-9c29740c9fa8",
        "https://images.unsplash.com/photo-1500382017468-9049fed747ef",
        "https://images.unsplash.com/photo-1494548162494-384bba4ab999",
        "https://images.unsplash.com/photo-1520038410233-7141be7e6f97",
        "https://images.unsplash.com/photo-1441974231531-c6227db76b6e",
        "https://images.unsplash.com/photo-1508575478422-c401c540a858"
    ]
    return random.choice(image_urls)

# --- Page Definitions ---

def home_page():
    """Displays the home page with a quote and image."""
    st.markdown('<div class="main-header"><h1>☀️ Your Morning Buddy</h1></div>', unsafe_allow_html=True)
   
    

    # Feature cards
    st.markdown("### ✨ What Would You Like To Do Today?")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="custom-card">
            <div class="feature-icon">🌤️</div>
            <h3 style="text-align: center;">Weather Updates</h3>
            <p style="text-align: center;">Get real-time weather information and personalized recommendations for your city.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="custom-card">
            <div class="feature-icon">📰</div>
            <h3 style="text-align: center;">Latest News</h3>
            <p style="text-align: center;">Stay updated with news articles based on your interests, complete with summaries.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="custom-card">
            <div class="feature-icon">📅</div>
            <h3 style="text-align: center;">Smart Planner</h3>
            <p style="text-align: center;">Plan your perfect day with weather-aware itineraries and local events.</p>
        </div>
        """, unsafe_allow_html=True)

    # Quote section
    st.markdown(f'<div class="quote-box">"{get_random_quote()}"</div>', unsafe_allow_html=True)
    
    # Beautiful image
    st.image(get_random_image(), width='stretch')
    
    
# features------------------

#------------------------------   

def weather_news_page():
    """Displays the page for getting weather and news by city."""
    st.markdown('<div class="main-header"><h1>🌤️ Weather Information</h1></div>', unsafe_allow_html=True)
    
    st.markdown("### Enter Your City")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        city = st.text_input("City Name", placeholder="e.g., New York, London, Tokyo", label_visibility="collapsed")
    with col2:
        fetch_button = st.button("🔍 Get Weather", use_container_width=True)
    
    if fetch_button:
        if city:
            with st.spinner('Fetching weather data...'):
                temperature_output = temperature_of_city(city)
                st.markdown(f'<div class="weather-info">{temperature_output}</div>', unsafe_allow_html=True)
                st.success("✅ Weather information fetched successfully!")
        else:
            st.error("⚠️ Please enter a city name.")

def interest_news_page():
    """Displays the page for getting news by interest."""
    st.markdown('<div class="main-header"><h1>📰 News by Interest</h1></div>', unsafe_allow_html=True)
    
    st.markdown("### What Would You Like To Read About?")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        interest = st.text_input("Area of Interest", value="Technology", 
                                placeholder="e.g., Technology, Sports, Health, Business", 
                                label_visibility="collapsed")
    with col2:
        fetch_button = st.button("📱 Get News", use_container_width=True)
    
    if fetch_button:
        if interest:
            with st.spinner('Fetching latest news...'):
                articles = get_news(interest)
                
                if not articles or len(articles) == 0:
                    st.error("⚠️ No news found for this topic. Try a different interest.")
                else:
                    st.success(f"✅ Found {len(articles)} articles about {interest}")
                    
                    # Display news in a more organized way
                    for idx, article in enumerate(articles[:5]):
                        with st.container():
                            col_img, col_content = st.columns([1, 2])
                            
                            with col_img:
                                if article.get("urlToImage"):
                                    st.image(article["urlToImage"], width='stretch')
                                else:
                                    st.info("📷 No image available")
                            
                            with col_content:
                                st.markdown(f"### {article['title']}")
                                st.markdown(f"[🔗 Read full article]({article['url']})")
                                
                                with st.expander("📝 View Summary"):
                                    with st.spinner('Generating summary...'):
                                        summary = news_summarizer(article['url'])
                                        st.write(summary)
                            
                            st.markdown("---")
        else:
            st.error("⚠️ Please enter an area of interest.")

def smart_planner():
    """Displays the page for viewing the day's schedule."""
    st.markdown('<div class="main-header"><h1>📅 Smart Day Planner</h1></div>', unsafe_allow_html=True)
    
    st.markdown("### Plan Your Perfect Day")
    st.write("Get a personalized itinerary based on weather, local events, and attractions!")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        city = st.text_input("City Name", placeholder="e.g., Paris, Mumbai, Singapore", label_visibility="collapsed")
    with col2:
        plan_button = st.button("🚀 Create Plan", use_container_width=True)
    
    if plan_button:
        if city:
            with st.spinner('Creating your personalized itinerary...'):
                smart_plans = smart_plan(city)
                st.markdown(f'<div class="custom-card">{smart_plans}</div>', unsafe_allow_html=True)
                st.balloons()
                st.success("✅ Your day plan is ready! Have an amazing day!")
        else:
            st.error("⚠️ Please enter a city name.")

# --- Sidebar Navigation ---
with st.sidebar:
    st.markdown("*Createdwith❤️byLakhan*")
    st.markdown("---")
    
    st.markdown("# 🧭 Navigation")
    st.markdown("---")
    
    page_option = st.radio(
        "Choose a page:",
        ("🏠 Home", "🌤️ Weather", "📰 News", "📅 Smart Planner"),
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("### About")
    st.info("Morning Buddy helps you start your day right with weather updates, curated news, and smart planning Powered by AI!")
    
    
    

# --- Page Routing ---
if page_option == "🏠 Home":
    home_page()
elif page_option == "🌤️ Weather":
    weather_news_page()
elif page_option == "📰 News":
    interest_news_page()
elif page_option == "📅 Smart Planner":
    smart_planner()