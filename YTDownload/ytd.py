import tkinter as tk
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import asksaveasfilename
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
        self.downloadButton = ctk.CTkButton(master=mas, text="Download", command=self.download)
        self.downloadButton.grid(row=2, column=2, padx=20, pady=10, sticky="nsew")

        # Clear Button
        # self.clearButton = ctk.CTkButton(master=mas, text="Clear")
        # self.clearButton.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        # Download Option
        self.showDetailsButton = ctk.CTkButton(master=mas, text="Show Details", command=self.showDetails)
        self.showDetailsButton.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Details Label
        self.detailsLabel = ctk.CTkLabel(master=mas, text="Details")
        self.detailsLabel.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
        
        # Details TextBox
        self.textbox = ctk.CTkTextbox(master=mas, width=250)
        self.textbox.grid(row=3, column=1, rowspan=3, columnspan=3, padx=10, pady=10, sticky="nsew")

        # self.textbox.insert("0.0", "CTkTextbox\n\n" + "Title - YT Video Title\n" + "Views - 3B")


    def showDetails(self):
        if(self.checkAvailability()):
            print("Showing the details in the textbox")
            self.textbox.insert("0.0", f"Title - {self.ytObject.title}\nViews - {self.ytObject.views}\nDescription - {self.ytObject.description}\n\n\n")


    def download(self):
        if(self.checkAvailability()):
            self.showDetails()

            print(f"Downloading the corresponding {self.downloadTypeMenuOption.get().lower()} file")
            
            self.filePath = asksaveasfilename(filetypes=[("MP3 Files", "*.mp3")])
            print(self.filePath)

            if self.downloadTypeMenuOption.get().lower() == "video":
                self.ytVideo = self.ytObject.streams.get_highest_resolution()
                self.ytVideo.download(self.filePath)
            else:
                self.ytAudio = self.ytObject.streams.get_audio_only()
                self.ytAudio.download(self.filePath)

            self.textbox.insert("0.0", "DONWLOAD SUCCESSFULL!!\n\n\n")
                

    def checkAvailability(self):
        try:
            self.ytObject = YouTube(self.urlEntry.get())
            return True
        except:
            self.textbox.insert("0.0", "Error:404 URL Not Found\nKindly Re-Check your URL and try again\n\n\n")
            return False


