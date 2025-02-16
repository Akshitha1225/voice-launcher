### **Project: Voice Command System to Open Applications**  

#### **📌 Overview**  
This Python-based project allows users to open applications and websites using voice commands. When the user says **"hello [app]"** or **"hai [app]"**, the system recognizes the command and opens the corresponding app or website.

---

### **🚀 How to Run the Project**  

#### **Step 1: Install Dependencies**  
Make sure Python is installed. Then, install the required library:  
```sh
pip install SpeechRecognition
```

---

#### **Step 2: Run the Script**  
Open a terminal or command prompt, navigate to the project folder, and run:  
```sh
python task1.py
```

---

#### **Step 3: Speak Your Command**  
When the program starts, it will listen for your voice. Say:  
- **"hello WhatsApp"** → Opens WhatsApp  
- **"hello Chrome"** → Opens Google Chrome  
- **"hello YouTube"** → Opens YouTube  
- **"hello Notepad"** → Opens Notepad  
- **"hello Calculator"** → Opens Calculator  
- **"hello ChatGPT"** → Opens ChatGPT  
- **"hello Gmail"** → Opens Gmail  
- **"hello Camera"** → Opens the camera  
- **"hello File Explorer"** → Opens File Explorer  

---

### **⚡ Features**  
✅ Recognizes voice commands using **Google Speech Recognition**  
✅ Opens **local applications** and **websites**  
✅ **Customizable** – You can add more apps!  

---

### **🛠️ Troubleshooting**  
🔹 If the command is not recognized:  
- Ensure your **microphone is working**  
- Speak **clearly and loudly**  

🔹 If an app doesn’t open:  
- Check the **app path** in `app_commands` inside `task1.py`  
- Modify the `.exe` or URL accordingly  

