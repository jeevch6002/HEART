import streamlit as st

st.set_page_config(page_title="My Valentine 💖", page_icon="❤️", layout="centered")

# Session state for final screen
if "accepted" not in st.session_state:
    st.session_state.accepted = False

# 💓 Heartbeat Animation (CSS)
st.markdown("""
<style>
.heart {
  font-size: 80px;
  color: red;
  animation: beat 1s infinite;
  text-align: center;
}

@keyframes beat {
  0% { transform: scale(1); }
  25% { transform: scale(1.1); }
  40% { transform: scale(1); }
  60% { transform: scale(1.1); }
  100% { transform: scale(1); }
}
</style>
""", unsafe_allow_html=True)





# ================= FINAL LOVE SCREEN =================
if st.session_state.accepted:
    st.markdown("<div class='heart'>❤️</div>", unsafe_allow_html=True)

    st.markdown(
        "<h1 style='text-align:center; color:#ff4b4b;'>I Love You ❤️</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style='text-align:center; font-size:22px;'>
        You are my today, my tomorrow, and every heartbeat in between 💓<br><br>
        Thank you for being mine.<br><br>
        Happy Valentine’s Day 💖
        </div>
        """,
        unsafe_allow_html=True
    )

    st.balloons()
    st.stop()

# ================= MAIN APP =================

# Title
st.markdown(
    "<h1 style='text-align: center; color: #ff4b4b;'>💘 Happy Valentine’s Week 💘</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h3 style='text-align: center;'>To the love of my life ❤️</h3>",
    unsafe_allow_html=True
)

st.markdown("---")

# Love Letter
st.markdown(
    """
    <div style='text-align: center; font-size: 20px;'>
    Every moment with you feels like magic ✨<br><br>
    These are some of my favorite memories of us 💕
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# Photos
st.markdown("## 📸 Our Beautiful Moments")
col1, col2, col3 = st.columns(3)

with col1:
    st.image("media/pic1.jpeg", caption="My favorite smile 💖")
with col2:
    st.image("media/pic2.jpeg", caption="Us being us 😍")
with col3:
    st.image("media/pic3.jpeg", caption="Forever memory 💫")

st.markdown("---")

# Video
st.markdown("## 🎥 A Memory I’ll Always Cherish")
st.video("media/memory.mp4")

st.markdown("---")

# Proposal
st.markdown(
    "<h2 style='text-align: center;'>💌 Will you be my Valentine? 💌</h2>",
    unsafe_allow_html=True
)

col_yes, col_no = st.columns(2)

with col_yes:
    if st.button("😍 YES"):
        st.session_state.accepted = True
        st.rerun()

with col_no:
    st.button("🙈 NO (not allowed 😌)")
