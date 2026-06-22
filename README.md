# 🎓 Student Academic Management System

A desktop application built with **Python** and **Tkinter** for managing student academic records in educational institutions. Developed as a group project for **BSEM1201 – Group 8** at **Limkokwing University of Creative Technology**.

---

## 📌 Project Overview

The Student Academic Management System is designed to replace manual, paper-based academic record keeping with a fast, secure, and easy-to-use digital solution. It supports multiple user roles — Admin, Teacher, Principal, and Student — each with their own dashboard and permissions.

---

## 👥 Group Members

| Name | Role |
|------|------|
| Franklin Danner | Developer |
| Saffa Jimmy | Developer |
| Abubakarr | Developer |

---

## 🚀 Features

- 🔐 **Role-Based Login** — Admin, Teacher, Principal, Student
- ✅ **Account Approval System** — New accounts require Admin approval
- 📝 **Grade Management** — Teachers can add and update student grades
- 📊 **Result Viewing** — Students view their own results with letter grades and averages
- 🖨️ **Print Results** — Students can export and print their result sheet
- 👁️ **Audit Log** — All system activity is recorded with timestamps
- 💾 **Data Backup** — Admin can back up the system data as a JSON file
- 👥 **User Management** — Admin can view, approve, or reject all user accounts

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3 | Core programming language |
| Tkinter | Graphical User Interface (GUI) |
| JSON | Data storage for users and grades |
| OS / DateTime | File handling and timestamps |

---

## 📁 Project Structure


---

## ⚙️ How to Run

### Requirements
- Python 3.x installed on your computer
- Tkinter (comes built-in with Python)

### Steps

1. **Clone the repository**

2. **Navigate into the project folder**

3. **Run the application**

> No additional installations required. All libraries are part of Python's standard library.

---

## 🔑 How to Use

### First Time Setup
1. Run the application
2. Click **Admin Signup** and create the first Admin account
3. The first Admin is **automatically approved** and can log in immediately

### Adding Users
1. Log in as Admin
2. Other users sign up through the login screen
3. Admin approves or rejects accounts from the **Pending Approvals** panel

### Adding Grades (Teacher)
1. Log in as Teacher
2. Click **Add/Update Student Grades**
3. Enter the student username, subject, and score (0–100)

### Viewing Results (Student)
1. Log in as Student
2. Click **View My Results** to see grades and average
3. Click **Print My Results** to save a result sheet

---

## 📊 Grading Scale

| Score | Grade |
|-------|-------|
| 70 and above | A |
| 60 – 69 | B |
| 50 – 59 | C |
| 40 – 49 | D |
| Below 40 | F |

---

## 🔒 Security Features

- Role-based access control
- Account status system (Pending / Approved / Disapproved)
- Activity logging with timestamps
- Input validation on all forms

---

## 📌 Limitations

- Data stored in a local JSON file (not a full database)
- No password hashing
- Desktop only — no web access

---

## 🔮 Future Improvements

- Replace JSON with **SQLite or MySQL**
- Add **password hashing** for security
- Build a **web version** using Flask or Django
- Add **email notifications** for account approvals

---

## 📄 License

This project was created for academic purposes at **Limkokwing University of Creative Technology, Sierra Leone**.
© 2024 BSEM1201 Group 8. All rights reserved.
