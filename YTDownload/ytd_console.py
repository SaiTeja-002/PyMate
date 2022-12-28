from pytube import YouTube
from tkinter.filedialog import asksaveasfile


def downloadVideo(link):
    ytObject = YouTube(link)

    print("Title: ", ytObject.title)
    print("View: ", ytObject.views)

    # yt = ytObject.streams.get_by_resolution()
    # ytVideo = ytObject.streams.get_highest_resolution()
    ytAudio = ytObject.streams.get_audio_only()

    # ADD FOLDER HERE
    ytAudio.download('./DownloadsFolder')
    # f = asksaveasfile(initialfile = '{ytObject.title}+".mp3"', defaultextension=".mp3", filetypes=[("MP3 File", "*.mp3")])
    print(f)

def main():
    link = input("Enter the YouTube Link here : ")

    try:
        downloadVideo(link)
    except:
        print("Kindly Recheck your URL")



main()
print("hello")

# print(f"Title : {ytObject.check_availability()}")


