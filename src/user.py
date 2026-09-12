from .database import connect
from .event import view_events,search_event
from .booking import book_ticket,cancel_booking,booking_history
class User:
    def __init__(self,user_id,name,email,phone):
        self.user_id=user_id; self.name=name; self.email=email; self.phone=phone

def register_user():
    print("\n"+"="*55+"\n                    User Registration\n"+"="*55)
    name=input("Enter Name: ").strip(); email=input("Enter Email: ").strip(); phone=input("Enter Phone: ").strip()
    if not name or not email or not phone: print("All fields are required."); return
    try:
        with connect() as c:c.execute("INSERT INTO users(name,email,phone) VALUES(?,?,?)",(name,email,phone))
        print("Registration Successful!")
    except Exception: print("Registration failed. Email may already exist.")

def find_user():
    email=input("Enter your registered email: ").strip()
    with connect() as c:r=c.execute("SELECT user_id,name,email,phone FROM users WHERE email=?",(email,)).fetchone()
    if not r: print("User not found. Please register first."); return None
    return User(*r)

def user_panel():
    while True:
        print("\n"+"="*55+"\n                    Welcome to User Panel\n"+"="*55)
        print("1. User Registration\n2. View Events\n3. Search Event\n4. Book Tickets\n5. Cancel My Ticket\n6. Event Booking History\n7. Back to Main Menu")
        ch=input("\nEnter Your Choice: ")
        if ch=="1":register_user()
        elif ch=="2":view_events()
        elif ch=="3":search_event()
        elif ch in ("4","5","6"):
            u=find_user()
            if u:
                if ch=="4":book_ticket(u.user_id)
                elif ch=="5":cancel_booking(u.user_id)
                else:booking_history(u.user_id)
        elif ch=="7":break
        else:print("Invalid Choice.")
