import gooeypie as gp


class UserInterface:
    def __init__(self) -> None:
        self.width = 500
        self.height = 300

    def render_main_window(self):
        app = gp.GooeyPieApp("LockSmithy")  # title = "LockSmithy"
        app.width = self.width  # width = 500
        app.height = self.height  # height = 300

        app.run()


main = UserInterface()
main.render_main_window()
