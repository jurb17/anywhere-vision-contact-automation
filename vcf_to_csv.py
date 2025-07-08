import csv
import vobject
from datetime import datetime


# Check birthday fields in vCard and convert to MM/DD/YYYY format
def extract_birthday(vcard):
    if hasattr(vcard, "bday"):
        try:
            bday = vcard.bday.value
            if isinstance(bday, datetime):
                return bday.strftime("%m/%d/%Y")
            elif isinstance(bday, str):
                return datetime.strptime(bday, "%Y-%m-%d").strftime("%m/%d/%Y")
        except Exception:
            return ""
    return ""


# Extract data from fields with multiple entries, including phone number and email
def extract_multiple_fields(vcard, field_type, max_count=2):
    values = []
    for child in vcard.getChildren():
        if child.name.lower() == field_type.lower():
            values.append(child.value)
    # Pad list to desired length
    while len(values) < max_count:
        values.append("")
    return values[:max_count]


# Extract address from vCard, combining street, city, region, code, and country
def extract_address(vcard):
    if hasattr(vcard, "adr"):
        adr = vcard.adr.value
        parts = [adr.street, adr.city, adr.region, adr.code, adr.country]
        return ", ".join([p for p in parts if p])
    return ""


# Convert vCard field data to CSV format
def vcard_to_csv(vcf_file_path, output_csv_path):
    contacts = []

    with open(vcf_file_path, "r", encoding="utf-8") as file:
        vcard_data = file.read()

    for vcard in vobject.readComponents(vcard_data):
        emails = extract_multiple_fields(vcard, "email", 2)
        phones = extract_multiple_fields(vcard, "tel", 2)

        contact = {
            "First Name": getattr(vcard.n.value, "given", ""),
            "Last Name": getattr(vcard.n.value, "family", ""),
            "Email 1": emails[0],
            "Email 2": emails[1],
            "Phone 1": phones[0],
            "Phone 2": phones[1],
            "Company": vcard.org.value[0] if hasattr(vcard, "org") else "",
            "Job Title": vcard.title.value if hasattr(vcard, "title") else "",
            "Notes": vcard.note.value if hasattr(vcard, "note") else "",
            "Birthday": extract_birthday(vcard),
            "Address": extract_address(vcard),
        }

        contacts.append(contact)

    # Define column order
    fieldnames = [
        "First Name",
        "Last Name",
        "Email 1",
        "Email 2",
        "Phone 1",
        "Phone 2",
        "Company",
        "Job Title",
        "Notes",
        "Birthday",
        "Address",
    ]

    with open(output_csv_path, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for contact in contacts:
            writer.writerow(contact)

    print(f"✅ Successfully exported {len(contacts)} contacts to '{output_csv_path}'")


# === USAGE ===
# Call the function with the path to your vCard file and desired output CSV file
vcard_to_csv("./data/input_contacts.vcf", "output_contacts.csv")
