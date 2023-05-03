import pandas as pd
import streamlit as st

def stdmMap(df):
    confLST = df.conference
    confs = sorted(set(confLST))
    location = st.selectbox('Choose a conference:', confs)
    df = df[df['conference'] == location][['team', 'city', 'state', 'latitude', 'longitude']]
    st.write('Check out the', location, 'universities.')
    st.dataframe(df.sort_values('team'))
    st.subheader('Where Can You Find Them?')
    st.map(df)

def main():
    st.header('Visualize the Location of Stadiums Within a Conference')
    df = pd.read_csv('stadiums-geocoded.csv')
    stdmMap(df)
    st.write('Most conferences are home to teams within a relative distance of each other, but some '
             'possess outliers, like Idaho in the Sun Belt. Check it out!')

main()