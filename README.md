#  Employee Salary Prediction Web Application

[![Kaggle Dataset](https://img.shields.io/badge/dataset-Kaggle-blue)](https://www.kaggle.com/datasets/rkiattisak/salaly-prediction-for-beginer)
[![Kaggle Notebook](https://img.shields.io/badge/Kaggle_Notebook-Open-blue)](https://www.kaggle.com/code/roshians/employe-salary-prediction-using-ml)
[![View Demo](https://img.shields.io/badge/Demo-Streamlit%20App-brightgreen?logo=streamlit)](https://employe-salary-prediction-using-ml.streamlit.app/)


A Machine Learning-powered web app that accurately predicts employee salaries based on inputs such as age, gender, education level, job title, and years of experience. Designed with a modern UI using **Streamlit**, and trained using regression techniques in **scikit-learn**.

---

## Features

-  Predict salary using multiple input factors
-  Interactive and modern Streamlit UI
-  Real-time display of predicted salary, monthly salary, hourly rate
-  Visual R² Score indicating model performance
-  Trained using Linear Regression with proper preprocessing
-  Model caching for fast response

---

## Input Features

- Age
- Gender
- Education Level
- Job Title
- Years of Experience

---

## Tech Stack

| Layer       | Tools Used                        |
|-------------|-----------------------------------|
| UI          | Streamlit                         |
| ML Model    | XGBRegressor                      |
| Data Prep   | Pandas, NumPy, LabelEncoder, Scaler |
| Deployment  | Streamlit Cloud                   |

---



## Setup Instructions

### 1. Clone the Repository
```bash
git clone Sai-Varshithatatraju/Employee-Salary-Prediction
cd Employee-Salary-Prediction
````

### 2. Create a Virtual Environment

```bash
python -m venv venv

# On Windows
.\venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application Locally

```bash
streamlit run salary.py
```

---

## Model Information

* **Algorithm**: XGBoost Regressor
* **Evaluation Metric**: R² Score
* **Encoding**: Label Encoding for categorical fields
* **Scaling**: StandardScaler for numeric normalization

---

##  Screenshots

| Input Form                               |Salary Prediction Output                 |
| ---------------------------------------- | ---------------------------------------- |
| <img width="700" height="800" alt="sal1" src="https://github.com/user-attachments/assets/5355075e-b918-4b05-aaa0-03a9d41e6417" /> | <img width="700" height="800" alt="sal2" src="https://github.com/user-attachments/assets/a0397784-23bc-47ac-b620-d018cd773adb" /> |


---

## License
This project is developed solely for educational and internship purposes. All intellectual property rights are retained by the author.
