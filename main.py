import psycopg2

if __name__ == "__main__":
    try:
        conn = psycopg2.connect(
            user="felipe",
            password="password",
            host="postgresdocker",
            port=5432,
            database="DockerDB"
        )
    except psycopg2.Error as error:
        print(f"Error connecting to PostgreSQL platform: {error}")

    cur = conn.cursor()
    for i in range(1,7):
        cur.execute(f"INSERT INTO numbers (number) VALUES ({i})")
    conn.commit()
    cur.execute("SELECT * FROM numbers")
    for id, number in cur:
        print(f"id: {id}, number: {number}")
    cur.close()
    conn.close()