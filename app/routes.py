def includeme(config):
    config.add_route('user','/user')
    config.add_route('user_param','/user/{user_id}')
    config.add_route('login', '/login')

    config.add_route('student','/student')
    config.add_route('student_param', '/student/{student_id}')
    config.add_route('section','/section')
    config.add_route('section_session','/section/{section_id}/sessions')
    config.add_route('section_student', '/section/{section_id}/students')
    config.add_route('attendance_sheet', '/attendance-sheet')
    config.add_route('attendance', '/attendance-sheet/{attendance_sheet_id}/attendance')
    config.add_route('submit_attendance', '/attendance-sheet/{attendance_sheet_id}/submit')
    config.add_route('teacher','/teacher')
    config.add_route('teacher_session', '/teacher/{teacher_id}/sessions')

