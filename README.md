# Syntax Study — Chat Room App

A collaborative **chat room platform built with Django**, designed for programmers to study together, share knowledge, and collaborate on coding problems. The app includes authentication, profile customization, room creation, and light/dark theme support.

---

## 📌 What is this app?

This is a **topic-based chat room application** where users can:
- 🔑 Register, log in, and log out securely.  
- 👤 Edit their profile (update bio and change profile picture).  
- 🏠 Create and join **chat rooms** based on programming languages or topics.  
- 📝 Post messages in real-time discussions.  
- 🔍 Search topics and rooms easily with a search bar.  
- 🌞🌙 Switch seamlessly between **light and dark themes**.  
- 📱 Enjoy a **mobile-responsive design** that works across devices.  

It’s like a **mini-Discord/Slack for programmers**, but focused on **study and learning**.  

---

## ❓ Why build this app?

Programming is best learned together. Many beginners and advanced developers face challenges like:
- Finding peers to **discuss coding concepts**.  
- Preparing for **coding interviews** or studying algorithms.  
- Needing a **focused, distraction-free space** to collaborate.  

This app solves these problems by providing a dedicated platform for study-focused, programming-specific discussions.  

---

## ⚙️ How does it work?

The app is built using **Django** (Python web framework) with the following key components:

### 🔑 Authentication
- Django’s authentication system for **login, logout, and signup**.  
- Profile editing   

### 🏠 Rooms & Topics
- Each **Room** belongs to a **Topic** (e.g., Python, JavaScript, C++).  
- Users can create new rooms or join existing ones.  
- Messages are stored and displayed in room threads.  

### 🔍 Search
- Search bar allows filtering rooms by topic or name.  

### 🎨 Styling
- **Custom CSS** with **light and dark mode support**.  
- Responsive layout for both desktop and mobile.  

### 🛠️ Tech Stack
- **Backend**: Django  
- **Frontend**: Django Templates + CSS (with theme variables)  
- **Database**: SQLite (default, can be swapped for PostgreSQL/MySQL)  
- **Static/Media**: Django staticfiles (profile image upload support)  

---

## 🚀Demo

👉 [Syntax Study || Chat Room App](https://sub-keeper.netlify.app/)
