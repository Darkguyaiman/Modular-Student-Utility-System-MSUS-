<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:f4c20d,100:3776ab&height=200&section=header&text=Modular%20Student%20Utility%20System&fontSize=40&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=A%20Python%20App%20for%20Student%20Data%20Management&descAlignY=55&descAlign=50" width="100%" />
</div>

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.8+-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
<img src="https://img.shields.io/badge/Team-2%20Members-8e44ad?style=for-the-badge&logoColor=white" alt="2 Members"/>
<img src="https://img.shields.io/badge/Project-Principles%20of%20Programming-orange?style=for-the-badge" alt="Principles of Programming Project"/>


</div>

---

## Overview

The **Modular Student Utility System (MSUS)** is a collaborative Python application designed to provide comprehensive utility functions for analyzing student-related data including grades, names, and numerical operations. Built with modular programming principles, the system demonstrates clean code architecture, data persistence, and robust error handling.

<div align="center">

### Key Highlights

| Feature | Description |
|---------|-------------|
| **Modular Design** | Clean separation of concerns across multiple modules |
| **Data Persistence** | Automatic JSON/CSV save and load functionality |
| **Error Handling** | Comprehensive input validation and error recovery |
| **Analytics** | Built-in statistics and data analysis tools |

</div>

---

## Features

<table>
<tr>
<td width="50%">

### Mathematical Operations
- Count even/odd numbers in lists
- Calculate sum of digits
- Find averages and statistical ranges
- Advanced mathematical computations

### Text Processing
- Reverse sentence word order
- Convert numeric grades to letters
- Count words and characters
- Vowel/consonant analysis

</td>
<td width="50%">

### Student Management
- Add and remove student records
- Lookup student information
- Database statistics and analytics
- Bulk data operations

### File Operations
- JSON data persistence
- CSV import/export functionality
- Automatic backup systems
- Data integrity validation

</td>
</tr>
</table>

---

## Project Structure

```
MSUS/
├── main.py            — Central controller with menu interface
├── math_utils.py      — Mathematical processing utilities
├── text_utils.py      — Text manipulation and grading functions
├── student_utils.py   — Student data management and file operations
├── students.json      — Auto-generated student database
├── students.csv       — CSV export/import file
└── README.md          — Project documentation
```

<div align="center">
</div>


### Module Relationships

```mermaid
graph TD
    A[main.py] --> B[math_utils.py]
    A --> C[text_utils.py]
    A --> D[student_utils.py]
    D --> E[students.json]
    D --> F[students.csv]
    
    style A fill:#3498db,stroke:#2980b9,color:#fff
    style B fill:#e74c3c,stroke:#c0392b,color:#fff
    style C fill:#f39c12,stroke:#e67e22,color:#fff
    style D fill:#27ae60,stroke:#229954,color:#fff
    style E fill:#9b59b6,stroke:#8e44ad,color:#fff
    style F fill:#9b59b6,stroke:#8e44ad,color:#fff
```
