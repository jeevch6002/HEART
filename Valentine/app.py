import streamlit as st
import os
import time

st.set_page_config(page_title="My Valentine 💖", page_icon="❤️", layout="centered")

# ================= SAFE MEDIA HELPERS =================

def safe_image(path, caption=""):
    try:
        if os.path.exists(path):
            st.image(path, caption=caption)
    except Exception:
        pass

def safe_video(path):
    try:
        if os.path.exists(path):
            st.video(path)
    except Exception:
        pass

def safe_audio(path):
    try:
        if os.path.exists(path):
            with open(path, "rb") as audio:
                st.audio(audio.read(), format="audio/mp3", loop=True)
    except Exception:
        pass

# ================= SESSION STATE =================

if "accepted" not in st.session_state:
    st.session_state.accepted = False

if "show_memories" not in st.session_state:
    st.session_state.show_memories = False

if "play_music" not in st.session_state:
    st.session_state.play_music = False

# ================= LOVE THEME CSS =================

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #fff0f5, #ffe6eb);
}

.heart {
    font-size: 90px;
    color: #ff4b4b;
    animation: beat 1.2s infinite;
    text-align: center;
}

@keyframes beat {
    0% { transform: scale(1); }
    25% { transform: scale(1.12); }
    50% { transform: scale(1); }
    75% { transform: scale(1.12); }
    100% { transform: scale(1); }
}

.stButton > button {
    background: linear-gradient(45deg, #ff4b4b, #ff85a2);
    color: white;
    border-radius: 30px;
    padding: 0.6em 1.5em;
    font-size: 18px;
    border: none;
    transition: all 0.3s ease;
}

.stButton > button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 15px rgba(255,75,75,0.6);
}

img {
    border-radius: 20px;
    box-shadow: 0 8px 20px rgba(255, 105, 135, 0.3);
}
</style>
""", unsafe_allow_html=True)

# ================= MUSIC CONTROLS =================

st.markdown("<h3 style='text-align:center;'>🎶 Background Music</h3>", unsafe_allow_html=True)

col_music1, col_music2 = st.columns(2)

with col_music1:
    if st.button("▶️ Play Music"):
        st.session_state.play_music = True

with col_music2:
    if st.button("⏸ Stop Music"):
        st.session_state.play_music = False

if st.session_state.play_music:
    safe_audio("media/love.mp3")

st.markdown("---")

# ================= FINAL LOVE SCREEN =================

if st.session_state.accepted:
    st.markdown("<div class='heart'>❤️</div>", unsafe_allow_html=True)

    st.markdown(
        "<h1 style='text-align:center; color:#ff4b4b;'>I Love You ❤️</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style='text-align:center; font-size:22px; color:#444;'>
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

st.markdown(
    "<h1 style='text-align: center; color: #ff4b4b;'>💘 Happy Valentine’s Week 💘</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h3 style='text-align: center; color:#ff6f91;'>To the love of my life ❤️</h3>",
    unsafe_allow_html=True
)

st.markdown("---")

st.markdown(
    """
    <div style='text-align: center; font-size: 21px; color:#555;'>
    Every moment with you feels like magic ✨<br><br>
    Tap below to unlock our love story 💕
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# ================= MEMORY REVEAL =================

if not st.session_state.show_memories:
    if st.button("💝 Reveal Our Memories"):
        st.session_state.show_memories = True
        st.rerun()

if st.session_state.show_memories:
    col1, col2, col3 = st.columns(3)

    with col1:
        time.sleep(0.3)
        safe_image("media/pic1.jpeg", "My favorite smile 💖")

    with col2:
        time.sleep(0.3)
        safe_image("media/pic2.jpeg", "Us being us 😍")

    with col3:
        time.sleep(0.3)
        safe_image("media/pic3.jpeg", "Forever memory 💫")

    st.markdown("---")
    safe_video("media/memory.mp4")
    st.markdown("---")

# ================= PROPOSAL (UNCHANGED) =================

st.markdown(
    "<h2 style='text-align: center; color:#ff4b4b;'>💌 Will you be my Valentine? 💌</h2>",
    unsafe_allow_html=True
)

col_yes, col_no = st.columns(2)

with col_yes:
    if st.button("😍 YES"):
        st.session_state.accepted = True
        st.rerun()

with col_no:
    st.button("🙈 NO (not allowed 😌)")
