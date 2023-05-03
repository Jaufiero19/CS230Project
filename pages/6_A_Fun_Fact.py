import pandas as pd
import streamlit as st

def stats(df, numHotdogs=8):
    stdms = sorted(set(df.stadium))
    msLST = st.multiselect('Choose some stadiums to learn more about them!', stdms)
    rows = df[df.stadium.isin(msLST)]
    avgFans = rows.capacity.mean()
    st.write('These stadiums can hold an average of', round(avgFans, 1), 'fans...')
    fact = avgFans / numHotdogs
    st.write('Who can eat', round(fact, 1), "packs of 8-count BallPark Franks while watching the game! That's a lot of dogs!")
    return avgFans, fact

def main():
    df = pd.read_csv('stadiums-geocoded.csv')
    st.title('Stadium Facts')
    stats(df)
    picture = 'https://images.albertsons-media.com/is/image/ABS/188570015-ECOM?' \
              '$ng-ecom-pdp-desktop$&defaultImage=Not_Available'
    st.image(picture, caption="Go get em' now at https://www.ballparkbrand.com/hot-dogs")

main()
