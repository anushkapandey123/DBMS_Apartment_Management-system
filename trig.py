from database import view_from_backup
from delete import *

def foo():
    delete("Flat")
    new_result_trig = view_from_backup()
    df = pd.DataFrame(new_result_trig, columns=['flat_no', 'name', 'gender', 'email', 'dob', 'mobile_no', 'bhk', 'vn'])
    with st.sidebar.expander("Updated data"):
        st.dataframe(df)