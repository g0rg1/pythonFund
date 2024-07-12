import moviepy.editor

video = moviepy.editor.VideoFileClip('my_video.MOV')

audio = video.audio

audio.write_audiofile('my_audio.mp3')
