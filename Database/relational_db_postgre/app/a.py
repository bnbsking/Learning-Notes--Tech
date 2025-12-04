import psycopg

conn = psycopg.connect(
    host="db",  # Docker Compose 服务名
    dbname="mydb",
    user="myuser",
    password="mypassword"
)

cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name VARCHAR(50), age INT)")
cur.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Alice", 25))
conn.commit()

cur.execute("SELECT * FROM users")
print(cur.fetchall())

cur.close()
conn.close()
