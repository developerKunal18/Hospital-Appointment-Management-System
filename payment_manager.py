from config import (
    APPOINTMENT_FILE,
    PAYMENT_FILE,
    PAYMENT_METHODS
)

from storage import load_data, save_data
from utils import generate_id, current_datetime, find_by_id, money


def record_payment():
    appointments = load_data(APPOINTMENT_FILE)
    payments = load_data(PAYMENT_FILE)

    appointment_id = input("Appointment ID: ").strip()
    appointment = find_by_id(appointments, appointment_id)

    if not appointment:
        print("Appointment not found.")
        return

    if appointment["status"] != "Completed":
        print("Payment can only be recorded for completed appointments.")
        return

    if any(
        payment["appointment_id"] == appointment_id
        for payment in payments
    ):
        print("Payment has already been recorded.")
        return

    print("Consultation Fee:", money(appointment["consultation_fee"]))

    print("\nPayment Methods:")

    for index, method in enumerate(PAYMENT_METHODS, 1):
        print(f"{index}. {method}")

    try:
        choice = int(input("Select payment method: "))

        if not 1 <= choice <= len(PAYMENT_METHODS):
            print("Invalid payment method.")
            return

    except ValueError:
        print("Enter a valid choice.")
        return

    payment = {
        "id": generate_id("REC"),
        "appointment_id": appointment_id,
        "patient_id": appointment["patient_id"],
        "doctor_id": appointment["doctor_id"],
        "amount": appointment["consultation_fee"],
        "method": PAYMENT_METHODS[choice - 1],
        "paid_at": current_datetime()
    }

    payments.append(payment)
    save_data(PAYMENT_FILE, payments)

    print("\nPayment recorded successfully!")
    print("Receipt Number:", payment["id"])
    print("Amount Paid:", money(payment["amount"]))
    print("Payment Method:", payment["method"])


def view_payments():
    payments = load_data(PAYMENT_FILE)

    if not payments:
        print("No payments recorded.")
        return

    print("\n========== PAYMENT RECORDS ==========")

    for payment in payments:
        print("-" * 40)
        print("Receipt:", payment["id"])
        print("Appointment:", payment["appointment_id"])
        print("Patient ID:", payment["patient_id"])
        print("Amount:", money(payment["amount"]))
        print("Method:", payment["method"])
        print("Paid At:", payment["paid_at"])
