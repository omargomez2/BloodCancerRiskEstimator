
# 🧬 Cancer Type Prediction App with Streamlit

This project is a Streamlit-based web application that predicts the **possible type of cancer** based on values from a blood test. The model is trained using machine learning and provides an intuitive user interface with **sliders only**, making it easy for clinicians or researchers to use without technical knowledge.

## 🔍 Features

- 🔢 Input blood test values using sliders
- 🤖 Real-time cancer type prediction using a trained ML model
- 📊 Simple, responsive, and interactive web UI built with Streamlit
- 📁 Easily extendable with new models or additional features

## 🧠 Machine Learning Model

The model is trained using scikit-learn on a synthetic or real medical dataset. It classifies cancer types (e.g., leukemia, lymphoma, etc.) based on a set of numerical blood test values.

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/omargomez2/BloodCancerRiskEstimator.git
cd cancer-prediction-streamlit
```

### 2. Create and Activate a Virtual Environment (optional)
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the App
```bash
streamlit run app.py
```

The app will launch in your browser at `http://localhost:8501`.

## 📦 Requirements

- Python 3.8+
- Streamlit
- scikit-learn
- pandas
- numpy
- joblib

You can install all with:

```bash
pip install streamlit scikit-learn pandas numpy joblib
```

## 📁 File Structure

```
├── app.py                # Streamlit app file
├── model.pkl             # Trained ML model (Joblib format)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## ⚠️ Disclaimer

This application is for **educational and demonstration purposes only**. It is not intended for real-world medical use or diagnosis.

## 🙌 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change or improve.

---

## 📫 Contact

Built by Omar S. Gómez (https://www.linkedin.com/in/omargomez)
Feel free to connect or provide feedback!
