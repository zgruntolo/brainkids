def create_ui_callback(game_logic, renderer):
    # Handle the call between GameLogic and Renderer
    def ui_callback(action, *args):
        if action == "get_name":
            renderer.get_name()
        elif action == "assign_username":
            game_logic.assign_username(*args)
        elif action == "get_difficulty":
            renderer.get_difficulty(*args)
        elif action == "assign_difficulty":
            game_logic.assign_difficulty(*args)
        elif action == "setup_ui":
            renderer.setup_gui_images()
            renderer.answers_button(*args)
        elif action == "show_image":
            renderer.next_image(*args)
        elif action == "check_answer":
            game_logic.check_answer(*args)
        elif action == "correct_answer":
            renderer.correct_answer()
        elif action == "wrong_answer":
            renderer.wrong_answer()
        elif action == "end_game":
            renderer.end_game(*args)

    return ui_callback
