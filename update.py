import pandas as pd
import streamlit as st
from database import view_all_data, get_resident_data, get_staff_data, edit_resident_data, edit_staff_data,view_only_flat_no, view_only_staff_id, get_parking_data, edit_parking_data, update_parking, set_maintainence_fee

def update(sub_choice):

    if sub_choice == "Residents":
        result_resi = view_all_data(2)
        df = pd.DataFrame(result_resi, columns=['flat_no', 'name', 'gender', 'email', 'dob', 'mobile_no', 'bhk', 'vn'])
        with st.expander("Current Residents"):
            st.dataframe(df)
        list_of_flat = [i[0] for i in view_only_flat_no()]
        selected_flat = st.selectbox("Resident to Edit", list_of_flat)
        selected_result = get_resident_data(selected_flat)
        if selected_result:
            flat_no = selected_result[0][0]
            new_flat_no = selected_result[0][0]
            name = selected_result[0][1]
            new_name = selected_result[0][1]
            gender = selected_result[0][2]
            new_gender = selected_result[0][2]
            email = selected_result[0][3]
            dob = selected_result[0][4]
            new_dob = selected_result[0][4]
            mobile_no = selected_result[0][5]
            bhk = selected_result[0][6]
            new_bhk = selected_result[0][6]
            vn = selected_result[0][7]
            new_vn = selected_result[0][7] 

            col1, col2 = st.columns(2)
            with col1:
                # new_name = st.text_input("name:", name)
                new_email = st.text_input("email:", email)
                new_vn = st.selectbox("No. of vehicles:", ["1", "2", "3"]) 
            with col2:
                # new_date_of_joining = st.text_input("Doj:", date_of_joining)
                # new_source = st.text_input("Source:", source)
                new_mobile_no = st.text_input("Mobile No:", mobile_no)
                # new_salary = st.text_input("Salary:", salary)

            if st.button("Update Resident"):
                edit_resident_data(new_flat_no, new_name, new_gender, new_email, new_dob, new_mobile_no, new_bhk, new_vn,flat_no)
                st.success("Successfully updated") #:: {} to ::{}".format(train_name, new_train_name))
        update_parking(flat_no, new_vn)
        set_maintainence_fee(flat_no, new_vn)
        result1 = view_all_data(2)
        df1 = pd.DataFrame(result1, columns=['flat_no', 'name', 'gender', 'email', 'dob', 'mobile_no', 'bhk', 'vn'])
        with st.expander("Updated data:"):
            st.dataframe(df1)




    if sub_choice == "Staff":
        result_staff = view_all_data(4)
        df = pd.DataFrame(result_staff, columns=['name', 'address', 'date_of_joining', 'staff_id', 'flat_no', 'salary'])
        with st.expander("Current Staff"):
            st.dataframe(df)
        list_of_staff = [i[0] for i in view_only_staff_id()]
        selected_staff = st.selectbox("Staff to Edit", list_of_staff)
        selected_result1 = get_staff_data(selected_staff)
        if selected_result1:
            name = selected_result1[0][0]
            address = selected_result1[0][1]
            date_of_joining = selected_result1[0][2]
            staff_id = selected_result1[0][3]
            new_staff_id = selected_result1[0][3]
            flat_no = selected_result1[0][4]
            salary = selected_result1[0][5]
            new_name = selected_result1[0][0]
            new_date_of_joining = selected_result1[0][2]

            col1, col2 = st.columns(2)
            with col1:
                # new_name = st.text_input("name:", name)
                new_address = st.text_input("add:", address)
            with col2:
                # new_date_of_joining = st.text_input("Doj:", date_of_joining)
                # new_source = st.text_input("Source:", source)
                new_flat_no = st.text_input("Flat No:", flat_no)
                new_salary = st.text_input("Salary:", salary)

            if st.button("Update Staff"):
                edit_staff_data(new_name, new_address, new_date_of_joining, new_staff_id, new_flat_no, new_salary, name, address, date_of_joining, staff_id, flat_no, salary)
                st.success("Successfully updated") #:: {} to ::{}".format(train_name, new_train_name))
        result2 = view_all_data(4)
        df2 = pd.DataFrame(result2, columns=['name', 'address', 'date_of_joining', 'staff_id', 'flat_no', 'salary'])
        with st.expander("Updated data:"):
            st.dataframe(df2)


    # elif sub_choice == "Parking":
    #     # result_staff = view_all_data(3)
    #     # df = pd.DataFrame(result_staff, columns=['name', 'address', 'date_of_joining', 'staff_id', 'flat_no', 'salary'])
    #     # with st.expander("Current Status"):
    #     #     st.dataframe(df)
        
    #     list_of_staff = [i[0] for i in view_only_flat_no()]
    #     selected_staff = st.selectbox("Flat to Edit", list_of_staff)
    #     selected_result = get_parking_data(selected_staff)
    #     if selected_result:
    #         flat_no = selected_result[0][0]
    #         resident_vn = selected_result[0][1]
    #         visitor_vn = selected_result[0][2]
    #         # staff_id = selected_result[0][3]
    #         # new_staff_id = selected_result[0][3]
    #         new_flat_no = selected_result[0][0]
    #         # salary = selected_result[0][5]
    #         # new_flat_no = selected_result[0][0]
    #         # new_date_of_joining = selected_result[0][2]

    #         col1, col2 = st.columns(2)
    #         with col1:
    #             # new_name = st.text_input("name:", name)
    #             new_resident_vn = st.text_input("rvn:", resident_vn)
    #         with col2:
    #             # new_date_of_joining = st.text_input("Doj:", date_of_joining)
    #             # new_source = st.text_input("Source:", source)
    #             new_visitor_vn = st.text_input("vvn:", visitor_vn)
    #             # new_salary = st.text_input("Salary:", salary)

    #         if st.button("Update details"):
    #             edit_parking_data(new_flat_no, new_resident_vn, new_visitor_vn, flat_no, resident_vn, visitor_vn)#, name, address, date_of_joining, staff_id, flat_no, salary)
    #             st.success("Successfully updated") #:: {} to ::{}".format(train_name, new_train_name))
    #     result2 = view_all_data(3)
    #     df2 = pd.DataFrame(result2, columns=['flat_no', 'resident_vn', 'visitor_vn']) #, 'staff_id', 'flat_no', 'salary'])
    #     with st.expander("Updated data:"):
    #         st.dataframe(df2)





