# ✈️ British Airways Customer Booking Prediction

A machine learning project to predict whether a customer will complete their booking, enabling British Airways to optimize marketing and personalize user experiences.

![Model Status](https://img.shields.io/badge/model-trained-green)
![Python](https://img.shields.io/badge/python-3.10-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 📌 Project Summary

This project uses booking-related behavioral data to classify customers as likely or unlikely to complete their flight booking. The model helps the airline prioritize high-probability customers and design better interventions.

---

## 📁 Directory Structure

british-airways-customer-booking-prediction/
├── data/
│ └── customer_booking.csv
├── notebooks/
│ └── Getting_Started.ipynb
├── reports/
│ ├── Customer_Booking_Model_Summary.pptx
│ └── Predictive_Modeling_of_Customer_Booking_Behavior.pdf
├── visuals/
│ ├── roc_curve.png
│ ├── confusion_matrix.png
│ └── feature_importance.png
├── src/
│ ├── preprocess.py
│ └── model.py
├── requirements.txt
├── .gitignore
└── README.md

---

## 🔧 Features & Methods

- 🔍 **EDA** and Feature Engineering
- ⚙️ One-Hot + Target Encoding
- ⚖️ SMOTE for class imbalance
- 📈 Logistic Regression + Random Forest
- ✅ Evaluation: Accuracy, AUC, F1 Score, Confusion Matrix

---

## 📊 Key Results

| Metric       | Value   |
|--------------|---------|
| Accuracy     | 83%     |
| AUC Score    | 0.89    |
| F1 Score     | 0.81    |

> ✅ Logistic Regression outperformed others.  
> 📌 Features like booking origin, baggage choice, and trip type were top predictors.

---

## 🖼️ Visualizations

![ROC Curve](visuals/roc_curve.png)  
*ROC curve showing the model's AUC performance.*

![Confusion Matrix](visuals/confusion_matrix.png)  
*Visual breakdown of predicted vs actual bookings.*

---

## 🧠 Key Insights

- Extra services like **baggage**, **meals**, and **seat selection** are strong booking signals.
- **Booking origin country** and **purchase lead time** significantly impact conversion.
- Targeting premium service seekers may improve campaign ROI.

---

## 📌 Dependencies


pip install -r requirements.txt

---

## 🚀 Getting Started
```bash
pip install -r requirements.txt
python src/model.py
```

## 📄 Reports
- 📊 Presentation Slide (PPTX)
- 📑 Project Summary (PDF)

## ✍️ Author
Mihir Shinde



