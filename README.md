# Library Management System
A small library management system built with Oracle SQL (tables, triggers, procedures, functions) and a Python command-line interface using cx_Oracle.

This project demonstrates:  
- Database design with constraints, triggers, and PL/SQL procedures  
- A Python-based terminal UI for patrons and administrators  
- Core library operations: book checkout, return, fine calculation, adding/searching books, and reporting top borrowed books  

---

## Setup  

### 1. Database Setup  
Using SQL Developer or another Oracle client:  
1. Run `01_create_tables.sql` to create the database schema  
2. Run `02_backend_features.sql` to create triggers, functions, and procedures  

### 2. Python Environment  
Before running the app:  
1. Download and install [Oracle Instant Client](https://www.oracle.com/database/technologies/instant-client/downloads.html)  
2. Install dependencies:  
   ```bash
   pip install cx_Oracle

### 3. Database Connection
Open app.py and fill in your database connection details inside the get_connection() function:
- user
- password
- host, port, and sid (service name)
- lib_dir if required (Windows/macOS users may need this path for Oracle Instant Client)


## Running the Application
Start the application from the command line:  
```bash
python app.py
```

### Useful test data
- **book_id:** ranges 1001–1050
- **branch_id:** br01, br02
- **card_no:** use 1 (manually inserted test patron)


## Application Features

**Main Menu**
(1) Patron functions  
(2) Administrative functions  
(3) Quit 

**Patron Menu**
(1) Book checkout  
(2) Book return  
(3) Pay fine  
(4) Print loaned books list  
(5) Quit  

**Admin Menu**
(1) Add a book  
(2) Search book  
(3) New patron  
(4) Print branch information  
(5) Print top 10 frequently checked-out books  
(6) Quit  
