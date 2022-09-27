import streamlit as st
from PIL import Image

st.set_page_config(page_title="My Webpage", page_icon=":tada", layout="wide")

img1 = Image.open("templates\dog.png")
with st.container():
    st.title("LOVE FOR FORGOTTEN :heart:")

text_clm, img_clm = st.columns((1, 1))
with text_clm:
    with st.container():
        st.subheader(" A common system for all volunteers, doctors and animal welfare workers to easily track in a more efficient way for such animals and communication with each other through technology is needed. An easy adopting system for stray dogs to have a better home and tracking system to track stray dogs is needed")
st.write("####")
with img_clm:
    st.image(img1, width=400)

link = """ <br><a href='https://discord.gg/FZ6WpPERQz' style="text-decoration:none;"> <h3> Click here </h3></a>"""
btn1, btn2 = st.columns((1, 2))
with btn1:
    val = st.button(label="I lost a Pet")
    if (val == True):
        enter = None
        enter = st.text_input("Enter the location")
        file = st.file_uploader(
            "Please upload a photo of a single pet. Our facial recognition technology will scan your photo for possible pet matches")
        if (enter != None):
            st.markdown(link, unsafe_allow_html=True)


st.write("####")
with btn2:

    val = st.button(label="I Found a Pet")
    if (val == True):
        st.text_input("Enter the location")

st.write("---")
st.header("Recently Uploaded Pets")

img11, img2, img3, img4 = Image.open("templates\dog1.png"), Image.open(
    "templates\dg2.png"), Image.open("templates\dg3.png"), Image.open("templates\dg4.png")

c1, c2, c3, c4 = st.columns((0.5, 0.5, 0.5, 0.5))
with c1:
    st.image(img11, caption="")
    st.subheader("Found Pet")
    st.write("(Found 8hrs ago)")
with c2:
    st.image(img2)
    st.subheader("Found Pet")
    st.write("(Found 9hrs ago)")
with c3:
    st.image(img3)
    st.subheader("Found Pet")
    st.write("(Found 12hrs ago)")
with c4:
    st.image(img4)
    st.subheader("Found Pet")
    st.write("(Found 13hrs ago)")

st.write("###")
st.write("---")

button = """<br> <br> <center> <a href="https://discord.gg/FZ6WpPERQz"><img src="https://sparkcdnwus2.azureedge.net/sparkimageassets/XPDC2RH70K22MN-08afd558-a61c-4a63-9171-d3f199738e9f" height="100px" alt=""></a> <br> <h2> Discord </h2> <center>   """
img5 = Image.open("templates\side.png")
cc1, cc2 = st.columns((1, 1))
with cc1:
    st.subheader("Join Our Community ")
    st.write("###")
    st.write("###")
    st.markdown(button, unsafe_allow_html=True)

with cc2:
    st.image(img5)
st.write("---")

content = """ <footer style="font-weight:bold;"><h3> Dedicated to LOVE FOR FORGOTTEN</h3>  </footer> """

Im = "https://loveforforgotten.org/wp-content/uploads/2021/08/cropped-loveforforgotten-valueeverylife-logo.png"
nav = """
<style>
.btn{
padding: 14px;
    margin: 13px 0px 0px 44px;
    border-radius: 6px;
    border: 4px solid #0075ad;
    width: 135px;
    float: left;
    font_weight:bold;
    font-size: 20px;
    color:cyan;
    background: black;
}
.btn:hover {
    cursor: pointer;
    border: 2px solid;
    background: linear-gradient(#43cea2 , #185a9d);
    border-color: rgb(255, 252, 252);
    transition-duration: .3s;
}
</style>
<button class="btn" > Donate </button>"""
a, b, c = st.columns((1, 1, 1))
with a:

    st.markdown(content, unsafe_allow_html=True)
with b:
    st.image(Im)

with c:
    st.markdown(nav, unsafe_allow_html=True)
