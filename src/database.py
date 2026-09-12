import sqlite3
from pathlib import Path
DB_PATH = Path(__file__).resolve().parent.parent / "database" / "eventsphere.db"

def connect():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys=ON")
    return conn

def create_tables():
    with connect() as c:
        c.executescript("""
        CREATE TABLE IF NOT EXISTS events(
          event_id INTEGER PRIMARY KEY AUTOINCREMENT,
          event_name TEXT NOT NULL, category TEXT NOT NULL, venue TEXT NOT NULL,
          event_date TEXT NOT NULL, start_time TEXT NOT NULL, end_time TEXT NOT NULL,
          ticket_price REAL NOT NULL CHECK(ticket_price>=0),
          available_tickets INTEGER NOT NULL CHECK(available_tickets>=0));
        CREATE TABLE IF NOT EXISTS users(
          user_id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT NOT NULL, email TEXT NOT NULL UNIQUE, phone TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS bookings(
          booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
          booking_code TEXT NOT NULL UNIQUE, user_id INTEGER NOT NULL,
          event_id INTEGER NOT NULL, tickets_booked INTEGER NOT NULL CHECK(tickets_booked>0),
          total_amount REAL NOT NULL, booking_status TEXT NOT NULL DEFAULT 'Confirmed',
          booking_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
          FOREIGN KEY(user_id) REFERENCES users(user_id),
          FOREIGN KEY(event_id) REFERENCES events(event_id));
        """)
create_tables()
