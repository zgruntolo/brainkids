def create_game_ui_callback(game_logic, game_renderer):
    # Handle the call between GameLogic and Renderer
    def game_ui_callback(action, *args):
        if action == "request_player_name":
            game_renderer.request_player_name()
        elif action == "assign_username":
            game_logic.assign_username(*args)
        elif action == "request_game_difficulty":
            game_renderer.request_game_difficulty(*args)
        elif action == "assign_difficulty":
            game_logic.assign_difficulty(*args)
        elif action == "display_answer_buttons":
            game_renderer.show_answers_button(*args)
        elif action == "display_image":
            game_renderer.update_game_image(*args)
        elif action == "check_answer":
            game_logic.check_answer(*args)
        elif action == "show_correct_answer":
            game_renderer.show_correct_answer_message()
        elif action == "show_wrong_answer":
            game_renderer.show_wrong_answer_message()
        elif action == "display_game_results":
            game_renderer.display_game_results(*args)

    return game_ui_callback
