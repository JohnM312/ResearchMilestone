"""Movie Night Mixer: a polished PySide6 desktop app."""
from __future__ import annotations
import json, random, sys
from dataclasses import asdict, dataclass
from pathlib import Path
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QComboBox, QFrame, QHBoxLayout, QLabel, QMainWindow, QMessageBox, QPushButton, QSpinBox, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

DATA_FILE = Path("movie_night_favorites.json")
MOVIES = {"Adventure": [("The Map Under Midnight", "An old train ticket leads a mismatched crew toward a hidden coastal town."), ("Lanterns Beyond the Ridge", "A stormy hike becomes a race to return a stolen artifact.")], "Comedy": [("One More Takeout Order", "A harmless delivery mix-up snowballs into an unexpectedly great night."), ("The Accidental Reunion", "Three old friends bluff their way into a glamorous alumni event.")], "Mystery": [("The Last Light in Harbor House", "A curious visitor follows clues left in a seaside hotel guestbook."), ("Midnight at Platform Nine", "A missed train uncovers a code hidden in station announcements.")], "Sci-Fi": [("Signal After Sunset", "A college radio station receives a transmission from tomorrow."), ("Orbit of Us", "A tiny repair crew must save their ship before its last playlist ends.")]}
MOODS = {"Cozy": ("Soft lighting, blankets, and a comfort snack.", "☁"), "Chaotic": ("Loud reactions encouraged—pick the messiest snack.", "⚡"), "Chill": ("Keep the room calm and the phones face-down.", "◌"), "Spooky": ("Dim the lights; leave one lamp on for dramatic effect.", "☾")}
SNACKS = ["loaded popcorn", "mini tacos", "chocolate-covered pretzels", "nachos", "ice-cream sandwiches"]

@dataclass
class Favorite:
    title: str
    genre: str
    mood: str
    runtime: int

class MovieNightMixer(QMainWindow):
    def __init__(self):
        super().__init__(); self.favorites = self.load_favorites(); self.current = None
        self.setWindowTitle("Movie Night Mixer"); self.setMinimumSize(900, 620); self.build_ui(); self.refresh_favorites()

    def build_ui(self):
        central = QWidget(); central.setObjectName("central"); self.setCentralWidget(central)
        layout = QVBoxLayout(central); layout.setContentsMargins(34, 30, 34, 30); layout.setSpacing(18)
        header = QHBoxLayout(); title = QLabel("MOVIE NIGHT\nMIXER"); title.setObjectName("title"); header.addWidget(title); header.addStretch()
        badge = QLabel("✦ CURATED FOR TONIGHT"); badge.setObjectName("badge"); header.addWidget(badge, alignment=Qt.AlignmentFlag.AlignTop); layout.addLayout(header)
        subtitle = QLabel("Build a themed movie night in one click—then save the combinations your group loves."); subtitle.setObjectName("subtitle"); layout.addWidget(subtitle)
        controls = QFrame(); controls.setObjectName("controls"); row = QHBoxLayout(controls); row.setContentsMargins(18, 16, 18, 16); row.setSpacing(16)
        self.genre = self.combo(["Adventure", "Comedy", "Mystery", "Sci-Fi"]); self.mood = self.combo(["Cozy", "Chaotic", "Chill", "Spooky"]); self.group = QSpinBox(); self.group.setRange(1,12); self.group.setValue(3); self.group.setSuffix(" people"); self.runtime = self.combo(["Under 90 minutes", "Around 2 hours", "No time limit"])
        for label, widget in [("GENRE",self.genre),("MOOD",self.mood),("GROUP SIZE",self.group),("TIME",self.runtime)]:
            col = QVBoxLayout(); tag = QLabel(label); tag.setObjectName("fieldLabel"); col.addWidget(tag); col.addWidget(widget); row.addLayout(col)
        mix = QPushButton("MIX MY NIGHT  →"); mix.setObjectName("mixButton"); mix.clicked.connect(self.generate_night); row.addWidget(mix, alignment=Qt.AlignmentFlag.AlignBottom); layout.addWidget(controls)
        self.result = QFrame(); self.result.setObjectName("result"); card = QVBoxLayout(self.result); card.setContentsMargins(25,20,25,20)
        self.kicker = QLabel("YOUR NIGHT STARTS HERE"); self.kicker.setObjectName("resultKicker"); self.result_title = QLabel("Pick your ingredients, then hit Mix My Night."); self.result_title.setObjectName("resultTitle"); self.result_title.setWordWrap(True)
        self.description = QLabel("You’ll get a fictional feature, snack pairing, and an atmosphere tip."); self.description.setObjectName("resultDescription"); self.description.setWordWrap(True)
        self.save = QPushButton("♡ SAVE THIS NIGHT"); self.save.setObjectName("saveButton"); self.save.setEnabled(False); self.save.clicked.connect(self.save_current)
        for item in [self.kicker,self.result_title,self.description,self.save]: card.addWidget(item)
        layout.addWidget(self.result)
        saved = QLabel("SAVED NIGHTS"); saved.setObjectName("sectionLabel"); layout.addWidget(saved)
        self.table = QTableWidget(0,4); self.table.setObjectName("table"); self.table.setHorizontalHeaderLabels(["FEATURE","GENRE","MOOD","RUNTIME"]); self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows); self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers); self.table.verticalHeader().setVisible(False); self.table.horizontalHeader().setStretchLastSection(True); layout.addWidget(self.table)

    def combo(self, choices):
        box = QComboBox(); box.addItems(choices); return box

    def generate_night(self):
        genre, mood = self.genre.currentText(), self.mood.currentText(); title, plot = random.choice(MOVIES[genre]); minutes = {"Under 90 minutes":85,"Around 2 hours":115,"No time limit":140}[self.runtime.currentText()]; note, symbol = MOODS[mood]
        self.current = Favorite(title, genre, mood, minutes); self.kicker.setText(f"{symbol}  {mood.upper()} · {self.group.value()} PEOPLE · {minutes} MIN"); self.result_title.setText(title); self.description.setText(f"{plot}\n\nPair it with <b>{random.choice(SNACKS)}</b>. {note}"); self.save.setEnabled(True); self.save.setText("♡ SAVE THIS NIGHT")

    def save_current(self):
        if self.current in self.favorites: QMessageBox.information(self,"Already saved","That movie night is already in your saved list."); return
        self.favorites.append(self.current); self.save_favorites(); self.refresh_favorites(); self.save.setText("♥ SAVED TO FAVORITES")

    def refresh_favorites(self):
        self.table.setRowCount(len(self.favorites))
        for row, item in enumerate(self.favorites):
            for col, value in enumerate([item.title,item.genre,item.mood,f"{item.runtime} min"]): self.table.setItem(row,col,QTableWidgetItem(value))

    def load_favorites(self):
        if not DATA_FILE.exists(): return []
        try: return [Favorite(**item) for item in json.loads(DATA_FILE.read_text(encoding="utf-8"))]
        except (json.JSONDecodeError,OSError,TypeError): return []

    def save_favorites(self): DATA_FILE.write_text(json.dumps([asdict(x) for x in self.favorites],indent=2),encoding="utf-8")

STYLE = """
QWidget#central { background:#171622; color:#F6F2FF; } QLabel#title { color:#FFCF70; font-size:28px; font-weight:800; letter-spacing:3px; } QLabel#subtitle { color:#B5AFC8; font-size:13px; } QLabel#badge { background:#302C44; color:#BFD8FF; border-radius:12px; padding:8px 11px; font-size:11px; font-weight:700; } QFrame#controls { background:#252337; border:1px solid #3D3A52; border-radius:16px; } QLabel#fieldLabel, QLabel#sectionLabel, QLabel#resultKicker { color:#A7A0BC; font-size:10px; font-weight:700; letter-spacing:1.5px; } QComboBox,QSpinBox { background:#302D43; border:1px solid #4A4663; border-radius:8px; padding:8px 10px; min-width:128px; color:#F6F2FF; } QComboBox::drop-down { border:0; width:22px; } QPushButton#mixButton { background:#FFCA68; color:#282332; border:0; border-radius:9px; padding:11px 16px; font-weight:800; } QPushButton#mixButton:hover { background:#FFE09A; } QFrame#result { background:#38324D; border:1px solid #5B5276; border-radius:16px; } QLabel#resultTitle { color:#FFF7E6; font-size:25px; font-weight:800; margin-top:3px; } QLabel#resultDescription { color:#DDD6EC; font-size:13px; } QPushButton#saveButton { background:transparent; color:#FFCF70; border:1px solid #806A43; border-radius:8px; padding:8px 12px; font-weight:700; margin-top:4px; } QPushButton#saveButton:disabled { color:#857B97; border-color:#524B60; } QTableWidget#table { background:#211F31; alternate-background-color:#28253A; border:1px solid #3D3A52; border-radius:10px; gridline-color:#3D3A52; color:#E8E2F2; } QHeaderView::section { background:#302D43; color:#AAA1C4; border:0; padding:8px; font-weight:700; font-size:10px; } QTableWidget::item { padding:6px; border-bottom:1px solid #322F46; } QTableWidget::item:selected { background:#51466D; }
"""

if __name__ == "__main__":
    app = QApplication(sys.argv); app.setStyle("Fusion"); app.setFont(QFont("Segoe UI",10)); app.setStyleSheet(STYLE); window = MovieNightMixer(); window.show(); sys.exit(app.exec())
