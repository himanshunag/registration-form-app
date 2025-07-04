import streamlit as st
import os

# Set background color to lavender and all font colors to black for the main app area
st.markdown(
    """
    <style>
    .stApp {
        background-color: #E6E6FA;
        color: black;
    }
    .bold-label {
        font-weight: bold;
        font-size: 1.1em;
        color: black !important;
    }
    h1, h2, h3, h4, h5, h6, label, .css-10trblm, .css-1v0mbdj, .css-1cpxqw2 {
        color: black !important;
    }
    /* Hide Streamlit top menu and footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

# Center the main title
st.markdown(
    "<h1 style='text-align: center; color: black; font-size: 3em;'>Primo Mega Hardware</h1>",
    unsafe_allow_html=True
)

# Center the sub-title
st.markdown(
    "<h2 style='text-align: center; color: black;'>Registration Links Application</h2>",
    unsafe_allow_html=True
)

registration_links = {
    "Dealer": {
        "link": "https://forms.gle/2AzUDGpt4BbhpJbp8",
        "image": "./dealer.png"  # Place dealer.png in the same folder
    },
    "Welder": {
        "link": "https://forms.gle/LQWZ7F3YJ47Cw5X46",
        "image": "./welder.png"  # Place welder.png in the same folder
    },
    "Painter": {
        "link": "https://forms.gle/cqLpi7tVBSgwSoJz7",
        "image": "./painter.png"  # Place painter.png in the same folder
    }
}

# Bold select label
st.markdown(
    '<div style="display: flex; flex-direction: column; align-items: center;">'
    '<span class="bold-label">Select the type of registration:</span>',
    unsafe_allow_html=True
)
registration_type = st.selectbox(
    "",
    ["Select"] + list(registration_links.keys()),
    key="registration_type"
)
st.markdown('</div>', unsafe_allow_html=True)

if registration_type != "Select":
    url = registration_links[registration_type]["link"]
    image_path = registration_links[registration_type]["image"]
    st.markdown(f"<span style='color:black;'><a href='{url}' target='_blank'>{registration_type} Registration Link</a></span>", unsafe_allow_html=True)
    if image_path and os.path.exists(image_path):
        st.image(image_path, caption=f"{registration_type} Registration", width=250)