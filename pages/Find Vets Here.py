
from turtle import onclick, width

import streamlit as st
import pandas as pd
import numpy as np
# from mutliapp import MultiApp
# from apps import home,data,model

from PIL import Image

st.set_page_config(page_title="Find Vets", page_icon=":tada", layout="wide")

with st.container():
    st.title("LOVE FOR FORGOTTEN :heart:")

st.subheader("Find vet here :mag:")

option = st.selectbox(
    'Find vets in your district',
    ('Select', 'Bangalore', 'Mysore', 'Mangalore','Hassan','Bidar','Gulbarga','Belagavi','Bellari'))


i=[12.9716,77.5946]
df = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + i,
    columns=['lat', 'lon'])

st.write('You selected:', option)
if option=='Bangalore':
    i=[12.9716,77.5946]
elif option=='Mysore':
    i=[12.295,76.6394]
elif option=='Mangaloore':
    i=[12.914,74.856]
elif option=='Hassan':
    i=[13.003,76.1004]
elif option=='Bidar':
    i=[17.910,77.5199]
elif option=='Gulbarga':
    i=[17.3297,76.8343]
elif option=='Belagavi':
    i=[15.8497,74.4977]
elif option=='Bellari':
    i=[15.1397,76.9214]


df = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + i,
    columns=['lat', 'lon'])

st.map(df)


st.write("---")


content = """ <footer style="font-weight:bold;"><h3> Dedicated to LOVE FOR FORGOTTEN</h3>  </footer> """

Im="https://loveforforgotten.org/wp-content/uploads/2021/08/cropped-loveforforgotten-valueeverylife-logo.png"
nav ="""
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
a,b,c=st.columns((1,1,1))
with a:

    st.markdown(content,unsafe_allow_html=True)
with b:
    st.image(Im)

with c:
    st.markdown(nav,unsafe_allow_html=True)