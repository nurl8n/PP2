import psycopg2

# connection to db
conn = psycopg2.connect(database="pp2demo", user="pp2user", password="123", host="127.0.0.1", port="5432")
# create a cursor
cursor = conn.cursor()
# client side cursor, like querying
# server side cursor

# # create a table
# cursor.execute('''CREATE TABLE companies
#       (ID VARCHAR(50) NOT NULL,
#       NAME VARCHAR(50) NOT NULL,
#       RATING INT NOT NULL,
#       ADDRESS CHAR(50));''')
#
# # inserting data
# cursor.execute("insert into companies (ID, NAME, RATING, ADDRESS) values ('1', 'Kaspi', '10', 'Almaty')")
# cursor.execute("insert into companies (ID, NAME, RATING, ADDRESS) values ('2', 'Dar', '8', 'Astana')")
# cursor.execute("insert into companies (ID, NAME, RATING, ADDRESS) values ('3', 'Alfabank', '8', 'Moscow')")
# cursor.execute("insert into companies (ID, NAME, RATING, ADDRESS) values ('4', 'Google', '10', 'California')")
# cursor.execute("insert into companies (ID, NAME, RATING, ADDRESS) values ('5', 'Tesla', '10', 'California')")
# cursor.execute("insert into companies (ID, NAME, RATING, ADDRESS) values ('6', 'KaspiNewCopyPaste', '5', 'Taldykorgan')")
# cursor.execute("insert into companies (ID, NAME, RATING, ADDRESS) values ('7', 'SomeNoNameCompany', '3', 'KZMZ')")

# # execute query
# cursor.execute("select * from companies")
# for r in rows:
#     print(f"{r[0]} {r[1]} {r[2]} {r[3]}")

# cursor.execute("select * from companies WHERE RATING>=8")
# rows = cursor.fetchall()
# for r in rows:
#     print(f"{r[0]} {r[1]} {r[2]} {r[3]}")

# cursor.execute("select NAME, RATING from companies")
# rows = cursor.fetchall()
# for r in rows:
#     print(f"{r[0]} {r[1]}")

# cursor.execute("select * from companies where ADDRESS='California'")
# rows = cursor.fetchall()
# for r in rows:
#     print(f"{r[0]} {r[1]} {r[2]} {r[3]}")

# cursor.execute("select * from companies where NAME like 'Kas%'")
# rows = cursor.fetchall()
# for r in rows:
#     print(f"{r[0]} {r[1]} {r[2]} {r[3]}")

# cursor.execute("select * from companies where ADDRESS in ('Almaty', 'California')")
# rows = cursor.fetchall()
# for r in rows:
#     print(f"{r[0]} {r[1]} {r[2]} {r[3]}")

# cursor.execute("select * from companies where RATING between 2 and 7")
# rows = cursor.fetchall()
# for r in rows:
#     print(f"{r[0]} {r[1]} {r[2]} {r[3]}")

cursor.execute("select * from companies ORDER BY RATING DESC")
rows = cursor.fetchall()
for r in rows:
    print(f"{r[0]} {r[1]} {r[2]} {r[3]}")

# changes
# cursor.execute("update companies set ADDRESS='AlmatyChanged' where NAME='Dar'")
# cursor.execute("select * from companies")
# rows = cursor.fetchall()
# for r in rows:
#     print(f"{r[0]} {r[1]} {r[2]} {r[3]}")

# cursor.execute("update companies set name='HalykBank' where id='7'")
# cursor.execute("select * from companies")
# rows = cursor.fetchall()
# for r in rows:
#     print(f"{r[0]} {r[1]} {r[2]} {r[3]}")

# cursor.execute("delete from companies WHERE id='5'")
# cursor.execute("select * from companies")
# rows = cursor.fetchall()
# for r in rows:
#     print(f"{r[0]} {r[1]} {r[2]} {r[3]}")

# cursor.execute("delete from companies WHERE RATING<5")
# cursor.execute("select * from companies")
# rows = cursor.fetchall()
# for r in rows:
#     print(f"{r[0]} {r[1]} {r[2]} {r[3]}")

# cursor.execute("DROP DATABASE [IF EXISTS] pp2demo")

# cursor.execute("DROP TABLE IF EXISTS companies, students")



# committing the changes
conn.commit()

# close the cursor
cursor.close()
# close the connection
conn.close()

print("Opened database successfully")
