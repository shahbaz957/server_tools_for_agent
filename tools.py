import os 
def marks_to_grade_points(marks: int) -> float | str:
    """Converts a numerical mark into grade points based on a standard university scale.
    please  use this tool whenever you need to map a student's numerical score (0 to 100)
    to its corresponding grade point value (0.0 to 4.0) for GPA computation.
    """
    if not isinstance(marks, int) or marks < 0 or marks > 100:
        return "Error: marks must be an integer between 0 and 100"

    if marks >= 85:
        return 4.0
    elif marks >= 80:
        return 3.7
    elif marks >= 75:
        return 3.3
    elif marks >= 70:
        return 3.0
    elif marks >= 65:
        return 2.7
    elif marks >= 61:
        return 2.3
    elif marks >= 58:
        return 2.0
    elif marks >= 55:
        return 1.7
    elif marks >= 50:
        return 1.0
    else:
        return 0.0


def calculate_semester_gpa(
    grade_points: list[float], credit_hours: list[float]
) -> float | str:
    """Calculates the weighted semester Grade Point Average (GPA) from course grade points and credit hours.
    please use this tool to compute a overall semester GPA given a student's list of earned grade points and their respective course credit hours. 
    """
    if not grade_points or not credit_hours:
        return "Error: grade_points and credit_hours lists cannot be empty"

    if len(grade_points) != len(credit_hours):
        return "Error: grade_points and credit_hours lists must have equal lengths"

    if any(gp < 0.0 or gp > 4.0 for gp in grade_points):
        return "Error: all grade points must be between 0.0 and 4.0"

    if any(ch <= 0 for ch in credit_hours):
        return "Error: credit hours must be greater than 0"

    total_credits = sum(credit_hours)
    total_quality_points = sum(gp * ch for gp, ch in zip(grade_points, credit_hours))

    return round(total_quality_points / total_credits, 2) # takes upto 2 digits after decimal

def calculate_new_cgpa(current_cgpa: float, completed_credit_hours: float, semester_gpa: float, semester_credit_hours: float) -> float | str :
    """Calculate the new CGPA from current_cgpa , completed_credit_hours , semester gpa and semester_credit_hours. Please use this tool to calculate the new cgpa of the student"""
    if current_cgpa < 0.0 or current_cgpa > 4.0:
        return "Error: current_cgpa must be between 0.0 and 4.0"

    if semester_gpa < 0.0 or semester_gpa > 4.0:
        return "Error: semester_gpa must be between 0.0 and 4.0"

    if completed_credit_hours < 0.0:
        return "Error: completed_credit_hours cannot be negative"

    if semester_credit_hours <= 0.0:
        return "Error: semester_credit_hours must be greater than 0"
    new_cgpa = ((current_cgpa*completed_credit_hours) + (semester_gpa*semester_credit_hours)) / (completed_credit_hours + semester_credit_hours)
    return round(new_cgpa, 2)

def required_gpa_for_target(target_cgpa: float, current_cgpa: float, completed_credit_hours: float,
remaining_credit_hours: float) -> float|str :
    """Calculate the GPA needed to reach a target , by using the target_cpga , current cgpa , completed credit hours and remaining credit hours
    please us this tool to calculate the required cgpa for a student to reach tto the target cpga
    PARAMS : target_cgpa: float,
     - current_cgpa: float
     - completed_credit_hours: float
     - remaining_credit_hours: float
    """
    if target_cgpa < 0.0 or target_cgpa > 4.0:
        return "Error: target_cgpa must be between 0.0 and 4.0"

    if current_cgpa < 0.0 or current_cgpa > 4.0:
        return "Error: current_cgpa must be between 0.0 and 4.0"

    if completed_credit_hours < 0.0:
        return "Error: completed_credit_hours cannot be negative"

    if remaining_credit_hours <= 0.0:
        return "Error: remaining_credit_hours must be greater than 0"
    
    total_credit_hours = completed_credit_hours + remaining_credit_hours

    required_gpa = (
        (target_cgpa * total_credit_hours) - (current_cgpa * completed_credit_hours)
    ) / remaining_credit_hours

    return round(required_gpa, 2)


def get_semester_courses(semester: int) -> str:
    """Retrieves the list of courses and their credit hours for a specific semester in the BS Computer Science program.
    Use this tool whenever you need to fetch the course code, course title, or credit hours
    for a given semester (1 to 8) to construct course lists, compute semester totals"""
    if not isinstance(semester, int) or semester < 1 or semester > 8:
        return "Error: semester must be an integer between 1 and 8"

    courses_data = {
        1: [
            ("MS-251", "Probability & Statistics", 3.0),
            ("GE-160", "Applications of ICT", 3.0),
            ("GE-169", "Applied Physics", 3.0),
            ("GE-167", "Discrete Structures", 3.0),
            ("HQ-001", "Quran Translation - I", 0.5),
            ("GE-190", "Functional English", 3.0),
        ],
        2: [
            ("CC-112", "Programming Fundamentals", 3.0),
            ("CC-112-L", "Programming Fundamentals Lab", 1.0),
            ("CC-110", "Digital Logic Design", 2.0),
            ("CC-110-L", "Digital Logic Design Lab", 1.0),
            ("MS-252", "Linear Algebra", 3.0),
            ("GE-191", "Expository Writing", 3.0),
            ("GE-163", "Islamic Studies", 2.0),
            ("HQ-002", "Quran Translation - II", 0.5),
        ],
        3: [
            ("CC-211", "Object Oriented Programming", 3.0),
            ("CC-211-L", "Object Oriented Programming Lab", 1.0),
            ("CC-215", "Database Systems", 3.0),
            ("CC-215-L", "Database Systems Lab", 1.0),
            ("CC-210", "Computer Organization & Assembly Language", 3.0),
            ("GE-162", "Calculus & Analytical Geometry", 3.0),
            ("GE-192", "Introduction to Management", 2.0),
            ("HQ-003", "Quran Translation - III", 0.5),
        ],
        4: [
            ("CC-213", "Data Structures", 3.0),
            ("CC-213-L", "Data Structures Lab", 1.0),
            ("CC-312", "Information Security", 3.0),
            ("CC-214", "Computer Networks", 3.0),
            ("CC-212", "Software Engineering", 3.0),
            ("DC-220", "Advanced Database Management Systems", 3.0),
            ("HQ-004", "Quran Translation - IV", 0.5),
        ],
        5: [
            ("CC-313", "Analysis of Algorithms", 3.0),
            ("CC-310", "Artificial Intelligence", 3.0),
            ("DC-320", "Theory of Automata and Formal Languages", 3.0),
            ("DC-321", "Human Computer Interaction", 3.0),
            ("DC-322", "Computer Architecture", 3.0),
            ("EC-330", "Web Technologies / Elective", 3.0),
            ("HQ-005", "Quran Translation - V", 0.5),
        ],
        6: [
            ("CC-311", "Operating Systems", 3.0),
            ("EC-333", "Mobile Application Development / Elective", 3.0),
            ("EC-324", "Software Construction & Development / Elective", 3.0),
            ("EC-335", "Machine Learning / Elective", 3.0),
            ("EC-334", "Game Design and Development / Elective", 3.0),
            ("MS-253", "Multivariable Calculus", 3.0),
            ("HQ-006", "Quran Translation - VI", 0.5),
        ],
        7: [
            ("CC-411", "Final Year Project - I", 2.0),
            ("DC-328", "Parallel & Distributed Computing", 3.0),
            ("EC-345", "Computer Vision / Elective", 3.0),
            ("EC-425", "Software Quality Engineering / Elective", 3.0),
            ("MS-254", "Technical and Business Writing", 3.0),
            ("GE-263", "Entrepreneurship", 2.0),
            ("GE-262", "Professional Practices", 2.0),
            ("HQ-007", "Quran Translation - VII", 0.5),
        ],
        8: [
            ("CC-412", "Final Year Project - II", 4.0),
            ("DC-421", "Compiler Construction", 3.0),
            ("UE-272", "Introduction to Marketing", 3.0),
            ("GE-168", "Ideology and Constitution of Pakistan", 2.0),
            ("GE-363", "Civics and Community Engagement", 2.0),
            ("HQ-008", "Quran Translation - VIII", 0.5),
        ],
    }

    courses = courses_data[semester]
    formatted_list = [f"{code}: {title} ({ch} CH)" for code, title, ch in courses]
    return f"Semester {semester} Courses:\n" + "\n".join(formatted_list)


def get_remaining_credit_hours(current_semester: int) -> float | str:
    """Calculates the total remaining credit hours from a given current semester.
    use this tool whenever you need to determine how many credit hours a student has left to complete
the degree or when evaluating target CGPA feasibility and have to widen the window to adjust the target GCPA under 4 for correcteness or determining future credit horizons.
    ALWAYS GIVE THE SEMESTER IN WHICH THE STUDENT IS CURRENTLY ENROLLED
    """
    if not isinstance(current_semester, int) or current_semester < 1 or current_semester > 8:
        return "Error: semester must be an integer between 1 and 8"

    semester_credit_hours = {
        1: 15.5,
        2: 15.5,
        3: 16.5,
        4: 16.5,
        5: 18.5,
        6: 18.5,
        7: 18.5,
        8: 14.5,
    }

    remaining_ch = sum(credit_hours for sem, credit_hours in semester_credit_hours.items() if sem >= current_semester
    )
    return float(remaining_ch)

def save_report(filename: str, content: str) -> str : 
    """Save a summary and return a confirmation. use this tool whenever you need to persist a final generated report to the filesystem"""
    if not isinstance(filename, str) :
        return "Error: filename must be a non-empty string"

    if not isinstance(content, str):
        return "Error: content must be a string"
    try:
        # Normalize and prevent directory traversal out of local bounds
        safe_filename = os.path.basename(filename)
        if not safe_filename:
            return "Error: invalid filename provided"

        with open(safe_filename, "w", encoding="utf-8") as file:
            file.write(content)

        return f"Success: Report saved to {safe_filename}"
    except Exception as e:
        return f"Error: Failed to save file - {str(e)}"
