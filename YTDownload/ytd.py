import tkinter as tk
import customtkinter as ctk
from pytube import YouTube


class YTVideoDownloadFrame(ctk.CTkFrame):
    def __init__(self, *args, tabView, header_name="YTVideoDownloadFrame", **kwargs):
        super().__init__(*args, **kwargs)

        self.header_name = header_name
        tabName = "YT Video Download"
        mas = tabView.tab(tabName)

        # YT URL Label
        self.urlLabel = ctk.CTkLabel(master=mas, text="Enter your URL here: ")
        self.urlLabel.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # YT URL Entry
        self.urlEntry = ctk.CTkEntry(master=mas)
        self.urlEntry.grid(row=0, column=1, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Download Type
        self.downloadTypeLabel = ctk.CTkLabel(master=mas, text="Download Type")
        self.downloadTypeLabel.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        
        # Download Type drop-down
        self.downloadTypeMenuOption = ctk.CTkOptionMenu(master=mas, values=["Video", "Audio"])
        self.downloadTypeMenuOption.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        # Dummy Label
        self.dummyLabel = ctk.CTkLabel(master=mas, text="\t\t\t\t\t\t\t")
        self.dummyLabel.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")
        
        # Download Option
        self.downloadButton = ctk.CTkButton(master=mas, text="Download")
        self.downloadButton.grid(row=2, column=2, padx=20, pady=10, sticky="nsew")

        # Clear Button
        self.clearButton = ctk.CTkButton(master=mas, text="Clear")
        self.clearButton.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        # Download Option
        self.showDetailsButton = ctk.CTkButton(master=mas, text="Show Details")
        self.showDetailsButton.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

        # Details Label
        self.detailsLabel = ctk.CTkLabel(master=mas, text="Details")
        self.detailsLabel.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
        
        # Details TextBox
        self.textbox = ctk.CTkTextbox(master=mas, width=250)
        self.textbox.grid(row=3, column=1, rowspan=3, columnspan=3, padx=10, pady=10, sticky="nsew")

        self.textbox.insert("0.0", "CTkTextbox\n\n" + "Title - YT Video Title\n" + "Views - 3B")

