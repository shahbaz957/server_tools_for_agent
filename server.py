import sys
from pathlib import Path
from fastmcp import FastMCP

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

from server.tools import (
    marks_to_grade_points,
    calculate_semester_gpa,
    calculate_new_cgpa,
    required_gpa_for_target,
    get_semester_courses,
    get_remaining_credit_hours,
    save_report,
)

mcp = FastMCP("cgpa")
TOOLS = [marks_to_grade_points,
    calculate_semester_gpa,
    calculate_new_cgpa,
    required_gpa_for_target,
    get_semester_courses,
    get_remaining_credit_hours,
    save_report]

for tool in TOOLS:
    mcp.tool()(tool)

if __name__ == "__main__":
    mcp.run(transport="http", port=8000)