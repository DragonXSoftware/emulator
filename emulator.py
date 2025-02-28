import sys
import os
import subprocess
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QHBoxLayout, QMessageBox, QGridLayout)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

class MapEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Map Editor")
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.init_map()

    def init_map(self):
        # Simple 5x5 map grid for demonstration
        for y in range(5):
            for x in range(5):
                tile_button = QPushButton(f"Tile {x},{y}")
                tile_button.setFixedSize(50, 50)
                tile_button.clicked.connect(lambda _, tx=x, ty=y: self.edit_tile(tx, ty))
                self.layout.addWidget(tile_button, y, x)

    def edit_tile(self, x, y):
        QMessageBox.information(self, "Edit Tile", f"Editing tile at position ({x}, {y})")

class GBAEmulator(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.load_rom_button = QPushButton("Load and Run Pokémon ROM (.gba)")
        self.load_rom_button.clicked.connect(self.load_rom)
        self.layout.addWidget(self.load_rom_button)

        self.rom_data_label = QLabel("No ROM loaded.")
        self.layout.addWidget(self.rom_data_label)

        # Emulator Controls
        self.control_layout = QHBoxLayout()
        self.play_button = QPushButton("Play")
        self.pause_button = QPushButton("Pause")
        self.reset_button = QPushButton("Reset")
        self.start_button = QPushButton("Start - Edit Map")

        self.play_button.clicked.connect(self.play_rom)
        self.pause_button.clicked.connect(self.pause_rom)
        self.reset_button.clicked.connect(self.reset_rom)
        self.start_button.clicked.connect(self.open_map_editor)

        self.control_layout.addWidget(self.play_button)
        self.control_layout.addWidget(self.pause_button)
        self.control_layout.addWidget(self.reset_button)
        self.control_layout.addWidget(self.start_button)
        self.layout.addLayout(self.control_layout)

        self.rom_path = None
        self.process = None

    def load_rom(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Load ROM", "", "GBA Files (*.gba)", options=options)
        if file_name:
            self.rom_path = file_name
            self.rom_data_label.setText(f"ROM Loaded: {os.path.basename(file_name)}")
            self.play_rom()

    def play_rom(self):
        if self.rom_path and not self.process:
            self.process = subprocess.Popen(["mgba", self.rom_path])

    def pause_rom(self):
        if self.process:
            QMessageBox.information(self, "Pause", "Pause functionality not yet implemented.")

    def reset_rom(self):
        if self.process:
            self.process.terminate()
            self.process = None
            self.play_rom()

    def open_map_editor(self):
        self.map_editor = MapEditor()
        self.map_editor.show()

class GameMakerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ash's Last Dance - GBA Emulator Integration")
        self.central_widget = QWidget()
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

        # Add Emulator Panel
        self.gba_emulator = GBAEmulator(self)
        self.layout.addWidget(self.gba_emulator)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game_maker = GameMakerApp()
    game_maker.show()
    sys.exit(app.exec_())
