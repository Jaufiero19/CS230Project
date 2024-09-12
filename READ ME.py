'''
Name: Jake Aufiero
CS230: Section 6
Data: NCAA Football Stadiums

Description:
This program uses data visualization techniques, along with the Streamlit app, to generate charts and graphics that
analyze a dataset of NCAA football stadiums. In particular, it generates a bar chart, scatterplot chart, and
scatterplot map alongside multiple Streamlit widgets like select boxes, multiselects, sliders, and page design
features. All of these items utilize python coding features and data analytics capabilities to bring the webpage to
life and allow a viewer to browse the analysis of the dataset.
'''

import streamlit as st

def top():
    st.title('Data Visualization of NCAA Football Stadiums')
    st.header('Created by Jake Aufiero')
    picture = 'https://mgoblue.com/images/2015/8/7/11236115.jpeg'
    st.image(picture, caption='Michigan Stadium: Ann Arbor, MI')

top()
