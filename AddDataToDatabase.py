import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':'https://smartattendancerealtime-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

ref = db.reference('Students')

data = {
    "21273030252":
    {
        "name" : "Affan Shazer",
        "major": "AIML",
        "Starting_year": "2021",
        "total_attendance": "10",
        "Grade": "A",
        "Year": "4",
        "last_attendance_time": "2024-09-10 00:54:34"
    },
    "21273030195":
    {
        "name" : "Pallavi Patnaik",
        "major": "AIML",
        "Starting_year": "2021",
        "total_attendance": "20",
        "Grade": "A",
        "Year": "4",
        "last_attendance_time": "2024-09-10 00:54:34"
    },
    "21273030251":
    {
        "name" : "Elon Musk",
        "major": "Physics",
        "Starting_year": "2021",
        "total_attendance": "10",
        "Grade": "A",
        "Year": "4",
        "last_attendance_time": "2024-09-10 00:54:34"
    }

}

for key,value in data.items():
    ref.child(key).set(value)