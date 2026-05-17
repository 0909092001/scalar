 🎓 Student Dropout Prediction System

### AI-Powered Early Warning System for Education

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-green)
![Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A **machine learning system that predicts student dropout risk** using engagement and performance data.

This project demonstrates how **Artificial Intelligence can help universities identify at-risk students early** and improve retention through proactive interventions.

---

# 🚀 Why This Project Matters

Student dropout is one of the biggest challenges in education systems worldwide.

Traditional systems detect problems **after students fail or leave**.

This AI system enables **early detection of disengagement patterns** using:

* Behavioral learning analytics
* Machine learning prediction
* Student persona discovery

Institutions can **identify at-risk students weeks or months before dropout happens.**

---

# 🧠 AI Models Used

The system combines **three machine learning techniques** to understand student behavior.

| Model                   | Role                  | Purpose                                  |
| ----------------------- | --------------------- | ---------------------------------------- |
| **K-Means Clustering**  | Unsupervised Learning | Discover hidden student personas         |
| **Logistic Regression** | Interpretable Model   | Calculate dropout probability            |
| **Random Forest**       | Ensemble Model        | Stronger prediction for complex behavior |

This combination provides both **accuracy and explainability**.

---

# 📊 System Workflow

```
Student Engagement Data
        │
        ▼
Data Preprocessing
        │
        ▼
Feature Engineering
        │
        ▼
Machine Learning Models
│         │            │
▼         ▼            ▼
K-Means   Logistic     Random
Cluster   Regression   Forest
│         │            │
▼         ▼            ▼
Student   Dropout      Risk
Personas  Probability  Prediction
```

---

# 📂 Project Structure

```
student-dropout-prediction/
│
├── student_dropout_system.ipynb
│      Main machine learning notebook
│
├── student_data.csv
│      Dataset containing engagement metrics
│
├── start_windows.cmd
│      One-click launcher for Windows users
│
├── start_mac_linux.sh
│      Setup script for macOS and Linux
│
└── README.md
       Project documentation
```

---

# 📈 Dataset Features

The dataset represents **student engagement signals during a course**.

| Feature               | Description                    |
| --------------------- | ------------------------------ |
| attendance_rate       | Class attendance percentage    |
| assignment_submitted  | Assignment completion          |
| avg_quiz_score        | Average quiz performance       |
| coding_minutes        | Time spent practicing coding   |
| doubts_asked          | Questions asked by the student |
| late_submissions      | Number of late assignments     |
| project_commit_count  | Project activity level         |
| peer_messages_sent    | Collaboration with peers       |
| video_watched_percent | Lecture video engagement       |
| background            | Academic background            |
| dropout               | Target variable                |

These metrics simulate **Learning Management System (LMS) behavioral data**.

---

# 🧪 Machine Learning Experiments

## 1️⃣ Student Persona Discovery (K-Means)

K-Means clustering identifies **groups of learners based on engagement behavior**.

Example personas discovered:

| Cluster   | Persona                    |
| --------- | -------------------------- |
| Cluster 0 | Highly engaged learners    |
| Cluster 1 | Moderately active students |
| Cluster 2 | Passive participants       |
| Cluster 3 | High dropout risk students |

This helps educators understand **patterns of student participation**.

---

# 2️⃣ Dropout Probability Prediction

Logistic Regression calculates the **probability of a student dropping out**.

Example output:

```
Student 12 → Dropout Probability: 0.91
Student 24 → Dropout Probability: 0.04
```

Interpretation:

* **0.90+ → High risk**
* **0.40–0.70 → Moderate risk**
* **<0.20 → Safe student**

---

# 3️⃣ Feature Importance (Random Forest)

Random Forest determines **which behaviors contribute most to dropout risk**.

Example important features:

1️⃣ Coding practice time
2️⃣ Quiz performance
3️⃣ Late submissions
4️⃣ Attendance rate
5️⃣ Video engagement

These insights help **educators design targeted interventions**.

---

# ⚙️ Installation

## Step 1 — Install Python

Install **Python 3.10 or later**

Download from:

[https://www.python.org/downloads/](https://www.python.org/downloads/)

During installation enable:

```
Add Python to PATH
```

---

# ▶️ Running the System

## Windows (Recommended)

Open the project folder and double-click:

```
start_windows.cmd
```

This script automatically:

* Creates a virtual environment
* Installs dependencies
* Launches Jupyter Notebook

---

## macOS / Linux

Run the setup script:

```bash
bash start_mac_linux.sh
```

---

# 📒 Running the Notebook

When Jupyter opens:

Open:

```
student_dropout_system.ipynb
```

Run all cells sequentially.

Each cell contains explanations of the AI concepts used.

---

# 📊 Expected Outputs

Running the notebook produces:

### ✔ Student Behavior Clusters

Visualization of **student personas** discovered by K-Means.

---

### ✔ Dropout Risk Scores

Predicted **dropout probability for each student**.

---

### ✔ Feature Importance Chart

Visualization showing **which engagement metrics affect dropout most**.

---

# 🎯 Real-World Applications

This system can be applied in:

### Universities

Early identification of **students at risk of dropping out**.

### Online Learning Platforms

Improving **student engagement and retention**.

### EdTech Startups

Building **AI-driven learning analytics platforms**.

### Academic Research

Studying **student behavior patterns and learning outcomes**.

---

# 🔮 Future Improvements

Possible extensions of this project:

* Deep Learning dropout prediction models
* Real-time student monitoring dashboards
* Integration with LMS platforms (Moodle, Canvas)
* NLP analysis of student feedback
* Reinforcement learning for adaptive learning systems

---

# 🛠 Tech Stack

Core technologies used:

* Python
* Scikit-Learn
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook

Install dependencies manually if needed:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn jupyter
```

---

# 📚 Educational Purpose

This repository is designed for:

* AI workshops
* Machine learning courses
* EdTech research
* Educational data mining projects

---

# 👨‍💻 Author

**AI System Workshop Project**

Focus Areas:

* Machine Learning
* Predictive Analytics
* Educational Data Mining
* AI for Education


⭐ If you found this project useful, consider **starring the repository**.

