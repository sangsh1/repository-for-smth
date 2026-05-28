import streamlit as st
from datetime import datetime, timedelta, time
import math

# ─── 페이지 설정 ───────────────────────────────────────────────
st.set_page_config(
    page_title="수면 타이머 | SleepSync",
    page_icon="🌙",
    layout="centered",
)

# ─── 커스텀 CSS ───────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Dodum&family=Noto+Serif+KR:wght@400;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Gowun Dodum', sans-serif;
    background-color: #0d0d1a;
    color: #e8e0f5;
}

.main {
    background-color: #0d0d1a;
}

h1, h2, h3 {
    font-family: 'Noto Serif KR', serif;
    color: #c9b8f0;
}

.stApp {
    background: linear-gradient(135deg, #0d0d1a 0%, #1a1030 50%, #0d1a2e 100%);
}

/* 카드 스타일 */
.card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(201,184,240,0.15);
    border-radius: 16px;
    padding: 24px;
    margin: 16px 0;
    backdrop-filter: blur(10px);
}

/* 결과 박스 */
.result-box {
    background: linear-gradient(135deg, rgba(138,99,210,0.2), rgba(79,140,210,0.2));
    border: 1px solid rgba(138,99,210,0.4);
    border-radius: 20px;
    padding: 28px;
    margin: 12px 0;
    text-align: center;
}

.result-time {
    font-family: 'Noto Serif KR', serif;
    font-size: 2.8rem;
    font-weight: 700;
    color: #c9b8f0;
    letter-spacing: 2px;
}

.result-label {
    font-size: 0.9rem;
    color: #9b8db8;
    margin-top: 4px;
}

.badge {
    display: inline-block;
    background: rgba(138,99,210,0.3);
    border: 1px solid rgba(138,99,210,0.5);
    border-radius: 20px;
    padding: 4px 14px;
    font-size: 0.8rem;
    color: #c9b8f0;
    margin: 4px;
}

.tip-box {
    background: rgba(79,140,210,0.1);
    border-left: 3px solid #4f8cd2;
    border-radius: 0 12px 12px 0;
    padding: 16px 20px;
    margin: 10px 0;
    font-size: 0.9rem;
    color: #b8cce8;
}

.header-emoji {
    font-size: 3rem;
    text-align: center;
    display: block;
    margin-bottom: 8px;
}

.section-title {
    font-size: 1.1rem;
    color: #9b8db8;
    font-weight: 600;
    margin-bottom: 12px;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* 슬라이더 색상 */
.stSlider [data-baseweb="slider"] {
    accent-color: #8a63d2;
}

/* 버튼 */
.stButton > button {
    background: linear-gradient(135deg, #8a63d2, #4f8cd2);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 12px 32px;
    font-size: 1rem;
    font-family: 'Gowun Dodum', sans-serif;
    font-weight: 600;
    width: 100%;
    cursor: pointer;
    transition: all 0.3s;
}

.stButton > button:hover {
    opacity: 0.85;
    transform: translateY(-1px);
}

/* 구분선 */
hr {
    border-color: rgba(201,184,240,0.1);
}

/* time_input 스타일 */
.stTimeInput label {
    color: #c9b8f0 !important;
}

</style>
""", unsafe_allow_html=True)


# ─── 헤더 ───────────────────────────────────────────────────
st.markdown('<span class="header-emoji">🌙</span>', unsafe_allow_html=True)
st.markdown("<h1 style='text-align:center; font-size:2rem;'>SleepSync</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#9b8db8; margin-bottom:32px;'>나에게 딱 맞는 취침 시간과 준비 시간을 계산해드려요</p>", unsafe_allow_html=True)

# ─── 수면 사이클 상수 ────────────────────────────────────────
SLEEP_CYCLE_MIN = 90        # 한 수면 사이클 = 90분
FALL_ASLEEP_MIN = 15        # 평균 잠드는 시간

# ─── 입력 섹션 ──────────────────────────────────────────────
st.markdown("### 📊 나의 생활 패턴 입력")

with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<p class="section-title">⏰ 기상 정보</p>', unsafe_allow_html=True)

        # 기상 시간 (여러 날 입력 후 평균)
        st.markdown("**평소 기상 시간 (여러 날)**")
        num_days = st.slider("최근 며칠치 기상 시간을 입력할까요?", 2, 7, 3, key="num_days")

        wake_times = []
        for i in range(num_days):
            t = st.time_input(f"Day {i+1} 기상 시간", value=time(7, 0), key=f"wake_{i}")
            wake_times.append(t)

    with col2:
        st.markdown('<p class="section-title">🪥 준비 정보</p>', unsafe_allow_html=True)

        st.markdown("**외출 준비 항목별 시간 (분)**")
        shower   = st.slider("🚿 샤워 / 세안",    5, 60, 15)
        skincare = st.slider("💄 스킨케어 / 메이크업",  0, 60, 10)
        hair     = st.slider("💇 헤어 스타일링",  0, 40, 10)
        outfit   = st.slider("👗 옷 입기",         2, 30, 5)
        meal     = st.slider("🍳 아침 식사",        0, 60, 15)
        commute_buffer = st.slider("🚇 이동 전 여유 시간", 0, 30, 10)

    st.markdown('</div>', unsafe_allow_html=True)


# ─── 선호 수면 시간 ──────────────────────────────────────────
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<p class="section-title">😴 수면 설정</p>', unsafe_allow_html=True)

    col3, col4 = st.columns(2)
    with col3:
        preferred_cycles = st.select_slider(
            "원하는 수면 사이클 수 (1사이클 = 90분)",
            options=[4, 5, 6],
            value=5,
        )
        cycle_desc = {4: "6시간 (최소 권장)", 5: "7시간 30분 (최적)", 6: "9시간 (충분한 휴식)"}
        st.caption(f"→ {cycle_desc[preferred_cycles]}")

    with col4:
        extra_buffer = st.slider("⏳ 아침 여유 버퍼 시간 (분)", 0, 30, 5)

    st.markdown('</div>', unsafe_allow_html=True)


# ─── 계산 버튼 ───────────────────────────────────────────────
st.markdown("")
calculate = st.button("✨ 나의 수면 루틴 계산하기")

# ─── 계산 로직 & 결과 ────────────────────────────────────────
if calculate:

    # 1. 평균 기상 시간 계산 (분 단위 평균 후 time 변환)
    total_minutes = sum(t.hour * 60 + t.minute for t in wake_times)
    avg_minutes   = round(total_minutes / len(wake_times))
    avg_wake_hour = avg_minutes // 60
    avg_wake_min  = avg_minutes % 60
    avg_wake      = time(avg_wake_hour % 24, avg_wake_min)

    # 2. 총 준비 시간
    total_prep = shower + skincare + hair + outfit + meal + commute_buffer + extra_buffer

    # 3. 외출 준비 시작 시간 (기상 후 준비 시작은 기상 시간 = 준비 시작)
    wake_dt   = datetime(2000, 1, 1, avg_wake_hour % 24, avg_wake_min)
    prep_start = wake_dt  # 기상 = 준비 시작
    ready_by  = wake_dt + timedelta(minutes=total_prep)

    # 4. 취침 권장 시간 (수면 사이클 기반)
    sleep_duration_min = preferred_cycles * SLEEP_CYCLE_MIN
    bedtime_dt = wake_dt - timedelta(minutes=sleep_duration_min + FALL_ASLEEP_MIN)

    # 5. 이른 알람 추가 여유를 위한 알람 시간 (준비 시작 = 기상 = 알람)
    alarm_time = wake_dt

    # ── 결과 출력 ──
    st.markdown("---")
    st.markdown("### 🎯 나만의 수면 루틴")

    # 평균 기상 시간 표시
    st.markdown(f"""
    <div class="tip-box">
        📊 <b>입력한 {num_days}일치 기상 시간 평균: {avg_wake.strftime('%H시 %M분')}</b>
    </div>
    """, unsafe_allow_html=True)

    col5, col6 = st.columns(2)

    with col5:
        st.markdown(f"""
        <div class="result-box">
            <div class="result-label">🌙 권장 취침 시간</div>
            <div class="result-time">{bedtime_dt.strftime('%H:%M')}</div>
            <div class="result-label">{preferred_cycles}사이클 × 90분 + 잠드는 시간 15분</div>
        </div>
        """, unsafe_allow_html=True)

    with col6:
        st.markdown(f"""
        <div class="result-box">
            <div class="result-label">⏰ 알람 & 기상 시간</div>
            <div class="result-time">{alarm_time.strftime('%H:%M')}</div>
            <div class="result-label">평균 기상 시간 기준</div>
        </div>
        """, unsafe_allow_html=True)

    col7, col8 = st.columns(2)

    with col7:
        st.markdown(f"""
        <div class="result-box">
            <div class="result-label">🪥 준비 시작 ~ 완료</div>
            <div class="result-time">{prep_start.strftime('%H:%M')} ~ {ready_by.strftime('%H:%M')}</div>
            <div class="result-label">총 준비 시간: {total_prep}분</div>
        </div>
        """, unsafe_allow_html=True)

    with col8:
        sleep_hrs = sleep_duration_min // 60
        sleep_mns = sleep_duration_min % 60
        st.markdown(f"""
        <div class="result-box">
            <div class="result-label">😴 총 수면 시간</div>
            <div class="result-time">{sleep_hrs}h {sleep_mns:02d}m</div>
            <div class="result-label">{preferred_cycles}사이클 기준</div>
        </div>
        """, unsafe_allow_html=True)

    # ── 준비 항목 상세 ──
    st.markdown("### 📋 아침 루틴 타임라인")

    items = [
        ("🚿", "샤워 / 세안",      shower),
        ("💄", "스킨케어 / 메이크업", skincare),
        ("💇", "헤어 스타일링",     hair),
        ("👗", "옷 입기",          outfit),
        ("🍳", "아침 식사",         meal),
        ("⏳", "이동 전 여유",       commute_buffer + extra_buffer),
    ]

    current = wake_dt
    for emoji, label, mins in items:
        if mins > 0:
            end = current + timedelta(minutes=mins)
            st.markdown(f"""
            <div style="display:flex; align-items:center; gap:12px; padding:10px 16px;
                        background:rgba(255,255,255,0.03); border-radius:10px; margin:6px 0;
                        border-left:3px solid rgba(138,99,210,0.4);">
                <span style="font-size:1.4rem;">{emoji}</span>
                <div style="flex:1;">
                    <div style="color:#c9b8f0; font-weight:600;">{label}</div>
                    <div style="color:#9b8db8; font-size:0.85rem;">{current.strftime('%H:%M')} → {end.strftime('%H:%M')} ({mins}분)</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            current = end

    # ── 수면 팁 ──
    st.markdown("### 💡 수면 품질 향상 팁")
    tips = [
        "취침 1시간 전 스마트폰 화면을 줄이면 멜라토닌 분비에 도움이 돼요.",
        "수면 사이클(90분)에 맞춰 자면 렘수면 중에 깨지 않아 개운해요.",
        "매일 같은 시간에 자고 일어나면 생체 리듬이 안정돼요.",
        f"취침 시간 {bedtime_dt.strftime('%H:%M')}을 핸드폰 알림으로 설정해 보세요!",
    ]
    for tip in tips:
        st.markdown(f'<div class="tip-box">💬 {tip}</div>', unsafe_allow_html=True)

    st.balloons()
