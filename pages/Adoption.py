
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Find Vets", page_icon=":tada", layout="wide")


with st.container():
    st.title("ADOPTION")

st.write("---")
img1 = Image.open("templates\DOG9.png")
a,b=st.columns((1,1))
with a:
    st.title(""" Our shelters have some amazing dogs that are eagerly waitingto find a forever home and a loving family!
    Bringing home a pet is akin to
    welcoming a new family member and therefore a commitment to the pet’s health
    and wellbeing for its lifetime. This commitment has physical, emotional, 
    and financial implications and therefore, before you decide to register with us as an adopter, 
    please read through the following information carefully and make an informed decision""")
with b:
    st.image(img1,width=600)    

st.write("---") 
with st.container():
    st.title("DOGS AVAILABLE FOR ADOPTION")

html = """<h4>Available</h4>
<ul>
    <li>Animal ID: 43096032958</li>
    <li>Animal Breed: Boxer</li>
   
</ul>"""
html1 = """<h4>Available</h4>
<ul>
    <li>Animal ID: 43096032958</li>
    <li>Animal Breed: Bulldog</li>
   
</ul>"""
html2 = """<h4>Available</h4>
<ul>
    <li>Animal ID: 43096032958</li>
    <li>Animal Breed: Norfolk terrier</li>
   
</ul>"""
html3 = """<h4>Available</h4>
<ul>
    <li>Animal ID: 43096032958</li>
    <li>Animal Breed: Papillon</li>
   
</ul>"""
c1, c2, c3, c4 = st.columns((0.5, 0.5, 0.5, 0.5))
with c1:
    st.image("templates\Boxer_02362.jpg", caption="")
    st.markdown(html,unsafe_allow_html=True)
    
with c2:
    st.image("templates\Bulldog_02808.jpg")
    st.markdown(html1,unsafe_allow_html=True)
with c3:
    st.image("templates\Norfolk_terrier_07038.jpg")
    st.markdown(html2,unsafe_allow_html=True)
with c4:
    st.image("templates\Papillon_07446.jpg")
    st.markdown(html3,unsafe_allow_html=True)
st.write("---")


content = """ <footer style="font-weight:bold;"><h3> Dedicated to LOVE FOR FORGOTTEN</h3>  </footer> """

Im="https://loveforforgotten.org/wp-content/uploads/2021/08/cropped-loveforforgotten-valueeverylife-logo.png"
nav ="""
<style>
button{
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
button:hover {
    cursor: pointer;
    border: 2px solid;
    background: linear-gradient(#43cea2 , #185a9d);
    border-color: rgb(255, 252, 252);
    transition-duration: .3s;
}
</style>
<button > Donate </button>"""
a,b,c=st.columns((1,1,1))
with a:

    st.markdown(content,unsafe_allow_html=True)
with b:
    st.image(Im)

with c:
    st.markdown(nav,unsafe_allow_html=True)