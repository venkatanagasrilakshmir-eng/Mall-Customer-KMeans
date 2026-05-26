# Mall Customer Segmentation using K-Means Clustering

## Project Overview

This project applies the K-Means Clustering Algorithm to segment mall customers based on their:

- Annual Income
- Spending Score

The goal is to identify customer groups for business analysis and marketing strategies.

---

# Project Structure

```bash
Mall-Customer-KMeans/
│
├── dataset/
│   └── Mall_Customers.csv
│
├── notebooks/
│   └── customer_segmentation.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── train_model.py
│   ├── visualize.py
│   └── utils.py
│
├── outputs/
│   ├── elbow_method.png
│   ├── customer_clusters.png
│   └── clustered_data.csv
│
├── requirements.txt
├── README.md
└── main.py
```

---

# Features

✅ Data Preprocessing  
✅ Elbow Method Visualization  
✅ K-Means Clustering  
✅ Customer Cluster Visualization  
✅ Save Clustered Dataset  
✅ Modular Python Structure  

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn

---

# Dataset

Dataset used:

- Mall Customers Dataset

Download here:

[kaggle.com](https://reference-url-citation.invalid/0)

---

# Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPO_LINK
cd Mall-Customer-KMeans
```

Install required libraries:

```bash
pip install -r requirements.txt
```

---

# Run the Project

```bash
python main.py
```

---

# Jupyter Notebook

Run notebook:

```bash
jupyter notebook
```

Open:

```bash
notebooks/customer_segmentation.ipynb
```

---

# Output Screenshots

## 1. Elbow Method

- Finds optimal number of clusters

## 2. Customer Clusters

- Visualizes segmented customers

## 3. Clustered Dataset

- CSV file with cluster labels

---

# Sample Output

## Elbow Method

```python
Optimal clusters = 5
```

---

# Customer Segments

| Cluster | Description |
|---|---|
| Cluster 1 | High Income, High Spending |
| Cluster 2 | High Income, Low Spending |
| Cluster 3 | Average Customers |
| Cluster 4 | Low Income, High Spending |
| Cluster 5 | Low Income, Low Spending |

---

# Future Improvements

- Add Streamlit Web App
- Deploy on Heroku
- Add Interactive Dashboard
- Use Advanced Clustering Algorithms

---

# Author

Developed using Python and Machine Learning.

---

# License

This project is open-source and free to use.
