# AI-Based Student Performance & Career Recommendation System

## Project Overview

The **AI-Based Student Performance & Career Recommendation System** is a web-based application that analyzes a student's academic performance, technical skills, soft skills, interests, and career preferences.

The system uses a Machine Learning model to recommend a suitable career path based on the information provided by the student.

The application provides a personalized career recommendation along with career details, required skills, and suggested next steps.

The system also includes an **Admin Panel** for managing students, assessments, and AI-generated career recommendations.

---

## Problem Statement

Students often have difficulty deciding which career path is suitable for them because they may not know how their academic performance, technical skills, interests, and career preferences relate to different career options.

This project aims to develop an AI-based system that analyzes these factors and provides a career recommendation to help students explore suitable career paths.

---

## Objectives

- Collect student academic and skill information.
- Analyze technical and soft skills.
- Consider student interests and career preferences.
- Use Machine Learning to predict a suitable career.
- Store student assessments and recommendations in a MySQL database.
- Display personalized career information.
- Allow students to view their latest saved recommendation.
- Provide an Admin Panel for managing student and assessment information.
- Evaluate the Machine Learning model during development.

---

## Technologies Used

### Frontend

- HTML
- CSS

### Backend

- Python
- Flask

### Database

- MySQL
- MySQL Workbench

### Machine Learning

- Python
- Pandas
- Scikit-learn
- Random Forest Classifier
- Joblib

### Development Tools

- Visual Studio Code
- Git
- GitHub
- Python Virtual Environment (`venv`)

---

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

The trained model and preprocessing object are saved using **Joblib** and loaded by the Flask application.

### Model Evaluation

The Machine Learning model was evaluated using a train-test split during development.

The current training dataset is synthetic and is intended for **academic project demonstration and prototype purposes**. Therefore, the model's results should not be considered a reliable real-world career assessment.

---

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

---

## Main Features

### Student Features

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
- Session-based authentication

### Admin Features

- Admin login
- Admin dashboard
- View total registered students
- View total assessments
- View AI recommendations
- Manage and search registered students
- View student assessment history
- Search assessments
- View complete assessment details
- Search AI career recommendations
- View recommended careers for students
- Admin session protection

---

## System Workflow

The system follows the following workflow:

1. Student registers an account.
2. Student logs into the system.
3. Student completes the assessment form.
4. Academic performance, technical skills, soft skills, interests, and career preferences are collected.
5. The data is processed using the saved preprocessing model.
6. The Machine Learning model predicts a career category.
7. The assessment and recommendation are stored in MySQL.
8. The student receives a personalized career recommendation.
9. The student can view the latest saved recommendation.
10. The administrator can view students, assessments, and recommendations through the Admin Panel.

---

## Database

The application uses **MySQL** for storing application data.

The database stores information related to:

- Students
- Student assessments
- Career recommendations
- Administrator accounts

Sensitive database credentials are stored in an `.env` file and are not included in the GitHub repository.

---

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
│   ├── recommendation.html
│   │
│   ├── admin_login.html
│   ├── admin_dashboard.html
│   ├── admin_students.html
│   ├── admin_assessments.html
│   ├── admin_assessment_detail.html
│   ├── admin_recommendations.html
│   └── admin_student_assessments.html
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore