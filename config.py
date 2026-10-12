import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

PATIENT_FILE = os.path.join(DATA_DIR, "patients.json")
DOCTOR_FILE = os.path.join(DATA_DIR, "doctors.json")
APPOINTMENT_FILE = os.path.join(DATA_DIR, "appointments.json")
PAYMENT_FILE = os.path.join(DATA_DIR, "payments.json")

SPECIALIZATIONS = [
    "General Physician",
    "Cardiologist",
    "Dermatologist",
    "Dentist",
    "Orthopedic",
    "Pediatrician",
    "Neurologist"
]

APPOINTMENT_STATUSES = [
    "Scheduled",
    "Completed",
    "Cancelled"
]

PAYMENT_METHODS = [
    "Cash",
    "UPI",
    "Card",
    "Bank Transfer"
]

DEFAULT_APPOINTMENT_MINUTES = 30
