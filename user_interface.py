import gooeypie as gp


class UserInterface:
    def __init__(self) -> None:
        self.width = 500
        self.height = 300

    def render_main_window(self):
        app = gp.GooeyPieApp("LockSmithy")  # title = "LockSmithy"
        app.width = self.width  # width = 500
        app.height = self.height  # height = 300
        app.set_grid(7, 4)  # set_grid(rows = 7, columns = 4)

        # create title text
        styled_label = gp.StyleLabel(app, "LockSmithy")
        styled_label.font_style = "normal"
        styled_label.font_weight = "bold"
        styled_label.font_name = "Helvetica"
        styled_label.font_size = 40
        app.add(styled_label, 1, 1)

        app.run()


main = UserInterface()
main.render_main_window()
