# 💬 Python Chat Application (Socket + Tkinter)

A simple **real-time chat application** built in Python using:  
- **Sockets** (for networking)  
- **Threads** (for handling multiple tasks)  
- **Tkinter** (for GUI client interface)  

The project consists of:
- A **Server** (runs in terminal)  
- A **GUI Client** (runs with Tkinter)  

---

## 🚀 Features
- Real-time chat between server and client  
- Server runs in terminal (console-based)  
- Client has a **GUI chatbox** using Tkinter  
- Supports multiple messages until exit  
- Type `"exit"` in the server to close the chat  

---

## 🛠️ Tech Stack
- [Python](https://www.python.org/) 🐍  
- `socket` → TCP communication  
- `threading` → background receive/send handling  
- `tkinter` → GUI chat client  

---

## 📂 Project Structure
CHAT_BOT/
│── server.py # Console-based server
│── client_gui.py # GUI client with Tkinter
│── README.md # Project documentation


## 📦 Installation & Setup

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/chat-app.git
   cd chat_bot

   
## run the app 
In first terminal
---cmd
python client_gui.py

In second terminal
---cmd
python server.py

