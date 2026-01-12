# Student Marks Prediction – End-to-End Machine Learning Project  

An end-to-end machine learning system that predicts a student's marks using features such as study hours, past performance, attendance, and behavioral/academic patterns.  
This project demonstrates a full ML workflow including **EDA → preprocessing → model training → evaluation → deployment**.

---

##  Project Highlights  

- Built a **complete ML pipeline** to predict student marks  
- Includes **EDA, data cleaning, feature engineering, and model building**  
- Implemented multiple regression models and selected the best  
- Created a **production-ready prediction script**  
- End-to-end structure following real-world ML standards  
- Scalable for API / UI integration  

---

## Tech Stack

| Category | Tools Used |
|----------|------------|
| Language | Python |
| ML Libraries | Scikit-learn, NumPy, Pandas |
| Visualization | Matplotlib, Seaborn |
| Development | Jupyter Notebook, VS Code |
| Deployment Ready | Can be wrapped into Flask/FastAPI |



---

## Dataset Details  

*(Update based on your dataset columns)*  
Typical features used for predicting student marks:

- Study Hours  
- Attendance Percentage  
- Previous Exam Scores  
- Sleep Duration  
- Assignment Completion  
- Internet/Phone Usage  
- Target: **Final Exam Marks**

Dataset preprocessing includes:  
- Handling missing values  
- Scaling numerical features  
- Encoding categoricals  
- Removing outliers  
- Splitting into train/test  

---

## Model Training  

Models tested:

- Linear Regression  
- Lasso Regression  
- Ridge Regression  
- Random Forest Regressor  
- Gradient Boosting Regressor  

Common metrics used:

- R² Score  
- MAE (Mean Absolute Error)  
- RMSE  

*(Fill these with your real results)*  
Example:

| Model | R² Score |
|-------|----------|
| Linear Regression | 0.87 |
| Random Forest | 0.93 |
| Gradient Boosting | 0.95 |

---

## Final Prediction Script  

After training, the best model is saved in:




 ## Folder Structure
```bash
machine-learning-project/
│── data/                     # Raw and processed datasets (if applicable)
│── notebooks/                # Jupyter notebooks for experiments  
│── scripts/                  # Standalone Python scripts  
│── models/                   # Saved/trained model artifacts  
│── README.md                 # Project documentation  
│── requirements.txt          # Python dependencies  
```



> Install dependencies and  How to Run
```bash

git clone https://github.com/kumar-kiran-24/machine-learning-project
cd machine-learning-project
pip install -r requirments.txt

python app.py
```








