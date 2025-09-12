# 🔑 Password Generator (Streamlit)

A secure and customizable **Password Generator** built with **Streamlit**.  
It allows users to generate strong passwords with adjustable length, character sets, and quantity.  

---

## 🚀 Features
- Choose **password length** (4 – 64 characters)  
- Generate **multiple passwords** at once (1 – 20)  
- Options to include:
  - ✅ Lowercase letters (a-z)  
  - ✅ Uppercase letters (A-Z)  
  - ✅ Digits (0-9)  
  - ✅ Symbols (!@#$%^&* etc.)  
- Uses Python’s **`secrets`** module for cryptographically secure password generation  
- Copy/Download generated passwords instantly  

---

## 🛠️ Tech Stack
- [Python](https://www.python.org/) 🐍  
- [Streamlit](https://streamlit.io/) (UI Framework)  
- Built-in modules:  
  - `secrets` → secure random generation  
  - `string` → character sets  

---

## 📦 Installation & Setup

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/password-generator.git
   cd password-generator

## run the app 
---cmd
streamlit run password_app.py