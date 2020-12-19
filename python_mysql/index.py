import mysql.connector

midb = mysql.connector.connect(
    host='localhost',
    user='jonu',
    password='jonulo321',
    database='prueba'
)

cursor = midb.cursor()

# INSERT NEW VALUES:
# sql = 'insert into Usuario (email, username, edad) values (%s, %s, %s)'
# values = ('newmail@mail.com', 'jonuulo', 24)

#UPDATE DATA:
# sql = 'update Usuario set email = %s where id = %s'
# values = ('jonuulo@gmail.com', 4)

# DELETE VALUES:
# sql = 'delete from Usuario where id = %s'
# values = (4,)

# ALWAY EXECUTE THIS LINE FOR CREATE AND UPDATE:
# cursor.execute(sql, values)

# FOR EVERY MODIFICATION TO THE DB:
# midb.commit()

# SEE THE INSERTION APLICATED:
# print(cursor.rowcount)

# CONSULT VALUES:

# cursor.execute('select * from Usuario')

# LIMIT RESPONSES FROM BD:
cursor. execute('select * from Usuario limit 2')

resultado = cursor.fetchall()

print(resultado)
