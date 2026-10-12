import uuid
from datetime import datetime, date


def generate_id(prefix):
    return f"{prefix}-{uuid.uuid4().hex[:8].upper()}"


def current_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def find_by_id(records, record_id, key="id"):
    return next(
        (
            record for record in records
            if record.get(key) == record_id
        ),
        None
    )


def read_nonempty(prompt):
    value = input(prompt).strip()

    if not value:
        print("This field is required.")
        return None

    return value


def parse_appointment_datetime(date_text, time_text):
    try:
        appointment = datetime.strptime(
            f"{date_text} {time_text}",
            "%Y-%m-%d %H:%M"
        )

        if appointment <= datetime.now():
            print("Appointment must be in the future.")
            return None

        return appointment

    except ValueError:
        print("Use date YYYY-MM-DD and time HH:MM.")
        return None


def money(amount):
    return f"₹{amount:.2f}"
