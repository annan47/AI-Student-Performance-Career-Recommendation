# AI-Based Student Performance & Career Recommendation System

## Project Overview

The AI-Based Student Performance & Career Recommendation System is a web-based application that analyzes a student's academic performance, technical skills, soft skills, interests and career preferences.

The system uses a Machine Learning model to recommend a suitable career path based on the information provided by the student.

The application provides a personalized career recommendation along with career details, required skills and suggested next steps.

## Problem Statement

Students often have difficulty deciding which career path is suitable for them because they may not know how their academic performance, technical skills, interests and career preferences relate to different career options.

This project aims to develop an AI-based system that analyzes these factors and provides a career recommendation to help students explore suitable career paths.

## Objectives

- Collect student academic and skill information.
- Analyze technical and soft skills.
- Consider student interests and career preferences.
- Use Machine Learning to predict a suitable career.
- Store student assessments and recommendations securely in a MySQL database.
- Display personalized career information.
- Allow students to view their latest saved recommendation.

## Technologies Used

### Frontend

- HTML
- CSS

### Backend

- Python
- Flask

### Database

- MySQL

### Machine Learning

- Python
- Pandas
- Scikit-learn
- Random Forest Classifier
- Joblib

### Development Tools

- Visual Studio Code
- MySQL Workbench
- Git
- GitHub

## AI / Machine Learning

The system uses a **Random Forest Classifier** for career prediction.

The model uses student information such as:

- Academic marks
- Overall percentage
- Number of projects
- Programming skills
- Technical skills
- Soft skills
- Career interests
- Work preferences
- Career goals

Categorical values are converted into numerical features using **One-Hot Encoding** before being provided to the Machine Learning model.

## Career Categories

The current prototype supports the following career categories:

1. Data Scientist
2. Machine Learning Engineer
3. Full Stack Developer
4. Software Developer
5. Cyber Security Analyst
6. Database Administrator
7. Network Engineer
8. Cloud Engineer
9. UI UX Designer

## Main Features

- Student registration
- Student login
- Password hashing
- Student dashboard
- Academic assessment
- Technical skill assessment
- Soft skill assessment
- Career interest assessment
- AI-based career prediction
- Career description
- Recommended skills
- Suggested next step
- MySQL data storage
- View latest career recommendation
- Machine Learning model evaluation

## Project Structure

```text
AI-Student-Performance-Career-Recommendation/
│
├── ai/
│   ├── career_model.pkl
│   ├── preprocessor.pkl
│   ├── generate_data.py
│   ├── train_model.py
│   ├── training_data.csv
│   └── training_data_backup.csv
│
├── static/
│   └── css/
│       └── style.css
│
├── templates/
│   ├── index.html
│   ├── register.html
│   ├── login.html
│   ├── dashboard.html
│   ├── assessment.html
│   └── recommendation.html
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore