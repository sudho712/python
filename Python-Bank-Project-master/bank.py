import mysql.connector

# Database connection
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Default username for XAMPP MySQL
            password="",  # Default password for XAMPP MySQL
            database="bank_db"
        )
        print("Connected to the database successfully!")
        return connection
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

# Create a new account
def create_account(name, email, phone, balance):
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        try:
            query = "INSERT INTO accounts (name, email, phone, balance) VALUES (%s, %s, %s, %s)"
            data = (name, email, phone, balance)
            cursor.execute(query, data)
            conn.commit()
            print("Account created successfully!")
        except mysql.connector.Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

# Read account details
def view_account(account_id):
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        try:
            query = "SELECT * FROM accounts WHERE account_id = %s"
            cursor.execute(query, (account_id,))
            account = cursor.fetchone()
            if account:
                print(f"Account Details: {account}")
            else:
                print("Account not found.")
        except mysql.connector.Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

# Update account balance
def update_balance(account_id, new_balance):
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        try:
            query = "UPDATE accounts SET balance = %s WHERE account_id = %s"
            cursor.execute(query, (new_balance, account_id))
            conn.commit()
            if cursor.rowcount:
                print("Balance updated successfully!")
            else:
                print("Account not found.")
        except mysql.connector.Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

# Delete an account
def delete_account(account_id):
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        try:
            query = "DELETE FROM accounts WHERE account_id = %s"
            cursor.execute(query, (account_id,))
            conn.commit()
            if cursor.rowcount:
                print("Account deleted successfully!")
            else:
                print("Account not found.")
        except mysql.connector.Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

# Menu for the Bank Management System
def bank_menu():
    while True:
        print("\n--- Bank Management System ---")
        print("1. Create Account")
        print("2. View Account")
        print("3. Update Balance")
        print("4. Delete Account")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = input("Enter name: ").strip()
            email = input("Enter email: ").strip()
            phone = input("Enter phone: ").strip()
            try:
                balance = float(input("Enter initial balance: ").strip())
                create_account(name, email, phone, balance)
            except ValueError:
                print("Invalid balance. Please enter a number.")
        elif choice == "2":
            try:
                account_id = int(input("Enter account ID: ").strip())
                view_account(account_id)
            except ValueError:
                print("Invalid account ID. Please enter a number.")
        elif choice == "3":
            try:
                account_id = int(input("Enter account ID: ").strip())
                new_balance = float(input("Enter new balance: ").strip())
                update_balance(account_id, new_balance)
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
        elif choice == "4":
            try:
                account_id = int(input("Enter account ID: ").strip())
                delete_account(account_id)
            except ValueError:
                print("Invalid account ID. Please enter a number.")
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the menu
if __name__ == "__main__":
    bank_menu()
