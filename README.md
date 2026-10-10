# Movie Night Mixer — PySide6 Research Milestone

**Movie Night Mixer** is a themed desktop app made with **Python** and **PySide6**. The user chooses a genre, mood, group size, and available time. The app generates a fictional movie-night recommendation with a snack and atmosphere tip, and can save favorite combinations locally.

## Run it on Windows

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install --upgrade pip
py -m pip install -r requirements.txt
py main.py
```

If PowerShell blocks activation, use `\.venv\Scripts\activate.bat` in Command Prompt instead.

## Research notes

PySide6 is a Python binding for Qt 6 and can run the same Qt Widgets application on Windows, macOS, and Linux. Qt Quick/QML is an alternative better suited to highly animated or touch-first interfaces; Qt Widgets was chosen here for its strong controls, layouts, tables, and desktop UI support.

| Technology | Strength | Trade-off |
| --- | --- | --- |
| PySide6 | Polished, cross-platform desktop UI and Qt tools | Larger installation; Qt licensing matters |
| Tkinter | Included with many Python installs | Less styling flexibility |
| Kivy | Touch/mobile apps | Less conventional desktop controls |
| React/Django web app | Browser access | Server/browser deployment required |

### Libraries and concepts

- `PySide6.QtWidgets`: window, input controls, result card, buttons, and table.
- `PySide6.QtCore.Qt`: UI alignment constants.
- `PySide6.QtGui.QFont`: app-wide font.
- Built-in `random`, `json`, and `dataclasses`: variety, local persistence, and a clear data model.
- Signals and slots connect the buttons to `generate_night` and `save_current`.
- Qt style sheets give the interface a custom dark, cinema-inspired visual design.

### Package manager: pip

`pip` installs packages into the active `.venv` virtual environment. The `requirements.txt` file lets a teammate reproduce the installation with `py -m pip install -r requirements.txt`. Useful commands are `py -m pip list`, `py -m pip show PySide6`, and `py -m pip freeze > requirements-lock.txt`.

### Deployment and limitations

PySide6 wheels include Qt binaries, so a separate Qt installation is not required for this project. For distribution to users without Python, `pyside6-deploy` can bundle an executable using Nuitka; test the package on each operating system. This sample intentionally uses fictional titles and local JSON. A future version could use a real movie API, posters, ratings, and a database.

## Video demo

Run `py main.py`, set the four options, click **Mix My Night**, explain the result card, save a favorite, and restart the app to show that the saved table persists.

## GitHub checklist

- [ ] Push this project to your personal repository with multiple meaningful commits.
- [ ] Record/upload the demo video.
- [ ] Create `Research Milestone: <yourusername>` in the team repository.
- [ ] Add the repository and video links, then mention `@instructors` and required TAs.

## Sources

- [Qt for Python: Getting Started](https://doc.qt.io/qtforpython-6/gettingstarted.html)
- [Qt for Python: Deployment](https://doc.qt.io/qtforpython-6/deployment/index.html)
