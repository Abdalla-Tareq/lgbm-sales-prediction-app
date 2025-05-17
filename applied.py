import streamlit as st
import pandas as pd
import joblib
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore")

# --- Load the model and preprocessor ---
try:
    model = joblib.load(r'D:\python\NLP\Applied\lgb_model.pkl')
    preprocessor = joblib.load(r'D:\python\NLP\Applied\preprocessor.pkl')
except FileNotFoundError:
    st.error("Error: Model or preprocessor file not found. Please ensure 'lgb_model.pkl' and 'preprocessor.pkl' are in the same folder.")
    st.stop()

# --- App title ---
st.title("Predicting Supplement Sales Revenue")

st.write("Enter sales data to predict revenue, or upload a CSV file for analysis.")

# --- Input method ---
input_mode = st.radio("Select input method:", ("Manual Input", "Upload CSV"))

if input_mode == "Manual Input":
    input_cols = ['Date', 'Product ID', 'Product Name', 'Category', 'Price',
                  'Units Sold', 'Units Returned', 'Discount', 'Location', 'Platform', 'Marketing Spend', 'Promotions']

    input_data = {}
    st.header("Enter Features:")
    for col in input_cols:
        if col == 'Date':
            input_data[col] = st.date_input(f"Select {col}")
        elif col in ['Price', 'Units Sold', 'Units Returned', 'Discount', 'Marketing Spend', 'Promotions']:
            input_data[col] = st.number_input(f"Enter {col}", value=0.0, format="%.2f")
        else:
            input_data[col] = st.text_input(f"Enter {col}")

    if st.button("Predict Revenue"):
        input_df = pd.DataFrame([input_data])
        input_df['Date'] = pd.to_datetime(input_df['Date'])

        try:
            processed_input = preprocessor.transform(input_df)
            prediction = model.predict(processed_input)
            predicted_revenue = max(0, prediction[0])
            st.success(f"Predicted Revenue: {predicted_revenue:,.2f} $")
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")

else:
    st.header("Upload CSV File")
    uploaded_file = st.file_uploader("Upload a CSV file with sales data", type=["csv"])

    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.success("File uploaded successfully!")
            st.write("Preview of uploaded data:")
            st.dataframe(df.head())

            # --- Optional: Predict revenue for entire file ---
            if st.button("Predict for Uploaded Data"):
                try:
                    df['Date'] = pd.to_datetime(df['Date'])
                    processed_df = preprocessor.transform(df)
                    predictions = model.predict(processed_df)
                    df['Predicted Revenue'] = np.maximum(predictions, 0)
                    st.write("Prediction Results:")
                    st.dataframe(df[['Product Name', 'Predicted Revenue']])

                    csv = df.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        label="Download Predictions as CSV",
                        data=csv,
                        file_name='predicted_revenues.csv',
                        mime='text/csv')

                except Exception as e:
                    st.error(f"Prediction error: {e}")

            # --- Optional: Plotting ---
            st.subheader("Visualize Uploaded Data")
            plot_type = st.selectbox("Select chart type:", ["Line Chart", "Bar Chart"])
            x_col = st.selectbox("X-axis:", df.columns)
            y_col = st.selectbox("Y-axis:", df.columns)

            try:
                fig, ax = plt.subplots()
                if plot_type == "Line Chart":
                    sns.lineplot(data=df, x=x_col, y=y_col, ax=ax)
                elif plot_type == "Bar Chart":
                    sns.barplot(data=df, x=x_col, y=y_col, ax=ax)
                st.pyplot(fig)
            except Exception as e:
                st.error(f"Plotting error: {e}")

        except Exception as e:
            st.error(f"Error loading file: {e}")

st.markdown("---")
st.caption("This app is built using a LightGBM model for sales revenue prediction.")