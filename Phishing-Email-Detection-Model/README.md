# 🛡️ Phishing Email Detection System

## Overview

The Phishing Email Detection System is a Machine Learning-based cybersecurity application designed to identify phishing emails and distinguish them from legitimate emails.

The system analyzes email content, extracts suspicious patterns such as URLs and phishing-related keywords, and classifies emails as either **Phishing** or **Safe** using a trained Scikit-learn machine learning model.

This project was developed as part of a cybersecurity internship to demonstrate practical implementation of machine learning techniques in email threat detection.

---

## Features

### Email Classification

* Detects whether an email is **Phishing** or **Safe**
* Uses a trained Machine Learning model for prediction

### URL Analysis

* Identifies URLs present in email content
* Counts suspicious links found within emails

### Keyword Detection

* Detects commonly used phishing keywords such as:

  * urgent
  * verify
  * password
  * login
  * suspended
  * bank
  * click here
  * free
  * winner

### Risk Assessment

* Assigns a risk level:

  * Low
  * Medium
  * High

### Machine Learning Metrics

* Displays model accuracy
* Displays confusion matrix results

### User-Friendly Dashboard

* Modern cybersecurity-themed interface
* Real-time email analysis
* Responsive design

---

## Technologies Used

| Technology   | Purpose               |
| ------------ | --------------------- |
| Python       | Backend Development   |
| Flask        | Web Framework         |
| Scikit-learn | Machine Learning      |
| Pandas       | Dataset Processing    |
| Joblib       | Model Serialization   |
| HTML         | Frontend Structure    |
| CSS          | User Interface Design |

---

## Project Structure

```text
Phishing-Email-Detection-Model/

├── app.py
├── train_model.py
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
├── README.md

├── dataset/
│   └── phishing_emails.csv

├── templates/
│   └── index.html

├── static/
│   ├── style.css
│   └── background.png

└── screenshots/
```

## Machine Learning Workflow

1. Load phishing and legitimate email dataset.
2. Clean and preprocess email text.
3. Convert text into numerical features using TF-IDF Vectorization.
4. Train the classification model.
5. Evaluate model performance.
6. Save trained model and vectorizer.
7. Use the trained model for real-time email analysis.

---

## Model Performance

### Accuracy

```text
100%
```

### Confusion Matrix

```text
[[1 0]
 [0 1]]
```

> Note: Accuracy may vary depending on dataset size and quality.

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Train Model

```bash
python train_model.py
```

### Run Application

```bash
python app.py
```

### Open Browser

```text
http://127.0.0.1:5000
```

---

## Example Phishing Email

```text
URGENT!

Your bank account has been suspended.

Click here immediately:

http://fake-bank-login.com

Verify your password now.
```

### Output

```text
Classification: PHISHING
Risk Level: HIGH
URLs Found: 1
Suspicious Keywords:
- urgent
- verify
- password
- bank
- click
- suspended
```

---

## Example Safe Email

```text
Hello Team,

The project review meeting is scheduled for tomorrow at 10:00 AM.

Please bring the updated presentation.

Regards,
Manager
```

### Output

```text
Classification: SAFE
Risk Level: LOW
```

---

## Screenshots

### Homepage

Add screenshot here.

### Phishing Detection

Add screenshot here.

### Safe Email Detection

Add screenshot here.

---

## Future Enhancements

* Larger Training Dataset
* Advanced Feature Engineering
* Deep Learning Models
* Email Header Analysis
* Attachment Scanning
* Real-Time Threat Intelligence Integration
* PDF Report Generation
* Export Analysis Results

---

## Learning Outcomes

This project helped in understanding:

* Machine Learning Fundamentals
* Cybersecurity Threat Detection
* Natural Language Processing
* Feature Extraction
* Flask Web Development
* Email Security Analysis
* Risk Assessment Techniques

---

## Disclaimer

This project is intended for educational and internship learning purposes only. It should not be used as a replacement for enterprise-grade email security solutions.
