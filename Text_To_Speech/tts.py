import tkinter as tk
import tkinter.messagebox
import customtkinter as ctk
import PyPDF2 as pypdf
import pyttsx3
import os
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename


class TextToSpeechFrame(ctk.CTkFrame):
    def __init__(self, *args, tabView, header_name="TextToSpeechFrame", **kwargs):
        super().__init__(*args, **kwargs)

        self.header_name = header_name
        tabName = "Text To Speech"
        mas = tabView.tab(tabName)

        # Speaker Settings
        self.speaker = pyttsx3.init()
        self.availableVoices = self.speaker.getProperty("voices")

        # Select Input File Button
        self.selectTextFileButton = ctk.CTkButton(master=mas, text="Select Text File", command=self.selectInputFile)
        self.selectTextFileButton.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
        # Label that displays the path of the text file selected
        self.selectTextFileLabel = ctk.CTkLabel(master=mas, text="Select Text File Label")
        self.selectTextFileLabel.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Select Output Button
        self.outputFileButton = ctk.CTkButton(master=mas, text="Save At", command=self.selectOutputFile)
        self.outputFileButton.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        # Label that displays the path at which the audio file will be saved
        self.outputFileLabel = ctk.CTkLabel(master=mas, text="Output File Label")
        self.outputFileLabel.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        # Assistant Label
        self.assistantLabel = ctk.CTkLabel(master=mas, text="Assistant")
        self.assistantLabel.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        # Assistant details
        self.assistantOptionMenu = ctk.CTkOptionMenu(master=mas, values=[str(assistant.id) for assistant in self.availableVoices])
        self.assistantOptionMenu.grid(row=3, column=1, columnspan=2, sticky="w", padx=(20, 0), pady=(10, 10))

        # Pace Label
        self.paceLabel = ctk.CTkLabel(master=mas, text="Pace")
        self.paceLabel.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        # Pace Entry Filed
        self.paceEntry = ctk.CTkEntry(master=mas, placeholder_text="100 [Recommended]")
        self.paceEntry.grid(row=4, column=1, columnspan=2, padx=(20, 0), pady=(0, 0), sticky="ew")
        # self.paceEntry.set("100")

        # Narrate Button
        self.narrateButton = ctk.CTkButton(master=mas, text="Narrate", command=self.narrate)
        self.narrateButton.grid(row=5, column=0, padx=10, pady=10, sticky="w")

        # Create MP3 Button
        self.createMp3Button = ctk.CTkButton(master=mas, text="Create MP3", command=self.createMp3)
        self.createMp3Button.grid(row=5, column=1, padx=10, pady=10, sticky="ew")
        
        # Clear the entries
        self.clear = ctk.CTkButton(master=mas, text="Clear Entries", command=self.clearEntries)
        self.clear.grid(row=5, column=2, padx=10, pady=10, sticky="e")


    # Function that opens a dialog box to select the required text file
    def selectInputFile(self):
        self.inputFilePath = askopenfilename(filetypes=[("PDF File", "*.pdf")])
        self.selectTextFileLabel.configure(text=self.inputFilePath)

    def selectOutputFile(self):
        self.outputFilePath = asksaveasfilename(filetypes=[("MP3 File", "*.mp3")]) + ".mp3"
        self.outputFileLabel.configure(text=self.outputFilePath)

    def setAssistantProperties(self):
        # Reading the settings
        self.assistantId = self.assistantOptionMenu.get()
        self.pace = int(self.paceEntry.get())

        # Setting the properties of the assistant
        self.speaker.setProperty("voice", self.assistantId)
        self.speaker.setProperty("rate", self.pace)

    def narrate(self):
        speech = "Hello! I am your narrator and this is the pace at which I narrate your Audio File"

        self.setAssistantProperties()

        self.speaker.say(speech)
        self.speaker.runAndWait()

    def createMp3(self):
        self.setAssistantProperties()

        pdfReader = pypdf.PdfFileReader(open(self.inputFilePath, 'rb'))

        # Extract data from each page and convert into a speakable form
        data = ""
        for pageNumber in range(pdfReader.numPages):
            data += pdfReader.getPage(pageNumber).extractText()
        
        formattedData = data.strip().replace("\n", "    ")

        self.speaker.save_to_file(formattedData, self.outputFilePath)
        
        self.speaker.runAndWait()
        self.speaker.stop()

    def clearEntries(self):
        self.selectTextFileLabel.configure(text=" ")
        self.outputFileLabel.configure(text=" ")
        self.paceEntry.delete(0, 200)
