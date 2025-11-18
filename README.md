# Syntax Study — Chat Room App

A collaborative **chat room platform built with Django**, designed for programmers to study together, share knowledge, and collaborate on coding problems. The app includes authentication, profile customization, room creation, Cloudinary-hosted profile avatars, and light/dark theme support.

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

## 🚀 Cloudinary Avatar Hosting (Production Ready)

This project supports **secure image uploads** using **Cloudinary CDN**, ideal for production deployment.

| Mode | Avatar Upload Location |
|-------|------------------------|
| Local Development | Stored in `/media/` directory |
| Production (Render, etc.) | Uploaded to **Cloudinary** |

The app automatically switches between **local file storage** and **Cloudinary** based on environment configuration.

---

## ❓ Why build this app?

Learning and problem-solving improve dramatically when developers collaborate. This platform provides:

- Peer-driven learning  
- Topic-focused chat spaces  
- Zero-distraction study environment  
- Beginner-friendly interaction  

---

## ⚙️ How does it work?

The app is built using **Django** (Python web framework) with the following key components:

### 🔑 Authentication
- Django’s authentication system for **login, logout, and signup**.  
- Profile editing + avatar image upload  

### 🏠 Rooms & Topics
- Rooms are categorized by topics (Python, React, ML, DevOps, etc.)  
- Users can create new rooms or join existing ones.  
- Real chat threads stored per room  

### 🔍 Search
- Search bar allows filtering rooms by topic or room name.  

### 🎨 Styling
- **Custom CSS** with **light and dark mode support**.  
- Responsive layout for both desktop and mobile.  

### 🛠️ Tech Stack

| Layer | Technology |
|--------|-----------|
| Backend | **Django (Python)** |
| Frontend | Django Templates + CSS |
| Database | SQLite (dev), supports PostgreSQL |
| Auth | Django Auth |
| Media | Local FS + Cloudinary |
| Deployment | Render (optional) |

---

## 🚀Demo

👉 [Syntax Study || Chat Room App](https://syntax-studys.onrender.com/)
