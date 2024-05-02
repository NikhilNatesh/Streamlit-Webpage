import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/vjtech_pic.png")
img_lottie_animation = Image.open("images/machines_vj.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Welcome to VJ Technologies!")
    st.title("Worlds best X-ray Imaging System")
    st.write(
        "(VJT) is a global leader in providing digital radiography and computed tomography x-ray inspection systems and solutions for a variety of industries ranging from aerospace and automotive to food and nuclear"
    )
    st.write("[Learn More >](https://vjt.com/about-vjt/)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("We Listen to our customers problems and work with them to find the right equipment.")
        st.write("##")
        st.write(
            """
            - The data our reimagined, durable, user friendly, and fashionable systems deliver to our customers leaves them smiling as they show the cutting edge technology."

            If this sounds interesting to you, consider subscribing and turning on the notifications, so you don’t miss any content.
            """
        )
        st.write("[Support >](https://vjt.com/support/)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("X‑Ray Imaging Reimagined")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("What can VEDA do for you?")
        st.write(
            """
            CT SYSTEMS - 
            Our Vi5 CT Software has an advanced CT menu for the users who are Looking to test boundaries!
            VJ Technologies standard Veda CT Product line provides flexibility and Mechanical team's expertise were established with two decades of creating solutions for the worlds most challenging CT Systems.
            """
        )
        st.markdown("[Learn more...](https://vjt.com/ct-systems/)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("VJ Inspection Services")
        st.write(
            """
            The VJIS team of experts focus on delivering great scan results to help ensure the quality of your products, or expediting your development.
            """
        )
        st.markdown("[Learn more...](https://vjt.com/scanning-services/)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/n.nikhil042168@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()













































































































































































































































































