import tkinter as tk
from setting import Setting
from components.image_sharpening import ImageSharpening
from components.panorama import Panorama
from components.hdr import HDR
from components.srcnn import SRCNN

class Application():
    width = Setting.APPLICATION_WIDTH
    height = Setting.APPLICATION_HEIGHT

    sidebar_width = Setting.APPLICATION_PARAMETER_SIDEBAR_WIDTH
    sidebar_height = Setting.APPLICATION_PARAMETER_SIDEBAR_HEIGHT

    image_preview_width = Setting.APPLICATION_IMAGE_PREVIEW_WIDTH
    image_preview_height = Setting.APPLICATION_IMAGE_PREVIEW_HEIGHT

    cached_widget = {}
    widget_mapping = {
        Setting.OPTION_IMAGE_SHARPENING: ImageSharpening,
        Setting.OPTION_PANORAMA: Panorama,
        Setting.OPTION_HDR_IMAGE: HDR,
        Setting.OPTION_SRCNN: SRCNN
    }

    def __init__(self, parent, default_operator) -> None:
        self.main_frame = tk.Frame(parent, width=self.width, height=self.height)

        self.prepare_operator_widget(default_operator)
        self.allocate_operator_widget()
        self.render_widgets()


    def prepare_operator_widget(self, operator):
        operator_object = None
        if operator in self.cached_widget:
            operator_object = self.cached_widget[operator]
        else:
            operator_object = self.create_operator(operator)
            self.cached_widget[operator] = operator_object 

        self.operator = operator_object


    def create_operator(self, operator):
        return self.widget_mapping[operator](self.main_frame, 
                                             sidebar_width=self.sidebar_width, sidebar_height=self.sidebar_height,
                                             image_preview_width=self.image_preview_width, image_preview_height=self.image_preview_height)


    def allocate_operator_widget(self):
        self.widget_parameter_sidebar = self.operator.widget_parameter_sidebar
        self.widget_image_preview = self.operator.widget_image_preview

    def application_onchange_selection(self, selection):
        self.clear_previous_widgets()
        self.prepare_operator_widget(selection)
        self.allocate_operator_widget()
        self.render_widgets()
        print(f"current selection: {selection}")


    def clear_previous_widgets(self):
        self.widget_parameter_sidebar.forget()
        self.widget_image_preview.forget()


    def render_widgets(self):
        self.widget_parameter_sidebar.pack(side=tk.LEFT, fill=tk.Y)
        self.widget_image_preview.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

