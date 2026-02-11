# Online Multiplayer Chess

Description: An online multiplayer chess game. Supports infinite players playing against
random opponents on different machines on different networks. This project was created
using python 3.7, pygame and the sockets module from python3. It runs on a basic client
server system where a server script handles all incoming connections and game management.
The clients simply handle the UI and game play.

## Install

### Runtime dependencies

```bash
python -m pip install -r requirements.txt
```

> Note: This project uses `pygame`. In headless environments (no display), `pygame` may
> require additional OS packages and/or a virtual framebuffer (e.g., Xvfb) to create a
> window. The platform preview/startup flow is unchanged by this repository.

### Dev dependencies (lint/format)

This repository uses `ruff` (lint) and `black` (format).

```bash
python -m pip install -r requirements-dev.txt
```

## Linting / formatting (dev)

```bash
ruff check . --fix
black .
```

CI-style (check only):

```bash
ruff check .
black . --check
```

# Required:
- Python 3.x
- pygame

# TO MAKE THIS CODE WORK...
You will need to change the server address from within the following two files:
- client.py
- server.py

You will also need to run server.py on some kind of server. After that you can launch two instances of game from anywhere to play online chess.

# Known Bugs:
- Checkmate does not work, if you loose or win you will need to end the game by hitting "q"
- Very rare bug where a certain move will crash the game
- No Enpesant Pawn Rule

# LICENSE:
*NOT FOR COMMERCIAL USE*
If you intened to use any of my code for commercial use please contact me and get my permission. If you intend to make money using any of my code please ask my permission.

# 💻 Launch Your Software Development Career Today!  

🎓 **No degree? No problem!** My program equips you with everything you need to break into tech and land an entry-level software development role.  

🚀 **Why Join?**  
- 💼 **$70k+ starting salary potential**  
- 🕐 **Self-paced:** Complete on your own time  
- 🤑 **Affordable:** Low risk compared to expensive bootcamps or degrees
- 🎯 **45,000+ job openings** in the market  

👉 **[Start your journey today!](https://techwithtim.net/dev)**  
No experience needed—just your determination. Future-proof your career and unlock six-figure potential like many of our students have!
