import requests
from dataclasses import dataclass


@dataclass
class DataDownloader:
    image_folder_path: str
    video_folder_path: str
    audio_folder_path: str

    def download_photo(self, url: str):
        ...

    def download_video(self, url: str):
        ...

    def download_audio(self, url: str):
        ...

    def download_url_sequence(self, urls: list):
        ...
