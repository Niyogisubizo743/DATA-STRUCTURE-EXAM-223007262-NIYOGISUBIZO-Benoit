# topic6_tree_structure.py

"""
Topic 6: Implement a tree to represent hierarchical device groupings in the home security monitoring system.

This module provides an implementation of a Tree structure,
which is used to represent hierarchical data like device groupings (e.g., locations, rooms).
"""

class TreeNode:
    def __init__(self, data):
        self.data = data  # Node data (e.g., Location, Room, Device)
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)
        print(f"[Tree] Added child '{child_node.data}' to parent '{self.data}'.")

    def remove_child(self, child_data):
        for child in self.children:
            if child.data == child_data:
                self.children.remove(child)
                print(f"[Tree] Removed child '{child_data}' from parent '{self.data}'.")
                return True
        print(f"[Tree] Child '{child_data}' not found under parent '{self.data}'.")
        return False

    def find_node(self, data):
        if self.data == data:
            return self
        for child in self.children:
            result = child.find_node(data)
            if result:
                return result
        return None

    def move_child(self, child_data, new_parent_node):
        for child in self.children:
            if child.data == child_data:
                self.children.remove(child)
                new_parent_node.add_child(child)
                print(f"[Tree] Moved '{child_data}' from '{self.data}' to '{new_parent_node.data}'.")
                return True
        print(f"[Tree] Child '{child_data}' not found under parent '{self.data}'.")
        return False

    def display(self, level=0):
        print(' ' * level * 4 + f"- {self.data}")
        for child in self.children:
            child.display(level + 1)

class Tree:
    def __init__(self, root_data):
        self.root = TreeNode(root_data)
        print(f"[Tree] Created tree with root '{root_data}'.")

    def add_node(self, parent_data, child_data):
        parent_node = self.root.find_node(parent_data)
        if parent_node:
            # Check for duplicate child under the same parent
            if any(child.data == child_data for child in parent_node.children):
                print(f"[Tree] Child '{child_data}' already exists under parent '{parent_data}'.")
                return
            child_node = TreeNode(child_data)
            parent_node.add_child(child_node)
        else:
            print(f"[Tree] Parent '{parent_data}' not found.")

    def remove_node(self, parent_data, child_data):
        parent_node = self.root.find_node(parent_data)
        if parent_node:
            parent_node.remove_child(child_data)
        else:
            print(f"[Tree] Parent '{parent_data}' not found.")

    def move_node(self, child_data, current_parent_data, new_parent_data):
        current_parent = self.root.find_node(current_parent_data)
        new_parent = self.root.find_node(new_parent_data)
        if current_parent and new_parent:
            current_parent.move_child(child_data, new_parent)
        else:
            if not current_parent:
                print(f"[Tree] Current parent '{current_parent_data}' not found.")
            if not new_parent:
                print(f"[Tree] New parent '{new_parent_data}' not found.")

    def find_and_display_node(self, data):
        node = self.root.find_node(data)
        if node:
            print(f"\n--- Subtree for '{data}' ---")
            node.display()
        else:
            print(f"[Tree] Node '{data}' not found in the tree.")

    def display_tree(self):
        print("\n--- Hierarchical Device Groupings ---")
        self.root.display()

def main():
    root_name = input("Enter the root of the tree (e.g., 'HomeSecuritySystem'): ").strip()
    if not root_name:
        print("[Error] Root name cannot be empty.")
        return
    tree = Tree(root_name)

    while True:
        print("\n=== Tree Operations ===")
        print("1. Add Device Group/Room")
        print("2. Add Device to Group/Room")
        print("3. Remove Device Group/Room")
        print("4. Move Device/Group to Another Group/Room")
        print("5. Search for a Device/Group")
        print("6. Display Hierarchical Structure")
        print("7. Exit")
        choice = input("Select an option (1-7): ")

        if choice == '1':
            parent = input("Enter parent group/room name (e.g., 'Living Room'): ").strip()
            child = input("Enter new group/room name to add (e.g., 'Main Door Sensor'): ").strip()
            if parent and child:
                tree.add_node(parent, child)
            else:
                print("[Error] Parent and child names cannot be empty.")
        elif choice == '2':
            parent = input("Enter group/room name to add a device to: ").strip()
            device = input("Enter device name to add (e.g., 'Sensor S3'): ").strip()
            if parent and device:
                tree.add_node(parent, device)
            else:
                print("[Error] Group/room and device names cannot be empty.")
        elif choice == '3':
            parent = input("Enter parent group/room name: ").strip()
            child = input("Enter group/room name to remove: ").strip()
            if parent and child:
                tree.remove_node(parent, child)
            else:
                print("[Error] Parent and child names cannot be empty.")
        elif choice == '4':
            child = input("Enter device/group name to move: ").strip()
            current_parent = input("Enter current parent group/room name: ").strip()
            new_parent = input("Enter new parent group/room name: ").strip()
            if child and current_parent and new_parent:
                tree.move_node(child, current_parent, new_parent)
            else:
                print("[Error] Device/group and parent names cannot be empty.")
        elif choice == '5':
            data = input("Enter device/group name to search for: ").strip()
            if data:
                tree.find_and_display_node(data)
            else:
                print("[Error] Search query cannot be empty.")
        elif choice == '6':
            tree.display_tree()
        elif choice == '7':
            print("Exiting Topic 6.")
            break
        else:
            print("[Error] Invalid choice. Please select a number between 1 and 7.")

if __name__ == "__main__":
    main()
