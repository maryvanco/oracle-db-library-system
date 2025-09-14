from sqlite3 import Cursor
import cx_Oracle
import datetime as dt
import sys



# ---------- Get connection ----------
cx_Oracle.init_oracle_client(lib_dir=" ") 

def get_connection():
    try:
        dsn = cx_Oracle.makedsn(
            host= " ",
            port= 1521,
            sid= " ")
        conn = cx_Oracle.connect(
            user= " ",
            password= " ",
            dsn=dsn
        )
        return conn
    except cx_Oracle.DatabaseError as e:
        print("Could not connect to database:", e)
        sys.exit(1)

conn = get_connection()

# Get a cursor object from the connection
cur = conn.cursor()




# ---------- Insert data into tables ----------

# Delete data
cur.execute("DELETE FROM book_loans")
cur.execute("DELETE FROM book_copies")
cur.execute("DELETE FROM branches")
cur.execute("DELETE FROM book_authors")
cur.execute("DELETE FROM borrowers")
cur.execute("DELETE FROM books")
cur.execute("DELETE FROM publishers")

# Data
publishers_data_tuples = [('Scribner', '123 Scribner Ln, New York, NY', '212-555-1234'),
                          ('J.B. Lippincott and Co.', '215 Lippincott Ave, Philadelphia, PA', '215-555-2345'),
                          ('Little, Brown and Company', '34 Beacon St, Boston, MA', '617-555-3456'),
                          ('T. Egerton', '1 Egerton Way, London, UK', '020-555-4567'),
                          ('Secker and Warburg', '10 Secker St, London, UK', '020-555-5678'),
                          ('Allen and Unwin', '83 Alexander St, Sydney, AU', '020-555-6789'),
                          ('Bloomsbury', '50 Bedford Square, London, UK', '020-555-7890'),
                          ('Smith, Elder and Co.', '15 Waterloo Pl, London, UK', '020-555-1111')]

books_data_tuples = [(1001, 'The Great Gatsby', 'Scribner'),
                     (1002, 'To Kill a Mockingbird', 'J.B. Lippincott and Co.'),
                     (1003, 'The Catcher in the Rye', 'Little, Brown and Company'),
                     (1004, 'Pride and Prejudice', 'T. Egerton'),
                     (1005, '1984', 'Secker and Warburg'),
                     (1006, 'The Lord of the Rings', 'Allen and Unwin'),
                     (1007, 'Harry Potter and the Sorcerer''s Stone', 'Bloomsbury'),
                     (1008, 'The Hobbit', 'Allen and Unwin'),
                     (1009, 'Jane Eyre', 'Smith, Elder and Co.'),
                     (1010, 'Wuthering Heights', 'Scribner'),
                     (1011, 'Don Quixote', 'Scribner'),
                     (1012, 'Crime and Punishment', 'Scribner'),
                     (1013, 'The Adventures of Huckleberry Finn', 'Scribner'),
                     (1014, 'The Grapes of Wrath', 'J.B. Lippincott and Co.'),
                     (1015, 'Brave New World', 'J.B. Lippincott and Co.'),
                     (1016, 'Great Expectations', 'J.B. Lippincott and Co.'),
                     (1017, 'War and Peace', 'J.B. Lippincott and Co.'),
                     (1018, 'Lolita', 'J.B. Lippincott and Co.'),
                     (1019, 'Ulysses', 'J.B. Lippincott and Co.'),
                     (1020, 'One Hundred Years of Solitude', 'Little, Brown and Company'),
                     (1021, 'The Little Prince', 'Little, Brown and Company'),
                     (1022, 'The Diary of a Young Girl', 'Little, Brown and Company'),
                     (1023, 'The Hitchhiker''s Guide to the Galaxy', 'Little, Brown and Company'),
                     (1024, 'His Dark Materials', 'Little, Brown and Company'),
                     (1025, 'The Alchemist', 'Little, Brown and Company'),
                     (1026, 'Animal Farm', 'Little, Brown and Company'),
                     (1027, 'Catch-22', 'Little, Brown and Company'),
                     (1028, 'The Handmaid''s Tale', 'Little, Brown and Company'),
                     (1029, 'The Picture of Dorian Gray', 'Little, Brown and Company'),
                     (1030, 'The Count of Monte Cristo', 'T. Egerton'),
                     (1031, 'Little Women', 'T. Egerton'),
                     (1032, 'Rebecca', 'T. Egerton'),
                     (1033, 'The Lion, the Witch, and the Wardrobe', 'T. Egerton'),
                     (1034, 'The Adventures of Pinocchio', 'T. Egerton'),
                     (1035, 'The Call of the Wild', 'T. Egerton'),
                     (1036, 'The Book Thief', 'T. Egerton'),
                     (1037, 'The Kite Runner', 'Secker and Warburg'),
                     (1038, 'The Nightingale', 'Secker and Warburg'),
                     (1039, 'Gone with the Wind', 'Secker and Warburg'),
                     (1040, 'A Tale of Two Cities', 'Secker and Warburg'),
                     (1041, 'David Copperfield', 'Allen and Unwin'),
                     (1042, 'Moby Dick', 'Allen and Unwin'),
                     (1043, 'Frankenstein', 'Allen and Unwin'),
                     (1044, 'The Odyssey', 'Bloomsbury'),
                     (1045, 'The Divine Comedy', 'Bloomsbury'),
                     (1046, 'The Iliad', 'Bloomsbury'),
                     (1047, 'The Brothers Karamazov', 'Bloomsbury'),
                     (1048, 'One Day in the Life of Ivan Denisovich', 'Smith, Elder and Co.'),
                     (1049, 'Dracula', 'Smith, Elder and Co.'),
                     (1050, 'The Stranger', 'Smith, Elder and Co.')]

authors_data_tuples = [(1001, 'F. Scott Fitzgerald'),
                       (1002, 'Harper Lee'),
                       (1003, 'J.D. Salinger'),
                       (1004, 'Jane Austen'),
                       (1005, 'George Orwell'),
                       (1006, 'J.R.R. Tolkien'),
                       (1007, 'J.K. Rowling'),
                       (1008, 'J.R.R. Tolkien'),
                       (1009, 'Charlotte Brontë'),
                       (1010, 'Emily Brontë'),
                       (1011, 'Miguel de Cervantes'),
                       (1012, 'Fyodor Dostoevsky'),
                       (1013, 'Mark Twain'),
                       (1014, 'John Steinbeck'),
                       (1015, 'Aldous Huxley'),
                       (1016, 'Charles Dickens'),
                       (1017, 'Leo Tolstoy'),
                       (1018, 'Vladimir Nabokov'),
                       (1019, 'James Joyce'),
                       (1020, 'Gabriel García Márquez'),
                       (1021, 'Antoine de Saint-Exupéry'),
                       (1022, 'Anne Frank'),
                       (1023, 'Douglas Adams'),
                       (1024, 'Philip Pullman'),
                       (1025, 'Paulo Coelho'),
                       (1026, 'George Orwell'),
                       (1027, 'Joseph Heller'),
                       (1028, 'Margaret Atwood'),
                       (1029, 'Oscar Wilde'),
                       (1030, 'Alexandre Dumas'),
                       (1031, 'Louisa May Alcott'),
                       (1032, 'Daphne du Maurier'),
                       (1033, 'C.S. Lewis'),
                       (1034, 'Carlo Collodi'),
                       (1035, 'Jack London'),
                       (1036, 'Markus Zusak'),
                       (1037, 'Khaled Hosseini'),
                       (1038, 'Kristin Hannah'),
                       (1039, 'Margaret Mitchell'),
                       (1040, 'Charles Dickens'),
                       (1041, 'Charles Dickens'),
                       (1042, 'Herman Melville'),
                       (1043, 'Mary Shelley'),
                       (1044, 'Homer'),
                       (1045, 'Dante Alighieri'),
                       (1046, 'Homer'),
                       (1047, 'Fyodor Dostoevsky'),
                       (1048, 'Aleksandr Solzhenitsyn'),
                       (1049, 'Bram Stoker'),
                       (1050, 'Albert Camus')]

branches_data_tuples = [('br01', 'Aspen Library', '701 N Aspen Dr, Vernon Hills, IL'),
                        ('br02', 'Evergreen Library', '290 Evergreen Dr, Vernon Hills, IL')]

borrowers_data_tuples = [('Mary Vanco', '1262 Briar Ln', '555-502-3282'),
                         ('Ava Thompson', '1425 Elmwood Avenue', '555-329-2938'),
                         ('Isabella Patel', '3882 Maple Street', '555-821-6472'),
                         ('Oliver Kim', '7610 Oak Ridge Drive', '555-407-1365'),
                         ('Lucas Schneider', '2295 Willow Lane', '555-732-8049'),
                         ('Jack Brooks', '8473 Birchwood Road', '555-694-2187'),
                         ('Lily Delgado', '6159 Cedar Crest Way', '555-160-9324'),
                         ('Owen Walsh', '3027 Pine Hill Drive', '555-748-3106'),
                         ('Nora Freeman', '4901 Rosewood Boulevard', '555-235-4790'),
                         ('Asher McCoy', '1338 Sycamore Street', '555-983-6275')]

copies_data_tuples = [(1001, 'br01', 5),
                      (1001, 'br02', 15),
                      (1002, 'br01', 0),
                      (1002, 'br02', 1),
                      (1003, 'br01', 5),
                      (1003, 'br02', 1),
                      (1004, 'br01', 0),
                      (1004, 'br02', 0),
                      (1005, 'br01', 2),
                      (1005, 'br02', 4),
                      (1006, 'br01', 0),
                      (1006, 'br02', 20),
                      (1007, 'br01', 2),
                      (1007, 'br02', 4),
                      (1008, 'br01', 20),
                      (1008, 'br02', 0),
                      (1009, 'br01', 20),
                      (1009, 'br02', 15),
                      (1010, 'br01', 1),
                      (1010, 'br02', 4),
                      (1011, 'br01', 10),
                      (1011, 'br02', 2),
                      (1012, 'br01', 2),
                      (1012, 'br02', 3),
                      (1013, 'br01', 10),
                      (1013, 'br02', 4),
                      (1014, 'br01', 10),
                      (1014, 'br02', 10),
                      (1015, 'br01', 20),
                      (1015, 'br02', 3),
                      (1016, 'br01', 20),
                      (1016, 'br02', 5),
                      (1017, 'br01', 3),
                      (1017, 'br02', 3),
                      (1018, 'br01', 20),
                      (1018, 'br02', 1),
                      (1019, 'br01', 5),
                      (1019, 'br02', 10),
                      (1020, 'br01', 10),
                      (1020, 'br02', 3),
                      (1021, 'br01', 10),
                      (1021, 'br02', 2),
                      (1022, 'br01', 2),
                      (1022, 'br02', 1),
                      (1023, 'br01', 20),
                      (1023, 'br02', 4),
                      (1024, 'br01', 5),
                      (1024, 'br02', 1),
                      (1025, 'br01', 5),
                      (1025, 'br02', 20),
                      (1026, 'br01', 20),
                      (1026, 'br02', 15),
                      (1027, 'br01', 3),
                      (1027, 'br02', 5),
                      (1028, 'br01', 0),
                      (1028, 'br02', 0),
                      (1029, 'br01', 4),
                      (1029, 'br02', 2),
                      (1030, 'br01', 5),
                      (1030, 'br02', 0),
                      (1031, 'br01', 4),
                      (1031, 'br02', 2),
                      (1032, 'br01', 1),
                      (1032, 'br02', 0),
                      (1033, 'br01', 10),
                      (1033, 'br02', 15),
                      (1034, 'br01', 4),
                      (1034, 'br02', 3),
                      (1035, 'br01', 4),
                      (1035, 'br02', 0),
                      (1036, 'br01', 20),
                      (1036, 'br02', 3),
                      (1037, 'br01', 5),
                      (1037, 'br02', 4),
                      (1038, 'br01', 0),
                      (1038, 'br02', 3),
                      (1039, 'br01', 15),
                      (1039, 'br02', 0),
                      (1040, 'br01', 3),
                      (1040, 'br02', 3),
                      (1041, 'br01', 2),
                      (1041, 'br02', 2),
                      (1042, 'br01', 0),
                      (1042, 'br02', 15),
                      (1043, 'br01', 10),
                      (1043, 'br02', 15),
                      (1044, 'br01', 2),
                      (1044, 'br02', 3),
                      (1045, 'br01', 10),
                      (1045, 'br02', 20),
                      (1046, 'br01', 5),
                      (1046, 'br02', 0),
                      (1047, 'br01', 15),
                      (1047, 'br02', 3),
                      (1048, 'br01', 10),
                      (1048, 'br02', 0),
                      (1049, 'br01', 2),
                      (1049, 'br02', 0),
                      (1050, 'br01', 2),
                      (1050, 'br02', 1)]

# Insert data
insert_publishers = 'insert into publishers (name, address, phone) values (:1, :2, :3)'
cur.executemany(insert_publishers, publishers_data_tuples)

insert_books = 'insert into books (book_id, title, publisher_name) values (:1, :2, :3)'
cur.executemany(insert_books, books_data_tuples)

insert_authors = 'insert into book_authors (book_id, author_name) values (:1, :2)'
cur.executemany(insert_authors, authors_data_tuples)

insert_branches = 'insert into branches (branch_id, branch_name, address) values (:1, :2, :3)'
cur.executemany(insert_branches, branches_data_tuples)

insert_borrowers = 'insert into borrowers (name, address, phone) values (:1, :2, :3)'
cur.executemany(insert_borrowers, borrowers_data_tuples)

insert_copies = 'insert into book_copies (book_id, branch_id, no_of_copies) values (:1, :2, :3)'
cur.executemany(insert_copies, copies_data_tuples)

# Insert test loan data
cur.execute("insert into borrowers (card_no, name, address, phone) values(1, 'Sample', '123 Street', '555-111-2222')")

cur.execute("SELECT card_no FROM borrowers WHERE phone = :1", ["555-502-3282"])
mary_id = cur.fetchone()[0]

loans_data_tuples = [(1001, 'br01', mary_id),
                     (1002, 'br02', mary_id)]

insert_loans = 'insert into book_loans (book_id, branch_id, card_no) values (:1, :2, :3)'
cur.executemany(insert_loans, loans_data_tuples)

conn.commit()





# ---------- Action Functions ----------

def checkout_book(conn, card_no: int):
    book_id = int(input("Enter book_id: "))
    branch_id = input("Enter branch_id: ")
    cur = conn.cursor()
    try:
        cur.callproc("issue_book", [book_id, branch_id, card_no])
        conn.commit()

        # Fetch the generated date_due
        cur.execute("""SELECT date_due 
                    FROM book_loans 
                    WHERE book_id=:b AND branch_id=:br AND card_no=:c 
                    ORDER BY date_out DESC 
                    FETCH FIRST 1 ROWS ONLY""",
                    b=book_id, br=branch_id, c=card_no)
        row = cur.fetchone()
        if not row:
            print("No copies available.")
            return
        date_due = row[0].strftime("%Y-%m-%d") if row else "unknown"
        print(f"Book check out complete. Return book by {date_due}")
    except cx_Oracle.DatabaseError as e:
        conn.rollback()
        print("Error", e)

def return_book(con, card_no: int):
    book_id = int(input("Enter book_id: "))
    branch_id = input("Enter branch_id: ")
    cur = con.cursor()
    try:
        cur.callproc("book_return", [book_id, branch_id, card_no])
        con.commit()
        print("Book returned.")
    except cx_Oracle.DatabaseError as e:
        con.rollback()
        print("Error", e)

def pay_fine(con, card_no: int):
    cur = con.cursor()
    try:
        # 1) Compute fines from PL/SQL FUNCTION
        amount = cur.callfunc("calc_unpaid_dues", cx_Oracle.NUMBER, [card_no]) or 0
        print(f"Current fines: ${float(amount):.2f}")

        confirm = input("Return book(s) and pay fine? (y/N): ")
        if confirm != "y":
            print("Cancelled.")
            return

        # 2) Call PL/SQL PROCEDURE that zeroes unpaid_dues
        cur.callproc("pay_fine", [card_no])
        con.commit()
        print("Fines cleared.")

    except cx_Oracle.DatabaseError as e:
        con.rollback()
        print("Error", e)

def print_current_loans(con, card_no: int):
    cur = con.cursor()
    try:
        cur.execute(
            """
            SELECT bl.book_id, b.title, bl.branch_id, bl.date_out, bl.date_due
            FROM book_loans bl
            JOIN books b ON b.book_id = bl.book_id
            WHERE bl.card_no = :c
              AND bl.date_returned IS NULL
            ORDER BY bl.date_due
            """, c=card_no)
        rows = cur.fetchall()
        if not rows:
            print("No current loans.")
            return
        for book_id, title, branch_id, date_out, date_due in rows:
            print(f"{book_id} | {title} | {branch_id} | {date_out:%Y-%m-%d} | {date_due:%Y-%m-%d}")
    except cx_Oracle.DatabaseError as e:
        print("Error", e)

def add_book(con):
    book_id = int(input("New book_id: "))
    title = input("Title: ")
    publisher_name = input("Publisher name: ") or None
    cur = con.cursor()
    try:
        cur.callproc("add_book", [book_id, title, publisher_name])
        con.commit()
        print("Book added.")
    except cx_Oracle.DatabaseError as e:
        con.rollback()
        print("Error", e)

def search_book(con):
    book_id = int(input("Book ID: "))
    cur = con.cursor()
    try:
        cur.execute("""SELECT br.branch_2name, bc.no_of_copies, b.title, ba.author_name
                    FROM book_copies bc
                    JOIN books b ON bc.book_id = b.book_id
                    JOIN book_authors ba ON b.book_id = ba.book_id
                    JOIN branches br ON bc.branch_id = br.branch_id
                    WHERE bc.book_id = :b
                    """, b=book_id)
        rows = cur.fetchall()
        if not rows:
            print('Book not found.')
            return
        for branch_name, copies, title, author in rows:
            print(f"{branch_name} | Copies Available: {copies} | {title} By {author}")
    except cx_Oracle.DatabaseError as e:
        print("Error", e)

def new_patron(con):
    name = input("Name: ")
    addr = input("Address: ")
    phone = input("Phone (XXX-XXX-XXXX): ")
    cur = con.cursor()
    try:
        cur.callproc("new_patron", [name, addr, phone])
        con.commit()

        # Fetch the generated card_no
        cur.execute("""SELECT card_no 
                    FROM borrowers 
                    WHERE name=:n AND phone=:p 
                    ORDER BY card_no DESC 
                    FETCH FIRST 1 ROWS ONLY""",
                    n=name, p=phone)
        row = cur.fetchone()
        card_no = row[0] if row else "unknown"
        print(f"Patron created. Card number: {card_no}")
    except cx_Oracle.DatabaseError as e:
        con.rollback()
        print("Error", e)

def print_branch_info(con):
    cur = con.cursor()
    try:
        cur.execute("SELECT branch_id, branch_name, address FROM branches ORDER BY branch_name")
        rows = cur.fetchall()
        if not rows:
            print("(No branches.)")
            return
        for bid, bname, addr in rows:
            print(f"{bid} | {bname} | {addr or ''}")
    except cx_Oracle.DatabaseError as e:
        print("Error", e)

def print_top10(con):
    cur = con.cursor()
    try:
        cur.execute(
            """
            SELECT b.book_id,
                   b.title,
                   LISTAGG(ba.author_name, ', ') WITHIN GROUP (ORDER BY ba.author_name) AS authors,
                   COUNT(*) AS times_checked_out
            FROM book_loans bl
            JOIN books b ON b.book_id = bl.book_id
            LEFT JOIN book_authors ba ON ba.book_id = b.book_id
            GROUP BY b.book_id, b.title
            ORDER BY times_checked_out DESC, b.title
            FETCH FIRST 10 ROWS ONLY
            """)
        rows = cur.fetchall()
        for i, (book_id, title, authors, cnt) in enumerate(rows, start=1):
            print(f"{i} | {book_id} | {title} | {(authors or '')} | {cnt}")
    except cx_Oracle.DatabaseError as e:
        print("Error", e)




# ---------- Menus ----------

def patron_menu(con, card_no: int):
    while True:
        print("\nPATRON MENU")
        print("(1) Book checkout")
        print("(2) Book return")
        print("(3) Pay fine")
        print("(4) Print loaned books list")
        print("(5) Back")
        choice = input("Choose: ")
        if choice == "1":
            checkout_book(con, card_no)
        elif choice == "2":
            return_book(con, card_no)
        elif choice == "3":
            pay_fine(con, card_no)
        elif choice == "4":
            print_current_loans(con, card_no)
        elif choice == "5":
            break
        else:
            print("Invalid choice.")


def admin_menu(con):
    while True:
        print("\nADMIN MENU")
        print("(1) Add a book")
        print("(2) Search book (by id)")
        print("(3) New patron")
        print("(4) Print branch information")
        print("(5) Top 10 most checked-out books")
        print("(6) Back")
        choice = input("Choose: ")
        if choice == "1":
            add_book(con)
        elif choice == "2":
            search_book(con)
        elif choice == "3":
            new_patron(con)
        elif choice == "4":
            print_branch_info(con)
        elif choice == "5":
            print_top10(con)
        elif choice == "6":
            break
        else:
            print("Invalid choice.")


def main():
    con = get_connection()
    try:
        while True:
            print("\nMAIN MENU")
            print("(1) Patron functions")
            print("(2) Administrative functions")
            print("(3) Quit")
            choice = input("Choose: ")

            if choice == "1":
                # Ask for card number
                try:
                    card_no = int(input("Enter card number: "))
                except ValueError:
                    print("Invalid number.")
                    continue
                # Check if card number exists    
                cur = con.cursor()
                cur.execute("SELECT 1 FROM borrowers WHERE card_no = :c", c=card_no)
                if cur.fetchone() is None:
                    print("No such patron.")
                    continue
                patron_menu(con, card_no)
            elif choice == "2":
                admin_menu(con)
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")
    finally:
        try:
            con.close()
        except Exception:
            pass


# Close cursor
cur.close()
# Close connection
conn.close()

if __name__ == "__main__":
    main()