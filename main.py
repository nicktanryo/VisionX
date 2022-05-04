import tkinter as tk
from application import Application

from menu import Menu
from setting import Setting

class MyApp(tk.Tk):

    width = Setting.MENU_WIDTH
    height = Setting.MENU_HEIGHT

    def __init__(self, *args, **kwargs) -> None:
        tk.Tk.__init__(self, *args, **kwargs)

        self.main_frame = tk.Frame(self, width=self.width, height=self.height)
        self.main_frame.pack(fill=tk.BOTH, expand=tk.TRUE)

        self.application_selection = tk.StringVar(value=Setting.OPTION_IMAGE_SHARPENING)

        self.widget_menu_bar = Menu(parent=self.main_frame, option_var=self.application_selection, on_change=self.on_change_selection)
        self.widget_menu_bar.main_frame.pack(side=tk.TOP, fill=tk.X)
        self.widget_menu_bar.main_frame.pack_propagate(0)

        self.widget_application = Application(parent=self.main_frame)
        self.widget_application.main_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=tk.TRUE)

    def on_change_selection(self):
        print(str(self.application_selection.get()))

    @property
    def centre_position(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_cordinate = int((screen_width / 2) - (self.width / 2))
        y_cordinate = int((screen_height / 2) - (self.height / 2))

        return f"{self.width}x{self.height}+{x_cordinate}+{y_cordinate}"

        


def main():
    window_root = MyApp()
    window_root.title("VisionX")
    window_root.minsize(width=Setting.MIN_WINDOW_WIDTH, height=Setting.MIN_WINDOW_HEIGHT)
    window_root.eval('tk::PlaceWindow . center')
    # window_root.bind_all("<Button-1>", lambda event: event.widget.focus_set())

    window_root.mainloop()

if __name__ == "__main__":
    main()