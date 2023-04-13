import streamlit as st
import mysql.connector

from read import read
from create import create
from delete import delete
from join import join
from aggr import aggr
from update import update
from database import pro
from trig import foo

def main():
    # def add_bg_from_url():
    #     st.markdown(
    #         f"""
    #         <style>
    #         .stApp {{
    #             background-image: url("https://img.freepik.com/free-vector/bookshop-background-design_1212-306.jpg");
    #             background-attachment: fixed;
    #             background-size: cover
    #         }}
    #         </style>
    #         """,
    #         unsafe_allow_html=True
    #     )

    # with st.container():
    #     # add_bg_from_url()
        st.markdown(f'<h1 style="color:#E0144C;font-size:40px;border-radius:2%;text-align:center;">Platinum Apartments</h1>', unsafe_allow_html=True)
        
        menu = ["Main", "Insert", "View", "Edit", "Delete"]
        
        choice = st.sidebar.selectbox("Menu", menu)
        # st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRo0IK-8w2N5v7_sXsFblitiG40KYtv0oUB0w&usqp=CAU", use_column_width='always')
        # create_table()
        if choice == "Main":
            st.markdown(f'<h3 style="text-align:center;color:#E97777;">This is the best apartment in Bengaluru<h3>', unsafe_allow_html=True)
            st.markdown(f'<h4 style="text-align:center;color:#E97777;">To start with, we are moving towards the culture of nuclear families where most adults work. Life is more stressful than ever and people have less time on hand. Given these circumstances, it is much easier to manage an apartment than an independent house.</h4>', unsafe_allow_html=True)
            
        if choice == "Insert":
            sub_menu = ["Residents", "Staff", "Visitors"]
            sub_choice = st.selectbox("Sub_menu", sub_menu)
            st.subheader("Enter details:")
            create(sub_choice)
        if choice == "View":
            st.subheader("View the table")
            read()
        elif choice == "Edit":
            sub_menu = ["Residents", "Staff"]
            sub_choice = st.selectbox("Sub_menu", sub_menu)
            st.subheader("Update the table")
            update(sub_choice)
        elif choice == "Delete":
            sub_menu = ["Flat", "Staff", "Delete visitor data older than 1 year"]
            sub_choice = st.selectbox("Sub_menu", sub_menu)
            st.subheader("Delete the details")
            delete(sub_choice)

        menu = ["View Join Results", "Join1", "Join2"] #, "Join3", "Join4"]
        choice = st.sidebar.selectbox("Join", menu)

        if choice == "Join1":
            join(1)

        if choice == "Join2":
            join(2)

        # if choice == "Join3":
        #     join(3)

        menu = ["View Aggregate Results", "Aggr1", "Aggr2"]
        choice = st.sidebar.selectbox("Aggregate", menu)

        if choice == "Aggr1":
            aggr(1)

        if choice == "Aggr2":
            aggr(2)

        menu = ["Use Procedure", "Procedure"]
        choice = st.sidebar.selectbox("View Procedure", menu)

        if choice == "Procedure":
            pro()


        menu = ["Use Trigger","Trigger"]
        choice = st.sidebar.selectbox("Trigger", menu)

        if choice == "Trigger":
            foo()
            


            
    # else:
    #     st.subheader("About tasks")
if __name__ == '__main__':
    main()