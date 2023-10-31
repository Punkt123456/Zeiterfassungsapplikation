import sqlite3
import datetime

class TimeTracker:
    def __init__(self):
        self.conn = sqlite3.connect('zeiterfassung.db')  # Verbindung zur SQLite-Datenbank herstellen
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.c.execute('''
            CREATE TABLE IF NOT EXISTS zeiterfassung (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                start_time DATETIME,
                end_time DATETIME
            )
        ''')
        self.conn.commit()

    def start(self):
        if self.is_tracking():
            print("Die Zeiterfassung läuft bereits.")
        else:
            self.start_time = datetime.datetime.now()
            self.c.execute("INSERT INTO zeiterfassung (start_time) VALUES (?)", (self.start_time,))
            self.conn.commit()
            print("Zeiterfassung gestartet um", self.start_time)

    def stop(self):
        if not self.is_tracking():
            print("Die Zeiterfassung wurde nicht gestartet.")
        else:
            self.end_time = datetime.datetime.now()
            self.c.execute("UPDATE zeiterfassung SET end_time = ? WHERE end_time IS NULL", (self.end_time,))
            self.conn.commit()
            print("Zeiterfassung gestoppt um", self.end_time)
            elapsed_time = self.end_time - self.start_time
            print("Dauer:", elapsed_time)

    def is_tracking(self):
        self.c.execute("SELECT id FROM zeiterfassung WHERE end_time IS NULL")
        return self.c.fetchone() is not None

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    tracker = TimeTracker()
    while True:
        print("\nZeiterfassungsoptionen:")
        print("1. Start")
        print("2. Stop")
        print("3. Beenden")
        choice = input("Wählen Sie eine Option: ")

        if choice == "1":
            tracker.start()
        elif choice == "2":
            tracker.stop()
        elif choice == "3":
            tracker.close()
            break
        else:
            print("Ungültige Option. Bitte wählen Sie erneut.")
