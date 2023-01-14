import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
from datetime import datetime, time

st.title('Practice Streamlit 30 Days')

# Day 2
st.write('## Day 2')
st.write('Hello Streamlit!')

# Day 3
st.write('## Day 3')
st.header('st.button')
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

# Day 4
st.write('## Day 4')
st.write('https://youtu.be/Yk-unX4KnV4')

# Day 5
st.write('## Day 5')
st.header('st.write')
st.write('Hello, *World!* :sunglasses:')
st.write(1234)
df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')
df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

# Day 6
st.write('## Day 6')
st.write('Uploading your Streamlit app to GitHub')

# Day 7
st.write('## Day 7')
st.write('Deploying your Streamlit app with Streamlit Community Cloud')

# Day 8
st.write('## Day 8')
st.subheader('slider')
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

st.subheader('Range slider')
values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

st.subheader('Range time slider')
appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

st.subheader('Datetime slider')
start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

# Day 9
st.write('## Day 9')
st.subheader('st.line_chart')
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.dataframe(chart_data)
st.line_chart(chart_data)

# Day 10
st.write('## Day 10')
st.subheader('st.selectbox')
option = st.selectbox(
     'What is your favorite color?',
     ['Blue', 'Red', 'Green'])

st.write('Your favorite color is ', option)