"""gradebook.stats — aggregate statistics over grade records."""


def average_per_student(records: list[dict]) -> dict[str, float]:
    """Map each student name to their average score, rounded to 2 decimals."""
    # TODO: implement
    pass


def subjects_offered(records: list[dict]) -> set[str]:
    """Return the set of unique subjects across all records."""
    # TODO: implement
    pass


def top_scorer(records: list[dict]) -> tuple[str, float]:
    """Return (name, average) for the student with the highest average."""
    # TODO: implement
    pass

def average_per_student(records: list[dict]) -> dict[str, float]:
    avg = {}
    for r in records: avg.setdefault(r["name"], []).append(r["score"])
    return {n: round(sum(v)/len(v), 2) for n, v in avg.items()}

def subjects_offered(records: list[dict]) -> set[str]:
    return {r["subject"] for r in records}

def top_scorer(records: list[dict]) -> tuple[str, float]:
    avg = average_per_student(records)
    name = max(avg, key=avg.get)
    return name, avg[name]

def passing_students(records: list[dict], threshold: float = 60.0) -> list[str]:
    avg = average_per_student(records)
    return sorted([n for n,a in avg.items() if a >= threshold])



