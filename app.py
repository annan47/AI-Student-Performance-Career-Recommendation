from flask import Flask, render_template, request, session, redirect
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
import os
import pandas as pd
import joblib
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

# Load trained AI model and preprocessor
model = joblib.load("ai/career_model.pkl")
preprocessor = joblib.load("ai/preprocessor.pkl")

career_details = {
    "Data Scientist": {
        "description": "Analyzes data and uses statistics and machine learning to discover useful insights.",
        "skills": "Python, SQL, Statistics, Machine Learning, Data Analysis",
        "next_step": "Improve Python, SQL, statistics and machine learning skills."
    },

    "Machine Learning Engineer": {
        "description": "Builds and deploys machine learning models for real-world applications.",
        "skills": "Python, Machine Learning, Scikit-learn, Mathematics, Git",
        "next_step": "Practice machine learning algorithms and build ML projects."
    },

    "Full Stack Developer": {
        "description": "Develops both the frontend and backend parts of web applications.",
        "skills": "HTML, CSS, JavaScript, Python/Flask, SQL",
        "next_step": "Build complete web applications using frontend and backend technologies."
    },

    "Software Developer": {
        "description": "Designs, develops, tests and maintains software applications.",
        "skills": "Programming, OOP, SQL, Git, Problem Solving",
        "next_step": "Build programming projects and strengthen problem-solving skills."
    },

    "Cyber Security Analyst": {
        "description": "Protects computer systems, networks and data from security threats.",
        "skills": "Networking, Linux, Cyber Security, Python, Security Tools",
        "next_step": "Learn networking, Linux and fundamental cyber security concepts."
    },

    "Database Administrator": {
        "description": "Manages databases and helps ensure that data remains secure, available and reliable.",
        "skills": "SQL, MySQL, Database Design, Backup & Recovery, Database Security",
        "next_step": "Improve your SQL and database administration skills."
    },

    "Network Engineer": {
        "description": "Designs, manages and maintains computer networks and network infrastructure.",
        "skills": "Networking, TCP/IP, Routing, Switching, Network Security",
        "next_step": "Strengthen networking fundamentals and practice network configuration."
    },

    "Cloud Engineer": {
        "description": "Designs and manages applications, infrastructure and services on cloud platforms.",
        "skills": "Cloud Computing, Networking, Linux, Git, Security",
        "next_step": "Learn cloud fundamentals and practice deploying applications."
    },

    "UI UX Designer": {
        "description": "Designs user interfaces and experiences that are useful, accessible and easy to use.",
        "skills": "UI Design, UX Research, Wireframing, Prototyping, Creativity",
        "next_step": "Practice designing interfaces and create a UI/UX portfolio."
    }
}

def get_db_connection():
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

    return connection


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        password_hash = generate_password_hash(password)

        connection = get_db_connection()

        cursor = connection.cursor()

        query = """
            INSERT INTO students
            (name, email, password_hash)
            VALUES (%s, %s, %s)
        """

        cursor.execute(query, (name, email, password_hash))

        connection.commit()

        cursor.close()
        connection.close()

        return "Registration successful!"

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        query = """
            SELECT * FROM students
            WHERE email = %s
        """

        cursor.execute(query, (email,))

        student = cursor.fetchone()

        cursor.close()
        connection.close()

        if student is None:
            return "Email not registered!"

        if check_password_hash(student["password_hash"], password):
            session["student_id"] = student["student_id"]
            session["student_name"] = student["name"]
            return redirect("/dashboard")

        else:

            return "Incorrect password!"

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():

    if "student_id" not in session:
        return "Please login first!"

    return render_template(
        "dashboard.html",
        student_name=session["student_name"]
    )

@app.route("/assessment", methods=["GET", "POST"])
def assessment():

    if "student_id" not in session:
        return redirect("/login")

    if request.method == "POST":

        # Academic Information
        course = request.form["course"]
        semester = request.form["semester"]
        overall_percentage = request.form["overall_percentage"]

        programming_marks = request.form["programming_marks"]
        maths_marks = request.form["maths_marks"]
        database_marks = request.form["database_marks"]
        os_marks = request.form["os_marks"]
        network_marks = request.form["network_marks"]

        projects_completed = request.form["projects_completed"]


        # Technical Skills
        python = request.form["python"]
        java = request.form["java"]
        cpp = request.form["cpp"]
        html_css = request.form["html_css"]
        javascript = request.form["javascript"]
        sql_skill = request.form["sql"]
        machine_learning = request.form["machine_learning"]
        data_analysis = request.form["data_analysis"]
        git = request.form["git"]
        cloud = request.form["cloud"]


        # Soft Skills
        communication = request.form["communication"]
        problem_solving = request.form["problem_solving"]
        teamwork = request.form["teamwork"]
        leadership = request.form["leadership"]
        critical_thinking = request.form["critical_thinking"]
        creativity = request.form["creativity"]
        time_management = request.form["time_management"]


        # Career Information
        interest = request.form["interest"]
        work_type = request.form["work_type"]
        work_environment = request.form["work_environment"]
        problem_preference = request.form["problem_preference"]
        career_goal = request.form["career_goal"]

        # Prepare student data for AI prediction

        student_data = pd.DataFrame([{
        "overall_percentage": float(overall_percentage),
        "programming_marks": float(programming_marks),
        "maths_marks": float(maths_marks),
        "database_marks": float(database_marks),
        "os_marks": float(os_marks),
        "network_marks": float(network_marks),
        "projects_completed": int(projects_completed),

        "python": int(python),
        "java": int(java),
        "cpp": int(cpp),
        "html_css": int(html_css),
        "javascript": int(javascript),
        "sql_skill": int(sql_skill),
        "machine_learning": int(machine_learning),
        "data_analysis": int(data_analysis),
        "git": int(git),
        "cloud": int(cloud),

        "communication": int(communication),
        "problem_solving": int(problem_solving),
        "teamwork": int(teamwork),
        "leadership": int(leadership),
        "critical_thinking": int(critical_thinking),
        "creativity": int(creativity),
        "time_management": int(time_management),

        "interest": interest,
        "work_type": work_type,
        "career_goal": career_goal
}])    
        # Preprocess the student data
        student_processed = preprocessor.transform(student_data)

        # Predict career
        prediction = model.predict(student_processed)
        recommended_career = prediction[0]
        print("AI Recommended Career:", recommended_career)

        # Connect to MySQL
        connection = get_db_connection()
        cursor = connection.cursor()


        # Insert assessment
        query = """
            INSERT INTO assessments (
                student_id,
                course,
                semester,
                overall_percentage,
                programming_marks,
                maths_marks,
                database_marks,
                os_marks,
                network_marks,
                projects_completed,
                python,
                java,
                cpp,
                html_css,
                javascript,
                sql_skill,
                machine_learning,
                data_analysis,
                git,
                cloud,
                communication,
                problem_solving,
                teamwork,
                leadership,
                critical_thinking,
                creativity,
                time_management,
                interest,
                work_type,
                work_environment,
                problem_preference,
                career_goal,
                recommended_career
            )
            VALUES (
                %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s,
                %s, %s, %s
            )
        """

        update_student_query = """
        UPDATE students
        SET course = %s,
            semester = %s
        WHERE student_id = %s
    """

        cursor.execute(
        update_student_query,
        (course, semester, session["student_id"])
    )


        values = (
            session["student_id"],
            course,
            semester,
            overall_percentage,
            programming_marks,
            maths_marks,
            database_marks,
            os_marks,
            network_marks,
            projects_completed,
            python,
            java,
            cpp,
            html_css,
            javascript,
            sql_skill,
            machine_learning,
            data_analysis,
            git,
            cloud,
            communication,
            problem_solving,
            teamwork,
            leadership,
            critical_thinking,
            creativity,
            time_management,
            interest,
            work_type,
            work_environment,
            problem_preference,
            career_goal,
            recommended_career
        )


        cursor.execute(query, values)

        connection.commit()

        cursor.close()
        connection.close()


        details = career_details[recommended_career]

        assessment = {
        "course": course,
        "semester": semester,
        "overall_percentage": overall_percentage,
        "programming_marks": programming_marks,
        "maths_marks": maths_marks,
        "database_marks": database_marks,
        "projects_completed": projects_completed
        }       

        return render_template(
            "recommendation.html",
            recommended_career=recommended_career,
            description=details["description"],
            skills=details["skills"],
            next_step=details["next_step"],
            assessment=assessment
        )


    return render_template("assessment.html")

@app.route("/my-recommendation")
def my_recommendation():

    if "student_id" not in session:
        return redirect("/login")

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
        SELECT *
        FROM assessments
        WHERE student_id = %s
        ORDER BY assessment_id DESC
        LIMIT 1
    """

    cursor.execute(query, (session["student_id"],))

    assessment = cursor.fetchone()

    cursor.close()
    connection.close()

    if assessment is None:
        return "No assessment found. Please complete the assessment first."

    recommended_career = assessment["recommended_career"]

    details = career_details[recommended_career]

    return render_template(
    "recommendation.html",
    recommended_career=recommended_career,
    description=details["description"],
    skills=details["skills"],
    next_step=details["next_step"],
    assessment=assessment
)

@app.route("/admin-login", methods=["GET", "POST"])
def admin_login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        query = """
            SELECT *
            FROM admins
            WHERE username = %s
        """

        cursor.execute(query, (username,))

        admin = cursor.fetchone()

        cursor.close()
        connection.close()

        if admin is None:
            return "Admin username not found!"

        if check_password_hash(admin["password_hash"], password):

            session["admin_id"] = admin["admin_id"]
            session["admin_username"] = admin["username"]

            return redirect("/admin-dashboard")

        else:
            return "Incorrect admin password!"

    return render_template("admin_login.html")

@app.route("/admin-dashboard")
def admin_dashboard():

    if "admin_id" not in session:
        return redirect("/admin-login")

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    # Count total students
    cursor.execute("SELECT COUNT(*) AS total_students FROM students")
    total_students = cursor.fetchone()["total_students"]

    # Count total assessments
    cursor.execute("SELECT COUNT(*) AS total_assessments FROM assessments")
    total_assessments = cursor.fetchone()["total_assessments"]

    # Count total AI recommendations
    cursor.execute("""
        SELECT COUNT(*) AS total_recommendations
        FROM assessments
        WHERE recommended_career IS NOT NULL
    """)

    total_recommendations = cursor.fetchone()["total_recommendations"]

    cursor.close()
    connection.close()

    return render_template(
        "admin_dashboard.html",
        admin_username=session["admin_username"],
        total_students=total_students,
        total_assessments=total_assessments,
        total_recommendations=total_recommendations
    )

@app.route("/admin-students")
def admin_students():

    if "admin_id" not in session:
        return redirect("/admin-login")

    search = request.args.get("search", "")

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    if search:

        query = """
            SELECT
                student_id,
                name,
                email,
                course,
                semester,
                created_at
            FROM students
            WHERE name LIKE %s
               OR email LIKE %s
            ORDER BY student_id DESC
        """

        search_value = "%" + search + "%"

        cursor.execute(
            query,
            (search_value, search_value)
        )

    else:

        query = """
        SELECT
        s.student_id,
        s.name,
        s.email,
        s.course,
        s.semester,
        s.created_at,
        COUNT(a.assessment_id) AS assessment_count
        FROM students s
        LEFT JOIN assessments a
        ON s.student_id = a.student_id
        GROUP BY
        s.student_id,
        s.name,
        s.email,
        s.course,
        s.semester,
        s.created_at
        ORDER BY s.student_id DESC
    """

        cursor.execute(query)

    students = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "admin_students.html",
        students=students,
        search=search
    )

@app.route("/admin-student/<int:student_id>/assessments")
def admin_student_assessments(student_id):

    if "admin_id" not in session:
        return redirect("/admin-login")

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
        SELECT
            a.assessment_id,
            s.name AS student_name,
            s.email AS student_email,
            a.course,
            a.semester,
            a.overall_percentage,
            a.projects_completed,
            a.interest,
            a.recommended_career
        FROM assessments a
        JOIN students s
            ON a.student_id = s.student_id
        WHERE s.student_id = %s
        ORDER BY a.assessment_id DESC
    """

    cursor.execute(query, (student_id,))

    assessments = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "admin_student_assessments.html",
        assessments=assessments
    )

@app.route("/admin-assessments")
def admin_assessments():

    if "admin_id" not in session:
        return redirect("/admin-login")

    search = request.args.get("search", "")

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    if search:

        query = """
            SELECT
                a.assessment_id,
                s.name AS student_name,
                a.course,
                a.semester,
                a.overall_percentage,
                a.projects_completed,
                a.interest,
                a.recommended_career
            FROM assessments a
            JOIN students s
                ON a.student_id = s.student_id
            WHERE s.name LIKE %s
            ORDER BY a.assessment_id DESC
        """

        search_value = "%" + search + "%"

        cursor.execute(
            query,
            (search_value,)
        )

    else:

        query = """
            SELECT
                a.assessment_id,
                s.name AS student_name,
                a.course,
                a.semester,
                a.overall_percentage,
                a.projects_completed,
                a.interest,
                a.recommended_career
            FROM assessments a
            JOIN students s
                ON a.student_id = s.student_id
            ORDER BY a.assessment_id DESC
        """

        cursor.execute(query)

    assessments = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "admin_assessments.html",
        assessments=assessments,
        search=search
    )

@app.route("/admin-recommendations")
def admin_recommendations():

    if "admin_id" not in session:
        return redirect("/admin-login")

    search = request.args.get("search", "")

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    if search:

        query = """
            SELECT
                a.assessment_id,
                s.name AS student_name,
                a.overall_percentage,
                a.interest,
                a.recommended_career
            FROM assessments a
            JOIN students s
                ON a.student_id = s.student_id
            WHERE a.recommended_career IS NOT NULL
              AND (
                    s.name LIKE %s
                    OR a.recommended_career LIKE %s
                  )
            ORDER BY a.assessment_id DESC
        """

        search_value = "%" + search + "%"

        cursor.execute(
            query,
            (search_value, search_value)
        )

    else:

        query = """
            SELECT
                a.assessment_id,
                s.name AS student_name,
                a.overall_percentage,
                a.interest,
                a.recommended_career
            FROM assessments a
            JOIN students s
                ON a.student_id = s.student_id
            WHERE a.recommended_career IS NOT NULL
            ORDER BY a.assessment_id DESC
        """

        cursor.execute(query)

    recommendations = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "admin_recommendations.html",
        recommendations=recommendations,
        search=search
    )

@app.route("/admin-assessment/<int:assessment_id>")
def admin_assessment_detail(assessment_id):

    if "admin_id" not in session:
        return redirect("/admin-login")

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    query = """
        SELECT
            a.*,
            s.name AS student_name,
            s.email AS student_email
        FROM assessments a
        JOIN students s
            ON a.student_id = s.student_id
        WHERE a.assessment_id = %s
    """

    cursor.execute(query, (assessment_id,))

    assessment = cursor.fetchone()

    cursor.close()
    connection.close()

    if assessment is None:
        return "Assessment not found!"

    return render_template(
        "admin_assessment_detail.html",
        assessment=assessment
    )

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/login")

@app.route("/admin-logout")
def admin_logout():

    session.pop("admin_id", None)
    session.pop("admin_username", None)

    return redirect("/admin-login")

if __name__ == "__main__":
    app.run(debug=True)