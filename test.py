# topic1_define_data_structures.py

"""
Topic 1: Define data structures and discuss their importance in home security monitoring system.

This module defines the fundamental data structures used in the Home Security Monitoring System.
These structures include Sensor, Alarm, and User classes, each serving a specific purpose in the system.
"""

class Sensor:
    def __init__(self, sensor_id, sensor_type, location):
        self.sensor_id = sensor_id
        self.sensor_type = sensor_type  # e.g., 'motion', 'door', 'window'
        self.location = location
        self.status = 'inactive'  # 'active' or 'inactive'

    def activate(self):
        self.status = 'active'
        print(f"Sensor {self.sensor_id} activated.")

    def deactivate(self):
        self.status = 'inactive'
        print(f"Sensor {self.sensor_id} deactivated.")

    def __str__(self):
        return f"Sensor(ID:{self.sensor_id}, Type:{self.sensor_type}, Location:{self.location}, Status:{self.status})"

class Alarm:
    def __init__(self, alarm_id, alarm_type):
        self.alarm_id = alarm_id
        self.alarm_type = alarm_type  # e.g., 'sirene', 'light'
        self.state = 'off'  # 'on' or 'off'

    def turn_on(self):
        self.state = 'on'
        print(f"Alarm {self.alarm_id} turned on.")

    def turn_off(self):
        self.state = 'off'
        print(f"Alarm {self.alarm_id} turned off.")

    def __str__(self):
        return f"Alarm(ID:{self.alarm_id}, Type:{self.alarm_type}, State:{self.state})"

class User:
    def __init__(self, user_id, name, role):
        self.user_id = user_id
        self.name = name
        self.role = role  # e.g., 'admin', 'guest'

    def __str__(self):
        return f"User(ID:{self.user_id}, Name:{self.name}, Role:{self.role})"

def main():
    sensors = {}
    alarms = {}
    users = {}

    while True:
        print("\n=== Home Security Monitoring System ===")
        print("1. Manage Sensors")
        print("2. Manage Alarms")
        print("3. Manage Users")
        print("4. Display All Data")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            manage_sensors(sensors)
        elif choice == '2':
            manage_alarms(alarms)
        elif choice == '3':
            manage_users(users)
        elif choice == '4':
            display_all(sensors, alarms, users)
        elif choice == '5':
            print("Exiting System.")
            break
        else:
            print("Invalid choice. Please try again.")

def manage_sensors(sensors):
    while True:
        print("\n--- Manage Sensors ---")
        print("1. Add Sensor")
        print("2. Activate Sensor")
        print("3. Deactivate Sensor")
        print("4. View Sensors")
        print("5. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            sensor_id = input("Enter Sensor ID: ")
            sensor_type = input("Enter Sensor Type (motion/door/window): ")
            location = input("Enter Sensor Location: ")
            if sensor_id in sensors:
                print("Sensor ID already exists.")
            else:
                sensors[sensor_id] = Sensor(sensor_id, sensor_type, location)
                print("Sensor added successfully.")
        elif choice == '2':
            sensor_id = input("Enter Sensor ID to activate: ")
            sensor = sensors.get(sensor_id)
            if sensor:
                sensor.activate()
            else:
                print("Sensor not found.")
        elif choice == '3':
            sensor_id = input("Enter Sensor ID to deactivate: ")
            sensor = sensors.get(sensor_id)
            if sensor:
                sensor.deactivate()
            else:
                print("Sensor not found.")
        elif choice == '4':
            if not sensors:
                print("No sensors available.")
            else:
                for sensor in sensors.values():
                    print(sensor)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def manage_alarms(alarms):
    while True:
        print("\n--- Manage Alarms ---")
        print("1. Add Alarm")
        print("2. Turn On Alarm")
        print("3. Turn Off Alarm")
        print("4. View Alarms")
        print("5. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            alarm_id = input("Enter Alarm ID: ")
            alarm_type = input("Enter Alarm Type (sirene/light): ")
            if alarm_id in alarms:
                print("Alarm ID already exists.")
            else:
                alarms[alarm_id] = Alarm(alarm_id, alarm_type)
                print("Alarm added successfully.")
        elif choice == '2':
            alarm_id = input("Enter Alarm ID to turn on: ")
            alarm = alarms.get(alarm_id)
            if alarm:
                alarm.turn_on()
            else:
                print("Alarm not found.")
        elif choice == '3':
            alarm_id = input("Enter Alarm ID to turn off: ")
            alarm = alarms.get(alarm_id)
            if alarm:
                alarm.turn_off()
            else:
                print("Alarm not found.")
        elif choice == '4':
            if not alarms:
                print("No alarms available.")
            else:
                for alarm in alarms.values():
                    print(alarm)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def manage_users(users):
    while True:
        print("\n--- Manage Users ---")
        print("1. Add User")
        print("2. View Users")
        print("3. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            user_id = input("Enter User ID: ")
            name = input("Enter User Name: ")
            role = input("Enter User Role (admin/guest): ")
            if user_id in users:
                print("User ID already exists.")
            else:
                users[user_id] = User(user_id, name, role)
                print("User added successfully.")
        elif choice == '2':
            if not users:
                print("No users available.")
            else:
                for user in users.values():
                    print(user)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def display_all(sensors, alarms, users):
    print("\n--- All Data ---")
    print("\nSensors:")
    if not sensors:
        print("No sensors available.")
    else:
        for sensor in sensors.values():
            print(sensor)
    print("\nAlarms:")
    if not alarms:
        print("No alarms available.")
    else:
        for alarm in alarms.values():
            print(alarm)
    print("\nUsers:")
    if not users:
        print("No users available.")
    else:
        for user in users.values():
            print(user)

if __name__ == "__main__":
    main()
