# 📋 Deal Creation Logic (Phase 2)

This document outlines the logic used in the `update_contacts.py` script to programmatically create **HubSpot deals** based on contact information.

---

## 🧠 Summary

We search all contacts in HubSpot whose **"Membership Notes" field contains the word "bought"**. When found, we assume the contact has made a purchase and create a new deal in HubSpot using:

- **Deal Name**: `{First Name} Glasses Purchase`
- **Pipeline ID**: `default`
- **Deal Stage ID**: `closedwon`

The deal is then associated back to the contact who triggered the match.

---

## 🛠️ Implementation Details

- Uses the `CONTAINS_TOKEN` filter on the property `hs_content_membership_notes`.
- Assumes `dealstage` and `pipeline` values are already configured correctly in HubSpot.
- Rate-limited with a 0.3s pause between API calls.
- Relies on `hubspot_tokens.py` for token authentication.

---

## ⚠️ To Improve / To-Do

- Refine keyword matching logic to handle more purchase terms (e.g. "ordered", "paid", etc.).
- Prevent duplicate deal creation (e.g. if the same person already has a deal).
- Log or flag contacts with ambiguous or missing names/emails.
