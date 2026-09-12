# 🎟️ EventSphere - Advanced Event Ticket Reservation System

A console-based **Event Ticket Reservation System** built with **Python, OOP, and SQLite**.

EventSphere allows administrators to manage events and users to search, book, cancel, and view their event bookings. The system also provides sales reports and CSV export functionality.

---

## 📌 Project Overview

EventSphere is designed to simulate a real-world event ticket booking platform for:

- 🎵 Music Festivals
- 💻 Workshops
- 🎮 Gaming Events
- 🎤 Conferences
- 📚 Training Programs
- 🎭 Other Live Events

The project focuses on applying **Python programming, Object-Oriented Programming, database management, CRUD operations, and file handling** in a practical application.

---

## ✨ Features

### 👨‍💼 Admin Features

- Add new events
- View all events
- Update event details
- Delete events
- View event reports
- Calculate total revenue
- Find popular events
- View daily sales
- Export booking data to CSV

### 👤 User Features

- User registration
- Search events
- View available events
- Book tickets
- Cancel bookings
- View booking history
- Receive unique booking codes

### 🎟️ Booking Features

- Ticket availability checking
- Overbooking prevention
- Automatic ticket deduction
- Ticket restoration after cancellation
- Unique booking code generation
- Booking status tracking
- Booking history

---

## 🛠️ Tech Stack

| Technology | Usage |
|---|---|
| **Python 3.x** | Application development |
| **SQLite** | Database |
| **OOP** | Application architecture |
| **sqlite3** | Database connectivity |
| **CSV** | Booking data export |
| **datetime** | Booking timestamps and booking codes |
| **pathlib** | File and directory handling |
| **Git & GitHub** | Version control |

---

## 🧠 Python Concepts Used

This project demonstrates practical usage of:

- Variables and Data Types
- Conditional Statements
- Loops
- Functions
- Modules and Packages
- Classes and Objects
- Object-Oriented Programming
- Exception Handling
- Lists and Tuples
- String Operations
- File Handling
- CSV Processing
- SQLite Database Operations
- CRUD Operations
- SQL Queries
- Foreign Keys
- Input Validation
- Date and Time Handling

---

## 📦 Project Modules

| Module | Responsibility |
|---|---|
| `main.py` | Application entry point and main menu |
| `event.py` | Event management and event search |
| `user.py` | User registration and user operations |
| `booking.py` | Ticket booking, cancellation and history |
| `database.py` | SQLite connection and database tables |
| `admin.py` | Admin panel and event management |
| `reports.py` | Revenue, sales and event reports |

---

## 🗂️ Project Structure

```text
EventSphere/
│
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── admin.py
│   ├── booking.py
│   ├── database.py
│   ├── event.py
│   ├── reports.py
│   └── user.py
│
├── database/
│   └── eventsphere.db
│
└── exports/
    └── bookings.csv
