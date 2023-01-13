#Youtube Downloader
#pip install youtube-dl

import sys
import subprocess

def download_video(url):
    try:
        print('Downloading video...')
        subprocess.call(['youtube-dl', '-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4', '-o', 'video.mp4', url])
        print('Download complete!')
    except:
        print('Error downloading video')
        sys.exit()

def download_audio(url):
    try:
        print('Downloading audio...')
        subprocess.call(['youtube-dl', '-f', 'bestaudio[ext=m4a]', '-o', 'audio.m4a', url])
        print('Download complete!')
    except:
        print('Error downloading audio')
        sys.exit()


def main():
    print('Welcome to the YouTube Downloader')
    print('Enter 1 to download video, 2 to download audio: ')
    opção = input()
    print('Enter video URL: ')
    url = input()
    if opção == '1':
        download_video(url)
    elif opção == '2':
        download_audio(url)
    else:
        print('Invalid option')
        sys.exit()
