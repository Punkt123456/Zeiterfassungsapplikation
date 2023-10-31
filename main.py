import datetime

class TimeTracker:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        if self.start_time is not None:
            print("Die Zeiterfassung läuft bereits.")
        else:
            self.start_time = datetime.datetime.now()
            print("Zeiterfassung gestartet um", self.start_time)

    def stop(self):
        if self.start_time is None:
            print("Die Zeiterfassung wurde nicht gestartet.")
        else:
            self.end_time = datetime.datetime.now()
            print("Zeiterfassung gestoppt um", self.end_time)
            elapsed_time = self.end_time - self.start_time
            print("Dauer:", elapsed_time)

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
            break
        else:
            print("Ungültige Option. Bitte wählen Sie erneut.")
