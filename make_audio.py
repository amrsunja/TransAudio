from moviepy.editor import *



class DetachAudio:
    def __init__(self, place):
        self.place = str(place)
        self.name = self.place.split('/')[-1]

        video = VideoFileClip(self.place)
        audio = video.audio
        

        audio.write_audiofile(f'audio/{self.name[0:-4]}.mp3')
        
