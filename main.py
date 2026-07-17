from database import connect_db

def add_student():
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        print("\n--- Enter Student Details ---")
        name = input("Enter Name: ")
        roll_no = input("Enter Roll No: ")
        email = input("Enter Email: ")
        
        try:
            query = "INSERT INTO students (name, roll_no, email) VALUES (%s, %s, %s)"
            values = (name, roll_no, email)
            cursor.execute(query, values)
            conn.commit()
            print("✅ Student added successfully!")
        except Exception as e:
            print(f"❌ Error adding student: {e}")
        finally:
            cursor.close()
            conn.close()

def view_students():
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        try:
            query = "SELECT * FROM students"
            cursor.execute(query)
            records = cursor.fetchall()
            
            if not records:
                print("\nℹ️ No student records found!")
            else:
                print("\n--- Student Records ---")
                print(f"{'ID':<5} | {'Name':<20} | {'Roll No':<15} | {'Email':<25}")
                print("-" * 75)
                for row in records:
                    print(f"{row[0]:<5} | {row[1]:<20} | {row[2]:<15} | {row[3]:<25}")
        except Exception as e:
            print(f"❌ Error fetching students: {e}")
        finally:
            cursor.close()
            conn.close()

def update_student():
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        print("\n--- Update Student Details ---")
        roll_no = input("Enter Roll No of the student to update: ")
        new_name = input("Enter New Name: ")
        new_email = input("Enter New Email: ")
        
        try:
            query = "UPDATE students SET name = %s, email = %s WHERE roll_no = %s"
            values = (new_name, new_email, roll_no)
            cursor.execute(query, values)
            conn.commit()
            
            if cursor.rowcount > 0:
                print("✅ Student details updated successfully!")
            else:
                print("⚠️ No student found with that Roll No!")
                
        except Exception as e:
            print(f"❌ Error updating student: {e}")
        finally:
            cursor.close()
            conn.close()

def delete_student():
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        print("\n--- Delete Student Record ---")
        roll_no = input("Enter Roll No of the student to delete: ")
        
        # Confirming before deletion (Double check)
        confirm = input(f"Are you sure you want to delete student with Roll No '{roll_no}'? (y/n): ").lower()
        
        if confirm == 'y':
            try:
                query = "DELETE FROM students WHERE roll_no = %s"
                cursor.execute(query, (roll_no,))
                conn.commit()
                
                if cursor.rowcount > 0:
                    print("✅ Student record deleted successfully!")
                else:
                    print("⚠️ No student found with that Roll No!")
            except Exception as e:
                print(f"❌ Error deleting student: {e}")
            finally:
                cursor.close()
                conn.close()
        else:
            print("❌ Deletion cancelled!")
            cursor.close()
            conn.close()

def main_menu():
    while True:
        print("\n================================")
        print("   STUDENT MANAGEMENT SYSTEM    ")
        print("================================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("\nEnter your choice (1/2/3/4/5): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("\nThank you! Exiting App...")
            break
        else:
            print("⚠️ Invalid choice! Please enter 1, 2, 3, 4, or 5.")

# Running the main application
if __name__ == "__main__":
    main_menu()