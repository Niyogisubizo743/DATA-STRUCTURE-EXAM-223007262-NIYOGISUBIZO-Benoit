# topic7_quick_sort.py

"""
Topic 7: Use Quick Sort to sort the home security monitoring system data based on priority.

This module provides an implementation of the Quick Sort algorithm
to sort Active Alerts based on their priority levels.
"""

def quick_sort(data, low, high, key=lambda x: x):
    if low < high:
        pi = partition(data, low, high, key)
        quick_sort(data, low, pi - 1, key)
        quick_sort(data, pi + 1, high, key)


def partition(data, low, high, key):
    pivot = key(data[high])
    i = low - 1
    for j in range(low, high):
        if key(data[j]) <= pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
    data[i + 1], data[high] = data[high], data[i + 1]
    return i + 1


class Alert:
    def __init__(self, alert_id, sensor_id, alert_type, priority, timestamp, message):
        self.alert_id = alert_id
        self.sensor_id = sensor_id
        self.alert_type = alert_type  # e.g., 'intrusion', 'fire', 'temperature_anomaly'
        self.priority = priority  # Lower number means higher priority
        self.timestamp = timestamp
        self.message = message

    def __repr__(self):
        return (f"Alert(ID:{self.alert_id}, Sensor:{self.sensor_id}, Type:{self.alert_type}, "
                f"Priority:{self.priority}, Time:{self.timestamp}, Message:{self.message})")


def main():
    alerts = []

    while True:
        print("\n=== Alert Management and Sorting ===")
        print("1. Add Alert")
        print("2. Sort Alerts by Priority")
        print("3. Display Alerts")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            alert_id = input("Enter Alert ID: ")
            sensor_id = input("Enter Associated Sensor ID: ")
            alert_type = input("Enter Alert Type (intrusion/fire/temperature_anomaly): ").lower()
            while True:
                priority = input("Enter Alert Priority (1-5, 1 highest): ")
                if priority.isdigit() and 1 <= int(priority) <= 5:
                    priority = int(priority)
                    break
                else:
                    print("[Error] Please enter a valid priority between 1 and 5.")
            timestamp = input("Enter Alert Timestamp (e.g., 2025-01-05 14:30): ")
            message = input("Enter Alert Message: ")
            alerts.append(Alert(alert_id, sensor_id, alert_type, priority, timestamp, message))
            print("[Success] Alert added successfully.")
        elif choice == '2':
            if not alerts:
                print("[Info] No alerts to sort.")
            else:
                quick_sort(alerts, 0, len(alerts) - 1, key=lambda x: x.priority)
                print("[Success] Alerts sorted by priority.")
        elif choice == '3':
            if not alerts:
                print("[Info] No alerts available.")
            else:
                print("\n--- Alerts List ---")
                for alert in alerts:
                    print(alert)
        elif choice == '4':
            print("Exiting Topic 7.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
