import pandas as pd
import streamlit as st
from database import view_all_data, delete_data_staff_on_flat_no, delete_data_staff_on_staff_id, delete_data_flat,delete_data_residents, view_only_flat_no, view_only_staff_id, update_staff, update_data_flat, update_parking_leave, delete_visitors

def delete(sub_choice):

    if sub_choice == "Flat":

        result = view_all_data(1)
        df = pd.DataFrame(result, columns=['flat_no', 'bhk', 'owner', 'square_feet'])
        with st.expander("Current data"):
            st.dataframe(df)
            list_of_flats = [i[0] for i in view_only_flat_no()]
            selected_flat = st.selectbox("Flat to delete", list_of_flats)
            st.warning("Do you want to delete ::{}".format(selected_flat))
        if st.button("Delete resident entry"):
            # delete_data_parking(selected_flat)
            # delete_data_staff_on_flat_no(selected_flat)
            # delete_data_visitors(selected_flat)
            # delete_data_residents(selected_flat)
            temp = "null"
            update_staff(selected_flat, temp)
            update_data_flat(selected_flat)
            update_parking_leave(selected_flat)
            delete_data_residents(selected_flat)

            
            
            st.success("Flat has been vacated successfully")


        new_result1 = view_all_data(1)
        new_result2 = view_all_data(2)
        df2 = pd.DataFrame(new_result1, columns=['flat_no', 'bhk', 'owner', 'square_feet'])
        df3 = pd.DataFrame(new_result2, columns=['flat_no', 'name', 'gender', 'email', 'dob', 'mobile_no', 'bhk', 'vn'])
        with st.expander("Updated data"):
            st.dataframe(df2) 
            st.dataframe(df3)


    if sub_choice == "Staff":

        result = view_all_data(4)
        df = pd.DataFrame(result, columns=['name', 'address', 'date_of_joining', 'staff_id', 'flat_no', 'salary'])
        with st.expander("Current data"):
            st.dataframe(df)
            list_of_staff = [i[0] for i in view_only_staff_id()]
            selected_staff = st.selectbox("Task to delete", list_of_staff)
            st.warning("Do you want to delete ::{}".format(selected_staff))
        if st.button("Delete resident entry"):
            # delete_data_parking(selected_staff)
            delete_data_staff_on_staff_id(selected_staff)
            
            
            
            st.success("Staff has been deleted successfully")


        new_result1 = view_all_data(4)
        
        df2 = pd.DataFrame(new_result1, columns=['name', 'address', 'date_of_joining', 'staff_id', 'flat_no', 'salary'])
        # df3 = pd.DataFrame(new_result2, columns=['flat_no', 'name', 'gender', 'apartment_type', 'dob', 'mobile_no', 'vn'])
        with st.expander("Updated data"):
            st.dataframe(df2) 
            # st.dataframe(df3)

    
    if sub_choice == "Delete visitor data older than 1 year":
        st.warning("Do you want to delete the visitor entry")
        if st.button("Delete visitor entry"):
            delete_visitors()
            st.success("Visitors deleted")
        new_result1 = view_all_data(5)
        
        df2 = pd.DataFrame(new_result1, columns=['flat_no', 'name', 'date_of_visit', 'phone_no', 'vehicle_number'])
        # df3 = pd.DataFrame(new_result2, columns=['flat_no', 'name', 'gender', 'apartment_type', 'dob', 'mobile_no', 'vn'])
        with st.expander("Updated data"):
            st.dataframe(df2)


