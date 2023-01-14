import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
from datetime import datetime, time
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

st.title('Streamlit Day 11 - 20')

# Day 11
st.write('## Day 11')
st.subheader('st.multiselect')
options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])
st.write('You selected:', options)

# Day 12
st.write('## Day 12')
st.subheader('st.checkbox')
st.write ('What would you like to order?')
icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')
if icecream:
     st.write("Great! Here's some more 🍦")
if coffee: 
     st.write("Okay, here's some coffee ☕")
if cola:
     st.write("Here you go 🥤")

# Day 13
st.write('## Day 13')
st.subheader('Spin up a cloud development environment')
st.write('https://gitpod.io/#/https://github.com/dataprofessor/streamlit101/')
st.write('pip freeze > requirements.txt')

# Day 14
st.write('## Day 14')
st.subheader('Streamlit Components')
df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
pr = df.profile_report()
# st_profile_report(pr)

# Day 15
st.write('## Day 15')
st.subheader('st.latex')
st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')

# Day 16
st.write('## Day 16')
st.subheader('Customizing the theme of Streamlit apps')
number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)

# Day 17
st.write('## Day 17')
st.subheader('st.secrets')
st.write("Name: ", st.secrets["name"])
st.write("ID: ", st.secrets['me_info']['id'])

# Day 18
st.write('## Day 18')
st.subheader('st.file_uploader')
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)    
    st.subheader('DataFrame')
    st.write(df)
    st.subheader('Descriptive Statistics')
    st.write(df.describe())
else:
    st.info('☝️ Upload a CSV file')   

# Day 19
st.write('## Day 19')
st.subheader('How to layout your Streamlit app')
st.write(''':green[**st.set_page_config(layout="wide")**] - Displays the contents of the app in wide mode (otherwise by default, the contents are encapsulated in a fixed width box.
\n:green[**st.sidebar**] - Places the widgets or text/image displays in the sidebar.
\n:green[**st.expander**] - Places text/image displays inside a collapsible container box.
\n:green[**st.columns**] - Creates a tabular space (or column) within which contents can be placed inside.''')

