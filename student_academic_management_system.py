import tkinter as tk
from tkinter import ttk, messagebox, filedialog, simpledialog
import json
import os
from datetime import datetime

# --------------------------
# FILES & STORAGE
# --------------------------
DATA_FILE = "student_management_data.json"
LOG_FILE = "system_audit.log"

# Default subjects for all students
DEFAULT_SUBJECTS = ["Math", "English", "Science", "Social Studies", "Religious Education"]

def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return {"users": [], "grades": []}
    return {"users": [], "grades": []}

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def write_log(action, username, role):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] | {role} | {username} | {action}\n")

# --------------------------
# VALIDATION & CHECKS
# --------------------------
def validate_input(name, username, password):
    if not name.strip() or not username.strip() or not password.strip():
        return False, "All fields are required!"
    if len(password) < 4:
        return False, "Password must be at least 4 characters!"
    return True, "Valid"

def find_user(username, password, role):
    data = load_data()
    for user in data["users"]:
        if (user["username"].strip().lower() == username.strip().lower()
            and user["password"] == password
            and user["role"] == role):
            return user
    return None

# --------------------------
# MAIN APPLICATION
# --------------------------
class StudentAcademicManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Academic Management System")
        self.root.geometry("580x620")
        self.root.resizable(False, False)
        self.current_frame = None
        self.logged_in_user = None
        self.show_login_screen()

    def clear_screen(self):
        if self.current_frame:
            self.current_frame.destroy()

    # --------------------------
    # LOGIN SCREEN
    # --------------------------
    def show_login_screen(self):
        self.clear_screen()
        self.logged_in_user = None
        self.current_frame = ttk.Frame(self.root, padding=25)
        self.current_frame.pack(fill="both", expand=True)

        header = tk.Label(self.current_frame, text="STUDENT ACADEMIC MANAGEMENT SYSTEM",
                          font=("Arial", 13, "bold"), fg="white", bg="#E02020", padx=10, pady=10)
        header.pack(fill="x", pady=(0,20))

        ttk.Label(self.current_frame, text="Select Role:", font=("Arial", 10, "bold")).pack(anchor="w")
        self.selected_role = tk.StringVar(value="Admin")
        roles_frame = ttk.Frame(self.current_frame)
        roles_frame.pack(fill="x", pady=8)
        ttk.Radiobutton(roles_frame, text="Teacher", variable=self.selected_role, value="Teacher").pack(side="left", padx=10)
        ttk.Radiobutton(roles_frame, text="Principal", variable=self.selected_role, value="Principal").pack(side="left", padx=10)
        ttk.Radiobutton(roles_frame, text="Admin", variable=self.selected_role, value="Admin").pack(side="left", padx=10)
        ttk.Radiobutton(roles_frame, text="Student", variable=self.selected_role, value="Student").pack(side="left", padx=10)

        ttk.Label(self.current_frame, text="Username / Email:").pack(anchor="w", pady=(15,3))
        self.username_entry = ttk.Entry(self.current_frame, width=60)
        self.username_entry.pack(fill="x")

        ttk.Label(self.current_frame, text="Password:").pack(anchor="w", pady=(12,3))
        self.password_entry = ttk.Entry(self.current_frame, width=60, show="*")
        self.password_entry.pack(fill="x")

        self.show_pass_var = tk.BooleanVar()
        ttk.Checkbutton(self.current_frame, text="Show Password", variable=self.show_pass_var,
                        command=lambda: self.password_entry.config(show="" if self.show_pass_var.get() else "*")).pack(anchor="w", pady=5)

        login_btn = tk.Button(self.current_frame, text="LOGIN", bg="#228B22", fg="white",
                              font=("Arial", 10, "bold"), width=22, command=self.do_login)
        login_btn.pack(pady=12)

        reset_btn = tk.Button(self.current_frame, text="🔑 Forgot / Reset Password", bg="#FF8C00", fg="white",
                              font=("Arial", 9), width=25, command=self.reset_password)
        reset_btn.pack(pady=5)

        ttk.Label(self.current_frame, text="DON'T HAVE AN ACCOUNT?", font=("Arial", 9, "bold")).pack(pady=(10,8))
        signup_frame = ttk.Frame(self.current_frame)
        signup_frame.pack()
        tk.Button(signup_frame, text="Student Signup", bg="#228B22", fg="white",
                  font=("Arial", 9), command=lambda: self.show_signup_form("Student")).grid(row=0, column=0, padx=5)
        tk.Button(signup_frame, text="Teacher Signup", bg="#228B22", fg="white",
                  font=("Arial", 9), command=lambda: self.show_signup_form("Teacher")).grid(row=0, column=1, padx=5)
        tk.Button(signup_frame, text="Principal Signup", bg="#228B22", fg="white",
                  font=("Arial", 9), command=lambda: self.show_signup_form("Principal")).grid(row=0, column=2, padx=5)
        tk.Button(signup_frame, text="Admin Signup", bg="#6A0DAD", fg="white",
                  font=("Arial", 9), command=lambda: self.show_signup_form("Admin")).grid(row=1, column=1, pady=8)

        self.status_label = ttk.Label(self.current_frame, text="", foreground="red", wraplength=520)
        self.status_label.pack(pady=10)

    # --------------------------
    # RESET PASSWORD
    # --------------------------
    def reset_password(self):
        self.clear_screen()
        self.current_frame = ttk.Frame(self.root, padding=30)
        self.current_frame.pack(fill="both", expand=True)

        ttk.Label(self.current_frame, text="🔑 RESET YOUR PASSWORD", font=("Arial", 14, "bold")).pack(pady=20)

        ttk.Label(self.current_frame, text="Enter your Username:").pack(anchor="w", pady=5)
        user_entry = ttk.Entry(self.current_frame, width=60)
        user_entry.pack(fill="x")

        ttk.Label(self.current_frame, text="Enter your Role:").pack(anchor="w", pady=10)
        role_var = tk.StringVar(value="Student")
        ttk.Radiobutton(self.current_frame, text="Student", variable=role_var, value="Student").pack(anchor="w")
        ttk.Radiobutton(self.current_frame, text="Teacher", variable=role_var, value="Teacher").pack(anchor="w")
        ttk.Radiobutton(self.current_frame, text="Principal", variable=role_var, value="Principal").pack(anchor="w")
        ttk.Radiobutton(self.current_frame, text="Admin", variable=role_var, value="Admin").pack(anchor="w")

        ttk.Label(self.current_frame, text="New Password:").pack(anchor="w", pady=10)
        new_pass = ttk.Entry(self.current_frame, width=60, show="*")
        new_pass.pack(fill="x")

        status = ttk.Label(self.current_frame, text="", foreground="red")
        status.pack(pady=15)

        def submit_reset():
            uname = user_entry.get().strip().lower()
            role = role_var.get()
            pwd = new_pass.get().strip()

            if not uname or not pwd:
                status.config(text="Fill all fields!")
                return
            if len(pwd) < 4:
                status.config(text="Password too short!")
                return

            data = load_data()
            found = None
            for user in data["users"]:
                if user["username"].strip().lower() == uname and user["role"] == role:
                    found = user
                    break

            if not found:
                status.config(text="Username / Role not found!")
                return

            found["password"] = pwd
            save_data(data)
            write_log("Password reset", uname, role)
            status.config(text="✅ Password updated successfully!", foreground="green")
            messagebox.showinfo("Done", "You can now login with your new password.")

        ttk.Button(self.current_frame, text="Update Password", command=submit_reset, width=25).pack(pady=10)
        ttk.Button(self.current_frame, text="⬅ Back to Login", command=self.show_login_screen, width=25).pack()

    # --------------------------
    # LOGIN & SIGNUP
    # --------------------------
    def do_login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        role = self.selected_role.get()

        if not username or not password:
            self.status_label.config(text="❌ Enter username and password")
            return

        user = find_user(username, password, role)
        if not user:
            self.status_label.config(text="❌ Invalid details or role")
            return
        if user["status"] == "Pending":
            self.status_label.config(text="⏳ Account Pending: Wait for Admin approval")
            return
        if user["status"] == "Disapproved":
            self.status_label.config(text="❌ Account Disapproved")
            return

        self.status_label.config(text="✅ Login Successful", foreground="green")
        self.logged_in_user = user
        write_log("Successful login", username, role)
        self.open_dashboard()

    def show_signup_form(self, role):
        self.clear_screen()
        self.current_frame = ttk.Frame(self.root, padding=25)
        self.current_frame.pack(fill="both", expand=True)

        ttk.Label(self.current_frame, text=f"{role.upper()} REGISTRATION", font=("Arial", 13, "bold")).pack(pady=20)

        ttk.Label(self.current_frame, text="Full Name:").pack(anchor="w")
        name_entry = ttk.Entry(self.current_frame, width=60)
        name_entry.pack(fill="x")

        ttk.Label(self.current_frame, text="Username / Email:").pack(anchor="w", pady=10)
        user_entry = ttk.Entry(self.current_frame, width=60)
        user_entry.pack(fill="x")

        ttk.Label(self.current_frame, text="Password:").pack(anchor="w", pady=10)
        pass_entry = ttk.Entry(self.current_frame, width=60, show="*")
        pass_entry.pack(fill="x")

        status = ttk.Label(self.current_frame, text="")
        status.pack(pady=15)

        def submit():
            name = name_entry.get().strip()
            uname = user_entry.get().strip()
            pwd = pass_entry.get().strip()
            ok, msg = validate_input(name, uname, pwd)
            if not ok:
                status.config(text=msg)
                return

            data = load_data()
            if any(u["username"].strip().lower() == uname.lower() for u in data["users"]):
                status.config(text="❌ Username already exists!")
                return

            if role == "Admin" and len(data["users"]) == 0:
                acc_status = "Approved"
                msg = "✅ Admin account created — login now!"
            else:
                acc_status = "Pending"
                msg = "✅ Submitted — waiting for Admin approval"

            data["users"].append({
                "name": name, "username": uname, "password": pwd, "role": role, "status": acc_status
            })
            save_data(data)
            write_log("New registration", uname, role)
            status.config(text=msg, foreground="green")
            messagebox.showinfo("Complete", msg)

        ttk.Button(self.current_frame, text="Submit Registration", command=submit, width=25).pack(pady=10)
        ttk.Button(self.current_frame, text="⬅ Back to Login", command=self.show_login_screen, width=25).pack()

    # --------------------------
    # DASHBOARDS
    # --------------------------
    def open_dashboard(self):
        if self.logged_in_user["role"] == "Admin":
            self.admin_dashboard()
        elif self.logged_in_user["role"] == "Principal":
            self.principal_dashboard()
        elif self.logged_in_user["role"] == "Teacher":
            self.teacher_dashboard()
        elif self.logged_in_user["role"] == "Student":
            self.student_dashboard()

    def admin_dashboard(self):
        self.clear_screen()
        self.current_frame = tk.Frame(self.root, bg="#4B006E", padx=30, pady=20)
        self.current_frame.pack(fill="both", expand=True)

        tk.Label(self.current_frame, text="ADMIN DASHBOARD", font=("Arial", 16, "bold"), fg="white", bg="#4B006E").pack(pady=10)
        tk.Label(self.current_frame, text=f"Welcome, {self.logged_in_user['name']}", fg="white", bg="#4B006E").pack(pady=10)

        btn_style = {"width":32, "bg":"#7A2F99", "fg":"white", "font":("Arial",10), "relief":"raised"}
        tk.Button(self.current_frame, text="📋 Pending Approvals", **btn_style, command=self.pending_approvals).pack(pady=6)
        tk.Button(self.current_frame, text="👥 View All Users", **btn_style, command=self.view_all_users).pack(pady=6)
        tk.Button(self.current_frame, text="👁️ System Usage Log", **btn_style, command=self.view_system_usage).pack(pady=6)
        tk.Button(self.current_frame, text="🚪 Logout", **btn_style, bg="#A02020", command=self.logout).pack(pady=20)

    def teacher_dashboard(self):
        self.clear_screen()
        self.current_frame = tk.Frame(self.root, bg="#2E8B57", padx=30, pady=20)
        self.current_frame.pack(fill="both", expand=True)

        tk.Label(self.current_frame, text="TEACHER PANEL", font=("Arial", 16, "bold"), fg="white", bg="#2E8B57").pack(pady=10)
        tk.Label(self.current_frame, text=f"Welcome, {self.logged_in_user['name']}", fg="white", bg="#2E8B57").pack(pady=10)

        btn_style = {"width":32, "bg":"#3CB371", "fg":"white", "font":("Arial",10), "relief":"raised"}
        tk.Button(self.current_frame, text="📝 Enter Grades for Student", **btn_style, command=self.add_all_subject_grades).pack(pady=6)
        tk.Button(self.current_frame, text="📊 View All Grades", **btn_style, command=self.view_all_grades).pack(pady=6)
        tk.Button(self.current_frame, text="🚪 Logout", **btn_style, bg="#A02020", command=self.logout).pack(pady=20)

    def student_dashboard(self):
        self.clear_screen()
        self.current_frame = tk.Frame(self.root, bg="#1E90FF", padx=30, pady=20)
        self.current_frame.pack(fill="both", expand=True)

        tk.Label(self.current_frame, text="STUDENT PANEL", font=("Arial", 16, "bold"), fg="white", bg="#1E90FF").pack(pady=10)
        tk.Label(self.current_frame, text=f"Welcome, {self.logged_in_user['name']}", fg="white", bg="#1E90FF").pack(pady=10)

        btn_style = {"width":32, "bg":"#4682B4", "fg":"white", "font":("Arial",10), "relief":"raised"}
        tk.Button(self.current_frame, text="📄 View My Results", **btn_style, command=self.view_my_results).pack(pady=6)
        tk.Button(self.current_frame, text="🖨️ Print My Results", **btn_style, command=self.print_my_results).pack(pady=6)
        tk.Button(self.current_frame, text="🚪 Logout", **btn_style, bg="#A02020", command=self.logout).pack(pady=20)

    def principal_dashboard(self):
        self.clear_screen()
        self.current_frame = tk.Frame(self.root, bg="#D2691E", padx=30, pady=20)
        self.current_frame.pack(fill="both", expand=True)

        tk.Label(self.current_frame, text="PRINCIPAL PANEL", font=("Arial", 16, "bold"), fg="white", bg="#D2691E").pack(pady=10)
        tk.Label(self.current_frame, text=f"Welcome, {self.logged_in_user['name']}", fg="white", bg="#D2691E").pack(pady=10)

        btn_style = {"width":32, "bg":"#CD853F", "fg":"white", "font":("Arial",10), "relief":"raised"}
        tk.Button(self.current_frame, text="📊 View All Grades", **btn_style, command=self.view_all_grades).pack(pady=6)
        tk.Button(self.current_frame, text="🚪 Logout", **btn_style, bg="#A02020", command=self.logout).pack(pady=20)

    # --------------------------
    # NEW: ENTER ALL SUBJECTS AT ONCE
    # --------------------------
    def add_all_subject_grades(self):
        student_username = simpledialog.askstring("Student", "Enter Student Username:")
        if not student_username:
            return

        data = load_data()
        student = next((u for u in data["users"] if u["username"].lower() == student_username.lower() and u["role"] == "Student"), None)
        if not student:
            messagebox.showerror("Error", "Student not found!")
            return

        # Create simple window to enter all subjects
        grade_window = tk.Toplevel(self.root)
        grade_window.title(f"Enter Grades for {student['name']}")
        grade_window.geometry("400x450")
        grade_window.resizable(False, False)

        entries = {}
        ttk.Label(grade_window, text=f"Student: {student['name']}", font=("Arial",11,"bold")).pack(pady=15)
        ttk.Label(grade_window, text="Enter score between 0 and 100", foreground="gray").pack(pady=5)

        for subj in DEFAULT_SUBJECTS:
            frame = ttk.Frame(grade_window)
            frame.pack(fill="x", padx=30, pady=5)
            ttk.Label(frame, text=f"{subj}:", width=15).pack(side="left")
            ent = ttk.Entry(frame, width=10)
            ent.pack(side="left")
            entries[subj] = ent

        def save_grades():
            try:
                for subj, ent in entries.items():
                    score = float(ent.get().strip())
                    if not (0 <= score <= 100):
                        raise ValueError
                    # Save grade
                    grade_entry = {
                        "student_username": student_username,
                        "student_name": student["name"],
                        "subject": subj,
                        "score": score,
                        "teacher": self.logged_in_user["name"],
                        "date_added": datetime.now().strftime("%Y-%m-%d")
                    }
                    # Update or add
                    existing = next((g for g in data["grades"] if g["student_username"] == student_username and g["subject"] == subj), None)
                    if existing:
                        existing.update(grade_entry)
                    else:
                        data["grades"].append(grade_entry)

                save_data(data)
                write_log(f"Entered all grades for {student_username}", self.logged_in_user["username"], "Teacher")
                messagebox.showinfo("Success", "All grades saved successfully!")
                grade_window.destroy()

            except ValueError:
                messagebox.showerror("Error", "Enter valid numbers 0-100 only!")

        ttk.Button(grade_window, text="Save All Grades", command=save_grades, width=20).pack(pady=20)

    # --------------------------
    # GRADE & REPORT FUNCTIONS
    # --------------------------
    def view_all_grades(self):
        self.clear_screen()
        self.current_frame = ttk.Frame(self.root, padding=20)
        self.current_frame.pack(fill="both", expand=True)

        ttk.Label(self.current_frame, text="ALL STUDENT GRADES", font=("Arial",13,"bold")).pack(pady=15)
        data = load_data()
        grades = data["grades"]

        if not grades:
            ttk.Label(self.current_frame, text="No grades recorded yet").pack(pady=40)
        else:
            txt = tk.Text(self.current_frame, width=75, height=25)
            txt.pack()
            txt.insert("end", f"{'Student':<20} {'Subject':<15} {'Score':<8} {'Teacher':<15}\n")
            txt.insert("end", "-"*70 + "\n")
            for g in grades:
                txt.insert("end", f"{g['student_name']:<20} {g['subject']:<15} {g['score']:<8} {g['teacher']:<15}\n")
            txt.config(state="disabled")

        ttk.Button(self.current_frame, text="⬅ Back", command=self.open_dashboard).pack(pady=10)

    def view_my_results(self):
        self.clear_screen()
        self.current_frame = ttk.Frame(self.root, padding=20)
        self.current_frame.pack(fill="both", expand=True)

        ttk.Label(self.current_frame, text="MY RESULTS", font=("Arial",13,"bold")).pack(pady=15)
        data = load_data()
        my_grades = [g for g in data["grades"] if g["student_username"] == self.logged_in_user["username"]]

        if not my_grades:
            ttk.Label(self.current_frame, text="No results available yet").pack(pady=40)
            return

        txt = tk.Text(self.current_frame, width=70, height=25)
        txt.pack()
        txt.insert("end", f"Name: {self.logged_in_user['name']}\nUsername: {self.logged_in_user['username']}\n\n")
        txt.insert("end", f"{'Subject':<20} {'Score':<10} {'Grade':<10}\n")
        txt.insert("end", "-"*50 + "\n")
        total = 0
        for g in my_grades:
            score = g["score"]
            grade = "A" if score >=70 else "B" if score >=60 else "C" if score >=50 else "D" if score >=40 else "F"
            txt.insert("end", f"{g['subject']:<20} {score:<10} {grade:<10}\n")
            total += score
        avg = round(total / len(my_grades), 2)
        txt.insert("end", f"\nTotal: {total} | Average: {avg}%")
        txt.config(state="disabled")

        ttk.Button(self.current_frame, text="⬅ Back", command=self.student_dashboard).pack(pady=10)

    def print_my_results(self):
        data = load_data()
        my_grades = [g for g in data["grades"] if g["student_username"] == self.logged_in_user["username"]]
        if not my_grades:
            messagebox.showinfo("Print", "No results to print.")
            return

        report = [
            "="*50,
            "STUDENT ACADEMIC MANAGEMENT SYSTEM",
            "OFFICIAL RESULT SHEET",
            "="*50,
            f"Name: {self.logged_in_user['name']}",
            f"Username: {self.logged_in_user['username']}",
            f"Date: {datetime.now().strftime('%Y-%m-%d')}",
            "-"*50,
            f"{'Subject':<20} {'Score':<10} {'Grade':<10}"
        ]
        total = 0
        for g in my_grades:
            score = g["score"]
            grade = "A" if score >=70 else "B" if score >=60 else "C" if score >=50 else "D" if score >=40 else "F"
            report.append(f"{g['subject']:<20} {score:<10} {grade:<10}")
            total += score
        avg = round(total / len(my_grades), 2)
        report.extend(["-"*50, f"Total: {total}", f"Average: {avg}%", "="*50])

        path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text File", "*.txt")], initialfile=f"Result_{self.logged_in_user['name']}.txt")
        if path:
            with open(path, "w", encoding="utf-8") as f:
                f.write("\n".join(report))
            messagebox.showinfo("Saved", "Result saved — open and print it.")

    # --------------------------
    # ADMIN SUPPORT FUNCTIONS
    # --------------------------
    def pending_approvals(self):
        self.clear_screen()
        self.current_frame = ttk.Frame(self.root, padding=20)
        self.current_frame.pack(fill="both", expand=True)

        ttk.Label(self.current_frame, text="PENDING ACCOUNTS", font=("Arial",13,"bold")).pack(pady=15)
        data = load_data()
        pending = [u for u in data["users"] if u["status"] == "Pending"]

        if not pending:
            ttk.Label(self.current_frame, text="No pending requests").pack(pady=40)
        else:
            for u in pending:
                row = ttk.Frame(self.current_frame)
                row.pack(fill="x", pady=4)
                ttk.Label(row, text=f"{u['role']} | {u['name']} | {u['username']}").pack(side="left", padx=5)
                ttk.Button(row, text="✅ Approve", command=lambda u=u: self.change_status(u, "Approved")).pack(side="right")
                ttk.Button(row, text="❌ Reject", command=lambda u=u: self.change_status(u, "Disapproved")).pack(side="right")

        ttk.Button(self.current_frame, text="⬅ Back", command=self.admin_dashboard).pack(pady=20)

    def change_status(self, user, new_status):
        data = load_data()
        for u in data["users"]:
            if u["username"] == user["username"]:
                u["status"] = new_status
        save_data(data)
        write_log(f"Account {new_status}", user["username"], "Admin")
        self.pending_approvals()

    def view_all_users(self):
        self.clear_screen()
        self.current_frame = ttk.Frame(self.root, padding=20)
        self.current_frame.pack(fill="both", expand=True)
        ttk.Label(self.current_frame, text="ALL REGISTERED USERS", font=("Arial",13,"bold")).pack(pady=15)
        data = load_data()
        txt = tk.Text(self.current_frame, width=75, height=25)
        txt.pack()
        for u in data["users"]:
            txt.insert("end", f"{u['role']} | {u['name']} | {u['username']} | {u['status']}\n")
        txt.config(state="disabled")
        ttk.Button(self.current_frame, text="⬅ Back", command=self.admin_dashboard).pack(pady=10)

    def view_system_usage(self):
        self.clear_screen()
        self.current_frame = ttk.Frame(self.root, padding=20)
        self.current_frame.pack(fill="both", expand=True)
        ttk.Label(self.current_frame, text="SYSTEM ACTIVITY LOG", font=("Arial",13,"bold")).pack(pady=15)
        txt = tk.Text(self.current_frame, width=75, height=28)
        txt.pack()
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                txt.insert("end", f.read())
        else:
            txt.insert("end", "No activity yet.")
        txt.config(state="disabled")
        ttk.Button(self.current_frame, text="⬅ Back", command=self.admin_dashboard).pack(pady=10)

    def logout(self):
        write_log("Logged out", self.logged_in_user["username"], self.logged_in_user["role"])
        self.show_login_screen()

# --------------------------
# RUN THE APP
# --------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentAcademicManagementSystem(root)
    root.mainloop()