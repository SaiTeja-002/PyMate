import tkinter as tk
import tkinter.filedialog
import tkinter.messagebox
import customtkinter as ctk
import PyPDF2 as pypdf
import pyttsx3


class TextToSpeech:
    def __init__(self, appRef, tabView):
        tabName = "Text To Speech"
        mas = tabView.tab(tabName)
        # super().__init__(master=tabView.tab("YT Video Download"))
        print("YT INIT")
        # self.ytLabel = ctk.CTkLabel(master=tabView.tab("Text To Speech"), text="Takes a Text File and converts into an Audio File", justify=tk.LEFT)
        # self.ytLabel.grid(row=1, column=0, padx=20, pady=20)

        appRef.main_button_1 = ctk.CTkButton(master=mas, text="b1", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        appRef.main_button_1.grid(row=900, column=3, rowspan=3, padx=(20, 20), pady=(20, 20), sticky="nsew")


        appRef.main_button_2 = ctk.CTkButton(master=mas, text="b2", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        appRef.main_button_2.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")


        appRef.main_button_3 = ctk.CTkButton(master=mas, text="b3", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        appRef.main_button_3.grid(row=3, column=30, columnspan=3, padx=(20, 20), pady=(20, 20), sticky="nsew")


class TextToSpeechFrame(ctk.CTkFrame):
    def __init__(self, *args, tabView, header_name="TextToSpeechFrame", **kwargs):
        super().__init__(*args, **kwargs)

        self.header_name = header_name
        tabName = "Text To Speech"
        mas = tabView.tab(tabName)

        # Speaker Settings
        self.speaker = pyttsx3.init()
        self.availableVoices = self.speaker.getProperty("voices")
        
        # self.grid_columnconfigure(0, weight=1)
        # self.grid_columnconfigure(1, weight=1)
        # self.grid_columnconfigure((2, 3), weight=1)
        # self.grid_rowconfigure((0, 1, 2), weight=1)

        # self.slider_progressbar_frame = ctk.CTkFrame(self, fg_color="transparent")
        # self.slider_progressbar_frame.grid(row=1, column=1, columnspan=2, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # Select Input File Button
        self.inputFileButton = ctk.CTkButton(master=mas, text="Select Text File", command=self.selectInputFile)
        self.inputFileButton.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
        # Un-Editable Entry Field that shows the selected file path
        self.entry = ctk.CTkEntry(master=mas, placeholder_text="Selected file path is displayed here", state="disabled")
        self.entry.grid(row=0, column=1, columnspan=2, padx=(20, 0), pady=(0, 0), sticky="ew")

        # Select Output Button
        self.outputFileButton = ctk.CTkButton(master=mas, text="Save At", command=self.selectOutputFile)
        self.outputFileButton.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        # Un-Editable Entry Field that shows the selected file path
        # self.saveLocationVar = tk.StringVar('Selected_file_path_is_displayed_here')
        self.saveLocation = ctk.CTkEntry(master=mas, placeholder_text="Selected file path is displayed here")
        self.saveLocation.grid(row=1, column=1, columnspan=2, padx=(20, 0), pady=(0, 0), sticky="ew")

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
        self.createMp3Button.grid(row=5, column=1, padx=10, pady=10, sticky="e")
        
        # Clear the entries
        self.clear = ctk.CTkButton(master=mas, text="Clear Entries", command=self.clearEntries)
        self.clear.grid(row=5, column=2, padx=10, pady=10, sticky="e")


    def selectInputFile(self):
        print("Opening the input file dialog box")

    def selectOutputFile(self):
        print("Opening the output file dialog box")

    def narrate(self):
        speech = "Hello! I am your narrator and this is the pace at which I narrate your Audio File"

        # assistantId = assistantComboBox.currentData()
        # pace = int(speechRateEntryField.text())

        # assistantId = self.availableVoices[0].id
        assistantId = self.assistantOptionMenu.get()
        pace = 110

        # Setting the properties of the assistant
        self.speaker.setProperty("voice", assistantId)
        self.speaker.setProperty("rate", pace)
        self.speaker.say(speech)
        self.speaker.runAndWait()

    def createMp3(self):
        print("Generating the MP3 File")

    def clearEntries(self):
        print("Clearing all the entries")

        # self.header = ctk.CTkLabel(master=mas, text=self.header_name)
        # self.header.grid(row=0, column=0, padx=10, pady=10)
        #
        # self.radio_button_var = ctk.StringVar(value="")
        #
        # self.radio_button_1 = ctk.CTkRadioButton(master=mas, text="Option 1", value="Option 1",
        #                                                    variable=self.radio_button_var)
        # self.radio_button_1.grid(row=1, column=0, padx=10, pady=10)
        # self.radio_button_2 = ctk.CTkRadioButton(master=mas, text="Option 2", value="Option 2",
        #                                                    variable=self.radio_button_var)
        # self.radio_button_2.grid(row=2, column=0, padx=10, pady=10)
        # self.radio_button_3 = ctk.CTkRadioButton(master=mas, text="Option 3", value="Option 3",
        #                                                    variable=self.radio_button_var)
        # self.radio_button_3.grid(row=3, column=1, padx=10, pady=(10, 20))
