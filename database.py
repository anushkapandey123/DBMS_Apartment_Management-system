import pandas as pd

import mysql.connector 
mydb = mysql.connector.connect(
 host="database-1.cvh9tyrvaj5s.eu-north-1.rds.amazonaws.com", 
 user="admin", 
 password="anushka123", 
 database="database1",
 port=3306
)

c = mydb.cursor()

# --------------------------------ADD--------------------------------
def add_data_flat(flat_no, bhk, owner, square_feet): #, dest, available): 
    c.execute('INSERT INTO flat(flat_no, bhk, owner, square_feet) VALUES (%s,%s,%s,%s)',(flat_no, bhk, owner, square_feet))
    mydb.commit()

def add_data_residents(flat_no, name, gender, email, dob, mobile_no, bhk, vn): #, dest, available): 
    c.execute('INSERT INTO residents(flat_no, name, gender, email, dob, mobile_no, bhk, vn) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',(flat_no, name, gender, email, dob, mobile_no, bhk, vn))
    mydb.commit()

def add_data_staff(name, address, date_of_joining, staff_id, flat_no, salary):
    c.execute('INSERT INTO staff(name, address, date_of_joining, staff_id, flat_no, salary) VALUES (%s,%s,%s,%s,%s,%s)',(name, address, date_of_joining, staff_id, flat_no, salary))
    mydb.commit()

def add_data_parking(flat_no, resident_vn):
    c.execute('INSERT INTO parking(flat_no, resident_vn) VALUES (%s,%s)', (flat_no, resident_vn))
    mydb.commit()

def add_data_visitors(flat_no, name, date_of_visit, phone_no, vehicle_number):
    c.execute('INSERT INTO visitors(flat_no, name, date_of_visit, phone_no, vehicle_number) VALUES (%s,%s,%s,%s,%s)', (flat_no, name, date_of_visit, phone_no, vehicle_number))
    mydb.commit()

# ----------------------------VIEW----------------------------

def view_all_data(choice):
    if choice == 1:
        c.execute('SELECT * FROM flat') 
        data = c.fetchall()
        return data
    elif choice == 2:
        c.execute('SELECT * FROM residents') 
        data = c.fetchall()
        return data
    elif choice == 3:
        c.execute('SELECT * FROM parking') 
        data = c.fetchall()
        return data
    elif choice == 4:
        c.execute('SELECT * FROM staff') 
        data = c.fetchall()
        return data
    else:
        c.execute('SELECT * FROM visitors') 
        data = c.fetchall()
        return data

def view_only_flat_no(): 
    c.execute('SELECT flat_no FROM flat') 
    data = c.fetchall()
    return data

def view_only_staff_id(): 
    c.execute('SELECT staff_id FROM staff') 
    data = c.fetchall()
    return data

def view_only_staff_doj():
    c.execute('SELECT date_of_joining from staff')
    data = c.fetchall()
    return data

def view_from_backup():
    c.execute('SELECT * from backup_record')
    data = c.fetchall()
    return data

def find_vacant_flats(apartment_type):
    c.execute('SELECT flat_no from flat where owner="null" and bhk="{}"'.format(apartment_type))
    data = c.fetchall()
    return data

def view_vacant_flats(flat_no):
    c.execute('SELECT * from flat where flat_no=%s', (flat_no))
    data = c.fetchall()
    return data

def find_vacant_flats_staff():
    c.execute('SELECT flat_no from flat where owner')
    data = c.fetchall()
    return data


# ------------------------------DELETION-------------------------------

def delete_data_flat(flat_no): 
    c.execute('DELETE FROM flat WHERE flat_no="{}"'.format(flat_no)) 
    mydb.commit()

def delete_data_residents(flat_no): 
    c.execute('DELETE FROM residents WHERE flat_no="{}"'.format(flat_no)) 
    mydb.commit()

# def delete_data_parking(flat_no): 
#     c.execute('DELETE FROM parking WHERE flat_no="{}"'.format(flat_no)) 
#     mydb.commit()

def delete_visitors(flat_no): 
    c.execute('DELETE FROM visitors WHERE (DATEDIFF(year, date_of_visit, SYSDATE())) > 1') 
    mydb.commit()

def delete_visitors(): 
    c.execute('DELETE FROM visitors') 
    mydb.commit()

def delete_data_staff_on_flat_no(flat_no): 
    c.execute('DELETE FROM staff WHERE flat_no="{}"'.format(flat_no)) 
    mydb.commit()

def delete_data_staff_on_staff_id(staff_id): 
    c.execute('DELETE FROM staff WHERE staff_id="{}"'.format(staff_id)) 
    mydb.commit()


# -----------------------------UPDATE---------------------------
def edit_resident_data(new_flat_no, new_name, new_gender, new_email, new_dob, new_mobile_no, new_bhk, new_vn, flat_no):
    # c.execute('UPDATE residents SET flat_no="{}", name="{}", gender="{}", email="{}", dob="{}", mobile_no="{}", bhk="{}", vn="{}" WHERE flat_no="{}" and name="{}" and gender="{}" and email="{}" and dob="{}" and mobile_no="{}" and bhk="{}" and vn="{}"'.format(new_flat_no, new_name, new_gender, new_email, new_dob, new_mobile_no, new_bhk, new_vn, flat_no, name, gender, email, dob, mobile_no, bhk, vn))
    c.execute('UPDATE residents SET flat_no="{}", name="{}", gender="{}", email="{}", dob="{}", mobile_no="{}", bhk="{}", vn="{}" WHERE flat_no="{}"'.format(new_flat_no, new_name, new_gender, new_email, new_dob, new_mobile_no, new_bhk, new_vn, flat_no)) #, name, gender, email, dob, mobile_no, bhk, vn)) 
    mydb.commit()
    data = c.fetchall()
    return data

def edit_staff_data(new_name, new_address, new_date_of_joining, new_staff_id, new_flat_no, new_salary, name, address, date_of_joining, staff_id, flat_no, salary): 
    c.execute('UPDATE staff SET name="{}", address="{}", date_of_joining="{}", staff_id="{}", flat_no="{}", salary="{}" WHERE name="{}" and address="{}" and date_of_joining="{}" and staff_id="{}" and flat_no="{}" and salary="{}"'.format(new_name, new_address, new_date_of_joining, new_staff_id, new_flat_no, new_salary, name, address, date_of_joining, staff_id, flat_no, salary)) 
    mydb.commit()
    data = c.fetchall()
    return data

def edit_parking_data(new_flat_no, new_resident_vn, flat_no, resident_vn,):
    c.execute('UPDATE parking set flat_no=%s, resident_vn=%s WHERE flat_no=%s and resident_vn=%s', (new_flat_no, new_resident_vn, flat_no, resident_vn))
    mydb.commit()
    data = c.fetchall()
    return data

def update_parking(flat_no,new_vn):
    c.execute('UPDATE parking set resident_vn=%s WHERE flat_no=%s', (new_vn, flat_no))
    mydb.commit()
    data = c.fetchall()
    return data

def update_parking_leave(flat_no):
    c.execute('UPDATE parking set resident_vn=%s,fee=%s WHERE flat_no=%s',("null", 0.0000, flat_no))
    mydb.commit()
    data = c.fetchall()
    return data


def get_resident_data(flat_no):
    c.execute('SELECT * FROM residents WHERE flat_no = "{}"'.format(flat_no))
    data = c.fetchall()
    return data

def get_staff_data(staff_id):
    c.execute('SELECT * FROM staff WHERE staff_id = "{}"'.format(staff_id))
    data = c.fetchall()
    return data

def get_parking_data(flat_no):
    c.execute('SELECT * FROM parking WHERE flat_no = "{}"'.format(flat_no))
    data = c.fetchall()
    return data

# def update_parking(flat_no, vvn):
#     c.execute('UPDATE parking SET visitor_vn =%s WHERE flat_no =%s', (vvn, flat_no))
#     mydb.commit()

def update_staff(flat_no, temp):
    c.execute('UPDATE staff SET flat_no =%s WHERE flat_no =%s', (temp, flat_no))
    mydb.commit()

def update_data_flat(flat_no):
    c.execute('UPDATE flat SET owner =%s WHERE flat_no =%s', ("null", flat_no))
    mydb.commit()

def insert_data_flat(name, flat_no):
    c.execute('UPDATE flat SET owner =%s WHERE flat_no =%s', (name, flat_no))
    mydb.commit()

def set_maintainence_fee(flat_no,no_vehicle):
    if no_vehicle == "1":
        c.execute('UPDATE parking SET fee =%s WHERE flat_no =%s', ("1000", flat_no))
        mydb.commit()

    elif  no_vehicle == "2":
        c.execute('UPDATE parking SET fee =%s WHERE flat_no =%s', ("2000", flat_no))
        mydb.commit()

    else:
        c.execute('UPDATE parking SET fee =%s WHERE flat_no =%s', ("3000", flat_no))
        mydb.commit()


    











#-----------------------------JOIN-------------------------------
def j1():
    c.execute('SELECT p.flat_no, name, fee from parking as p join residents as r on p.flat_no = r.flat_no')
    data = c.fetchall()
    return data

# def j2():
#     c.execute('SELECT distinct(name), s.flat_no from staff as s join parking as p on s.staff_id = p.staff_id')
#     data = c.fetchall()
#     return data

def j2():
    c.execute('SELECT distinct(owner), name from flat as f join visitors as v on f.flat_no = v.flat_no')
    data = c.fetchall()
    return data

# def j3():
#     c.execute('SELECT distinct(owner), name from flat as f join visitors as v on f.flat_no = v.flat_no')
#     data = c.fetchall()
#     return data


def ag1():
    c.execute('SELECT count(name) from staff where address like "%SB Colony"')
    data = c.fetchall()
    return data

def ag2():
    c.execute('SELECT count(flat_no), flat_no from visitors group by flat_no order by count(flat_no) desc')
    data = c.fetchall()
    return data


def pro():
    # c.execute('CALL update_sal_final()')
    # mydb.commit()
    c.callproc('update_sal_final', [])
    df = pd.DataFrame()
    for result in c.stored_results():
        temp_df = pd.DataFrame(result.fetchall())

    return df











    
# def view_all_data2(): 
    
# def view_all_data3(): 
    
# def view_all_data4(): 
    
# def view_all_data5(): 
    