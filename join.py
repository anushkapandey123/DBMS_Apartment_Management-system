import streamlit as st
import pandas as pd
from database import j1
from database import j2
# from database import j3
def join(optn):
    if optn == 1:
        result = j1()
        df = pd.DataFrame(result, columns=['flat_no', 'name', 'fee'])
        with st.sidebar.expander("View parking area"):
            st.dataframe(df)


    # elif optn == 2:
    #     result = j2()
    #     df = pd.DataFrame(result, columns=['name', 'flat_no'])
    #     with st.sidebar.expander("View names"):
    #         st.dataframe(df)

    elif optn == 2:
        result = j2()
        df = pd.DataFrame(result, columns=['resident_name', 'visitor_name'])
        with st.sidebar.expander("View names"):
            st.dataframe(df)


    