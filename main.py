import bcrypt
import base64

passwd = input("Type a password: ").encode('utf-8')
passwd2 = input("Type the password again: ").encode('utf-8')
salty = bcrypt.gensalt(10)
hashed = bcrypt.hashpw(passwd, salty)
sixtyfour = base64.b64encode(hashed)

if bcrypt.checkpw(passwd2, hashed):
  print(f"""Password is correct! 
  The hashed password is: {hashed.decode("utf-8")} 
  The salt is: {salty.decode("utf-8")}
  The hashed password base64 encoded: {sixtyfour.decode("utf-8")}
  """)
else:
  print("Password is incorrect")