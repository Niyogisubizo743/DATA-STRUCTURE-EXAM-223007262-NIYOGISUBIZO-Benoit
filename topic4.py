# topic4_deque.py

"""
Topic 4: Create Deque to manage a fixed number of security commands in the home security monitoring system.

This module provides an implementation of a Deque,
which is used to manage security commands or maintenance tasks with a fixed size.
When the deque reaches its maximum size, adding a new command will prompt the user to confirm the removal of an existing command.
"""

from collections import deque

class FixedDeque:
    def __init__(self, max_size):
        self.deque = deque()
        self.max_size = max_size

    def is_full(self):
        return len(self.deque) >= self.max_size

    def get_rear_item(self):
        return self.deque[-1] if self.deque else None

    def get_front_item(self):
        return self.deque[0] if self.deque else None

    def add_front(self, item):
        self.deque.appendleft(item)
        print(f"[Deque] Added '{item}' to the front.")

    def add_rear(self, item):
        self.deque.append(item)
        print(f"[Deque] Added '{item}' to the rear.")

    def remove_front(self):
        if self.deque:
            item = self.deque.popleft()
            print(f"[Deque] Removed '{item}' from the front.")
            return item
        print("[Deque] Deque is empty. Cannot remove from front.")
        return None

    def remove_rear(self):
        if self.deque:
            item = self.deque.pop()
            print(f"[Deque] Removed '{item}' from the rear.")
            return item
        print("[Deque] Deque is empty. Cannot remove from rear.")
        return None

    def search_command(self, item):
        if item in self.deque:
            position = list(self.deque).index(item) + 1
            print(f"[Deque] Command '{item}' found at position {position} from the front.")
            return True
        print(f"[Deque] Command '{item}' not found in the deque.")
        return False

    def clear_deque(self):
        self.deque.clear()
        print("[Deque] All commands have been cleared from the deque.")

    def display(self):
        if not self.deque:
            print("Current Deque: [Empty]")
        else:
            print("Current Deque:")
            for idx, cmd in enumerate(self.deque, start=1):
                print(f"  {idx}. {cmd}")

def main():
    print("=== Deque Management for Home Security System ===")
    while True:
        max_size_input = input("Enter maximum number of security commands to manage (positive integer): ").strip()
        if max_size_input.isdigit() and int(max_size_input) > 0:
            max_size = int(max_size_input)
            break
        else:
            print("[Error] Please enter a valid positive integer.")

    fixed_deque = FixedDeque(max_size)

    while True:
        print("\n--- Deque Operations ---")
        print("1. Add Security Command to Front")
        print("2. Add Security Command to Rear")
        print("3. Remove Security Command from Front")
        print("4. Remove Security Command from Rear")
        print("5. Search for a Security Command")
        print("6. Clear All Security Commands")
        print("7. Display Deque")
        print("8. Exit")
        choice = input("Select an option (1-8): ").strip()

        if choice == '1':
            command = input("Enter security command to add to front (e.g., 'Lock all doors'): ").strip()
            if not command:
                print("[Error] Command cannot be empty.")
                continue

            if fixed_deque.is_full():
                removed_item = fixed_deque.get_rear_item()
                print(f"[Warning] Adding this command will exceed the maximum size of {fixed_deque.max_size}.")
                print(f"       '{removed_item}' will be removed to accommodate the new command.")
                confirmation = input("Do you want to proceed? (yes/no): ").strip().lower()
                if confirmation == 'yes':
                    fixed_deque.remove_rear()
                    fixed_deque.add_front(command)
                else:
                    print("[Info] Operation canceled. Command not added.")
            else:
                fixed_deque.add_front(command)

        elif choice == '2':
            command = input("Enter security command to add to rear (e.g., 'Arm all alarms'): ").strip()
            if not command:
                print("[Error] Command cannot be empty.")
                continue

            if fixed_deque.is_full():
                removed_item = fixed_deque.get_front_item()
                print(f"[Warning] Adding this command will exceed the maximum size of {fixed_deque.max_size}.")
                print(f"       '{removed_item}' will be removed to accommodate the new command.")
                confirmation = input("Do you want to proceed? (yes/no): ").strip().lower()
                if confirmation == 'yes':
                    fixed_deque.remove_front()
                    fixed_deque.add_rear(command)
                else:
                    print("[Info] Operation canceled. Command not added.")
            else:
                fixed_deque.add_rear(command)

        elif choice == '3':
            fixed_deque.remove_front()

        elif choice == '4':
            fixed_deque.remove_rear()

        elif choice == '5':
            command = input("Enter the security command to search for: ").strip()
            if not command:
                print("[Error] Command cannot be empty.")
                continue
            fixed_deque.search_command(command)

        elif choice == '6':
            if not fixed_deque.deque:
                print("[Info] Deque is already empty.")
                continue
            confirmation = input("Are you sure you want to clear all commands? (yes/no): ").strip().lower()
            if confirmation == 'yes':
                fixed_deque.clear_deque()
            else:
                print("[Info] Clear operation canceled.")

        elif choice == '7':
            fixed_deque.display()

        elif choice == '8':
            print("Exiting Topic 4.")
            break

        else:
            print("[Error] Invalid choice. Please select a number between 1 and 8.")

if __name__ == "__main__":
    main()
