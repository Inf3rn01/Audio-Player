from PyQt6 import QtWidgets
from ui import Ui_MainWindow
import os
from PyQt6.QtMultimedia import QMediaPlayer
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtGui import QIcon
import random
from PyQt6.QtCore import Qt, QPoint

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setFixedSize(318, 347)
    MainWindow.setWindowFlag(Qt.WindowType.FramelessWindowHint)
    player = QMediaPlayer()
    ui.playing = False
    MainWindow.show()
    
    # Пока не знаю, как перемещать окно
    '''def mousePressEvent(event):
        ui.oldPos = event.globalPosition().toPoint()

    def mouseMoveEvent(event):
        delta = QPoint (event.globalPosition().toPoint() - ui.oldPos)
        ui.move(MainWindow.x() + delta.x(), ui.y() + delta.y())
        ui.oldPos = event.globalPosition().toPoint()
        event.accept()'''
    
    def button_close():
        ui.closeButton(sys.exit())
    
    def button_collapse():
        MainWindow.showMinimized()

    def button_on_off(widget):
        if widget.isVisible():
            widget.hide()
        else: 
            widget.show()
        

    def select_folder():
        folder_path = QFileDialog.getExistingDirectory(MainWindow, "Выберите папку с музыкой")
        if folder_path:
            music_files = [file for file in os.listdir(folder_path) if file.endswith(".mp3")]
            ui.listWidget.clear()
            ui.listWidget.addItems(music_files)
    
    
    def previous_song():
        pass
    
    
    def toggle_playback():
        if ui.playing:
            player.pause()
            ui.playing = False
            ui.playMusicButton.setIcon(QIcon("D:\\PythonProjects\\AudioPlayer\\src\\client\\icons\\white\\play-circle.svg"))
        else:
            player.play()
            ui.playing = True
            ui.playMusicButton.setIcon(QIcon("D:\\PythonProjects\\AudioPlayer\\src\\client\\icons\\white\\pause-circle.svg"))
    
    def next_song():
        pass
    
    def shuffle_song():
        spisok_pesen = [ui.listWidget.item(i).text()
                 for i in range(ui.listWidget.count())]
        
        random.shuffle(spisok_pesen)
        ui.listWidget.clear()
        for music in spisok_pesen:
            ui.listWidget.addItem(music)
         
    
    ui.closeButton.clicked.connect(button_close)
    ui.collapseButton.clicked.connect(button_collapse)
    ui.powerButton.clicked.connect(lambda: button_on_off(ui.listWidget))
    ui.powerButton.clicked.connect(lambda: button_on_off(ui.toolWidget))
    ui.folderButton.clicked.connect(select_folder)
    ui.backMusicButton.clicked.connect(previous_song)
    ui.playMusicButton.clicked.connect(toggle_playback)
    ui.nextMusicButton.clicked.connect(next_song)
    ui.shuffleButton.clicked.connect(shuffle_song)
    
    
    
    sys.exit(app.exec())
    