# ============================================================
# Banker's Algorithm for Deadlock Avoidance
# Course: Operating System Lab (ENCA252)
# Program: BCA (AI & DS)
# RAKESH G  2401201064  BCA (AI & DS) - 'B'
# ============================================================

import os
import time

# -------------------------------------------------------
# Task 1: System Input and Data Representation
# -------------------------------------------------------

def get_system_input():
    """
    Accepts number of processes, resources,
    allocation matrix, maximum matrix, and available resources.
    """
    print("=" * 55)
    print("   BANKER'S ALGORITHM - Deadlock Avoidance")
    print("=" * 55)

    n = int(input("\nEnter number of processes: "))
    m = int(input("Enter number of resource types: "))

    print("\n--- Input Allocation Matrix ---")
    print(f"(Enter {m} values per process, space-separated)\n")
    allocation = []
    for i in range(n):
        row = list(map(int, input(f"  Allocation for P{i}: ").split()))
        allocation.append(row)

    print("\n--- Input Maximum Matrix ---")
    print(f"(Enter {m} values per process, space-separated)\n")
    maximum = []
    for i in range(n):
        row = list(map(int, input(f"  Maximum for P{i}: ").split()))
        maximum.append(row)

    print("\n--- Input Available Resources ---")
    available = list(map(int, input(f"  Available ({m} values): ").split()))

    return n, m, allocation, maximum, available


# -------------------------------------------------------
# Task 2: Need Matrix Calculation
# -------------------------------------------------------

def calculate_need(n, m, allocation, maximum):
    """
    Need[i][j] = Maximum[i][j] - Allocation[i][j]
    """
    need = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(maximum[i][j] - allocation[i][j])
        need.append(row)
    return need


def display_matrices(n, m, allocation, maximum, available, need):
    """Display all matrices in a readable table format."""
    print("\n" + "=" * 55)
    print("           SYSTEM STATE")
    print("=" * 55)

    header = f"{'Process':<10}"
    for j in range(m):
        header += f"{'Alloc R'+str(j):<12}"
    for j in range(m):
        header += f"{'Max R'+str(j):<12}"
    for j in range(m):
        header += f"{'Need R'+str(j):<12}"
    print(header)
    print("-" * (10 + 12 * m * 3))

    for i in range(n):
        row = f"{'P'+str(i):<10}"
        for j in range(m):
            row += f"{allocation[i][j]:<12}"
        for j in range(m):
            row += f"{maximum[i][j]:<12}"
        for j in range(m):
            row += f"{need[i][j]:<12}"
        print(row)

    print(f"\n  Available Resources: {available}")
    print("=" * 55)


# -------------------------------------------------------
# Task 3 & 4: Banker's Safety Algorithm + Safe Sequence
# -------------------------------------------------------

def bankers_safety_algorithm(n, m, allocation, need, available):
    """
    Safety Algorithm:
    1. Work = Available
    2. Finish[i] = False for all i
    3. Find process i where Finish[i]=False and Need[i] <= Work
    4. Work = Work + Allocation[i], Finish[i] = True
    5. Repeat until all finished or no progress
    Returns: (is_safe, safe_sequence)
    """
    work = available[:]          # Step 1: Work = Available
    finish = [False] * n         # Step 2: Finish array
    safe_sequence = []

    print("\n--- Running Safety Algorithm ---\n")

    count = 0
    while count < n:
        found = False
        for i in range(n):
            if not finish[i]:
                # Step 3: Check if Need[i] <= Work
                can_allocate = all(need[i][j] <= work[j] for j in range(m))
                if can_allocate:
                    # Step 4: Allocate resources
                    print(f"  Process P{i} can execute.")
                    print(f"    Need:       {need[i]}")
                    print(f"    Work before:{work}")
                    work = [work[j] + allocation[i][j] for j in range(m)]
                    print(f"    Work after: {work}\n")
                    finish[i] = True
                    safe_sequence.append(i)
                    found = True
                    count += 1

        # Step 5: No process could be allocated — unsafe
        if not found:
            break

    is_safe = all(finish)
    return is_safe, safe_sequence


# -------------------------------------------------------
# Task 5: Result Analysis
# -------------------------------------------------------

def display_result(is_safe, safe_sequence):
    """Display final result with explanation."""
    print("=" * 55)
    print("              RESULT ANALYSIS")
    print("=" * 55)

    if is_safe:
        seq = " -> ".join([f"P{i}" for i in safe_sequence])
        print(f"\n  ✅ System is in a SAFE STATE.")
        print(f"\n  Safe Sequence: {seq}")
        print("""
  Explanation:
  The system can allocate resources to each process
  in the above order without causing a deadlock.
  Each process can complete and release its resources,
  allowing the next process to proceed safely.
  This matches the theoretical expectation of
  Banker's Algorithm — deadlock is avoided by
  ensuring the system never enters an unsafe state.
        """)
    else:
        print(f"\n  ❌ System is in an UNSAFE STATE.")
        print("""
  Explanation:
  No safe sequence exists. The system may deadlock
  because processes are holding resources that others
  need, creating a circular wait. Banker's Algorithm
  correctly identifies this unsafe state and would
  deny any further resource requests that could
  lead to this situation.
        """)
    print("=" * 55)


# -------------------------------------------------------
# Main Program
# -------------------------------------------------------

def main():
    os.system('clear')  # Clear terminal (Linux)

    # Task 1: Input
    n, m, allocation, maximum, available = get_system_input()

    # Task 2: Need Matrix
    need = calculate_need(n, m, allocation, maximum)
    display_matrices(n, m, allocation, maximum, available, need)

    time.sleep(1)

    # Task 3 & 4: Safety Algorithm + Safe Sequence
    is_safe, safe_sequence = bankers_safety_algorithm(
        n, m, allocation, need, available
    )

    # Task 5: Result Analysis
    display_result(is_safe, safe_sequence)


if __name__ == "__main__":
    main()