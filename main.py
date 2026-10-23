from src.admin import admin_panel
from src.user import user_panel

def main():
    while True:
        print("-" * 75)
        print("          EventSphere - Event Ticket Reservation System")
        print("-" * 75)
        print("\n1. Admin Panel")
        print("2. User Panel")
        print("3. Exit")
        choice = input("\nEnter Your Choice: ")
        if choice == "1": admin_panel()
        elif choice == "2": user_panel()
        elif choice == "3":
            print("\nThank you for visiting EventSphere. -- Please Visit Again --")
            break
        else: print(" ! Invalid Choice.")

if __name__ == "__main__":
    main()
