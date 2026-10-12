from datetime import datetime

from config import (
    PATIENT_FILE,
    DOCTOR_FILE,
    APPOINTMENT_FILE,
    PAYMENT_FILE
)

from storage import load_data
from utils import money


def daily_appointment_report():
    appointments = load_data(APPOINTMENT_FILE)
    today = datetime.now().strftime("%Y-%m-%d")

    todays_appointments = [
        appointment for appointment in appointments
        if appointment["appointment_at"].startswith(today)
    ]

    print("\n========== DAILY APPOINTMENT REPORT ==========")
    print("Date:", today)
    print("Total Appointments:", len(todays_appointments))

    for appointment in todays_appointments:
        print(
            appointment["appointment_at"],
            "|", appointment["patient_name"],
            "|", appointment["doctor_name"],
            "|", appointment["status"]
        )


def hospital_statistics():
    patients = load_data(PATIENT_FILE)
    doctors = load_data(DOCTOR_FILE)
    appointments = load_data(APPOINTMENT_FILE)
    payments = load_data(PAYMENT_FILE)

    print("\n========== HOSPITAL STATISTICS ==========")
    print("Registered Patients:", len(patients))
    print(
        "Active Doctors:",
        sum(1 for doctor in doctors if doctor["active"])
    )
    print("Total Appointments:", len(appointments))
    print(
        "Scheduled Appointments:",
        sum(
            1 for appointment in appointments
            if appointment["status"] == "Scheduled"
        )
    )
    print(
        "Completed Appointments:",
        sum(
            1 for appointment in appointments
            if appointment["status"] == "Completed"
        )
    )
    print(
        "Cancelled Appointments:",
        sum(
            1 for appointment in appointments
            if appointment["status"] == "Cancelled"
        )
    )

    revenue = sum(payment["amount"] for payment in payments)

    print("Recorded Consultation Revenue:", money(revenue))


def doctor_appointment_report():
    doctors = load_data(DOCTOR_FILE)
    appointments = load_data(APPOINTMENT_FILE)

    print("\n========== DOCTOR APPOINTMENT REPORT ==========")

    if not doctors:
        print("No doctors registered.")
        return

    for doctor in doctors:
        doctor_appointments = [
            appointment for appointment in appointments
            if appointment["doctor_id"] == doctor["id"]
        ]

        print("-" * 40)
        print("Doctor:", doctor["name"])
        print("Specialization:", doctor["specialization"])
        print("Total Appointments:", len(doctor_appointments))
        print(
            "Completed:",
            sum(
                1 for appointment in doctor_appointments
                if appointment["status"] == "Completed"
            )
        )
        print(
            "Cancelled:",
            sum(
                1 for appointment in doctor_appointments
                if appointment["status"] == "Cancelled"
            )
        )


def revenue_report():
    payments = load_data(PAYMENT_FILE)

    selected_month = input(
        "Enter month (YYYY-MM), or press Enter for current month: "
    ).strip()

    if not selected_month:
        selected_month = datetime.now().strftime("%Y-%m")

    try:
        datetime.strptime(selected_month, "%Y-%m")
    except ValueError:
        print("Enter the month in YYYY-MM format.")
        return

    monthly_payments = [
        payment for payment in payments
        if payment["paid_at"].startswith(selected_month)
    ]

    revenue = sum(
        payment["amount"]
        for payment in monthly_payments
    )

    print("\n========== REVENUE REPORT ==========")
    print("Month:", selected_month)
    print("Number of Payments:", len(monthly_payments))
    print("Total Recorded Revenue:", money(revenue))
