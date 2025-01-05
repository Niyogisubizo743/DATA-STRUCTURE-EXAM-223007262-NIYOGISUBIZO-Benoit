# topic5_dynamic_tracking.py

"""
Topic 5: Use Doubly Linked List to track active alerts dynamically in home security monitoring system.

This module uses a DoublyLinkedList to dynamically track active alerts or real-time notifications.
Each alert is timestamped automatically with the current system time upon creation.
"""

from datetime import datetime

class DoublyNode:
    def __init__(self, data):
        self.data = data  # Alert object
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add_alert(self, alert):
        new_node = DoublyNode(alert)
        if not self.head:
            self.head = new_node
            print(f"[Active Alerts] Added '{alert.alert_id}' as the first active alert.")
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
        print(f"[Active Alerts] Added '{alert.alert_id}' to active alerts.")

    def remove_alert(self, alert_id):
        current = self.head
        while current:
            if current.data.alert_id == alert_id:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                print(f"[Active Alerts] Resolved and removed alert '{alert_id}'.")
                return True
            current = current.next
        print(f"[Active Alerts] Alert '{alert_id}' not found.")
        return False

    def clear_alerts(self):
        self.head = None
        print("[Active Alerts] All active alerts have been cleared.")

    def display_alerts(self):
        if not self.head:
            print("Active Alerts: [No active alerts]")
            return
        print("Active Alerts:")
        current = self.head
        while current:
            alert = current.data
            print(f"  ID: {alert.alert_id}, Type: {alert.alert_type}, "
                  f"Sensor: {alert.sensor_id}, Priority: {alert.priority}, "
                  f"Time: {alert.timestamp}, Message: {alert.message}")
            current = current.next

class Alert:
    def __init__(self, alert_id, sensor_id, alert_type, priority, message):
        self.alert_id = alert_id
        self.sensor_id = sensor_id
        self.alert_type = alert_type  # e.g., 'intrusion', 'fire', 'temperature_anomaly'
        self.priority = priority  # Lower number means higher priority
        self.timestamp = self.get_current_timestamp()
        self.message = message

    def get_current_timestamp(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return (f"Alert(ID:{self.alert_id}, Sensor:{self.sensor_id}, Type:{self.alert_type}, "
                f"Priority:{self.priority}, Time:{self.timestamp}, Message:{self.message})")

def main():
    active_alerts = DoublyLinkedList()
    alert_ids = set()  # To ensure unique alert IDs

    while True:
        print("\n=== Active Alerts Management ===")
        print("1. Add Active Alert")
        print("2. Resolve (Remove) Active Alert")
        print("3. Display Active Alerts")
        print("4. Clear All Active Alerts")
        print("5. Exit")
        choice = input("Select an option (1-5): ").strip()

        if choice == '1':
            alert_id = input("Enter Alert ID (unique): ").strip()
            if not alert_id:
                print("[Error] Alert ID cannot be empty.")
                continue
            if alert_id in alert_ids:
                print("[Error] Alert ID already exists. Please use a unique ID.")
                continue
            sensor_id = input("Enter Associated Sensor ID: ").strip()
            if not sensor_id:
                print("[Error] Sensor ID cannot be empty.")
                continue
            alert_type = input("Enter Alert Type (intrusion/fire/temperature_anomaly): ").lower()
            if alert_type not in ['intrusion', 'fire', 'temperature_anomaly']:
                print("[Error] Invalid alert type. Please choose from 'intrusion', 'fire', or 'temperature_anomaly'.")
                continue
            while True:
                priority = input("Enter Alert Priority (1-5, 1 highest): ").strip()
                if priority.isdigit() and 1 <= int(priority) <= 5:
                    priority = int(priority)
                    break
                else:
                    print("[Error] Please enter a valid priority between 1 and 5.")
            message = input("Enter Alert Message: ").strip()
            if not message:
                print("[Error] Message cannot be empty.")
                continue
            new_alert = Alert(alert_id, sensor_id, alert_type, priority, message)
            active_alerts.add_alert(new_alert)
            alert_ids.add(alert_id)
        elif choice == '2':
            if not active_alerts.head:
                print("[Active Alerts] No active alerts to resolve.")
                continue
            alert_id = input("Enter Alert ID to resolve: ").strip()
            if not alert_id:
                print("[Error] Alert ID cannot be empty.")
                continue
            if active_alerts.remove_alert(alert_id):
                alert_ids.discard(alert_id)
        elif choice == '3':
            active_alerts.display_alerts()
        elif choice == '4':
            if not active_alerts.head:
                print("[Active Alerts] No active alerts to clear.")
                continue
            confirmation = input("Are you sure you want to clear all active alerts? (yes/no): ").strip().lower()
            if confirmation == 'yes':
                active_alerts.clear_alerts()
                alert_ids.clear()
            else:
                print("[Info] Clear operation canceled.")
        elif choice == '5':
            print("Exiting Topic 5.")
            break
        else:
            print("[Error] Invalid choice. Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()
