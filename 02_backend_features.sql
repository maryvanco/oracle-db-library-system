-- Final Project


-- Trigger to set a due date 
CREATE OR REPLACE TRIGGER create_date_due
BEFORE INSERT ON book_loans
FOR EACH ROW
BEGIN
    -- date due is 21 days after date out
    :NEW.date_due := :NEW.date_out + 21;
END;
/


-- Trigger to prevent loans when there are zero copies available
CREATE OR REPLACE TRIGGER prevent_loan_zero_copies
BEFORE INSERT ON book_loans
FOR EACH ROW
DECLARE
    v_copies NUMBER;
BEGIN
    -- Look up number of available copies
    SELECT no_of_copies INTO v_copies
    FROM book_copies
    WHERE book_id = :NEW.book_id AND branch_id = :NEW.branch_id;
    
    -- Raise error
    IF v_copies <= 0 THEN
        RAISE_APPLICATION_ERROR(-20001, 'Book not available');
    END IF;
    
EXCEPTION
    WHEN no_data_found THEN
        RAISE_APPLICATION_ERROR(-20002, 'Not found');
END;
/


-- Trigger to update no_of_copies when a book is loaned or returned
CREATE OR REPLACE TRIGGER update_no_of_copies
AFTER INSERT OR UPDATE ON book_loans
FOR EACH ROW
BEGIN
    -- New loan
    IF INSERTING THEN
        UPDATE book_copies 
        SET no_of_copies = no_of_copies - 1
        WHERE book_id = :NEW.book_id AND branch_id = :NEW.branch_id;
    
    -- Book returned
    ELSIF UPDATING AND :OLD.date_returned IS NULL AND :NEW.date_returned IS NOT NULL THEN
        UPDATE book_copies 
        SET no_of_copies = no_of_copies + 1
        WHERE book_id = :NEW.book_id AND branch_id = :NEW.branch_id;
    END IF;
END;
/



-- Function to calculate unpaid dues
CREATE OR REPLACE FUNCTION calc_unpaid_dues(
    p_card_no IN NUMBER)
RETURN NUMBER
IS 
    total_dues NUMBER := 0;
BEGIN
    SELECT SUM((SYSDATE - date_due) * 0.25) INTO total_dues
    FROM book_loans
    WHERE card_no = p_card_no 
      AND date_returned IS NULL
      AND SYSDATE > date_due;
      
RETURN NVL(total_dues, 0);
END;
/
  


-- Pay fine
CREATE OR REPLACE PROCEDURE pay_fine(
    p_card_no IN NUMBER)
IS
BEGIN
    -- Mark all overdue, unreturned books as returned now
    UPDATE book_loans
    SET date_returned = SYSDATE
    WHERE card_no = p_card_no
    AND date_returned IS NULL
    AND SYSDATE > date_due;
     
    -- Clear patron balance
    UPDATE borrowers
    SET unpaid_dues = 0
    WHERE card_no = p_card_no;
    
    IF SQL%ROWCOUNT = 0 THEN
        RAISE_APPLICATION_ERROR(-20041, 'Patron not found.');
    END IF;
EXCEPTION
    WHEN OTHERS THEN
        RAISE;
END pay_fine;
/


-- Book check out
CREATE OR REPLACE PROCEDURE issue_book(
    p_book_id IN NUMBER,
    p_branch_id IN VARCHAR2,
    p_card_no IN NUMBER)
IS
BEGIN
    INSERT INTO book_loans(book_id, branch_id, card_no)
      VALUES(p_book_id, p_branch_id, p_card_no);
EXCEPTION
    WHEN OTHERS THEN
        RAISE_APPLICATION_ERROR(-20003, 'Error issuing book: ' || SQLERRM);
END issue_book;
/



-- Book return
CREATE OR REPLACE PROCEDURE book_return(
    p_book_id IN NUMBER,
    p_branch_id IN VARCHAR2,
    p_card_no IN NUMBER)
IS
BEGIN
    UPDATE book_loans
    SET date_returned = SYSDATE
    WHERE book_id = p_book_id 
      AND branch_id = p_branch_id
      AND card_no = p_card_no
      AND date_returned IS NULL;
      
    -- Message 
    IF SQL%ROWCOUNT = 0 THEN
        RAISE_APPLICATION_ERROR(-20010, 'No active loan found to return.');
    END IF;
    
EXCEPTION
    WHEN OTHERS THEN
        RAISE;
END book_return;
/



-- Add a book
CREATE OR REPLACE PROCEDURE add_book(
    p_book_id IN NUMBER,
    p_title IN VARCHAR2,
    p_author IN VARCHAR2,
    p_publisher_name IN VARCHAR2)
IS
    publisher_missing EXCEPTION;
    PRAGMA EXCEPTION_INIT(publisher_missing, -2291);
BEGIN
    INSERT INTO books VALUES(p_book_id, p_title, p_publisher_name);
    INSERT INTO book_authors(p_book_id, p_author)
EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
        RAISE_APPLICATION_ERROR(-20011, 'Book ID already exists.');
    WHEN publisher_missing THEN
        RAISE_APPLICATION_ERROR(-20012, 'Publisher not found.');
    WHEN OTHERS THEN
        RAISE;
END add_book;
/




-- New patron
CREATE OR REPLACE PROCEDURE new_patron(
    p_name VARCHAR2,
    p_address VARCHAR2,
    p_phone VARCHAR2)
IS
    check_violation EXCEPTION;
    PRAGMA EXCEPTION_INIT(check_violation, -2290);
BEGIN
    INSERT INTO borrowers (name, address, phone) VALUES(p_name, p_address, p_phone);
    
EXCEPTION
    WHEN check_violation THEN
        RAISE_APPLICATION_ERROR(-20030, 'Invalid phone number format. Use XXX-XXX-XXXX.');
    WHEN DUP_VAL_ON_INDEX THEN
        RAISE_APPLICATION_ERROR(-20032, 'Duplicate key for borrower.');
    WHEN OTHERS THEN
        RAISE;
END new_patron;
/













