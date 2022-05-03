import tkinter as tk
from turtle import heading

class Application():
    width = 1280
    height = 670

    def __init__(self, parent) -> None:
        self.main_frame = tk.Frame(parent, width=self.width, height=self.height, background="#555")
