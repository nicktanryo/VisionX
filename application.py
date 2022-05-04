import tkinter as tk
from turtle import heading

from setting import Setting

class Application():
    width = Setting.APPLICATION_WIDTH
    height = Setting.APPLICATION_HEIGHT

    def __init__(self, parent) -> None:
        self.main_frame = tk.Frame(parent, width=self.width, height=self.height, background=Setting.COLOR_GRAY)
