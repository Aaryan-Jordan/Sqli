from passlib.hash import bcrypt
from sqlite3 import connect

u = input("Enter username : ")
password = input("Enter password : ")
hashed_password = bcrypt.hash(password)

print(hashed_password)

conn = connect('l3.db')
# add password_has to the field where username is equal to u
c = conn.cursor()
c.execute("UPDATE cred SET password_hash=? WHERE username=?", (hashed_password, u))
conn.commit()
conn.close()
print("Password updated successfully")
