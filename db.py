import sqlite3
import bcrypt

class Database:
    def __enter__(self):
        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.commit()
        self.conn.close()


def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')


def verify_password(hashed_password, password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))


def insert_student(fd):
    with Database() as cursor:
        cursor.execute("""INSERT INTO students (
                        student_id, student_password, student_name, room_number, hostel_block, email)
                        VALUES (?, ?, ?, ?, ?, ?)""", (fd['student_id'], hash_password(fd['student_password']), fd['student_name'], fd['room_number'], fd['hostel_block'], fd['email']))

def insert_admin(fd):
    with Database() as cursor:
        cursor.execute("""insert into admins (
                        admin_name, admin_password, admin_hostel, admin_email)
                        VALUES (?, ?, ?, ?)""", (fd['admin_name'], hash_password(fd['admin_password']), fd['admin_hostel'], fd['admin_email'])
        )

def insert_complaint(fd, session):
    with Database() as cursor:
        cursor.execute("""INSERT INTO complaints (
                        student_id, complaint_type, complaint_text)
                        VALUES (?, ?, ?)""", (session['data']['student_id'], fd['complaint_type'], fd['complaint_text']))


def update_complaint_status(ID, status):
    with Database() as cursor:
        cursor.execute("""UPDATE complaints SET complaint_status = ? WHERE complaint_id = ?""", (status, ID))
        
        
def verify_admin(fd):
    with Database() as cursor:
        cursor.execute("""SELECT * FROM admins WHERE admin_hostel = ?""", (fd['admin_hostel'],))
        res = cursor.fetchone()
        if not res:
            return False
        return verify_password(res[2], fd['admin_password'])


def verify_student(fd):
    with Database() as cursor:
        cursor.execute("""SELECT * FROM students WHERE student_id = (?)""", (fd['student_id'],))
        res = cursor.fetchone()
        if not res:
            return False
        return verify_password(res[1], fd['student_password'])


def get_data(ID, who):
    if who == "student":
        with Database() as cursor:
            cursor.execute("""SELECT * FROM students WHERE student_id = (?)""", (ID,))
            res = cursor.fetchone()
            return {"student_id": res[0],
                    "name": res[2],
                    "hostel": res[4]}
    else:
        with Database() as cursor:
            cursor.execute("""SELECT * FROM admins WHERE admin_hostel = ?""", (ID,))
            res = cursor.fetchone()
            return {"name": res[1],
                    "hostel": res[3]}
            
            
def get_complaints(ID, who):
    if who == "student":
        with Database() as cursor:
            cursor.execute("SELECT * FROM complaints WHERE student_id = ?", (ID, ))
            return cursor.fetchall()
    else:
        with Database() as cursor:
            cursor.execute("SELECT * FROM complaints JOIN students WHERE hostel_block=?", (ID,))
            return cursor.fetchall()

def get_complaint(ID):
    with Database() as cursor:
        cursor.execute("SELECT * FROM complaints where complaint_id=?", (ID,))
        return cursor.fetchone()
