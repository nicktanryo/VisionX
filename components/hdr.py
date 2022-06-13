import tkinter as tk

class HDR():

    def __init__(self, parent, sidebar_width, sidebar_height, image_preview_width, image_preview_height):
        self.widget_parameter_sidebar = tk.Frame(parent, width=sidebar_width, height=sidebar_height, background="#f00")
        self.widget_image_preview = tk.Frame(parent, width=image_preview_width, height=image_preview_height, background="#0f0")
