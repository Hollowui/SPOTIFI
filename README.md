# SPOTIFI

SPOTIFI is a desktop music playlist manager built with Python and Tkinter.  
The application allows users to load local audio files, organize them into playlists, sort songs by metadata, save/load playlists as JSON files, and navigate through songs using sequential or random playback modes.

> This project was created as a practical Python desktop application focused on GUI development, file handling, playlist management, and custom data structures.

## Features

- Load a single song from the local file system
- Load an entire album/folder of `.mp3` or `.flac` files
- Display song metadata in a playlist interface
- Navigate between songs using previous/next controls
- Switch between sequential and random playback modes
- Save playlists to JSON files
- Load playlists from JSON files
- Delete a selected song or clear the full playlist
- Sort songs by:
  - artist
  - title
  - album
  - track number
  - duration
- View listening history
- Uses a custom circular doubly linked list for playlist navigation
- Uses a stack-like structure to store playback history

## Technologies Used

- Python
- Tkinter
- Mutagen
- Pyllist
- JSON
- Deque from Python collections
