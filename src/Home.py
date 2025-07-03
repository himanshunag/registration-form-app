import streamlit as st
import os

# Set background color to lavender for the main app area
st.markdown(
    """
    <style>
    .stApp {
        background-color: #E6E6FA;
    }
    .bold-label {
        font-weight: bold;
        font-size: 1.1em;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Center the logo using columns, with fallback if file is missing
col1, col2, col3 = st.columns([1,2,1])
with col2:
    logo_path = "tgg_logo.png"
    if os.path.exists(logo_path):
        st.image(logo_path, width=180)
    else:
        st.image("https://upload.wikimedia.org/wikipedia/commons/a/ab/Logo_TV_2015.png", width=180)  # fallback logo

# Center the main title
st.markdown(
    "<h1 style='text-align: center; color: black; font-size: 3em;'>Primo Mega Hardware</h1>",
    unsafe_allow_html=True
)

# Center the sub-title
st.markdown(
    "<h2 style='text-align: center;'>Registration Links Application</h2>",
    unsafe_allow_html=True
)

registration_links = {
    "Dealer": {
        "link": "https://forms.gle/2AzUDGpt4BbhpJbp8",
        "image": "dealer.png"  # Place dealer.png in the same folder
    },
    "Welder": {
        "link": "https://forms.gle/LQWZ7F3YJ47Cw5X46",
        "image": "welder.png"  # Place welder.png in the same folder
    },
    "Painter": {
        "link": "https://forms.gle/cqLpi7tVBSgwSoJz7",
        "image": "painter.png"  # Place painter.png in the same folder
    }
}

# Bold select label
st.markdown('<span class="bold-label">Select the type of registration:</span>', unsafe_allow_html=True)
registration_type = st.selectbox(
    "",
    ["Select"] + list(registration_links.keys())
)

if registration_type != "Select":
    url = registration_links[registration_type]["link"]
    image_path = registration_links[registration_type]["image"]
    st.markdown(f"[{registration_type} Registration Link]({url})", unsafe_allow_html=True)
    if image_path and os.path.exists(image_path):
        st.image(image_path, caption=f"{registration_type} Registration", width=250)