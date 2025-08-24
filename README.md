# Django Class Management System
This is a Simple Class Management System Developed for Educational Purpose using Python (Django).
Feel free to make changes based on your requirements.


## Features of this Project

### A. Admin Users Can
1. See Overall Summary Charts of Stuudents Performance, Staffs Perfomrances, Courses, Subjects, Leave, etc.
2. Manage Staffs (Add, Update and Delete)
3. Manage Students (Add, Update and Delete)
4. Manage Course (Add, Update and Delete)
5. Manage Subjects (Add, Update and Delete)
6. Manage Sessions (Add, Update and Delete)
7. View Student Attendance
8. Review and Reply Student/Staff Feedback
9. Review (Approve/Reject) Student/Staff Leave

### B. Staff/Teachers Can
1. See the Overall Summary Charts related to their students, their subjects, leave status, etc.
2. Take/Update Students Attendance
3. Add/Update Result
4. Apply for Leave
5. Send Feedback to HOD

### C. Students Can
1. See the Overall Summary Charts related to their attendance, their subjects, leave status, etc.
2. View Attendance
3. View Result
4. Apply for Leave
5. Send Feedback to HOD

### Installation
**1. Create a Folder where you want to save the project**

**2. Clone this project**
```
$  git clone https://github.com/imjayjoshi/Class-Management-System.git
```

Then, Enter the project
```
$  cd Class-Management-System
```

**3. Activate a Virtual Environment**

For Windows in cmd
```
$  fine/scripts/activate
```

**4. Install Requirements from 'requirements.txt'**
```python
$  pip install -r requirements.txt
```

**5. Now Make Migrations and Run Server**

Command for PC:
```python
$  python manage.py makemigrations
$  python manage.py migrate
$  python manage.py runserver
```

**5. Now Load Data From Datadump.json File**

Command:
```
$  python manage.py loaddata datadump.json
```

**6. Login Credentials**

Create Super User (HOD)
```
$  python manage.py createsuperuser
```
Then Add Email, Username and Password

**or Use Default Credentials**

*For HOD /SuperAdmin*
Email: jayjoshi@gmail.com

Password: jay

*For Staff*
Email: kdumatar88@gmail.com

Password: keyur

*For Student*
Email: sanjivanigohil@gmail.com

Password: sanjivani

## Output ScreeShot
[Screenshots.pdf](https://github.com/im-umang/Class-Management-System/files/15138417/Final.PPT.pdf)
