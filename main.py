from patient_manager import (
    add_patient,
    view_patients,
    search_patient,
    update_patient
)

from doctor_manager import (
    add_doctor,
    view_doctors,
    search_doctor,
    deactivate_doctor
)

from appointment_manager import (
    book_appointment,
    view_appointments,
    search_appointment,
    update_appointment_status,
    patient_appointment_history
)

from payment_manager import (
    record_payment,
    view_payments
)

from report_manager import (
    daily_appointment_report,
    hospital_statistics,
    doctor_appointment_report,
    revenue_report
)


def main():
    actions = {
        "1": add_patient,
        "2": view_patients,
        "3": search_patient,
        "4": update_patient,
        "5": add_doctor,
        "6": view_doctors,
        "7": search_doctor,
        "8": deactivate_doctor,
        "9": book_appointment,
        "10": view_appointments,
        "11": search_appointment,
        "12": update_appointment_status,
        "13": patient_appointment_history,
        "14": record_payment,
        "15": view_payments,
        "16": daily_appointment_report,
        "17": doctor_appointment_report,
        "18": hospital_statistics,
        "19": revenue_report
    }

    options = [
        "Add Patient",
        "View Patients",
        "Search Patient",
        "Update Patient",
        "Add Doctor",
        "View Doctors",
        "Search Doctor",
        "Deactivate Doctor",
        "Book Appointment",
        "View Appointments",
        "Search Appointment",
        "Update Appointment Status",
        "Patient Appointment History",
        "Record Payment",
        "View Payments",
        "Daily Appointment Report",
        "Doctor Appointment Report",
        "Hospital Statistics",
        "Monthly Revenue Report"
    ]

    while True:
        print("\n" + "=" * 50)
        print("     HOSPITAL APPOINTMENT MANAGEMENT SYSTEM")
        print("=" * 50)

        for number, option in enumerate(options, 1):
            print(f"{number}. {option}")

        print("0. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "0":
            print("Thank you for using the application!")
            break

        action = actions.get(choice)

        if action:
            try:
                action()
            except (RuntimeError, OSError) as error:
                print("Application error:", error)
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
