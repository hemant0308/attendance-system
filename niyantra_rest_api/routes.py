def includeme(config):
    config.add_route('login', '/login')

    config.add_route('student','/student')
    config.add_route('student_param', '/student/{id}')
    config.add_route('section','/student-group')
    config.add_route('section_session','/student-group/{section_id}/session')
    config.add_route('attendance_sheet', '/attendance-sheet')
    config.add_route('attendance', '/attendance-sheet/{attendance_sheet_id}/attendance')
