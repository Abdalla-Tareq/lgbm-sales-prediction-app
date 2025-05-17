
# Supplement Sales Revenue Prediction App

A web application built with **Streamlit** to predict **supplement sales revenue** using a trained **LightGBM** model. This app allows both manual data input and bulk CSV upload for predictions. It also supports data visualization to explore uploaded datasets.

---

## 📌 Overview

This project is designed for businesses and analysts who want to:
- Predict the expected revenue of supplement product sales based on historical and product-specific data.
- Upload CSV datasets to generate bulk predictions.
- Visualize data using line and bar charts.

The model was trained separately, and its preprocessor and serialized model are used directly in the app.

---

## 🧰 Technologies Used

- [Python 3.8+](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [LightGBM](https://lightgbm.readthedocs.io/)
- [Pandas](https://pandas.pydata.org/)
- [NumPy](https://numpy.org/)
- [Seaborn & Matplotlib](https://seaborn.pydata.org/)
- [Scikit-learn](https://scikit-learn.org/)
- [Joblib](https://joblib.readthedocs.io/en/latest/)

---

## 📂 Project Structure

```
.
├── applied.py                  # Main Streamlit app script
├── lgb_model.pkl               # Trained LightGBM regression model
├── preprocessor.pkl            # Scikit-learn ColumnTransformer or pipeline
├── sample_data.csv             # Sample CSV data (optional)
├── README.md                   # Project documentation
```

---

## 🧪 How It Works

1. **Manual Input Mode**
    - Users can enter product and sales data one record at a time.
    - The input is passed through the preprocessor, then predicted using the model.

2. **CSV Upload Mode**
    - Users upload a `.csv` file with proper columns.
    - Predictions are generated for the entire dataset.
    - Option to download the results as a `.csv` file.

3. **Visualization**
    - After uploading a dataset, users can choose columns to visualize.
    - Supported chart types: Line Chart and Bar Chart.

---

## 🔧 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/supplement-sales-predictor.git
cd supplement-sales-predictor
```

### 2. Create a Virtual Environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
If `requirements.txt` is not provided, install manually:
```bash
pip install streamlit pandas numpy seaborn matplotlib scikit-learn lightgbm joblib
```

### 4. Add Model Files
Ensure that both `lgb_model.pkl` and `preprocessor.pkl` are placed in the project root.

### 5. Run the App
```bash
streamlit run applied.py
```

---

## 📊 Expected CSV Format for Upload

```csv
Date,Product ID,Product Name,Category,Price,Units Sold,Units Returned,Discount,Location,Platform,Marketing Spend,Promotions
2023-01-01,P001,Protein X,Protein,39.99,150,2,10.0,Online,Website,500,1
2023-01-08,P002,Vitamin C,Vitamins,19.99,300,4,5.0,Retail Store,Amazon,350,1
```

Column descriptions:
- **Date**: Date of the record (YYYY-MM-DD)
- **Product ID** / **Product Name**: Identifier
- **Category**: e.g., Protein, Vitamins, etc.
- **Price**, **Units Sold**, **Units Returned**, **Discount**, **Marketing Spend**, **Promotions**: numeric inputs
- **Location** and **Platform**: categorical values

---

## 📈 Example Use Case

A supplement company wants to forecast weekly revenue based on:
- Number of units sold
- Discounts offered
- Marketing efforts per channel

The app can be used by:
- Business analysts for reporting
- Marketing teams to test promotional impact
- Retail strategists to evaluate performance by location/platform

---

## 📥 Output

- **Predicted Revenue** is displayed immediately on screen.
- **CSV Download**: After processing a dataset, results with predictions can be downloaded.

---

## 📌 Future Improvements

- Add model training script and notebook
- Implement logging and error reporting
- Deploy app to Streamlit Cloud or Hugging Face Spaces
- Include more advanced visualizations (histograms, heatmaps)

---

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## 🙋 Contact

For questions or feedback, feel free to reach out:
- GitHub: [your-username](https://github.com/Abdalla-Tareq)
- Email: abdallat764@gmail.com

---

Built with using Streamlit and LightGBM
