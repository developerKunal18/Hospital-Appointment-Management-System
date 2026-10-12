from datetime import timedelta

from config import (
    PATIENT_FILE,
    DOCTOR_FILE,
    APPOINTMENT_FILE,
    DEFAULT_APPOINTMENT_MINUTES
)

from storage import load_data, save_data
from utils import (
    generate_id,
    find_by_id,
    parse_appointment_datetime
)


def appointments_overlap(start_a, end_a, start_b, end_b):
    return start_a < end_b and start_b < end_a


def book_appointment():
    patients = load_data(PATIENT_FILE)
    doctors = load_data(DOCTOR_FILE)
    appointments = load_data(APPOINTMENT_FILE)

    patient_id = input("Patient ID: ").strip()
    doctor_id = input("Doctor ID: ").strip()

    patient = find_by_id(patients, patient_id)
    doctor = find_by_id(doctors, doctor_id)

    if not patient:
        print("Patient not found.")
        return

    if not doctor or not doctor["active"]:
        print("Active doctor not found.")
        return

    date_text = input("Appointment Date (YYYY-MM-DD): ").strip()
    time_text = input("Appointment Time (HH:MM, 24-hour): ").strip()

    start = parse_appointment_datetime(date_text, time_text)

    if start is None:
        return

    end = start + timedelta(minutes=DEFAULT_APPOINTMENT_MINUTES)

    for appointment in appointments:
        if appointment["status"] != "Scheduled":
            continue

        existing_start = parse_appointment_datetime_for_record(
            appointment["appointment_at"]
        )

        existing_end = existing_start + timedelta(
            minutes=appointment["duration_minutes"]
        )

        if (
            appointment["doctor_id"] == doctor_id
            and appointments_overlap(
                start, end, existing_start, existing_end
            )
        ):
            print("This doctor already has an appointment at that time.")
            return

    appointment = {
        "id": generate_id("APT"),
        "patient_id": patient_id,
        "patient_name": patient["name"],
        "doctor_id": doctor_id,
        "doctor_name": doctor["name"],
        "appointment_at": start.strftime("%Y-%m-%d %H:%M:%S"),
        "duration_minutes": DEFAULT_APPOINTMENT_MINUTES,
        "consultation_fee": doctor["consultation_fee"],
        "status": "Scheduled",
        "created_at": __import__("utils").current_datetime()
    }

    appointments.append(appointment)
    save_data(APPOINTMENT_FILE, appointments)

    print("\nAppointment booked successfully!")
    print("Appointment ID:", appointment["id"])
    print("Patient:", patient["name"])
    print("Doctor:", doctor["name"])
    print("Date and Time:", appointment["appointment_at"])
    print("Consultation Fee: ₹", appointment["consultation_fee"])


def parse_appointment_datetime_for_record(value):
    from datetime import datetime

    return datetime.strptime(value, "%Y-%m-%d %H:%M:%S")


def view_appointments():
    appointments = load_data(APPOINTMENT_FILE)

    if not appointments:
        print("No appointments found.")
        return

    print("\n========== APPOINTMENTS ==========")

    for appointment in sorted(
        appointments,
        key=lambda item: item["appointment_at"]
    ):
        print("-" * 45)
        print("Appointment ID:", appointment["id"])
        print("Patient:", appointment["patient_name"])
        print("Doctor:", appointment["doctor_name"])
        print("Date:", appointment["appointment_at"])
        print("Status:", appointment["status"])
        print("Fee: ₹", appointment["consultation_fee"])


def search_appointment():
    appointments = load_data(APPOINTMENT_FILE)

    appointment_id = input("Appointment ID: ").strip()
    appointment = find_by_id(appointments, appointment_id)

    if not appointment:
        print("Appointment not found.")
        return

    for key, value in appointment.items():
        print(f"{key}: {value}")


def update_appointment_status():
    appointments = load_data(APPOINTMENT_FILE)

    appointment_id = input("Appointment ID: ").strip()
    appointment = find_by_id(appointments, appointment_id)

    if not appointment:
        print("Appointment not found.")
        return

    if appointment["status"] != "Scheduled":
        print("Only scheduled appointments can be updated.")
        return

    print("1. Mark Completed")
    print("2. Cancel Appointment")

    choice = input("Select option: ").strip()

    if choice == "1":
        appointment_time = parse_appointment_datetime_for_record(
            appointment["appointment_at"]
        )

        if appointment_time > __import__("datetime").datetime.now():
            print("A future appointment cannot be marked completed.")
            return

        appointment["status"] = "Completed"

    elif choice == "2":
        appointment["status"] = "Cancelled"

    else:
        print("Invalid choice.")
        return

    save_data(APPOINTMENT_FILE, appointments)
    print("Appointment status updated successfully.")


def patient_appointment_history():
    appointments = load_data(APPOINTMENT_FILE)
    patient_id = input("Patient ID: ").strip()

    matches = [
        appointment for appointment in appointments
        if appointment["patient_id"] == patient_id
    ]

    if not matches:
        print("No appointments found for this patient.")
        return

    for appointment in sorted(
        matches,
        key=lambda item: item["appointment_at"],
        reverse=True
    ):
        print(
            appointment["id"],
            appointment["appointment_at"],
            appointment["doctor_name"],
            appointment["status"]
        )
