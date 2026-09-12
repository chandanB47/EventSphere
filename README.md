# EventSphere - Advanced Event Ticket Reservation System

Console-based Python + SQLite reservation system for workshops, music festivals, gaming events, conferences and other live events.

## Features
- Admin event CRUD
- User registration
- Event search
- Ticket availability and overbooking prevention
- Booking and cancellation
- Unique booking codes
- Booking history
- Revenue, popular-event and daily-sales reports
- CSV export
- SQLite persistence
- OOP architecture

## Run
`python main.py`

## Structure
```text
EventSphere/
├── main.py
├── src/
│   ├── __init__.py
│   ├── database.py
│   ├── event.py
│   ├── user.py
│   ├── booking.py
│   ├── admin.py
│   └── reports.py
├── database/
├── exports/
├── README.md
├── requirements.txt
└── .gitignore
```
