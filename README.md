# ⚔️ Game of Thrones Character Finder

> Find characters similar to your favourite using Machine Learning

![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-deployed-red?style=flat&logo=streamlit)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange?style=flat&logo=scikit-learn)
![Status](https://img.shields.io/badge/Status-Live-brightgreen?style=flat)

## 🔗 Live Demo
**[👉 Click here to try the app](https://got-character-finder-mkatucs7hsygtwyinkwo4s.streamlit.app/)**

---

## 📸 Screenshot
![GOT Character Finder](<img width="1265" height="661" alt="image" src="https://github.com/user-attachments/assets/b8cfba2f-b2d0-4eea-ab0e-b4f07527160e" />
![Uploading image.png…]()
)

---

## 🧠 How It Works

1. **Data:** 389 Game of Thrones characters from official GOT API
2. **Feature Engineering:** Combined house allegiance, family relationships, alliances, battle connections, and royal status into text tags
3. **Vectorization:** TF-IDF Vectorizer converts character tags to numerical vectors
4. **Similarity:** Cosine Similarity finds the most similar characters
5. **Result:** Top 5 most similar characters with match percentage
---
Character Data (JSON)
↓
Feature Engineering (Tags)
↓
TF-IDF Vectorization
↓
Cosine Similarity Matrix (389×389)
↓
Top 5 Similar Characters
## ✨ Features

- 🏰 Select from 389 GOT characters
- ⚔️ Find top 5 most similar characters
- 📊 Similarity percentage score
- 🎭 Actor name display
- 👑 Royal status indicator
- 🧠 Algorithm explanation

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.12 | Core language |
| Pandas | Data processing |
| Scikit-learn | TF-IDF + Cosine Similarity |
| NumPy | Matrix operations |
| Streamlit | Web application |
| Pickle | Model serialization |

---

## 📁 Project Structure
GOT-Character-Finder/
├── app.py                  ← Streamlit application
├── characters.pkl          ← Processed character data
├── similarity.pkl          ← Precomputed similarity matrix
├── requirements.txt        ← Dependencies
├── GOT.ipynb              ← Jupyter notebook (EDA + model)
└── README.md
