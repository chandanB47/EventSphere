from .database import connect
from .booking import export_bookings
def show_reports():
    while True:
        print("\n1. Total Revenue\n2. Popular Event\n3. Daily Sales\n4. Export Bookings CSV\n5. Back")
        ch=input("Enter Choice: ")
        with connect() as c:
            if ch=="1":
                x=c.execute("SELECT COALESCE(SUM(total_amount),0) FROM bookings WHERE booking_status='Confirmed'").fetchone()[0]
                print(f"Total Revenue: ₹{x:.2f}")
            elif ch=="2":
                x=c.execute("""SELECT e.event_name,SUM(b.tickets_booked) FROM bookings b JOIN events e ON b.event_id=e.event_id WHERE b.booking_status='Confirmed' GROUP BY b.event_id ORDER BY 2 DESC LIMIT 1""").fetchone()
                print(f"Popular Event: {x[0]} ({x[1]} tickets)" if x else "No sales yet.")
            elif ch=="3":
                for x in c.execute("""SELECT DATE(booking_time),SUM(tickets_booked),SUM(total_amount) FROM bookings WHERE booking_status='Confirmed' GROUP BY DATE(booking_time) ORDER BY 1 DESC""").fetchall():print(f"{x[0]} | Tickets: {x[1]} | Revenue: ₹{x[2]:.2f}")
            elif ch=="4":export_bookings()
            elif ch=="5":break
            else:print("Invalid Choice.")
