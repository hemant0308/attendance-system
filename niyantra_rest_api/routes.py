def includeme(config):
    config.add_route('login', '/login')

    config.add_route('attendee','/attendee')
    config.add_route('attendee_param', '/attendee/{id}')
    config.add_route('attendance', '/attendance')
