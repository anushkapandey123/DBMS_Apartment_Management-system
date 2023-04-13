import streamlit as st
import pandas as pd
from database import add_data_residents
from database import add_data_flat
from database import add_data_staff
# from database import update_data_parking
from database import view_all_data, add_data_visitors, update_parking, find_vacant_flats, find_vacant_flats_staff, insert_data_flat, view_vacant_flats, set_maintainence_fee

def create(sub_choice):
    col1, col2 = st.columns(2)
    # if sub_choice == "Flat":
    #     with col1:
    #         flat_no = st.text_input("Flat_No:")
    #         bhk = st.text_input("BHK:")
    #     with col2:
    #         owner = st.text_input("Owner:")
    #         square_feet = st.selectbox("Square Feet", ["200", "300", "400"])
    #     if st.button("Add"):
    #         add_data_flat(flat_no, bhk, owner, square_feet)
    #         st.success("Successfully added the train details: {}".format(flat_no))

    if sub_choice == "Residents":
        with col1:
            
            
            name = st.text_input("name:")
            gender = st.selectbox("Gender", ["F", "M"])
            no_vehicle = st.selectbox("Number", ["1", "2", "3"])
            
            # if no_vehicle == "1":
            #     vn1 = st.text_input("vn1:")
            # elif no_vehicle == "2":
            #     vn1 = st.text_input("vn1:")
            #     vn2 = st.text_input("vn2:")
            # else:
            #     vn1 = st.text_input("vn1:")
            #     vn2 = st.text_input("vn2:")
            #     vn3 = st.text_input("vn3:")
        with col2:
            email = st.text_input("email:")
            dob = st.text_input("DOB:")
            mobile_no = st.text_input("Mobile No:")
            apartment_type = st.text_input("BHK:")
        

            vacant_flats = find_vacant_flats(apartment_type)
            st.text("Vacant flats")
            for i in vacant_flats:
                    st.text(i)

            flat_no = st.text_input("Flat_No:")
            set_maintainence_fee(flat_no, no_vehicle)
            
        if st.button("Add"):
            if apartment_type == "2-BHK":
                square_feet = 200
                # check whether flat is vacant or not
               
                
                insert_data_flat(name, flat_no) #, apartment_type, name, square_feet)
            elif apartment_type == "3-BHK":
                square_feet = 300
                
                insert_data_flat(name, flat_no) #, apartment_type, name, square_feet)
            else:
                square_feet = 400
                # check whether flat is vacant or not
                
                insert_data_flat(name, flat_no) #, apartment_type, name, square_feet)
            
            update_parking(flat_no, no_vehicle)
            set_maintainence_fee(flat_no, no_vehicle)
            add_data_residents(flat_no, name, gender, email, dob, mobile_no, apartment_type,no_vehicle)
            st.success("Successfully added the resident details: {}".format(flat_no))

    
    elif sub_choice == "Staff" :
        with col1:
            name = st.text_input("Name:")
            address = st.text_input("ADDR:")
            salary = st.text_input("Salary:")
        with col2:
            date_of_joining = st.text_input("Doj:")
            staff_id = st.text_input("staff id:")

        if st.button("View current status"):
            result1 = view_all_data(1)
            df = pd.DataFrame(result1, columns=['flat_no', 'bhk', 'owner', 'square_feet'])
            with st.expander("View all available apartments"):
                st.dataframe(df)
            
            flat_no = st.text_input("Flat No:")
        if st.button("Add"):
            add_data_staff(name, address, date_of_joining, staff_id, flat_no, salary)
            st.success("Successfully added the staff details: {}".format(flat_no))

    
        
    
    elif sub_choice == "Visitors":
        with col1:
            flat_no = st.text_input("Flat Name:")
            name = st.text_input("Name:")
        with col2:
            date_of_visit = st.text_input("Dov:")
            vehicle_number = st.text_input("vehicle num:")
            phone_no = st.text_input("phone num:")
        if st.button("Add"):
            add_data_visitors(flat_no, name, date_of_visit, phone_no, vehicle_number)
            # find resident vehicle number
            # update_parking(flat_no, vehicle_number)
            # add_data_parking(flat_no, resident_vn, vehicle_number)
            st.success("Successfully added the visitor details: {}".format(flat_no))

        


