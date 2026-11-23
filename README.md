<div align="center">

# Contact Booklet — Python CLI Contact Manager
### Dual-Format Data Persistence, Structured CRUD Engine & Timestamped Diagnostics

[![Python](https://img.shields.io/badge/Python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![CLI](https://img.shields.io/badge/Interface-Command%20Line%20Interface-4D4D4D.svg?style=for-the-badge&logo=gnubash&logoColor=white)](https://en.wikipedia.org/wiki/Command-line_interface)
[![Storage](https://img.shields.io/badge/Data%20Formats-CSV%20%26%20JSON%20Sync-blue.svg?style=for-the-badge)](https://docs.python.org/3/library/json.html)
[![Logging](https://img.shields.io/badge/Diagnostics-Timestamped%20Error%20Logger-orange.svg?style=for-the-badge)](https://docs.python.org/3/library/logging.html)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

<p align="center">
  <b>A lightweight, resilient command-line contact management system featuring concurrent multi-format file serialization.</b><br>
  Built with defensive input validation, automated CSV-JSON synchronization, instant search indexing, and persistent error diagnostics.
</p>

---

</div>

## Executive Summary

Simple terminal applications frequently store data ephemerally or rely on fragile single-file storage without validation guards, leading to data loss or silent state corruption upon unexpected terminations.

**Contact Booklet** is an operational Python command-line utility architected for structured personal contact management. The application enforces complete **CRUD (Create, Read, Update, Delete)** operations backed by an automated dual-format synchronization layer: every mutation is atomically mirrored across both **CSV (tabular)** and **JSON (portable hierarchical)** stores. The engine incorporates strict regex validation for phone numbers and email domains, tabular terminal rendering, and a timestamped diagnostic error-logging daemon.

---

## System Architecture & Data Synchronization Pipeline

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              TERMINAL RUNTIME & MENU ROUTER                            │
└────────────────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
                       ┌─────────────────────────┐
                       │  Input Validation Guard │ ◄── Regex Format Verifier
                       │  (Name, Phone, Email)   │
                       └─────────────────────────┘
                                    │
       ┌────────────────────────────┼────────────────────────────┐
       ▼                            ▼                            ▼
┌──────────────┐             ┌──────────────┐             ┌──────────────┐
│ Create / Add │             │ Query / View │             │ Edit / Purge │
│ Auto-Index   │             │ Table Formatter│           │ Atomic Mutate│
└──────────────┘             └──────────────┘             └──────────────┘
       │                            │                            │
       └────────────────────────────┼────────────────────────────┘
                                    │
                                    ▼
                       ┌─────────────────────────┐
                       │ Dual-Format Sync Layer  │
                       └─────────────────────────┘
                                    │
                    ┌───────────────┴───────────────┐
                    ▼                               ▼
       ┌────────────────────────┐      ┌────────────────────────┐
       │   `contacts.csv`       │      │   `contacts.json`      │
       │ Tabular Export Engine  │      │ Portable Object Tree   │
       └────────────────────────┘      └────────────────────────┘
                    │                               │
                    └───────────────┬───────────────┘
                                    │
                         (On File I/O Exception)
                                    ▼
                       ┌─────────────────────────┐
                       │   `error_log.txt`       │
                       │ ISO-8601 Timestamp Log  │
                       └─────────────────────────┘
```

---

## Core Technical Features

| Feature Module | Technical Implementation | Practical Reliability Impact |
|:---|:---|:---|
| **Dual-Format Mirroring** | Programmatic simultaneous writes to both `contacts.csv` and `contacts.json`. | Guarantees data redundancy; seamless interoperability with spreadsheet tools and web APIs. |
| **Defensive Validation** | String normalization and regular expression pattern matching on phone and email entries. | Eliminates corrupted data entries before file serialization occurs. |
| **Index-Based Mutations** | Numerical primary key indexing allowing rapid single-record updates and deletions. | Prevents accidental modification of duplicate contact names. |
| **Tabular Console HUD** | Formatted column-aligned terminal output with header dividers. | Clear, structured legibility across varied terminal window widths. |
| **Structured Diagnostic Logger**| Exception handling blocks appending timestamped stack traces to `error_log.txt`. | Facilitates post-incident debugging without interrupting interactive user sessions. |

---

## Quickstart & Local Execution

```bash
# Clone the repository
git clone https://github.com/vsbeginner/ContactBooklet.git
cd ContactBooklet

# Run directly using Python (Zero external dependencies required)
python contact_booklet.py
```

### Example Interactive Session:
```text
====================================================
           CONTACT BOOKLET CLI MANAGER
====================================================
1. Add New Contact
2. View All Contacts
3. Search Contact by Name
4. Update Contact Details
5. Delete Contact
6. Export to External JSON
7. Import from External JSON
8. Exit Session
----------------------------------------------------
Select an option (1-8): 1

Enter Contact Name : Vinayak Sharma
Enter Phone Number : +91 9876543210
Enter Email Address: vsbeginner14@gmail.com
[SUCCESS] Contact successfully serialized to CSV and JSON stores.
```

---

## Candidate Profile & Institutional Details

- **Candidate Name**: Vinayak Sharma
- **Enrollment / Roll No**: 2501940012
- **GitHub Profile**: [@vsbeginner](https://github.com/vsbeginner)
- **LinkedIn Profile**: [Vinayak Sharma](https://www.linkedin.com/in/vinayak-sharma-24a8aa384/)
- **Email Contact**: vsbeginner14@gmail.com
- **Degree Program**: Master of Computer Applications (MCA)
- **Institution**: Department of Computer Science & Engineering, K.R. Mangalam University

---

<div align="center">
  <sub>Developed for academic excellence and technical portfolio showcase. Licensed under the <a href="LICENSE">MIT License</a>.</sub>
</div>
