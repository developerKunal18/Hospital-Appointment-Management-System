from config import DOCTOR_FILE, SPECIALIZATIONS
from storage import load_data, save_data
from utils import generate_id, find_by_id, read_nonempty


def add_doctor():
    doctors = load_data(DOCTOR_FILE)

    name = read_nonempty("Doctor Name: ")
    phone = read_nonempty("Phone Number: ")

    if name is None or phone is None:
        return

    if not phone.isdigit() or not 10 <= len(phone) <= 15:
        print("Enter a valid phone number.")
        return

    print("\nSpecializations:")

    for index, specialization in enumerate(SPECIALIZATIONS, 1):
        print(f"{index}. {specialization}")

    try:
        choice = int(input("Select specialization: "))

        if not 1 <= choice <= len(SPECIALIZATIONS):
            print("Invalid specialization.")
            return

    except ValueError:
        print("Enter a valid choice.")
        return

    fee_text = input("Consultation Fee: ₹").strip()

    try:
        fee = float(fee_text)

        if fee < 0:
            print("Fee cannot be negative.")
            return

    except ValueError:
        print("Enter a valid fee.")
        return

    doctor = {
        "id": generate_id("DOC"),
        "name": name,
        "phone": phone,
        "specialization": SPECIALIZATIONS[choice - 1],
        "consultation_fee": round(fee, 2),
        "active": True
    }

    doctors.append(doctor)
    save_data(DOCTOR_FILE, doctors)

    print("Doctor added successfully.")
    print("Doctor ID:", doctor["id"])


def view_doctors():
    doctors = load_data(DOCTOR_FILE)

    if not doctors:
        print("No doctors registered.")
        return

    for doctor in doctors:
        print("-" * 40)
        print("ID:", doctor["id"])
        print("Name:", doctor["name"])
        print("Specialization:", doctor["specialization"])
        print("Consultation Fee:", doctor["consultation_fee"])
        print("Active:", doctor["active"])


def search_doctor():
    doctors = load_data(DOCTOR_FILE)

    keyword = input("Enter Doctor ID or name: ").strip().casefold()

    matches = [
        doctor for doctor in doctors
        if keyword in doctor["id"].casefold()
        or keyword in doctor["name"].casefold()
        or keyword in doctor["specialization"].casefold()
    ]

    if not matches:
        print("No matching doctors found.")
        return

    for doctor in matches:
        print(doctor)


def deactivate_doctor():
    doctors = load_data(DOCTOR_FILE)
    appointments = load_data(
        __import__("config").APPOINTMENT_FILE
    )

    doctor_id = input("Doctor ID: ").strip()
    doctor = find_by_id(doctors, doctor_id)

    if not doctor:
        print("Doctor not found.")
        return

    has_future_appointments = any(
        appointment["doctor_id"] == doctor_id
        and appointment["status"] == "Scheduled"
        and appointment["appointment_at"] > __import__("utils").current_datetime()
        for appointment in appointments
    )

    if has_future_appointments:
        print("Reschedule or cancel future appointments first.")
        return

    doctor["active"] = False
    save_data(DOCTOR_FILE, doctors)

    print("Doctor deactivated.")
