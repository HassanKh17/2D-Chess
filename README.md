# ♟️ 2D Chess Game (Python - Pygame)

## 🧩 Overview
This project is a **2D Chess Game** built entirely using **Python** and **Pygame**.  
It features a fully functional chess engine with move validation, checkmate/stalemate detection, pawn promotion, and an interactive graphical interface.  

The goal of this project is to recreate a traditional chess experience in a simple, visually engaging way while reinforcing programming concepts such as:
- Object-oriented design  
- Game state management  
- GUI rendering with Pygame  
- Event-driven input handling  

---
## 🎥 Gameplay Demo

[![Watch the video](https://img.youtube.com/vi/ZA3ONDq-M34/maxresdefault.jpg)](https://youtu.be/ZA3ONDq-M34)


## 🖼️ Features

### 🎮 Gameplay
- Fully playable chess game between two human players.
- Turn-based system that enforces legal moves.
- Real-time move validation — prevents illegal moves.
- Checkmate and stalemate detection.
- Undo functionality (`Z` key to undo last move).
- Pawn promotion dialog (choice between Queen, Rook, Knight, Bishop).

### 🧠 Logic Engine
- Custom **`GameCondition`** class handles:
  - Piece movement logic for all pieces.
  - Move legality and turn switching.
  - Detection of check, checkmate, and stalemate.
  - Move logging for replay or undo.

### 🕹️ User Interface
- Built entirely with **Pygame**, providing a dynamic visual experience.
- Interactive **main menu** and **information screen**.
- Highlighted selected pieces and possible moves.
- Realistic chessboard and piece sprites.
- Backgrounds, custom fonts, and themed visuals.

### 🔊 Sound Effects & Music
- Piece movement sound.  
- Pawn promotion and checkmate audio cues.  
- Background music and game over sound.

---

## 🧰 Project Structure

```
📁 ChessGame/
│
├── GameDesign.py         # Core game logic, piece movement, and rules
├── Main.py               # Main game loop, UI, and event handling
├── /Game/Pieces/         # Folder containing all chess piece images (.png)
├── checkMusic.wav        # Check sound effect
├── chessMusic.wav        # Background music
├── pieceSound.wav        # Piece Move sound
├── gameOver.wav          # Game over sound
└──promotionSound1.wav   # Pawn promotion sound
```

> ⚠️ Make sure all media files (images, sounds, fonts) are correctly placed in their directories as referenced in the code.

---

## 🚀 How to Run

### ✅ Prerequisites
You’ll need **Python 3.x** and **Pygame** installed.

Install Pygame via pip:
```bash
pip install pygame
```

### ▶️ Launching the Game
Run the main script:
```bash
python Main.py
```

### 🧩 Controls
- **Mouse Left Click** → Select and move pieces.  
- **Z key** → Undo last move.  
- **Main Menu Buttons:**
  - **PLAY** → Start new game.
  - **INFO** → Learn about pieces and checkmate rules.
  - **QUIT** → Exit the game.

---

## ⚙️ Code Structure Highlights

### `GameDesign.py`
Handles the **game logic**:
- `GameCondition` – Stores the current state of the board and all valid moves.
- `Move` – Represents a single move, storing its start and end positions, captured pieces, and promotion data.

### `Main.py`
Handles the **visuals and user input**:
- Draws the chessboard and pieces using Pygame.
- Manages menus, user clicks, and event handling.
- Integrates music and sound effects.
- Implements a guiding system to highlight legal moves.

---

## 🧠 Future Improvements
- Add AI opponent using Minimax algorithm.
- Implement online multiplayer.
- Include move history UI panel.
- Add timer for each player.
- Make the UI responsive and scalable.

---

