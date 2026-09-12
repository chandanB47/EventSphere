from datetime import datetime
from pathlib import Path
from .database import connect
from .event import view_events

def generate_booking_code(booking_id): return f"EVT{datetime.now().year}{booking_id:04d}"

def book_ticket(user_id):
    view_events()
    try:
        eid=int(input("\nEnter Event ID: ")); qty=int(input("Enter Number of Tickets: "))
        if qty<=0: print("Tickets must be greater than zero."); return
        with connect() as c:
            e=c.execute("SELECT event_name,ticket_price,available_tickets FROM events WHERE event_id=?",(eid,)).fetchone()
            if not e: print("Event not found."); return
            name,price,available=e
            if available<qty: print(f"Only {available} tickets are available."); return
            cur=c.execute("INSERT INTO bookings(booking_code,user_id,event_id,tickets_booked,total_amount) VALUES(?,?,?,?,?)",("TEMP",user_id,eid,qty,price*qty))
            bid=cur.lastrowid; code=generate_booking_code(bid)
            c.execute("UPDATE bookings SET booking_code=? WHERE booking_id=?",(code,bid))
            c.execute("UPDATE events SET available_tickets=available_tickets-? WHERE event_id=?",(qty,eid))
        print(f"\nBooking Confirmed!\nBooking Code : {code}\nEvent : {name}\nTickets : {qty}\nTotal Amount : ₹{price*qty:.2f}")
    except ValueError:print("Invalid input.")

def booking_history(user_id):
    with connect() as c:
        rows=c.execute("""SELECT b.booking_code,e.event_name,b.tickets_booked,b.total_amount,b.booking_status,b.booking_time
        FROM bookings b JOIN events e ON b.event_id=e.event_id WHERE b.user_id=? ORDER BY b.booking_id DESC""",(user_id,)).fetchall()
    if not rows:print("No booking history found.");return
    print("\n"+"="*80+"\n                         Booking History\n"+"="*80)
    for r in rows:print(f"Code: {r[0]} | Event: {r[1]} | Tickets: {r[2]} | Amount: ₹{r[3]:.2f} | Status: {r[4]} | Time: {r[5]}")

def cancel_booking(user_id):
    booking_history(user_id)
    code=input("\nEnter Booking Code to Cancel: ").strip()
    with connect() as c:
        r=c.execute("SELECT booking_id,event_id,tickets_booked FROM bookings WHERE booking_code=? AND user_id=? AND booking_status='Confirmed'",(code,user_id)).fetchone()
        if not r:print("Active booking not found.");return
        bid,eid,qty=r
        c.execute("UPDATE bookings SET booking_status='Cancelled' WHERE booking_id=?",(bid,))
        c.execute("UPDATE events SET available_tickets=available_tickets+? WHERE event_id=?",(qty,eid))
    print("Booking Cancelled Successfully!")

def export_bookings():
    import csv

    # Create exports folder automatically
    export_dir = Path(__file__).resolve().parent.parent / "exports"
    export_dir.mkdir(parents=True, exist_ok=True)

    export_file = export_dir / "bookings.csv"

    with connect() as c:
        rows = c.execute("""
            SELECT
                b.booking_code,
                u.name,
                u.email,
                e.event_name,
                b.tickets_booked,
                b.total_amount,
                b.booking_status,
                b.booking_time
            FROM bookings b
            JOIN users u ON b.user_id = u.user_id
            JOIN events e ON b.event_id = e.event_id
            ORDER BY b.booking_id
        """).fetchall()

    with open(
        export_file,
        "w",
        newline="",
        encoding="utf-8"
    ) as f:

        writer = csv.writer(f)

        writer.writerow([
            "Booking Code",
            "User",
            "Email",
            "Event",
            "Tickets",
            "Amount",
            "Status",
            "Booking Time"
        ])

        writer.writerows(rows)

    print(f"Bookings exported successfully!")
    print(f"File: {export_file}")
