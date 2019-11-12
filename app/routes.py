def includeme(config):
    version = config.get_settings().get('api_version','/v1')
    config.add_route('user',version+'/user')
    config.add_route('user_param',version+'/user/{user_id}')
    config.add_route('login', version+'/login')

    config.add_route('student',version+'/student')
    config.add_route('student_param', version+'/student/{student_id}')
    config.add_route('section',version+'/section')
    config.add_route('section_session',version+'/section/{section_id}/sessions')
    config.add_route('section_student', version+'/section/{section_id}/students')
    config.add_route('attendance_sheet', version+'/attendance-sheet')
    config.add_route('attendance', version+'/attendance-sheet/{attendance_sheet_id}/attendance')
    config.add_route('submit_attendance', version+'/attendance-sheet/{attendance_sheet_id}/submit')
    config.add_route('teacher',version+'/teacher')
    config.add_route('teacher_session', version+'/teacher/{teacher_id}/sessions')

