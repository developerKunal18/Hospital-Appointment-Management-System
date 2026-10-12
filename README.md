# Hospital Appointment Management System

A Python-based application for managing patient records,
doctors, appointments, consultation payments, and reports.

## Features

- Patient registration and management
- Doctor registration and specialization management
- Appointment scheduling
- Prevention of overlapping doctor appointments
- Appointment cancellation
- Appointment status management
- Patient appointment history
- Payment recording
- Receipt ID generation
- Daily appointment reports
- Doctor-wise appointment reports
- Monthly revenue reports
- JSON data persistence

## Technologies Used

- Python
- JSON
- Datetime
- UUID

## Project Structure

```text
hospital-appointment-management/
├── main.py
├── config.py
├── storage.py
├── utils.py
├── patient_manager.py
├── doctor_manager.py
├── appointment_manager.py
├── payment_manager.py
├── report_manager.py
├── data/
│   ├── patients.json
│   ├── doctors.json
│   ├── appointments.json
│   └── payments.json
├── .gitignore
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/hospital-appointment-management.git
```

Open the project directory:

```bash
cd hospital-appointment-management
```

Run the application:

```bash
python main.py
```

No external packages are required.

## Workflow

1. Register a patient.
2. Register a doctor.
3. Book an appointment using the patient and doctor IDs.
4. View or search appointments.
5. Mark an appointment completed after its scheduled time.
6. Record the consultation payment.
7. Generate appointment and revenue reports.

## Appointment Rules

- Appointments must be scheduled in the future.
- Each appointment lasts 30 minutes.
- A doctor cannot have overlapping scheduled appointments.
- Only scheduled appointments can be completed or cancelled.
- Payments are recorded only for completed appointments.
- Duplicate payments for the same appointment are rejected.

## Future Improvements

- Django web interface
- MySQL database
- Role-based authentication
- Doctor availability calendars
- Appointment reminders
- PDF receipts
- Online payments
- Patient portal
- Email notifications
- Exportable reports

## Author

Kunal Karbhari

GitHub: https://github.com/developerKunal18

## Challenge

365 Days of Python Projects

Day 354 Completed
