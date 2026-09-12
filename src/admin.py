from .event import add_event,view_events,update_event,delete_event
from .reports import show_reports
def admin_panel():
    while True:
        print("\n"+"="*75+"\n                         Welcome to Admin Panel\n"+"="*75)
        print("1. Add Events\n2. View Events\n3. Update Events\n4. Delete Events\n5. Event Reports\n6. Back to Main Menu")
        ch=input("\nEnter Your Choice: ")
        if ch=="1":add_event()
        elif ch=="2":view_events()
        elif ch=="3":update_event()
        elif ch=="4":delete_event()
        elif ch=="5":show_reports()
        elif ch=="6":break
        else:print("Invalid Choice.")
