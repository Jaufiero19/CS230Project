import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

def confchart(df):
    fig = plt.figure()
    btdf = df[df['conference'] == 'Big Ten']
    secdf = df[df['conference'] == 'SEC']

    plt.plot(btdf.built, btdf.capacity , 'rx', label='Big Ten')
    plt.plot(secdf.built, secdf.capacity, 'bx', label='SEC')

    plt.title('Big Ten/SEC Stadium Comparison')
    plt.xlabel('Year Constructed')
    plt.ylabel('Capacity')
    locs, labels = plt.xticks(range(1915, 2020, 15))
    plt.setp(labels, rotation = 15)

    plt.legend()
    plt.show()
    return fig

def main():
    df = pd.read_csv('stadiums-geocoded.csv')
    st.title('An Everlasting Rivalry')
    st.subheader('See how two of the most talented conferences match up in terms of stadium capacity '
                 'and construction year!')
    fig = confchart(df)
    st.pyplot(fig)
    st.write('As you can see, the majority of Big Ten and SEC stadiums were constructed prior to 1945, '
             'which highlights the tenure of the two conferences within the NCAA. The SEC maintains a '
             'slight edge when it comes to stadiums containing 100,000+ fans, yet the Big Ten appears '
             'to be younger in terms of stadium age, with 5 of their 12 stadiums having been constructed '
             'after 1945.')

main()