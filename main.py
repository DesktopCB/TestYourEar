from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from PyQt5.QtWidgets import QMessageBox
from titlewindow import Ui_MainWindow
from pianowin import Ui_pianoWindow
from chose_guitar import Ui_Guitar
from mediumWin import Ui_mediumWin
from hardWin import Ui_hardWindow
import sys
from random import randint
from config import *
from info import *
import time

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.startWindow(MainWindow)
MainWindow.show()


def piano_sheets(sheet):
    global player, main_link, piano
    piano_link = 'piano/'
    player = QtMultimedia.QMediaPlayer()
    sound = QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(piano_link + f'{notes[sheet]}'))
    main_link = f'{piano_link}{notes[sheet]}'
    player.setMedia(sound)
    player.setVolume(100)
    player.play()

def guitar_sheets(sheet):
    global music, main_link_guitar, guitar_dir
    guitar_dir = 'guitar/'
    music = QtMultimedia.QMediaPlayer()
    sound = QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(guitar_dir + f'{notes3_guitar[sheet]}'))
    main_link_guitar = f'{guitar_dir}{notes3_guitar[sheet]}'
    # print('main - ' + main_link_guitar)
    music.setMedia(sound)
    music.setVolume(100)
    music.play()

def random_note_piano():
    global sound_random, link_sound_random, true
    numeric_id = str(randint(0, len(notes)-1))
    true = 0
    for key, values in notes2.items():
        if key == numeric_id:
            sound_random = values
            print(sound_random)
            piano_sheets(sound_random)
            link_sound_random = f'piano/{sound_random}.wav'

def random_note_guitar():
    global sound_random, link_sound_random, true, var_sheet
    true = 1
    id = str(randint(0, len(notes2_guitar)-1))
    for key, values in notes2_guitar.items():
        if key == id:
            sound_random = values
            print(sound_random)
            var_sheet = sheets[sound_random]
            var_sheet.sort()
            print(var_sheet)
            # print(link_sound_random)
            guitar_sheets(sound_random)

def replay_sheet_piano():
    piano_sheets(sound_random)

def replay_sheet_guitar():
    guitar_sheets(sound_random)

def chose_func():
    global guitarWindow
    guitarWindow = QtWidgets.QMainWindow()
    ui = Ui_Guitar()
    ui.chose(guitarWindow)
    MainWindow.close()
    guitarWindow.show()
    def return_to_main_window():
        guitarWindow.close()
        MainWindow.show()

    def start_medium():
        global medium_window
        medium_window = QtWidgets.QMainWindow()
        ui = Ui_mediumWin()
        ui.start_medium_window(medium_window)
        guitarWindow.close()
        medium_window.show()
        def back():
            medium_window.close()
            music.stop()
            guitarWindow.show()

        def for_buttons_guitar(sheet):
            ui.line_sheet.setText(sheet)
            guitar_sheets(sheet)

        def next():
            ui.line_sheet.setText('')
            random_note_guitar()
            ui.score += 1
            ui.text_score.setText(f'Score: {ui.score}')

        def eq():
            global youlose
            if ui.line_sheet.text() == sound_random:
                next()
            else:
                youlose = QMessageBox()
                youlose.setWindowTitle('YOU LOSE')
                youlose.setGeometry(600, 405, 200, 100)
                youlose.setText(f'you lose!\nScore: {ui.score}')
                youlose.setIcon(QMessageBox.Warning)
                youlose.setDefaultButton(QMessageBox.Retry)
                youlose.exec_()
                back()


        random_note_guitar()
        ui.C1.clicked.connect(lambda: for_buttons_guitar('C1'))
        ui.Cd1.clicked.connect(lambda: for_buttons_guitar('C#1'))
        ui.D1.clicked.connect(lambda: for_buttons_guitar('D1'))
        ui.Dd1.clicked.connect(lambda: for_buttons_guitar('D#1'))
        ui.E1.clicked.connect(lambda: for_buttons_guitar('E1'))
        ui.F1.clicked.connect(lambda: for_buttons_guitar('F1'))
        ui.Fd1.clicked.connect(lambda: for_buttons_guitar('F#1'))
        ui.G1.clicked.connect(lambda: for_buttons_guitar('G1'))
        ui.Gd1.clicked.connect(lambda: for_buttons_guitar('G#1'))
        ui.A1.clicked.connect(lambda: for_buttons_guitar('A1'))
        ui.Ad1.clicked.connect(lambda: for_buttons_guitar('A#1'))
        ui.B1.clicked.connect(lambda: for_buttons_guitar('B1'))
        ui.C2.clicked.connect(lambda: for_buttons_guitar('C4'))
        ui.Cd2.clicked.connect(lambda: for_buttons_guitar('C#4'))
        ui.D2.clicked.connect(lambda: for_buttons_guitar('D3'))
        ui.Dd2.clicked.connect(lambda: for_buttons_guitar('D#2'))
        ui.E2.clicked.connect(lambda: for_buttons_guitar('E1'))
        ui.F2.clicked.connect(lambda: for_buttons_guitar('F1'))
        ui.Fd2.clicked.connect(lambda: for_buttons_guitar('F#1'))
        ui.G2.clicked.connect(lambda: for_buttons_guitar('G1'))
        ui.Gd2.clicked.connect(lambda: for_buttons_guitar('G#1'))
        ui.A2.clicked.connect(lambda: for_buttons_guitar('A1'))
        ui.Ad2.clicked.connect(lambda: for_buttons_guitar('A#1'))
        ui.B2.clicked.connect(lambda: for_buttons_guitar('B4'))
        ui.C3.clicked.connect(lambda: for_buttons_guitar('C4'))
        ui.Cd3.clicked.connect(lambda: for_buttons_guitar('C#4'))
        ui.D3.clicked.connect(lambda: for_buttons_guitar('D3'))
        ui.Dd3.clicked.connect(lambda: for_buttons_guitar('D#2'))
        ui.E3.clicked.connect(lambda: for_buttons_guitar('E1'))
        ui.F3.clicked.connect(lambda: for_buttons_guitar('F1'))
        ui.Fd3.clicked.connect(lambda: for_buttons_guitar('F#1'))
        ui.G3.clicked.connect(lambda: for_buttons_guitar('G3'))
        ui.Gd3.clicked.connect(lambda: for_buttons_guitar('G#3'))
        ui.A3.clicked.connect(lambda: for_buttons_guitar('A4'))
        ui.Ad3.clicked.connect(lambda: for_buttons_guitar('A#4'))
        ui.B3.clicked.connect(lambda: for_buttons_guitar('B4'))
        ui.C4.clicked.connect(lambda: for_buttons_guitar('C4'))
        ui.Cd4.clicked.connect(lambda: for_buttons_guitar('C#4'))
        ui.D4.clicked.connect(lambda: for_buttons_guitar('D6'))
        ui.Dd4.clicked.connect(lambda: for_buttons_guitar('D#4'))
        ui.E4.clicked.connect(lambda: for_buttons_guitar('E5'))
        ui.F4.clicked.connect(lambda: for_buttons_guitar('F4'))
        ui.Fd4.clicked.connect(lambda: for_buttons_guitar('F#4'))
        ui.G4.clicked.connect(lambda: for_buttons_guitar('G3'))
        ui.Gd4.clicked.connect(lambda: for_buttons_guitar('G#3'))
        ui.A4.clicked.connect(lambda: for_buttons_guitar('A4'))
        ui.Ad4.clicked.connect(lambda: for_buttons_guitar('A#4'))
        ui.B4.clicked.connect(lambda: for_buttons_guitar('B4'))
        ui.C5.clicked.connect(lambda: for_buttons_guitar('C5'))
        ui.Cd5.clicked.connect(lambda: for_buttons_guitar('C#5'))
        ui.D5.clicked.connect(lambda: for_buttons_guitar('D6'))
        ui.Dd5.clicked.connect(lambda: for_buttons_guitar('D#4'))
        ui.E5.clicked.connect(lambda: for_buttons_guitar('E5'))
        ui.F5.clicked.connect(lambda: for_buttons_guitar('F4'))
        ui.Fd5.clicked.connect(lambda: for_buttons_guitar('F#4'))
        ui.G5.clicked.connect(lambda: for_buttons_guitar('G3'))
        ui.Gd5.clicked.connect(lambda: for_buttons_guitar('G#3'))
        ui.A5.clicked.connect(lambda: for_buttons_guitar('A5'))
        ui.Ad5.clicked.connect(lambda: for_buttons_guitar('A#5'))
        ui.B5.clicked.connect(lambda: for_buttons_guitar('B5'))
        ui.C6.clicked.connect(lambda: for_buttons_guitar('C5'))
        ui.Cd6.clicked.connect(lambda: for_buttons_guitar('C#5'))
        ui.D6.clicked.connect(lambda: for_buttons_guitar('D6'))
        ui.Dd6.clicked.connect(lambda: for_buttons_guitar('D#4'))
        ui.E6.clicked.connect(lambda: for_buttons_guitar('E6'))
        ui.F6.clicked.connect(lambda: for_buttons_guitar('F6'))
        ui.Fd6.clicked.connect(lambda: for_buttons_guitar('F#6'))
        ui.G6.clicked.connect(lambda: for_buttons_guitar('G6'))
        ui.Gd6.clicked.connect(lambda: for_buttons_guitar('G#6'))
        ui.A6.clicked.connect(lambda: for_buttons_guitar('A5'))
        ui.Ad6.clicked.connect(lambda: for_buttons_guitar('A#5'))
        ui.B6.clicked.connect(lambda: for_buttons_guitar('B5'))
        ui.E11.clicked.connect(lambda: for_buttons_guitar('E11'))
        ui.E66.clicked.connect(lambda: for_buttons_guitar('E5'))
        ui.A55.clicked.connect(lambda: for_buttons_guitar('A4'))
        ui.D44.clicked.connect(lambda: for_buttons_guitar('D3'))
        ui.G33.clicked.connect(lambda: for_buttons_guitar('G1'))
        ui.B22.clicked.connect(lambda: for_buttons_guitar('B1'))
        ui.replay_btn.clicked.connect(replay_sheet_guitar)
        ui.next_btn.clicked.connect(eq)
        ui.back_btn.clicked.connect(back)

    def start_hard():
        global hard_window, hard_list
        hard_window = QtWidgets.QMainWindow()
        ui = Ui_hardWindow()
        ui.start_hard_window(hard_window)
        guitarWindow.close()
        hard_window.show()
        hard_list = []
        def back():
            hard_window.close()
            music.stop()
            guitarWindow.show()

        def add_sheet(sheet):
            hard_list.append(sheet)
            hard_list.sort()
            print(hard_list)

        def next():
            global youwin, youlose
            # for i in hard_list:
            #     if hard_list.count(i) == 2:
            #         hard_list.remove(i)
            if hard_list == var_sheet:
                youwin = QMessageBox()
                youwin.setWindowTitle('YOU WIN!')
                youwin.setGeometry(600, 405, 200, 100)
                youwin.setText('Congratulations!\nYou win!')
                youwin.setIcon(QMessageBox.Warning)
                youwin.setDefaultButton(QMessageBox.Retry)
                youwin.exec_()
                back()
            else:
                youlose = QMessageBox()
                youlose.setWindowTitle('YOU LOSE')
                youlose.setGeometry(600, 405, 200, 100)
                youlose.setText(f'you lose!\nRetry')
                youlose.setIcon(QMessageBox.Warning)
                youlose.setDefaultButton(QMessageBox.Ok)
                youlose.exec_()
                back()
        random_note_guitar()
        ui.back_btn.clicked.connect(back)
        ui.replay_btn.clicked.connect(replay_sheet_guitar)
        ui.next_btn.clicked.connect(next)
        ui.C1.clicked.connect(lambda: add_sheet('C1'))
        ui.Cd1.clicked.connect(lambda: add_sheet('C#1'))
        ui.D1.clicked.connect(lambda: add_sheet('D1'))
        ui.Dd1.clicked.connect(lambda: add_sheet('D#1'))
        ui.E1.clicked.connect(lambda: add_sheet('E1'))
        ui.F1.clicked.connect(lambda: add_sheet('F1'))
        ui.Fd1.clicked.connect(lambda: add_sheet('F#1'))
        ui.G1.clicked.connect(lambda: add_sheet('G1'))
        ui.Gd1.clicked.connect(lambda: add_sheet('G#1'))
        ui.A1.clicked.connect(lambda: add_sheet('A1'))
        ui.Ad1.clicked.connect(lambda: add_sheet('A#1'))
        ui.B1.clicked.connect(lambda: add_sheet('B1'))
        ui.C2.clicked.connect(lambda: add_sheet('C2'))
        ui.Cd2.clicked.connect(lambda: add_sheet('C#2'))
        ui.D2.clicked.connect(lambda: add_sheet('D2'))
        ui.Dd2.clicked.connect(lambda: add_sheet('D#2'))
        ui.E2.clicked.connect(lambda: add_sheet('E2'))
        ui.F2.clicked.connect(lambda: add_sheet('F2'))
        ui.Fd2.clicked.connect(lambda: add_sheet('F#2'))
        ui.G2.clicked.connect(lambda: add_sheet('G2'))
        ui.Gd2.clicked.connect(lambda: add_sheet('G#2'))
        ui.A2.clicked.connect(lambda: add_sheet('A2'))
        ui.Ad2.clicked.connect(lambda: add_sheet('A#2'))
        ui.B2.clicked.connect(lambda: add_sheet('B2'))
        ui.C3.clicked.connect(lambda: add_sheet('C3'))
        ui.Cd3.clicked.connect(lambda: add_sheet('C#3'))
        ui.D3.clicked.connect(lambda: add_sheet('D3'))
        ui.Dd3.clicked.connect(lambda: add_sheet('D#3'))
        ui.E3.clicked.connect(lambda: add_sheet('E3'))
        ui.F3.clicked.connect(lambda: add_sheet('F3'))
        ui.Fd3.clicked.connect(lambda: add_sheet('F#3'))
        ui.G3.clicked.connect(lambda: add_sheet('G3'))
        ui.Gd3.clicked.connect(lambda: add_sheet('G#3'))
        ui.A3.clicked.connect(lambda: add_sheet('A3'))
        ui.Ad3.clicked.connect(lambda: add_sheet('A#3'))
        ui.B3.clicked.connect(lambda: add_sheet('B3'))
        ui.C4.clicked.connect(lambda: add_sheet('C4'))
        ui.Cd4.clicked.connect(lambda: add_sheet('C#4'))
        ui.D4.clicked.connect(lambda: add_sheet('D4'))
        ui.Dd4.clicked.connect(lambda: add_sheet('D#4'))
        ui.E4.clicked.connect(lambda: add_sheet('E4'))
        ui.F4.clicked.connect(lambda: add_sheet('F4'))
        ui.Fd4.clicked.connect(lambda: add_sheet('F#4'))
        ui.G4.clicked.connect(lambda: add_sheet('G4'))
        ui.Gd4.clicked.connect(lambda: add_sheet('G#4'))
        ui.A4.clicked.connect(lambda: add_sheet('A4'))
        ui.Ad4.clicked.connect(lambda: add_sheet('A#4'))
        ui.B4.clicked.connect(lambda: add_sheet('B4'))
        ui.C5.clicked.connect(lambda: add_sheet('C5'))
        ui.Cd5.clicked.connect(lambda: add_sheet('C#5'))
        ui.D5.clicked.connect(lambda: add_sheet('D5'))
        ui.Dd5.clicked.connect(lambda: add_sheet('D#5'))
        ui.E5.clicked.connect(lambda: add_sheet('E5'))
        ui.F5.clicked.connect(lambda: add_sheet('F5'))
        ui.Fd5.clicked.connect(lambda: add_sheet('F#5'))
        ui.G5.clicked.connect(lambda: add_sheet('G5'))
        ui.Gd5.clicked.connect(lambda: add_sheet('G#5'))
        ui.A5.clicked.connect(lambda: add_sheet('A5'))
        ui.Ad5.clicked.connect(lambda: add_sheet('A#5'))
        ui.B5.clicked.connect(lambda: add_sheet('B5'))
        ui.C6.clicked.connect(lambda: add_sheet('C6'))
        ui.Cd6.clicked.connect(lambda: add_sheet('C#6'))
        ui.D6.clicked.connect(lambda: add_sheet('D6'))
        ui.Dd6.clicked.connect(lambda: add_sheet('D#6'))
        ui.E6.clicked.connect(lambda: add_sheet('E6'))
        ui.F6.clicked.connect(lambda: add_sheet('F6'))
        ui.Fd6.clicked.connect(lambda: add_sheet('F#6'))
        ui.G6.clicked.connect(lambda: add_sheet('G6'))
        ui.Gd6.clicked.connect(lambda: add_sheet('G#6'))
        ui.A6.clicked.connect(lambda: add_sheet('A6'))
        ui.Ad6.clicked.connect(lambda: add_sheet('A#6'))
        ui.B6.clicked.connect(lambda: add_sheet('B6'))
        ui.E11.clicked.connect(lambda: add_sheet('E11'))
        ui.E66.clicked.connect(lambda: add_sheet('E66'))
        ui.A55.clicked.connect(lambda: add_sheet('A55'))
        ui.D44.clicked.connect(lambda: add_sheet('D44'))
        ui.G33.clicked.connect(lambda: add_sheet('G33'))
        ui.B22.clicked.connect(lambda: add_sheet('B22'))

    ui.btn_back_to_menu.clicked.connect(return_to_main_window)
    ui.medium.clicked.connect(start_medium)
    ui.hard.clicked.connect(start_hard)

def open_piano_window():
    global pianoWindow
    pianoWindow = QtWidgets.QMainWindow()
    ui = Ui_pianoWindow()
    ui.startpianoWindow(pianoWindow)
    MainWindow.close()
    pianoWindow.show()
    def return_to_main_window():
        pianoWindow.close()
        player.stop()
        MainWindow.show()


    def for_buttons_piano(sheet):
        ui.line_sheet.setText(sheet)
        piano_sheets(sheet)

    def eq():
        global youlose
        if ui.line_sheet.text() == sound_random:
            next()
        else:
            youlose = QMessageBox()
            youlose.setWindowTitle('YOU LOSE')
            youlose.setGeometry(600, 405, 200, 100)
            youlose.setText(f'you lose!\nScore: {ui.score}')
            youlose.setIcon(QMessageBox.Warning)
            youlose.setDefaultButton(QMessageBox.Retry)
            youlose.exec_()
            return_to_main_window()
    def next():
        ui.line_sheet.setText('')
        random_note_piano()
        ui.score += 1
        ui.text_score.setText(f'Score: {ui.score}')

    random_note_piano()
    ui.btn_back_to_menu.clicked.connect(return_to_main_window)
    ui.replay_note.clicked.connect(replay_sheet_piano)
    ui.next_btn.clicked.connect(eq)
    ui.A0.clicked.connect(lambda: for_buttons_piano('A0'))
    ui.B0.clicked.connect(lambda: for_buttons_piano('B0'))
    ui.C1.clicked.connect(lambda: for_buttons_piano('C1'))
    ui.D1.clicked.connect(lambda: for_buttons_piano('D1'))
    ui.E1.clicked.connect(lambda: for_buttons_piano('E1'))
    ui.F1.clicked.connect(lambda: for_buttons_piano('F1'))
    ui.G1.clicked.connect(lambda: for_buttons_piano('G1'))
    ui.A1.clicked.connect(lambda: for_buttons_piano('A1'))
    ui.B1.clicked.connect(lambda: for_buttons_piano('B1'))
    ui.C2.clicked.connect(lambda: for_buttons_piano('C2'))
    ui.D2.clicked.connect(lambda: for_buttons_piano('D2'))
    ui.E2.clicked.connect(lambda: for_buttons_piano('E2'))
    ui.F2.clicked.connect(lambda: for_buttons_piano('F2'))
    ui.G2.clicked.connect(lambda: for_buttons_piano('G2'))
    ui.A2.clicked.connect(lambda: for_buttons_piano('A2'))
    ui.B2.clicked.connect(lambda: for_buttons_piano('B2'))
    ui.C3.clicked.connect(lambda: for_buttons_piano('C3'))
    ui.D3.clicked.connect(lambda: for_buttons_piano('D3'))
    ui.E3.clicked.connect(lambda: for_buttons_piano('E3'))
    ui.F3.clicked.connect(lambda: for_buttons_piano('F3'))
    ui.G3.clicked.connect(lambda: for_buttons_piano('G3'))
    ui.A3.clicked.connect(lambda: for_buttons_piano('A3'))
    ui.B3.clicked.connect(lambda: for_buttons_piano('B3'))
    ui.C4.clicked.connect(lambda: for_buttons_piano('C4'))
    ui.D4.clicked.connect(lambda: for_buttons_piano('D4'))
    ui.E4.clicked.connect(lambda: for_buttons_piano('E4'))
    ui.F4.clicked.connect(lambda: for_buttons_piano('F4'))
    ui.G4.clicked.connect(lambda: for_buttons_piano('G4'))
    ui.A4.clicked.connect(lambda: for_buttons_piano('A4'))
    ui.B4.clicked.connect(lambda: for_buttons_piano('B4'))
    ui.C5.clicked.connect(lambda: for_buttons_piano('C5'))
    ui.D5.clicked.connect(lambda: for_buttons_piano('D5'))
    ui.E5.clicked.connect(lambda: for_buttons_piano('E5'))
    ui.F5.clicked.connect(lambda: for_buttons_piano('F5'))
    ui.G5.clicked.connect(lambda: for_buttons_piano('G5'))
    ui.A5.clicked.connect(lambda: for_buttons_piano('A5'))
    ui.B5.clicked.connect(lambda: for_buttons_piano('B5'))
    ui.C6.clicked.connect(lambda: for_buttons_piano('C6'))
    ui.D6.clicked.connect(lambda: for_buttons_piano('D6'))
    ui.E6.clicked.connect(lambda: for_buttons_piano('E6'))
    ui.F6.clicked.connect(lambda: for_buttons_piano('F6'))
    ui.G6.clicked.connect(lambda: for_buttons_piano('G6'))
    ui.A6.clicked.connect(lambda: for_buttons_piano('A6'))
    ui.B6.clicked.connect(lambda: for_buttons_piano('B6'))
    ui.C7.clicked.connect(lambda: for_buttons_piano('C7'))
    ui.D7.clicked.connect(lambda: for_buttons_piano('D7'))
    ui.E7.clicked.connect(lambda: for_buttons_piano('E7'))
    ui.F7.clicked.connect(lambda: for_buttons_piano('F7'))
    ui.G7.clicked.connect(lambda: for_buttons_piano('G7'))
    ui.A7.clicked.connect(lambda: for_buttons_piano('A7'))
    ui.B7.clicked.connect(lambda: for_buttons_piano('B7'))
    ui.C8.clicked.connect(lambda: for_buttons_piano('C8'))

def open_info():
    global infoWin
    infoWin = QtWidgets.QMainWindow()
    ui = Info_Window()
    ui.start_info(infoWin)
    MainWindow.close()
    infoWin.show()
    def return_to_main_window():
        infoWin.close()
        MainWindow.show()

    ui.back_btn.clicked.connect(return_to_main_window)


ui.btn_playpiano.clicked.connect(open_piano_window)

ui.btn_playguitar.clicked.connect(chose_func)
ui.info.clicked.connect(open_info)


sys.exit(app.exec_())
