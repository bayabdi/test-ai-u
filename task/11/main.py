import sqlite3

class EmployeeDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                salary REAL NOT NULL
            )
        ''')
        self.conn.commit()

    def add_employee(self, name, salary):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO Employees (name, salary) VALUES (?, ?)
        ''', (name, salary))
        self.conn.commit()

    def get_employees(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM Employees')
        return cursor.fetchall()

    def get_employee(self, employee_id):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM Employees WHERE id = ?', (employee_id,))
        return cursor.fetchone()

    def update_employee(self, employee_id, name, salary):
        cursor = self.conn.cursor()
        cursor.execute('''
            UPDATE Employees SET name = ?, salary = ? WHERE id = ?
        ''', (name, salary, employee_id))
        self.conn.commit()

    def delete_employee(self, employee_id):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM Employees WHERE id = ?', (employee_id,))
        self.conn.commit()

    def close_connection(self):
        self.conn.close()

# Пример использования:
if __name__ == "__main__":
    db = EmployeeDatabase("employee_database.db")

    # Добавить сотрудников
    db.add_employee("Petr I", 50000.0)
    db.add_employee("Captain Price", 60000.0)

    # Отображение всех сотрудников
    print("Все сотрудники:")
    employees = db.get_employees()
    for employee in employees:
        print(employee)

    # Обновление сотрудника
    db.update_employee(1, "Petr II", 55000.0)

    # Отображение конкретного сотрудника
    print("\nСотрудник с удостоверением личности 1:")
    print(db.get_employee(1))

    # Удалить сотрудника
    db.delete_employee(2)

    # Отображение всех сотрудников после удаления
    print("\nВсе сотрудники после удаления:")
    employees = db.get_employees()
    for employee in employees:
        print(employee)

    db.close_connection()
