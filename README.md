# 🏦 OS Lab Assignment 2 — Banker's Algorithm for Deadlock Avoidance

## 📌 Problem Statement

Deadlock is a situation in operating systems where a set of processes are unable to proceed because each is waiting for resources held by others. **Banker's Algorithm** is a deadlock avoidance technique that ensures the system remains in a safe state.

---

## 🎯 Objectives

- Understand deadlock concepts in operating systems
- Implement Banker's Algorithm for deadlock avoidance
- Calculate the Need Matrix using `Need = Maximum - Allocation`
- Determine safe/unsafe state using the Safety Algorithm
- Find the safe sequence of process execution

---

## 🛠️ Tools & Technology

| Tool | Details |
|------|---------|
| Language | Python 3.x |
| Libraries | `os`, `time` (built-in) |
| IDE | Visual Studio Code |
| Platform | Linux (Ubuntu) via VirtualBox |

---

## 📁 Repository Structure

```
OS-Lab-Assignment-2/
│
├── bankers_algorithm.py              # Main Python source code
├── OS_Lab_Assignment2_Report.docx    # Summary report
├── README.md                         # This file
│
├── Task 1 — System Input.png         # Screenshot: Input entry
├── Task 2 — Need Matrix.png          # Screenshot: Need matrix table
├── Task 3 — Safety Algorithm.png     # Screenshot: Safety algorithm execution
├── Task 4 — Safe Sequence.png        # Screenshot: Safe sequence output
└── Task 5 — Result Analysis.png      # Screenshot: Final result
```

---

## 🚀 How to Run

### Prerequisites
Make sure Python 3 is installed:
```bash
python3 --version
```

### Run the program
```bash
python3 bankers_algorithm.py
```

### Sample Input
```
Enter number of processes: 5
Enter number of resource types: 3

Allocation Matrix:
P0: 0 1 0
P1: 2 0 0
P2: 3 0 2
P3: 2 1 1
P4: 0 0 2

Maximum Matrix:
P0: 7 5 3
P1: 3 2 2
P2: 9 0 2
P3: 2 2 2
P4: 4 3 3

Available Resources: 3 3 2
```

---

## 📋 Tasks Overview

### Task 1 — System Input and Data Representation
- Input number of processes and resource types
- Input Allocation Matrix, Maximum Matrix, Available Resources

### Task 2 — Need Matrix Calculation
- Formula: `Need = Maximum - Allocation`
- Displays the complete Need Matrix

### Task 3 — Banker's Safety Algorithm
- Initialize Work = Available
- Find processes where Need ≤ Work
- Update Work after each allocation

### Task 4 — Safe Sequence Determination
- Stores and displays the safe execution order

### Task 5 — Result Analysis
- Identifies safe/unsafe state
- Explains the result with justification

---

## ✅ Sample Output

```
System is in a SAFE STATE.

Safe Sequence: P1 -> P3 -> P4 -> P0 -> P2

Explanation:
The system can allocate resources to each process
in the above order without causing a deadlock.
```

---

## 📚 Theory

The **Banker's Algorithm** works like a bank:
- The bank (OS) has limited resources (cash)
- Customers (processes) request resources (loans)
- The bank only grants a request if it can still satisfy all other customers
- This ensures the system never enters an **unsafe state**

**Key Formula:**
```
Need[i][j] = Maximum[i][j] - Allocation[i][j]
```

---

