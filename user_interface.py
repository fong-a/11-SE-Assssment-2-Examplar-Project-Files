import gooeypie as gp


class UserInterface:
    def __init__(self) -> None:
        self.width = 500
        self.height = 300

    def render_main_window(self):
        app = gp.GooeyPieApp("LockSmithy")  # title = "LockSmithy"
        app.width = self.width  # width = 500
        app.height = self.height  # height = 300
        app.set_grid(2, 2)  # set_grid(rows = 7, columns = 4)

        # create title text
        title_label = gp.StyleLabel(app, "LockSmithy")
        title_label.font_weight = "bold"
        title_label.font_name = "Helvetica"
        title_label.font_size = 10
        app.add(title_label, 1, 1)

        # create subtitle text
        subtitle_label = gp.StyleLabel(app, "Forging strong passwords since 2023")
        title_label.font_style = "normal"
        title_label.font_weight = "bold"
        title_label.font_name = "Helvetica"
        title_label.font_size = 20
        app.add(subtitle_label, 2, 1)

        app.run()


main = UserInterface()
main.render_main_window()
