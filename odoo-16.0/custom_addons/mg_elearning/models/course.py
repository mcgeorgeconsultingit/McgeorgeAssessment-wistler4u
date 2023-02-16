from odoo import api, fields, models, _, tools


class Course(models.Model):
    _name = "elearning.course"
    _description = "E-learning Courses"
    _order = "course_code"

    school_name = fields.Char(
        string="School Name",
        required=True,
        index="trigram",
        tracking=True,
        help="Enter school " "name.",
    )
    level = fields.Char(string="Level", required=True, help="Enter level.")
    academic_year = fields.Char(string="Academic year", required=True, help="Enter academic year.")
    semester = fields.Char(string="Semester", required=True, help="Enter semester")
    faculty = fields.Char(string="Faculty", required=True, help="Enter faculty.")
    department = fields.Char(string="Department", required=True, help="Enter department.")
    course_title = fields.Char(string="Course title", required=True, help="Enter course title.")
    course_code = fields.Char(
        string="Course code", required=True, size=8, help="Enter course code."
    )
