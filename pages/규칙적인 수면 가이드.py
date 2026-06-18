import streamlit as st
import pandas as pd
from datetime import datetime, date, time
import os

st.set_page_config(
    page_title="Sleep Routine Tracker",
    page_icon="🌙",
    layout="centered"
)

st.title("🌙 규칙적인 취침을 위한 수면 루틴 앱")

st.write("목표 취침 시간을 설정하고 매일의 수면 습관을 기록해 보세요.")

DATA_FILE = "sleep_data.csv"

if os.path.exists(DATA_FILE):
    df = pd.read_csv(DATA_FILE)
else:
    df = pd.DataFrame(columns=["date", "target", "actual", "score"])

target_time = st.time_input(
    "🎯 목표 취침 시간",
    value=time(22, 30)
)

actual_time = st.time_input(
    "🛏️ 실제 취침 시간",
    value=time(23, 0)
)

st.subheader("✅ 자기 전 루틴 체크")

phone = st.checkbox("취침 30분 전 스마트폰 사용 중단")
water = st.checkbox("물 마시기")
stretch = st.checkbox("가벼운 스트레칭")
light = st.checkbox("조명 어둡게 하기")
alarm = st.checkbox("알람 설정하기")

if st.button("기록 저장"):
    target_minutes = target_time.hour * 60 + target_time.minute
    actual_minutes = actual_time.hour * 60 + actual_time.minute

    diff = abs(actual_minutes - target_minutes)

    score = max(0, 100 - diff)

    new_data = pd.DataFrame([{
        "date": date.today(),
        "target": target_time.strftime("%H:%M"),
        "actual": actual_time.strftime("%H:%M"),
        "score": score
    }])

    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)

    st.success("수면 기록이 저장되었습니다!")

    st.metric("🌟 오늘의 수면 점수", f"{score}점")

    if score >= 90:
        st.info("매우 규칙적인 수면 습관이에요!")
    elif score >= 70:
        st.info("좋은 습관을 유지하고 있어요!")
    else:
        st.warning("취침 시간을 조금 더 일정하게 맞춰보세요.")

if not df.empty:
    st.subheader("📊 최근 수면 기록")

    recent_df = df.tail(7)

    st.dataframe(recent_df, use_container_width=True)

    st.line_chart(recent_df["score"])
