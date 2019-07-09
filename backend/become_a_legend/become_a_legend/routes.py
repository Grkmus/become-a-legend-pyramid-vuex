def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('post_register_form', '/register', request_method='POST')
    config.add_route('get_register_form', '/register')
    config.add_route('post_login_form', '/login', request_method='POST')
    config.add_route('get_login_form', '/login', request_method='GET')
    config.add_route('get_login_form_o', '/login', request_method='OPTIONS')
    config.add_route('logout', '/logout')

    config.add_route('get_all_players', '/player/all', request_method='GET')
    config.add_route('get_all_players_o', '/player/all', request_method='OPTIONS')
    config.add_route('create_player', '/player', request_method='POST')
    config.add_route('append_player_to_team', '/player/{id}/team/{team_id}', request_method='POST')
    config.add_route('append_player_to_event', '/player/{id}/event/{event_id}', request_method='POST')
    config.add_route('get_player', '/player/{id}', request_method='GET')
    config.add_route('get_player_o', '/player/{id}', request_method='OPTIONS')
    config.add_route('update_player', '/player/{id}', request_method='PUT')
    config.add_route('delete_player', '/player/{id}', request_method='DELETE')
    
    config.add_route('get_player_quiz_form', '/player/{id}/quiz')
    config.add_route('update_player_quiz', '/player/{id}/quiz', request_method='PUT')

    config.add_route('get_all_teams', '/team/all')
    config.add_route('add_team', '/team', request_method='POST')
    config.add_route('get_team', '/team/{id}')
    config.add_route('update_team', '/team/{id}', request_method='PUT')
    config.add_route('delete_team', '/team/{id}', request_method='DELETE')

    config.add_route('get_all_events', '/event/all', request_method='GET')
    config.add_route('get_all_events_o', '/event/all', request_method='OPTIONS')
    config.add_route('add_event', '/event', request_method='POST')
    config.add_route('get_event', '/event/{id}')
    config.add_route('update_event', '/event/{id}', request_method='PUT')
    config.add_route('delete_event', '/event/{id}', request_method='DELETE')

    
