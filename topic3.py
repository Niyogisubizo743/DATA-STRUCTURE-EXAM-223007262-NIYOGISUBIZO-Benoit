# topic3_circular_linked_list.py

"""
Topic 3: Implement Circular Linked List for home security monitoring system processing.

This module provides an implementation of CircularLinkedList,
which can be used for cyclic processing tasks like rotating through active sensors for periodic checks.
"""

class CircularNode:
    def __init__(self, data):
        self.data = data  # Sensor ID or Sensor object
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = CircularNode(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            print(f"[Sensor Rotation] Appended '{data}' as head.")
            return
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head
        print(f"[Sensor Rotation] Appended '{data}' to the rotation list.")

    def display(self):
        if not self.head:
            print("[Sensor Rotation] Rotation list is empty.")
            return
        elems = []
        current = self.head
        while True:
            elems.append(str(current.data))
            current = current.next
            if current == self.head:
                break
        print("Sensor Rotation List:", " -> ".join(elems) + " -> ...")

    def traverse(self, steps):
        if not self.head:
            print("[Sensor Rotation] Rotation list is empty.")
            return
        current = self.head
        traversal = []
        for _ in range(steps):
            traversal.append(str(current.data))
            current = current.next
        print("Traversal:", " -> ".join(traversal) + " -> ...")


def main():
    rotation_list = CircularLinkedList()

    while True:
        print("\n=== Sensor Rotation Management ===")
        print("1. Add Sensor to Rotation")
        print("2. Display Rotation List")
        print("3. Traverse Rotation List")
        print("4. Remove Sensor from Rotation")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            sensor_id = input("Enter Sensor ID to add to rotation: ")
            rotation_list.append(sensor_id)
        elif choice == '2':
            rotation_list.display()
        elif choice == '3':
            steps = input("Enter number of steps to traverse: ")
            if steps.isdigit() and int(steps) > 0:
                rotation_list.traverse(int(steps))
            else:
                print("[Error] Please enter a valid positive integer.")
        elif choice == '4':
            remove_sensor(rotation_list)
        elif choice == '5':
            print("Exiting System.")
            break
        else:
            print("Invalid choice. Please try again.")


def remove_sensor(rotation_list):
    print("\n--- Remove Sensor from Rotation ---")
    sensor_id = input("Enter Sensor ID to remove: ")
    if not rotation_list.head:
        print("[Error] Rotation list is empty.")
        return

    current = rotation_list.head
    prev = None
    while True:
        if current.data == sensor_id:
            if prev:
                prev.next = current.next
            else:
                # Removing head
                if current.next == rotation_list.head:
                    rotation_list.head = None
                else:
                    rotation_list.head = current.next
                    # Find last node to point to new head
                    last = rotation_list.head
                    while last.next != current:
                        last = last.next
                    last.next = rotation_list.head
            print(f"[Sensor Rotation] Removed '{sensor_id}' from rotation list.")
            return
        prev = current
        current = current.next
        if current == rotation_list.head:
            break
    print(f"[Error] Sensor '{sensor_id}' not found in rotation list.")


if __name__ == "__main__":
    main()
