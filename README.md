# Movie Night Mixer Research Milestone

An individual, interactive PySide6 desktop prototype for **Movie Night Mixer**. It demonstrates the chosen desktop framework and Python package manager without requiring a movie-streaming account, internet connection, external API, database server, or real movie catalog.

## What it does

1. Lets the user choose a movie genre: Adventure, Comedy, Mystery, or Sci-Fi.
2. Lets the user choose a mood, group size, and available runtime.
3. Generates a fictional movie-night recommendation based on those choices.
4. Pairs the recommendation with a snack and an atmosphere tip.
5. Lets the user save favorite movie-night combinations to a local table.

The app uses a small in-program collection of fictional titles and randomly selects a compatible option. This is intentional: it makes the prototype easy to test and demonstrates user input, events, UI updates, styling, and local data storage without relying on an external movie API.

## Technologies researched

| **Technology** | **Role** | **Why it fits Movie Night Mixer** |
| --- | --- | --- |
| Python | Application logic and local data handling | Accessible, readable, and includes useful built-in tools such as `random`, `json`, and `dataclasses`. |
| PySide6 | Desktop UI framework | Supports a polished local desktop app with drop-downs, buttons, styled cards, and tables. |
| pip + venv | Package/environment manager | Installs PySide6 in an isolated environment so another developer can reproduce the project setup. |
| JSON | Local prototype storage | Saves favorite movie-night ideas without adding a database or cloud service. |
| TMDb or OMDb (future evaluation) | Possible real movie-data API | Could provide real titles, posters, ratings, and streaming details in a future version, but is not needed for this milestone prototype. |

## Run it

Install Python once, then run these commands from the project folder in VS Code's terminal or PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install --upgrade pip
py -m pip install -r requirements.txt
py main.py
```

If PowerShell blocks the activation command, open Command Prompt in the project folder and run:

```bat
py -m venv .venv
.venv\Scripts\activate.bat
py -m pip install -r requirements.txt
py main.py
```

The first command creates an isolated environment. The install command reads `requirements.txt` and installs PySide6. The final command opens Movie Night Mixer.

## Project scope

This milestone prototype deliberately excludes real movie titles, streaming integrations, user accounts, cloud services, online APIs, sharing between users, and a full database. Saved favorites remain in a local `movie_night_favorites.json` file on the user's computer.

The shared capstone application could later expand these same UI patterns into real movie searches, filters, poster artwork, friend/group recommendations, watch-list sharing, ratings, and database-backed accounts.
