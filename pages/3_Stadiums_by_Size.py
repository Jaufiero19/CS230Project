import pandas as pd
import streamlit as st

def stdmSize(df):
    st.title('How Many Fans Can College Football Stadiums Hold?')
    sizes = st.slider('Check out which stadiums are the largest and which are the smallest!', value=[0, 110000], step=10000)
    #This is cool. Generates a new dataframe with two conditions and column slicing.
    nums = df[(df['capacity'] >= sizes[0]) & (df['capacity'] <= sizes[1])][['stadium', 'team', 'capacity']]
    sortedNums = nums.sort_values(['capacity'], ascending=[True])
    st.write('These stadiums hold between', sizes[0], 'and', sizes[1], 'fans.', sortedNums)


def main():
    df = pd.read_csv('stadiums-geocoded.csv')
    stdmSize(df)
    st.text("Challenge: Find which stadium holds 80,795 fans.", help='Hint: They wear blue and gold')

main()