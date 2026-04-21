# ☁️ Cloud Aggregator With Disaster Recovery

A complete multi-cloud web application that provides a **Single Dashboard** to manage cloud services across providers and ensures **Business Continuity** through Automated Disaster Recovery.

This project integrates **AWS S3** and **Azure Blob Storage** using a Flask-based web platform with authentication, monitoring, and failover controls.

---

# 🚀 Overview

Cloud Aggregator with Disaster Recovery is designed to simplify multi-cloud management by giving users one platform to control services hosted on multiple cloud providers.

The system also includes a disaster recovery mechanism that automatically transfers files from a primary cloud provider (**AWS**) to a backup provider (**Azure**) when failure occurs.

This helps reduce downtime and maintain service availability.

---

# ✨ Key Features

## 🔐 Authentication System
- User Registration
- Secure Login
- Logout
- Session Management

## ☁️ Multi-Cloud Aggregation
- Connect AWS S3
- Connect Azure Blob Storage
- Manage cloud data from one dashboard

## ♻️ Disaster Recovery
- Manual failover trigger
- Transfer files from AWS → Azure
- Maintenance mode switch
- Redirect users to backup server

## 📊 Dashboard
- Centralized control panel
- Access cloud tools
- Navigate modules easily

## 🎨 Responsive UI
- Bootstrap frontend
- Mobile friendly pages

---

# 🏗️ System Architecture

```text
User
 ↓
Flask Frontend Dashboard
 ↓
 ├── Authentication Module
 ├── Prediction Module
 ├── Disaster Recovery Module
 │     ├── AWS S3 (Primary)
 │     └── Azure Blob (Backup)
 └── Maintenance Server


📦 Modules
1. DR_frontend

Main application containing:
Flask routes
Login system
Templates
Static assets
Cloud integration
Disaster recovery logic

2. Zomato-hosted

Secondary Flask application used to:
Show maintenance mode
Redirect during failover
Simulate backup hosting


🛠️ Technologies Used
Backend
Python 3.x
Flask
Database
SQLite
SQLAlchemy ORM
Frontend
HTML5
CSS3
Bootstrap
Jinja2 Templates
Authentication
Flask-Login
Flask-WTF
Cloud Services
AWS S3 (boto3)
Azure Blob Storage SDK
ML / Data
Pandas
NumPy
Scikit-learn


📁 Project Structure
DR_PROJECT_FINAL_01/
│
├── DR_frontend/
│   ├── app.py
│   ├── requirements.txt
│   ├── database.db
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   └── templates/
│       ├── index.html
│       ├── login.html
│       ├── signup.html
│       ├── dashboard.html
│       ├── prediction.html
│       ├── prediction_result.html
│       ├── initiate_dr.html
│       └── ...
│
└── Zomato-hosted/
    ├── app.py
    └── README.md


🔑 Configuration

Create a .env file in project root:

SECRET_KEY=your_secret_key
DATABASE_URL=sqlite:///database.db

AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_BUCKET_NAME=your_bucket_name
AWS_REGION=us-east-1

AZURE_CONNECTION_STRING=your_connection_string
AZURE_CONTAINER_NAME=your_container_name


▶️ Run Application
python app.py
Open browser --> http://127.0.0.1:8000


🔄 How Disaster Recovery Works
Normal Mode
App runs using AWS resources
Files stored in S3 bucket
Failure Triggered
Maintenance mode enabled
Recovery process starts
Recovery Process
Read files from AWS S3
Upload files to Azure Blob Storage
Redirect users to backup server
Result
Minimal downtime
Data preserved
Service continues
