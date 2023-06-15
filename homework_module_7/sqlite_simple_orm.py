import sqlite3


class SQLiteORM:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        self.cursor.execute(query)
        self.conn.commit()

    def insert_data(self, columns_names, table_name, data):
        query = f'INSERT INTO {table_name}{columns_names} VALUES ({data})'
        self.cursor.execute(query)
        self.conn.commit()

    def update_data(self, table_name, column, value, condition_column, condition_value):
        query = f"UPDATE {table_name} SET {column} = '{value}' WHERE {condition_column} = '{condition_value}'"
        self.cursor.execute(query)
        self.conn.commit()

    def delete_data(self, table_name, condition_column, condition_value):
        query = f"DELETE FROM {table_name} WHERE {condition_column} = '{condition_value}'"
        self.cursor.execute(query)
        self.conn.commit()

    def select_all(self, table_name):
        query = f'SELECT * FROM {table_name}'
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def select_by_key(self, table_name, key_column, key_value):
        query = f"SELECT * FROM {table_name} WHERE {key_column} = '{key_value}'"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    orm = SQLiteORM('my_db.db')

    orm.create_table('people', 'id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER')

    orm.insert_data(('name', 'age'), 'people', "'John', 15")
    orm.insert_data(('name', 'age'), 'people', "'Anna', 30")
    orm.insert_data(('name', 'age'), 'people', "'Maks', 20")
    orm.insert_data(('name', 'age'), 'people', "'Bob', 50")
    print(f'Added records to the database: {orm.select_all("people")}')

    orm.update_data('people', 'age', 70, 'name', 'John')
    print(f"An updated record of John: {orm.select_by_key('people', 'name', 'John')}")

    orm.delete_data('people', 'name', 'Anna')
    print(f'All records after deleting Anna\'s record: {orm.select_all("people")}')

    orm.close_connection()
