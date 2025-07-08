# 📇 Apple to HubSpot Contact Automation

This project converts Apple Contacts exported as a `.vcf` (vCard) file into a clean, structured `.csv` file for easy import into **HubSpot**. It's built for small businesses that want to streamline their contact management and lay the foundation for automated customer engagement workflows.

---

## 🚀 Features
- Parses vCard (`.vcf`) contact exports from Apple devices
- Extracts key contact fields: First Name, Last Name, Email, Phone, Company
- Outputs a clean `.csv` formatted for HubSpot import
- Reusable Python script: drop in a new vCard file and convert it to csv for manual upload to Hubspot or other CRM tool

---

## 🧰 Tools Used
- Python 3.x
- `vobject` for parsing `.vcf` files
- `pandas` for structuring and exporting to `.csv`

---

## 📂 Folder Structure
```
.
├── input_contacts.vcf     # Your exported Apple Contacts file
├── vcard_to_csv.py      # Python script to run
├── output_contacts.csv    # Generated file, ready for HubSpot import
```

---

## 📦 Setup Instructions
1. Clone this repo or download the files
2. Install dependencies:
   ```bash
   pip install vobject pandas
   ```
3. Place your `.vcf` file in the root directory and name it `input_contacts.vcf`
4. Run the script:
   ```bash
   python vcard_to_csv.py
   ```
5. Upload `output_contacts.csv` to HubSpot via manual import

---

## 🔁 Optional: Automate with Zapier (Future Phase)
- Set up Zapier workflows triggered by HubSpot activity:
  - Send emails to new or updated contacts
  - Notify staff or add calendar events
  - Launch customer check-in sequences

---

## 🧠 Why This Exists
Small businesses often have customer data trapped in Apple Contacts or spreadsheets.
This tool unlocks that data and sets the stage for CRM-driven automation — no fancy tools or subscriptions required.

---

## 👤 Built By
**Jordan Urbaczek**  
Project Manager & Data Consultant  
[@JordanUrbaczek on LinkedIn](https://www.linkedin.com/in/jordanurbaczek/)

---

## 📄 License
MIT License – Free to use and modify.
