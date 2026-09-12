from .database import connect

class Event:
    def __init__(self,event_id,name,category,venue,date,start_time,end_time,price,available_tickets):
        self.event_id=event_id; self.name=name; self.category=category; self.venue=venue
        self.date=date; self.start_time=start_time; self.end_time=end_time
        self.price=price; self.available_tickets=available_tickets

    def display_event(self):
        print("-"*55)
        print(f"Event ID          : {self.event_id}")
        print(f"Event Name        : {self.name}")
        print(f"Category          : {self.category}")
        print(f"Venue             : {self.venue}")
        print(f"Date              : {self.date}")
        print(f"Time              : {self.start_time} - {self.end_time}")
        print(f"Ticket Price      : ₹{self.price:.2f}")
        print(f"Available Tickets : {self.available_tickets}")
        print("-"*55)

def add_event():
    print("\n"+"="*55+"\n                    Add New Event\n"+"="*55)
    try:
        d=(input("Enter Event Name: ").strip(),input("Enter Category: ").strip(),
           input("Enter Venue: ").strip(),input("Enter Event Date: ").strip(),
           input("Enter Start Time: ").strip(),input("Enter End Time: ").strip(),
           float(input("Enter Ticket Price: ")),int(input("Enter Available Tickets: ")))
        if not all(d[:6]) or d[6]<0 or d[7]<0: print("Invalid event details."); return
        with connect() as c:
            c.execute("""INSERT INTO events(event_name,category,venue,event_date,start_time,
            end_time,ticket_price,available_tickets) VALUES(?,?,?,?,?,?,?,?)""",d)
        print("Event Added Successfully!")
    except ValueError: print("Invalid number entered.")

def get_events():
    with connect() as c:
        return c.execute("SELECT event_id,event_name,category,venue,event_date,start_time,end_time,ticket_price,available_tickets FROM events ORDER BY event_id").fetchall()

def view_events():
    rows=get_events()
    if not rows: print("\nNo Events Available."); return
    print("\n"+"="*55+"\n                    Available Events\n"+"="*55)
    for r in rows: Event(*r).display_event()

def update_event():
    view_events()
    try:
        eid=int(input("\nEnter Event ID to Update: "))
        with connect() as c:
            r=c.execute("SELECT * FROM events WHERE event_id=?",(eid,)).fetchone()
            if not r: print("Event ID Not Found."); return
            x=list(r)
            for label,i in [("Event Name",1),("Category",2),("Venue",3),("Event Date",4),("Start Time",5),("End Time",6)]:
                v=input(f"{label} [{x[i]}] (Enter to keep): ").strip()
                if v:x[i]=v
            v=input(f"Ticket Price [{x[7]}] (Enter to keep): ").strip()
            if v:x[7]=float(v)
            v=input(f"Available Tickets [{x[8]}] (Enter to keep): ").strip()
            if v:x[8]=int(v)
            if x[7]<0 or x[8]<0: print("Invalid values."); return
            c.execute("""UPDATE events SET event_name=?,category=?,venue=?,event_date=?,start_time=?,end_time=?,ticket_price=?,available_tickets=? WHERE event_id=?""",(*x[1:9],eid))
        print("Event Updated Successfully!")
    except ValueError: print("Invalid input.")

def delete_event():
    view_events()
    try:
        eid=int(input("\nEnter Event ID to Delete: "))
        with connect() as c:
                n = c.execute(
            "SELECT COUNT(*) FROM bookings WHERE event_id=?",
            (eid,)
        ).fetchone()[0]

        if n:
            print("Cannot delete an event with booking history.")
            return

        cur = c.execute(
            "DELETE FROM events WHERE event_id=?",
            (eid,)
        )

        if cur.rowcount:
            print("Event Deleted Successfully!")
        else:
            print("Event ID Not Found.")
    except ValueError: print("Invalid Event ID.")

def search_event():
    term=input("Enter event name/category to search: ").strip()
    with connect() as c:
        rows=c.execute("SELECT event_id,event_name,category,venue,event_date,start_time,end_time,ticket_price,available_tickets FROM events WHERE event_name LIKE ? OR category LIKE ?",(f"%{term}%",f"%{term}%")).fetchall()
    if not rows: print("No matching events found."); return
    for r in rows: Event(*r).display_event()
