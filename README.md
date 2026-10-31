# Contact Management System

**PS No. 7 — Python 3**

A console-based contact book application supporting **Create, Read, Update and Delete (CRUD)** operations with search by name.

## Features

- Add a contact with name, phone number and email
- View all contacts
- Search contacts by name
- Update a contact's phone number
- Delete a contact
- Phone number validation: exactly 10 digits
- Duplicate phone numbers are prevented
- Loop-driven menu with Exit option
- Contacts are stored as a list of dictionaries

## Concepts Used

Python Lists, Dictionaries, Functions, Loops, Conditions, String Methods and CRUD operations.

## Run

```bash
python contact_management.py
```

## Required Test Cases

1. Add **Ravi Sharma**, phone `9876543210`, email `ravi@mail.com` → `Contact added: Ravi Sharma | 9876543210`
2. Add **Neha Rao**, phone `9999999999` → accepted as an exactly 10-digit number.
3. Invalid phone such as `98765` → `Invalid phone number. Enter exactly 10 digits.`; duplicate `9876543210` → `Contact with this number already exists.`
4. Search Ravi, update Ravi's phone to `9123456780`, then delete Neha Rao.

## Project Structure

```text
Contact-Managment-System/
├── contact_management.py
└── README.md
```

## Author

Ayush Kumar
