import mariadb

if __name__ == "__main__":
    try:
        conn = mariadb.connect(
            user="felipe",
            password="password",
            host="localhost",
            port=3306,
            database="Pinball"
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB platform: {e}")

