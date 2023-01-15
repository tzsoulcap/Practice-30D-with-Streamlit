import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
# from datetime import datetime, time
from time import time
import requests

st.set_page_config(layout="wide")


# Day 21
st.write('## Day 21')
st.subheader('st.progress')
with st.expander('About this app'):
    st.write('Display progress bar')

pg_bar = st.progress(0)

for percent in range(100):
    # time.sleep(0.01)
    pg_bar.progress(percent+1)
# show balloon in display when progress to 100
# st.balloons()

# Day 22
st.write('## Day 22')
st.subheader('st.form')

with st.form('my_form'):
    st.subheader('**Order your coffee**')

    # Input widgets
    coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
    coffee_roast_val = st.selectbox('Coffee roast', ['Light', 'Medium', 'Dark'])
    brewing_val = st.selectbox('Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
    serving_type_val = st.selectbox('Serving format', ['Hot', 'Iced', 'Frappe'])
    milk_val = st.select_slider('Milk intensity', ['None', 'Low', 'Medium', 'High'])
    owncup_val = st.checkbox('Bring own cup')

    # Every form must have a submit button
    submitted = st.form_submit_button('Submit')

if submitted:
    st.markdown(f'''
        ☕ You have ordered:
        - Coffee bean: `{coffee_bean_val}`      # `text` highlight text
        - Coffee roast: `{coffee_roast_val}`
        - Brewing: `{brewing_val}`
        - Serving type: `{serving_type_val}`
        - Milk: `{milk_val}`
        - Bring own cup: `{owncup_val}`
        ''')
else:
    st.write('☝️ Place your order!')

# short example form
form = st.form('my_form_2')
selected_val = form.slider('Select a value')
form.form_submit_button('Submit')

st.write('Selected value: ', selected_val)

# Day 23
st.write('## Day 23')
st.subheader('st.experimental_get_query_params')

st.write(st.experimental_get_query_params())
st.write(f"Name is `{st.experimental_get_query_params()['name'][0]}`")

# Day 24
st.write('## Day 24')
st.subheader('st.cache')

a0 = time()
st.subheader('Using st.cache')

# using cache
@st.cache(suppress_st_warning=True)
def load_data_a():
    df = pd.DataFrame(
        np.random.rand(2000000, 5),
        columns=['a', 'b', 'c', 'd', 'e']
    )
    return df

st.write(load_data_a())
a1 = time()
st.info(a1-a0)

# Not using cache
b0 = time()
st.subheader('Not using st.cache')

def load_data_b():
    df = pd.DataFrame(
        np.random.rand(2000000, 5),
        columns=['a', 'b', 'c', 'd', 'e']
    )
    return df

st.write(load_data_b())
b1 = time()
st.info(b1-b0)

# Day 25
st.write('## Day 25')
st.subheader('st.session_state')

def lbs_to_kg():
    st.session_state.kg = st.session_state.lbs/2.2046 
def kg_to_lbs():
    st.session_state.lbs = st.session_state.kg*2.2046

st.header('Input')
col1, spacer, col2 = st.columns([2,1,2])
with col1:
    pounds = st.number_input("Pounds:", key = "lbs", on_change = lbs_to_kg)
with col2:
    kilogram = st.number_input("Kilograms:", key = "kg", on_change = kg_to_lbs)

st.header('Output')
st.write("st.session_state object:", st.session_state)

st.header('Counter')
# def increment_counter():
#     st.session_state.count += 1


if 'count' not in st.session_state:
    st.session_state.count = 0

# increment = st.button('Increment', on_click=increment_counter)
# if increment:
#     st.session_state.count += 1

increment_value = st.number_input('Enter a value', value=0, step=1)
num = 1
def increment_counter(increment_value, n):
    st.session_state.count += increment_value
    st.session_state.count += n
def decrement_counter(increment_value, n):
    st.session_state.count -= increment_value
    st.session_state.count -= n

c1, c2, c3 = st.columns([2, 2, 4])
with c1:
    increment = st.button('Increment', on_click=increment_counter,
        args=(increment_value, num))
with c2:
    decrement = st.button('Decrement', on_click=decrement_counter,
        args=(increment_value, num))

st.write('Count = ', st.session_state.count)

# Day 26
st.write('## Day 26')
st.subheader('How to use API by building the Bored API app')

st.sidebar.header('Input')
selected_type = st.sidebar.selectbox('Select an activity type', ["education", "recreational", "social", "diy", "charity", "cooking", "relaxation", "music", "busywork"])

suggested_activity_url = f'http://www.boredapi.com/api/activity?type={selected_type}'
json_data = requests.get(suggested_activity_url)
suggested_activity = json_data.json()
c1, c2 = st.columns(2)
with c1:
    with st.expander('About this app'):
        st.write('Are you bored? The **Bored API app** provides suggestions on activities that you can do when you are bored. This app is powered by the Bored API.')
with c2:
    with st.expander('JSON data'):
        st.write(suggested_activity)
st.header('Suggested activity')
st.info(suggested_activity['activity'])

col1, col2, col3 = st.columns(3)
with col1:  # delta is green/red
    st.metric(label='Number of Participants', value=suggested_activity['participants'], delta='')
with col2:
    st.metric(label='Type of Activity', value=suggested_activity['type'].capitalize(), delta='')
with col3:
    st.metric(label='Price', value=suggested_activity['price'], delta='')

