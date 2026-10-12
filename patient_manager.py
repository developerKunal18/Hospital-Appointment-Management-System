from config import PATIENT_FILE
from storage import load_data, save_data
from utils import generate_id, find_by_id, read_nonempty


def add_patient():
    patients = load_data(PATIENT_FILE)

    name = read_nonempty("Patient Name: ")
    age_text = read_nonempty("Age: ")
    phone = read_nonempty("Phone Number: ")

    if name is None or age_text is None or phone is None:
        return

    try:
        age = int(age_text)

        if not 0 <= age <= 120:
            print("Enter an age between 0 and 120.")
            return

    except ValueError:
        print("Age must be a whole number.")
        return

    if not phone.isdigit() or not 10 <= len(phone) <= 15:
        print("Enter a phone number containing 10–15 digits.")
        return

    patient = {
        "id": generate_id("PAT"),
        "name": name,
        "age": age,
        "phone": phone,
        "created_at": __import__("utils").current_datetime()
    }

    patients.append(patient)
    save_data(PATIENT_FILE, patients)

    print("Patient registered successfully.")
    print("Patient ID:", patient["id"])


def view_patients():
    patients = load_data(PATIENT_FILE)

    if not patients:
        print("No patients registered.")
        return

    for patient in patients:
        print("-" * 40)
        print("ID:", patient["id"])
        print("Name:", patient["name"])
        print("Age:", patient["age"])
        print("Phone:", patient["phone"])


def search_patient():
    patients = load_data(PATIENT_FILE)

    keyword = input("Enter Patient ID or name: ").strip().casefold()

    if not keyword:
        print("Enter a search term.")
        return

    matches = [
        patient for patient in patients
        if keyword in patient["id"].casefold()
        or keyword in patient["name"].casefold()
    ]

    if not matches:
        print("Patient not found.")
        return

    for patient in matches:
        print(patient)


def update_patient():
    patients = load_data(PATIENT_FILE)

    patient_id = input("Patient ID: ").strip()
    patient = find_by_id(patients, patient_id)

    if not patient:
        print("Patient not found.")
        return

    name = input(f"Name [{patient['name']}]: ").strip()
    phone = input(f"Phone [{patient['phone']}]: ").strip()
    age_text = input(f"Age [{patient['age']}]: ").strip()

    if name:
        patient["name"] = name

    if phone:
        if not phone.isdigit() or not 10 <= len(phone) <= 15:
            print("Invalid phone number.")
            return
        patient["phone"] = phone

    if age_text:
        try:
            age = int(age_text)
            if not 0 <= age <= 120:
                print("Invalid age.")
                return
            patient["age"] = age
        except ValueError:
            print("Age must be a whole number.")
            return

    save_data(PATIENT_FILE, patients)
    print("Patient updated successfully.")
