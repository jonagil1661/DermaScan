import streamlit as st
import urllib.parse

st.set_page_config(
    page_title="About DermaScan",
    page_icon="🩺",
    layout="centered"
)


st.markdown(
    """
    <style>
        body {
            margin: 0;
            padding: 0;
        }
    
        .video-container {
            width: 100%;
            height: 100vh;
            overflow: hidden;
            z-index: -1;  
        }

        video {
            width: 100%;
            height: 100%;
            object-fit: cover;  
        }

        
        .overlay {
            position: absolute; 
            top: 30%;  
            left: 50%;
            transform: translateX(-50%);
            background: rgba(255, 255, 255, 0.8);
            padding: 40px;
            border-radius: 10px;
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            color: #333;
            z-index: 1;
            width: 80%;
            max-width: 1200px;
        }

        
        .content-container {
            position: relative;
            z-index: 3;
            padding: 20px;
        }

    </style>

    <div class="video-container">
        <video autoplay loop muted>
            <source src="https://www.pexels.com/download/video/3191861/" type="video/mp4">
        </video>
    </div>

    <!-- Title Overlay centered above the video -->
    <div class="overlay">DermaScan</div>

    <!-- Content area that will scroll -->
    <div class="content-container">
        <div class="content">
    """,
    unsafe_allow_html=True
)


st.title("About Us")
st.write("""
DermaScan is an interactive tool that allows users to input images of their skin and using a deep learning algorithm we here at DermaScan will
         help identify any potential skin diseases or conditions you may possibly have from here users can simply enter in their location
         and we will show you the specialists for your condition in the area!

### Features:
- Identify Potential Skin Conditions/Diseases
- Find nearby dermatology clinics
- Interactive map
- Simple and fast location search
""")

st.markdown("</div>", unsafe_allow_html=True)