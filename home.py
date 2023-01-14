import streamlit as st
import altair as alt
import pandas as pd
import numpy as np

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

