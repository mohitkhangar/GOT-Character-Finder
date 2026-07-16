import streamlit as st
import pickle
import pandas as pd
import numpy as np

# ── PAGE CONFIG ──────────────────────────────────────
st.set_page_config(
    page_title="GOT Character Finder",
    page_icon="⚔️",
    layout="wide"
)

# ── CUSTOM CSS ───────────────────────────────────────
st.markdown("""
<style>
    .stApp { background-color: #0d1117; }
    .title { 
        font-size: 2.5rem; 
        font-weight: bold;
        color: #c9a84c;
        text-align: center;
        text-shadow: 2px 2px 4px #000;
    }
    .subtitle {
        color: #8b949e;
        text-align: center;
        font-size: 1rem;
        margin-bottom: 2rem;
    }
    .card {
        background: linear-gradient(135deg, #161b22, #21262d);
        border: 1px solid #c9a84c;
        border-radius: 12px;
        padding: 15px;
        text-align: center;
        min-height: 200px;
    }
    .char-name {
        color: #c9a84c;
        font-weight: bold;
        font-size: 1rem;
    }
    .house-name {
        color: #8b949e;
        font-size: 0.85rem;
    }
    .score {
        color: #58a6ff;
        font-weight: bold;
        font-size: 1.1rem;
    }
    .selected-card {
        background: linear-gradient(135deg, #1f2937, #374151);
        border: 2px solid #c9a84c;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# ── LOAD DATA ────────────────────────────────────────
@st.cache_data
def load_data():
    chars = pickle.load(open('characters.pkl', 'rb'))
    sim = pickle.load(open('similarity.pkl', 'rb'))
    return chars, sim

characters, similarity = load_data()

# ── HELPER FUNCTIONS ─────────────────────────────────
def get_house_display(val):
    if isinstance(val, list):
        return val[0] if len(val) > 0 else 'Unknown'
    return str(val) if pd.notna(val) else 'Unknown'

def count_unique_houses(series):
    houses = set()
    for val in series:
        if isinstance(val, list):
            for h in val:
                if h:
                    houses.add(h)
        elif pd.notna(val):
            houses.add(val)
    return len(houses)

def get_char_info(name):
    row = characters[characters['characterName'] == name].iloc[0]
    return {
        'house': get_house_display(row['houseName']),
        'actor': str(row['actorName']) if pd.notna(row['actorName']) else 'Unknown',
        'royal': '👑 Royal' if row['royal'] == True else 'Not Royal',
    }

def recommend(name):
    idx = characters[characters['characterName'] == name].index[0]
    scores = sorted(
        list(enumerate(similarity[idx])),
        key=lambda x: x[1],
        reverse=True
    )[1:6]
    results = []
    for i, score in scores:
        row = characters.iloc[i]
        results.append({
            'name': row['characterName'],
            'house': get_house_display(row['houseName']),
            'actor': str(row['actorName']) if pd.notna(row['actorName']) else 'Unknown',
            'royal': '👑' if row['royal'] == True else '',
            'score': round(float(score) * 100, 1),
        })
    return results

# ── HEADER ───────────────────────────────────────────
st.markdown('<p class="title">⚔️ Game of Thrones Character Finder</p>',
            unsafe_allow_html=True)
st.markdown('<p class="subtitle">Discover characters similar to your favourite using Machine Learning</p>',
            unsafe_allow_html=True)
st.markdown("---")

# ── INPUT ────────────────────────────────────────────
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    char_list = sorted(characters['characterName'].dropna().tolist())
    selected = st.selectbox("🏰 Choose a Character", char_list)
    btn = st.button("⚔️ Find Similar Characters", use_container_width=True)

# ── SELECTED CHARACTER ───────────────────────────────
info = get_char_info(selected)
st.markdown("### 👑 Selected Character")
c1, c2, c3 = st.columns([1, 2, 1])
with c2:
    st.markdown(f"""
    <div class="selected-card">
        <h2 style='color:#c9a84c'>{selected}</h2>
        <p style='color:#8b949e'>🎭 Played by: <b>{info['actor']}</b></p>
        <p style='color:#8b949e'>🏰 House: <b>{info['house']}</b></p>
        <p style='color:#c9a84c'>{info['royal']}</p>
    </div>
    """, unsafe_allow_html=True)

# ── RESULTS ──────────────────────────────────────────
if btn:
    st.markdown("---")
    st.markdown("### ⚔️ Top 5 Similar Characters")

    results = recommend(selected)
    cols = st.columns(5)

    for col, r in zip(cols, results):
        with col:
            st.markdown(f"""
            <div class="card">
                <p class="char-name">{r['name']}</p>
                <p class="score">{r['score']}% match</p>
                <p class="house-name">🏰 {r['house']}</p>
                <p class="house-name">🎭 {r['actor']}</p>
                <p style='color:#c9a84c'>{r['royal']}</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")

    with st.expander("🧠 How does this work?"):
        st.markdown("""
        **Algorithm:** TF-IDF Vectorization + Cosine Similarity

        **Features used:**
        - 🏰 House allegiance
        - 👨‍👩‍👧 Family (parents, siblings)
        - ⚔️ Battle connections (killed, killedBy)
        - 🤝 Alliances and loyalties
        - 👑 Royal status

        **Dataset:** 389 GOT characters
        """)

# ── STATS ────────────────────────────────────────────
st.markdown("---")
col1, col2, col3 = st.columns(3)
col1.metric("Total Characters", "389")
col2.metric("Unique Houses", str(count_unique_houses(characters['houseName'])))
col3.metric("Royal Characters", str((characters['royal'] == True).sum()))

# ── FOOTER ───────────────────────────────────────────
st.markdown("---")
st.markdown("""
<p style='text-align:center; color:#8b949e; font-size:0.85rem'>
Built by <b style='color:#c9a84c'>Mohit Khangar</b> &nbsp;|&nbsp;
Python • Scikit-learn • Streamlit &nbsp;|&nbsp;
<a href='https://github.com/mohitkhangar' style='color:#c9a84c'>GitHub</a>
</p>
""", unsafe_allow_html=True)