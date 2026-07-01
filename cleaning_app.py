import streamlit as st
import random
from datetime import datetime

# הגדרת דף ותמיכה בעברית
st.set_page_config(page_title="צ'קליסט ניקיונות חכם", layout="centered")

st.markdown("""
    <style>
    body, div, p, h1, h2, h3, h4, h5, h6, label, span { direction: RTL; text-align: right; }
    .stCheckbox { direction: RTL; text-align: right; margin-bottom: 8px; }
    .stButton button { width: 100%; font-weight: bold; }
    .challenge-box { background-color: #f0f7f4; padding: 15px; border-radius: 10px; border-right: 5px solid #2e7d32; margin-bottom: 15px; }
    .passover-box { background-color: #fff3e0; padding: 15px; border-radius: 10px; border-right: 5px solid #ef6c00; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

st.title("🧼 עוזר הניקיונות החכם שלך")
st.write("הופכים את מטלות הבית למשחק משימות יומי!")

# מאגר המשימות המלא מתוך התמונה שלך
DAILY_TASKS = [
    "הוצאת מדיח", "הכנסת מדיח", "ניקוי פח ראשי", "הורדת זבל ראשי", 
    "הכנסת כביסה", "הוצאת כביסה", "תליית כביסה", "הורדת כביסה", 
    "קיפול כביסה", "ניקוי שולחן במטבח", "סידור רצפה סלון", 
    "סידור רצפה מטבח", "ניקוי שיש", "ניקוי תמי 4", "ניקוי כיור מטבח"
]

WEEKLY_TASKS = [
    "החלפה וניקוי פחי שירותים", "שטיפה של כל הבית", "החלפת מצעים בכל החדרים", 
    "ניקוי גז בסבון כלים", "ניקוי מגשים תמי 4", "סידור שידות עבודה", 
    "ניקוי כיור שירותים", "אבק", "ניקוי פינת טוסטרים", "ניקוי מיקרו", 
    "מראות", "לשים מגבת חדשה במקלחת"
]

MONTHLY_TASKS = [
    "ניקוי גז במסיר שומנים", "ניקוי מיקרו יסודי", "ספות", "ניקוי מדפי ירקות במקרר", 
    "אקונומיקה במקלחת", "ניקוי מקרר", "ניקוי מקפיא", "ניקוי פילטר מייבש", 
    "ניקוי חלונות", "ניקוי ארונות מטבח מבחוץ", "ניקוי מכונת כביסה"
]

PASSOVER_TASKS = [
    "ניקוי תנור במסיר שומנים", "צביעת קירות ותיקוני צבע", "ארגון ארונות בגדים", 
    "ניקוי מסילות חלונות", "ניקוי דלתות ומשקופים", "ניקוי ארונות מטבח מבפנים", 
    "ניקוי תריסים", "ניקוי יסודי מתחת למיטות", "מיון ותוקף תרופות"
]

# ניהול זיכרון (Session State) כדי שהמשימות הרנדומליות יישארו קבועות ולא ישתנו בכל קליק
if 'weekly_focus' not in st.session_state:
    st.session_state.weekly_focus = random.sample(WEEKLY_TASKS, min(3, len(WEEKLY_TASKS)))
if 'monthly_focus' not in st.session_state:
    st.session_state.monthly_focus = random.sample(MONTHLY_TASKS, min(2, len(MONTHLY_TASKS)))
if 'passover_focus' not in st.session_state:
    st.session_state.passover_focus = random.choice(PASSOVER_TASKS)

# בדיקת תאריך - האם אנחנו בתקופת הכנות לפסח? (החל מפברואר - חודש 2 ועד אפריל - חודש 4)
current_month = datetime.now().month
is_passover_season = current_month in [2, 3, 4]

# --- אזור 1: אתגרי השבוע (המשימות המורדמות) ---
st.markdown("## 🎯 משימות פוקוס להשבוע")
st.markdown("<div class='challenge-box'>", unsafe_allow_html=True)
st.write("**משימות שבועיות שנבחרו עבורך ברנדומליות:**")
for task in st.session_state.weekly_focus:
    st.checkbox(task, key=f"focus_w_{task}")

st.write("**משימות חודשיות שכדאי לסגור השבוע:**")
for task in st.session_state.monthly_focus:
    st.checkbox(task, key=f"focus_m_{task}")
st.markdown("</div>", unsafe_allow_html=True)

if st.button("🔄 רענן והגרל משימות פוקוס חדשות"):
    st.session_state.weekly_focus = random.sample(WEEKLY_TASKS, min(3, len(WEEKLY_TASKS)))
    st.session_state.monthly_focus = random.sample(MONTHLY_TASKS, min(2, len(MONTHLY_TASKS)))
    st.rerun()

# --- אזור 2: מודול פסח חכם (יופיע רק מפברואר ואילך) ---
if is_passover_season:
    st.markdown("## ☀️ מבצע פסח יצא לדרך!")
    st.markdown("<div class='passover-box'>", unsafe_allow_html=True)
    st.write(f"אנחנו בחודש {current_month}, הנה משימת פסח השבועית שלך כדי להגיע רגועים לחג:")
    st.info(f"✨ **{st.session_state.passover_focus}**")
    if st.checkbox("סיימתי את משימת הפסח השבועית!", key="passover_done"):
        st.balloons()
        st.success("כל הכבוד! אחד פחות!")
    
    if st.button("⏭️ הגרל משימת פסח אחרת"):
        st.session_state.passover_focus = random.choice(PASSOVER_TASKS)
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# --- אזור 3: משימות יומיות רגילות ---
st.markdown("## 📅 משימות קטנות - כל יום")
col1, col2 = st.columns(2)

# חלוקת המשימות היומיות לשני טורים שיהיה נוח בעיניים
mid = len(DAILY_TASKS) // 2
with col1:
    for task in DAILY_TASKS[:mid]:
        st.checkbox(task, key=f"daily_{task}")
with col2:
    for task in DAILY_TASKS[mid:]:
        st.checkbox(task, key=f"daily_{task}")

# כפתור איפוס יומי
if st.button("🧹 אפס את כל הסימונים ליום חדש"):
    for key in list(st.session_state.keys()):
        if key.startswith("daily_"):
            del st.session_state[key]
    st.rerun()