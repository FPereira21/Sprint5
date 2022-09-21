import numbers
import mariadb

if __name__ == "__main__":
    try:
        conn = mariadb.connect(
            user="felipe",
            password="password",
            host="172.18.0.1",
            port=3307,
            database="DockerDB"
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB platform: {e}")

    cur = conn.cursor()
    for i in range(1,7):
        cur.execute(f"INSERT INTO numbers (number) VALUES ({i})")
    conn.commit()
    cur.execute("SELECT * FROM numbers")
    for id, number in cur:
        print(f"id: {id}, number: {number}")
    conn.close()