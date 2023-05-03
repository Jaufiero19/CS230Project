import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

def bystate(df):
    st.title('Check Out How Many Stadiums Are in Each State and Conference!')
    st.header('Stadiums By State')
    #Creates a set sorted in alpha. This was needed as many states were repeated within the dataframe.
    states = sorted(set(df.state))
    msLST = st.multiselect('Select as many states as you like and see which stadiums exist within them! '
                           '(double-click a stadium for name if needed)', states)
    rows = df[df.state.isin(msLST)][['stadium', 'city', 'state']]
    #This is cool. Generates a sorted dataframe by two columns in ascneding order.
    sortedRows = rows.sort_values(['state', 'city'], ascending=[True, True])
    st.write('Here are the stadiums for the states you selected:', sortedRows)

def barchart(df):
    st.header('Stadiums By NCAA Conference')
    fig = plt.figure()
    #This filters the dataframe, making conference the index column, and every column containing the number of
    #unique values that exist within the respective conference
    df = df.groupby(by='conference').count()
    #Creates a series with conference as the index column and the number of stadiums in each conferecne as the
    #other column
    perConf = df.stadium

    plt.barh(perConf.index, perConf, color='orange')

    plt.title('Number of Stadiums By Conference')
    plt.xlabel('Quantity')
    plt.ylabel('Conference')
    plt.show()
    return fig

def main():
    df = pd.read_csv('stadiums-geocoded.csv')
    bystate(df)
    fig = barchart(df)
    st.pyplot(fig)
    st.write('The ACC, Big Ten, and SEC are co-leaders, with 14 stadiums in their respective conferences. '
             'The last four NCAA champions came from the SEC. (Georgia, Georgia, Alabama, LSU)')

main()
