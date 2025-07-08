# 📇 Anywhere Vision Contact Automation Project

This project is part of a 3-phase automation initiative for **Anywhere Vision**, an optician business aiming to improve how they manage and engage with their customer base using HubSpot.

This repo currently documents **Phase 1: Contact Setup**, which includes a working Python script for converting Apple Contacts to a structured CSV. It will expand to include Phases 2 and 3 as development progresses (tracked in separate branches and folders). that converts Apple Contacts exported as a `.vcf` (vCard) file into a structured `.csv` file ready for HubSpot import.

---

## 📌 Project Phases

### ✅ Phase 1: Setup (Complete)
- Export Apple Contacts as `.vcf`
- Convert to CSV using Python
- Upload CSV manually into HubSpot
- Centralize and structure baseline contact data

### 🛠 Phase 2: Programmatic Contact Updating *(In Progress)*
- Build a repeatable Python system to sync updated contact details from Apple Contacts to HubSpot
- Eliminate the need for manual updates in the HubSpot interface
- Actively developed in the `dev-phase-2` branch

### 🚀 Phase 3: Marketing Automations *(Coming Soon)*
- Use HubSpot + Zapier to trigger email campaigns, reminders, or alerts based on contact data changes
- Focus on re-engagement and retention workflows
- Development in the `dev-phase-3` branch

---

## 🚀 Features (Phase 1)
- Parses Apple vCard `.vcf` contact exports
- Extracts key fields: First Name, Last Name, Email, Phone, Company
- Outputs a clean `.csv` ready for HubSpot manual import
- Simple, repeatable script

---

## 🧰 Tools Used
- Python 3.x
- `vobject` for vCard parsing
- `pandas` for data transformation

---

## 📂 Folder Structure
```
.
├── convert_to_csv.py             # Phase 1 script (vCard to CSV)
├── output_contacts.csv           # HubSpot-ready output
├── data/
│   └── input_contacts.vcf        # Sample Apple Contact export
├── phase-2-sync/
│   └── update_contacts.py        # (Coming soon) Script to update HubSpot via API
├── phase-3-automation/
│   └── zapier_workflows.md       # (Coming soon) Notes & logic for marketing automation
├── docs/
│   └── project_overview.md       # Project summary, goals, and phase notes
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
   python convert_to_csv.py
   ```
5. Upload `output_contacts.csv` to HubSpot manually

---

## 🔁 Next Phases
- Follow development of Phase 2 and 3 in `dev-phase-2` and `dev-phase-3` branches
- GitHub Issues and enhancements will be added as work progresses

---

## 👤 Built By
**Jordan Urbaczek**  
Project Manager & Data Consultant  
[@JordanUrbaczek on LinkedIn](https://www.linkedin.com/in/jordanurbaczek/)

---

## 📄 License
MIT License – Free to use and modify.
