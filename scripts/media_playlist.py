from PySide2.QtCore import QDir, QObject, QUrl
from PySide2.QtMultimedia import QMediaPlaylist

from singleton import Singleton


class MediaPlaylist(QMediaPlaylist, metaclass=Singleton):
    def __init__(self, parent: QObject = None) -> None:
        super(MediaPlaylist, self).__init__(parent)

    def add(self, path: str):
        url = QUrl.fromUserInput(QDir.fromNativeSeparators(path))
        self.addMedia(url)
