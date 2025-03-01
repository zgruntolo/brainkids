def create_game_ui_callback(game_logic, game_renderer):
    # Creates a callback function to handle communication between GameLogic and Renderer.

    action_map = {
        "request_player_name": game_renderer.request_player_name,
        "assign_player_name": game_logic.assign_player_name,
        "request_game_difficulty": game_renderer.request_game_difficulty,
        "set_game_difficulty": game_logic.set_game_difficulty,
        "display_answers_button": game_renderer.display_answers_button,
        "display_image": game_renderer.display_image,
        "verify_player_answer": game_logic.verify_player_answer,
        "show_correct_answer_message": game_renderer.show_correct_answer_message,
        "show_wrong_answer_message": game_renderer.show_wrong_answer_message,
        "display_game_results": game_renderer.display_game_results,
    }

    def game_ui_callback(action, *args):
        # Executes the corresponding function based on the given action
        if action in action_map:
            action_map[action](*args)

    return game_ui_callback
