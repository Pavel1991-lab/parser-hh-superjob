import psycopg2



# Подключение к базе данных
conn = psycopg2.connect(database="vacansy",
                        user="pavel",
                        password="password",
                        host="localhost")
cur = conn.cursor()

employer_addresses = name_adress

for employer_info in employer_addresses:
    employer_name = employer_info['employer_name']
    employer_address = employer_info['employer_address']

    # Формирование SQL-запроса для вставки данных
    sql = "INSERT INTO employers (name, address) VALUES (%s, %s)"

    # Выполнение SQL-запроса с передачей данных
    cur.execute(sql, (employer_name, employer_address))

# Фиксация изменений и закрытие соединения
conn.commit()
cur.close()
conn.close()