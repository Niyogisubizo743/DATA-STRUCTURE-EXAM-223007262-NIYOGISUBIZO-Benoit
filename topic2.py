# topic2_linked_lists.py

"""
Topic 2: Implement Singly Linked List and Doubly Linked List to manage data in the home security monitoring system.

This module provides implementations for SinglyLinkedList (for Event Logs) and DoublyLinkedList (for Active Sessions) classes,
which can be used to manage dynamic data like event logs, active user sessions, etc.
"""

class SinglyNode:
    def __init__(self, data):
        self.data = data  # Event data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = SinglyNode(data)
        if not self.head:
            self.head = new_node
            print(f"[Event Log] Appended '{data}' as head.")
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        print(f"[Event Log] Appended '{data}' to the event log.")

    def display(self):
        elems = []
        current = self.head
        while current:
            elems.append(str(current.data))
            current = current.next
        print("Event Logs:", " -> ".join(elems) if elems else "No events recorded.")


class DoublyNode:
    def __init__(self, data):
        self.data = data  # Session data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = DoublyNode(data)
        if not self.head:
            self.head = new_node
            print(f"[Active Sessions] Added '{data}' as first session.")
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
        print(f"[Active Sessions] Added '{data}' to active sessions.")

    def remove(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                print(f"[Active Sessions] Removed session '{data}'.")
                return True
            current = current.next
        print(f"[Active Sessions] Session '{data}' not found.")
        return False

    def display(self):
        elems = []
        current = self.head
        while current:
            elems.append(str(current.data))
            current = current.next
        print("Active Sessions:", " <-> ".join(elems) if elems else "No active sessions.")


def main():
    event_logs = SinglyLinkedList()
    active_sessions = DoublyLinkedList()

    while True:
        print("\n=== Linked Lists Management for Home Security System ===")
        print("1. Manage Event Logs (Singly Linked List)")
        print("2. Manage Active Sessions (Doubly Linked List)")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            manage_event_logs(event_logs)
        elif choice == '2':
            manage_active_sessions(active_sessions)
        elif choice == '3':
            print("Exiting System.")
            break
        else:
            print("Invalid choice. Please try again.")


def manage_event_logs(event_logs):
    while True:
        print("\n--- Event Logs Management ---")
        print("1. Add Event")
        print("2. Display Event Logs")
        print("3. Back to Linked Lists Menu")
        choice = input("Select an option: ")

        if choice == '1':
            event = input("Enter event description (e.g., 'Sensor S1 triggered by intrusion at 14:30'): ")
            event_logs.append(event)
        elif choice == '2':
            event_logs.display()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")


def manage_active_sessions(active_sessions):
    while True:
        print("\n--- Active Sessions Management ---")
        print("1. Add Session")
        print("2. Remove Session")
        print("3. Display Active Sessions")
        print("4. Back to Linked Lists Menu")
        choice = input("Select an option: ")

        if choice == '1':
            session = input("Enter session details (e.g., 'User U1 logged in at 14:25'): ")
            active_sessions.append(session)
        elif choice == '2':
            session = input("Enter session details to remove: ")
            active_sessions.remove(session)
        elif choice == '3':
            active_sessions.display()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
