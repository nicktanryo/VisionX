import tkinter as tk
from setting import Setting

class Menu():
    width = Setting.MENU_WIDTH
    height = Setting.MENU_HEIGHT

    options = [
        Setting.OPTION_IMAGE_SHARPENING,
        Setting.OPTION_PANORAMA,
        Setting.OPTION_HDR_IMAGE,
        Setting.OPTION_SRCNN
    ]

    def __init__(self, parent, option_var, on_change) -> None:
        self.main_frame = tk.Frame(parent, width=self.width, height=self.height, background=Setting.COLOR_BACKGROUND)

        self.temp_radio_button = tk.Radiobutton(parent)

        self.radio_container = tk.Frame(self.main_frame, width=self.width, height=self.height, background=Setting.COLOR_BACKGROUND)
        self.radio_container.pack_propagate(0)
        self.radio_container.pack(fill=tk.Y)

        self.widget_options = {}
        for index, option in enumerate(self.options):
            self.widget_options[option] = tk.Radiobutton(
                self.radio_container, text=option, variable=option_var, value=option, command=on_change, 
                background=Setting.COLOR_BACKGROUND, foreground=Setting.COLOR_TEXT)
                
            self.widget_options[option].grid(row=0, column=index)

        self.radio_container.config(pady=(self.height - self.widget_options[self.options[0]].winfo_height()) // 4)

        # self.widget_image_sharpening = tk.Radiobutton(self.radio_container, text=Setting.OPTION_IMAGE_SHARPENING, variable=option_var, value=Setting.OPTION_IMAGE_SHARPENING, command=on_change)
        # self.widget_image_sharpening.grid(row=0, column=0, sticky=tk.W)
        # self.widget_panorama = tk.Radiobutton(self.radio_container, text=Setting.OPTION_PANORAMA, variable=option_var, value=Setting.OPTION_PANORAMA, command=on_change)
        # self.widget_panorama.grid(row=0, column=1)
        # self.widget_hdr_image = tk.Radiobutton(self.radio_container, text=Setting.OPTION_HDR_IMAGE, variable=option_var, value=Setting.OPTION_HDR_IMAGE, command=on_change)
        # self.widget_hdr_image.grid(row=0, column=2)
        # self.widget_srcnn = tk.Radiobutton(self.radio_container, text=Setting.OPTION_SRCNN, variable=option_var, value=Setting.OPTION_SRCNN, command=on_change)
        # self.widget_srcnn.grid(row=0, column=3, sticky=tk.E)
