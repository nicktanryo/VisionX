import tkinter as tk
from setting import Setting

class Menu():
    width = Setting.MENU_WIDTH
    height = Setting.MENU_HEIGHT

    def __init__(self, parent, option_var, on_change) -> None:
        self.main_frame = tk.Frame(parent, width=self.width, height=self.height, background="#000")

        self.widget_image_sharpening = tk.Radiobutton(self.main_frame, text=Setting.OPTION_IMAGE_SHARPENING, variable=option_var, value=Setting.OPTION_IMAGE_SHARPENING, command=on_change)
        self.widget_image_sharpening.pack()
        self.widget_panorama = tk.Radiobutton(self.main_frame, text=Setting.OPTION_PANORAMA, variable=option_var, value=Setting.OPTION_PANORAMA, command=on_change)
        self.widget_panorama.pack()
        self.widget_hdr_image = tk.Radiobutton(self.main_frame, text=Setting.OPTION_HDR_IMAGE, variable=option_var, value=Setting.OPTION_HDR_IMAGE, command=on_change)
        self.widget_hdr_image.pack()
        self.widget_srcnn = tk.Radiobutton(self.main_frame, text=Setting.OPTION_SRCNN, variable=option_var, value=Setting.OPTION_SRCNN, command=on_change)
        self.widget_srcnn.pack()
