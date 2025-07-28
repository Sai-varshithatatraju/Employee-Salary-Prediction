# 📊 **Employee Salary Prediction Web Application**

<b><a href="https://www.kaggle.com/datasets/rkiattisak/salaly-prediction-for-beginer" style="color: black; text-decoration: none;">Kaggle Dataset</a></b> |
<b><a href="https://www.kaggle.com/code/your-kaggle-notebook-url" style="color: black; text-decoration: none;">Kaggle Notebook</a></b> |
<b><a href="https://your-streamlit-app-url" style="color: black; text-decoration: none;">View Demo</a></b>

---

A **machine learning-powered web application** that accurately predicts employee salaries based on inputs such as **age**, **gender**, **education level**, **job title**, and **years of experience**.  
Built with a modern UI using **Streamlit**, and trained using **XGBoost regression**.

---

## 🚀 Features

- 💰 Predict salary using multiple input factors  
- 🎨 Interactive and modern **Streamlit UI**  
- 📊 Real-time display of:
  - Predicted annual salary
  - Monthly salary
  - Hourly rate  
- 📈 R² Score visualization  
- 🧠 Trained using **XGBoost Regressor**  
- ⚡ Model caching for instant responses  

---

## 🧾 Input Features

- Age  
- Gender  
- Education Level  
- Job Title  
- Years of Experience  

---

## 🧰 Tech Stack

| Layer        | Tools Used                                      |
|--------------|-------------------------------------------------|
| **UI**       | Streamlit                                       |
| **ML Model** | XGBRegressor                                    |
| **Data Prep**| Pandas, NumPy, LabelEncoder, StandardScaler     |
| **Deployment**| Streamlit Cloud                                |

---

## 🛠️ Setup Instructions

1. Clone the Repository
```bash
git clone https://github.com/Roshians/Employe-Salary-Prediction-Using-ML.git
cd Employe-Salary-Prediction-Using-ML

2. Create a Virtual Environment

python -m venv venv

# On Windows
.\venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate

3. Install Dependencies

pip install -r requirements.txt

4. Run the Application Locally

streamlit run app.py

---

## 📊 Model Information

- **Algorithm**: XGBoost Regressor  
- **Evaluation Metric**: R² Score  
- **Encoding**: Label Encoding for categorical fields  
- **Scaling**: StandardScaler for numeric normalization  
