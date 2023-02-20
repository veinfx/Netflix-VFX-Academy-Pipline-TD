import os
from pytube import YouTube
path = 'https://www.youtube.com/watch?v=tiao0m67fi8'
down = os.path.expanduser('~/mov')
YouTube(path).streams.get_highest_resolution().download(output_path=down)

