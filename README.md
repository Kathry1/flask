# 📊 Advertising Sales Prediction API

This is a Flask-based REST API that predicts product sales based on advertising budgets across different media channels (TV, radio, newspaper). The model is trained using a Lasso regression and can be retrained via uploaded CSV files.

## 🔍 Features

- `/` – Welcome page  
- `/api/v1/predict` – Make a prediction from JSON input  
- `/api/v1/retrain` – Retrain the model using a CSV file  

## 🧪 Example Usage

### `/api/v1/predict`  
**POST** request with JSON body:

```json
{
  "TV": 100,
  "radio": 20,
  "newspaper": 10
}
```

### Response:
```json
{
  "prediction": 13.42
}
```

### `/api/v1/retrain`  
**POST** request with a file upload:  
Upload a CSV file with the following columns:  
`TV`, `radio`, `newspaper`, `sales`

---

## 🚀 Technologies Used

- Python 3.10  
- Flask  
- scikit-learn (Lasso regression)  
- pandas  
- Git + GitHub  
- PythonAnywhere (deployment)

---

## 📦 Requirements

To install dependencies:

```bash
pip install -r requirements.txt
```

---

## 📁 Project Structure

```
.
├── app_model.py             # Flask app
├── model.py                 # Model training script
├── ad_model.pkl             # Pickled model
├── test_predict.py          # Local test client
├── test_retrain.py
├── predict_test_online.py
├── test_retrain_online.py
├── requirements.txt
└── data/
    ├── Advertising.csv
    └── Advertising_new.csv
```

---

## 📤 Deployment

This project is deployed via [PythonAnywhere](https://www.pythonanywhere.com/).  
You can access the live API here:  
👉 https://kathrypythonanywhere.pythonanywhere.com

---

## 📝 Author

Created with ❤️ by **Kathry1**  
GitHub: [https://github.com/Kathry1/flask](https://github.com/Kathry1/flask)
