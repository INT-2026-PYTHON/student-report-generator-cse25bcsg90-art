"""gradebook.reports — build a printable report from grade records."""

# TODO: use a RELATIVE import to pull from the sibling stats module.
# from .stats import average_per_student, subjects_offered, top_scorer, passing_students


def format_report(records: list[dict]) -> str:
    """
    Build a human-readable, multi-line report.

    The report MUST include:
      - Total number of records
      - Sorted list of subjects offered
      - Average score for each student (alphabetical order)
      - The top scorer (name + average)
      - The list of passing students (threshold 60.0)
    """
    # TODO: implement
    pass
def format_report(records: list[dict]) -> str:
    lines = [f"Total records: {len(records)}"]
    subs = sorted({r["subject"] for r in records})
    lines.append("Subjects offered: " + ", ".join(subs))
    avg = {}
    for r in records: avg.setdefault(r["name"], []).append(r["score"])
    for n in sorted(avg):
        a = sum(avg[n]) / len(avg[n])
        lines.append(f"{n}: Average = {a:.2f}")
    top = max(avg, key=lambda n: sum(avg[n])/len(avg[n]))
    lines.append(f"Top scorer: {top}")
    passers = [n for n in avg if sum(avg[n])/len(avg[n]) >= 60]
    lines.append("Passing students: " + ", ".join(sorted(passers)))
    return "\n".join(lines)
