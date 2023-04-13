import streamlit as st
import pandas as pd
from database import ag1
from database import ag2

def aggr(optn):

    if optn == 1:
        result = ag1()
        df = pd.DataFrame(result, columns=['number'])
        with st.sidebar.expander("View number of staff members who live in SB Colony"):
            st.dataframe(df)

    if optn == 2:
        result = ag2()
        df = pd.DataFrame(result, columns=['number', 'flat_no'])
        with st.sidebar.expander("View number of visitors for each resident till date"):
            st.dataframe(df)