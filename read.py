import pandas as pd
import streamlit as st
from database import view_all_data



def read():
    result1 = view_all_data(1)
    df = pd.DataFrame(result1, columns=['flat_no', 'bhk', 'owner', 'square_feet'])
    with st.expander("View all available apartments"):
        st.dataframe(df)

    result2 = view_all_data(2)
    df = pd.DataFrame(result2, columns=['flat_no', 'name', 'gender', 'email', 'dob', 'mobile_no', 'bhk', 'vn'])
    with st.expander("View all residents"):
        st.dataframe(df)

    result3 = view_all_data(3)
    df = pd.DataFrame(result3, columns=['flat_no', 'resident_vn', 'fee'])
    with st.expander("View parking area"):
        st.dataframe(df)

    result4 = view_all_data(4)
    df = pd.DataFrame(result4, columns=['name', 'address', 'date_of_joining', 'staff_id', 'flat_no', 'salary'])
    with st.expander("View all the staff members"):
        st.dataframe(df)

    result5 = view_all_data(5)
    df = pd.DataFrame(result5, columns=['flat_no', 'name', 'date_of_visit', 'phone_no', 'vehicle_number'])
    with st.expander("View all the visitors"):
        st.dataframe(df)
