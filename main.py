import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
import customtkinter as ctk
import sys
import os
import random

from Text_To_Speech import tts
from YTDownload import ytd

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

appWidth, appHeight = 900, 700

# app = ctk.CTk()
# app.geometry(f"{appWidth}x{appHeight}")
# app.title("PyMate")
#
# frame_1 = ctk.CTkFrame(master=app)
# frame_1.pack(pady=20, padx=60, fill="both", expand=True)
#
# label_1 = ctk.CTkLabel(master=frame_1, justify=tkinter.LEFT)
# label_1.pack(pady=10, padx=10)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("PyMate")
        self.geometry(f"{appWidth}x{appHeight}")

        # 4x4 Grid Layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3, 4), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        # self.mainFrame = ctk.CTkFrame(self)
        # self.mainFrame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        # self.mainFrame.grid_rowconfigure(4, weight=1)


        self.tabView = ctk.CTkTabview(self, width=300, corner_radius=20)
        self.tabView.grid(row=0, column=0, rowspan=3, columnspan=4, padx=10, pady=(0, 10), sticky="nsew")

        self.tabView.add("Text To Speech")
        self.tabView.add("YT Video Download")

        # self.yttabObject = tts.TextToSpeech(self, self.tabView)

        self.ttsFrame = tts.TextToSpeechFrame(self, tabView=self.tabView, header_name="TTS")
        self.ytdFrame = ytd.YTVideoDownloadFrame(self, tabView=self.tabView, header_name="YT Download")
        # self.ttsFrame.entry.grid(row=1, column=1, columnspan=1, padx=(10, 0), pady=(20, 20), sticky="nsew")
        # self.ttsFrame.grid(row=0, column=0, padx=200, pady=200)

        # self.tabView.tab("Text To Speech").grid_columnconfigure(0, weight=1)
        # self.tabView.tab("YT Video Download").grid_columnconfigure(0, weight=1)

        # Appearance Label
        self.appearanceLabel = ctk.CTkLabel(self, text="Appearance")
        self.appearanceLabel.grid(row=3, column=0, sticky="w", padx=(20, 0), pady=(0, 0))
        
        # Appearance Option Menu
        self.appearanceOptionemenu = ctk.CTkOptionMenu(self, values=["System", "Light", "Dark"], command=self.change_appearance_mode_event)
        self.appearanceOptionemenu.grid(row=3, column=0, sticky="w", padx=(100, 0), pady=(10, 10))

        # Color Theme Label
        self.zoomLabel = ctk.CTkLabel(self, text="Zoom")
        self.zoomLabel.grid(row=3, column=1, sticky="w", padx=(50, 0), pady=(0, 0))
        
        # Color Theme Option Menu
        self.zoomOptionMenu = ctk.CTkOptionMenu(self, values=[str(val)+"%" for val in range(50, 160, 10)], command=self.zoom)
        self.zoomOptionMenu.grid(row=3, column=1, sticky="w", padx=(100, 0), pady=(10, 10))
        self.zoomOptionMenu.set("100%")

        self.tabView.set("Text To Speech")

        
        # Color Theme Label
        # self.colorThemeLabel = ctk.CTkLabel(self, text="Color Theme")
        # self.colorThemeLabel.grid(row=3, column=2, sticky="w", padx=(20, 0), pady=(0, 0))
        
        # # Color Theme Option Menu
        # self.colorThemeColumnMenu = ctk.CTkOptionMenu(self, values=[str(val)+"%" for val in range(50, 160, 10)], command=self.zoom)
        # self.colorThemeColumnMenu.grid(row=3, column=2, sticky="w", padx=(100, 0), pady=(10, 10))

        
        # self.scaling_label = ctk.CTkLabel(self, text="Widget Scaling")
        # self.scaling_label.grid(row=3, column=2, sticky="e", padx=(0, 310), pady=(0, 0))

        
        # self.scaling_label = ctk.CTkLabel(self, text="Zoom")
        # self.scaling_label.grid(row=3, column=2, sticky="w", padx=(0, 0), pady=(0, 0))

        # self.scaling_optionemenu = ctk.CTkOptionMenu(self, values=[str(val)+"%" for val in range(50, 160, 10)], command=self.zoom)
        # self.scaling_optionemenu.grid(row=3, column=2, sticky="w", padx=(50, 0), pady=(10, 10))

    def change_appearance_mode_event(self, newMode):
        ctk.set_appearance_mode(newMode)

    def changeColorTheme(selfself, newTheme):
        ctk.set_default_color_theme(newTheme)

    def zoom(self, zoom):
        newScaling = int(zoom.replace("%", "")) / 100
        ctk.set_widget_scaling(newScaling)
        # customtkinter.set_spacing_scaling(float_value)  # padding and place positions
        # customtkinter.set_window_scaling(float_value)  # window geometry dimensions


class YT():
    def __init__(self, tabView):
        # super().__init__(master=tabView.tab("YT Video Download"))
        print("YT INIT")
        self.ytLabel = ctk.CTkLabel(master=tabView.tab("YT Video Download"), text="YouTube Video Downloader and Stats Analyzer")
        self.ytLabel.grid(row=2, column=1, padx=20, pady=20)


if __name__ == "__main__":
    app = App()
    app.mainloop()
