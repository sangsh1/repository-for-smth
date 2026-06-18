import streamlit as st
import json
import os
import random
from datetime import datetime
from gtts import gTTS
from streamlit_autorefresh import st_autorefresh

ALARM_FILE = "alarms.json"

st.set_page_config(
    page_title="외출시간 알람",
    page_icon="⏰"
)

st.title("⏰ 외출시간 음성 알람")

# 5초마다 새로고침
st_autorefresh(interval=5000, key="refresh")

# -----------------
# 파일 관리
# -----------------

def load_alarms():
    if os.path.exists(ALARM_FILE):
        with open(ALARM_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_alarms(data):
    with open(ALARM_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

alarms = load_alarms()

# -----------------
# 알람 추가
# -----------------

st.subheader("📅 외출 시간 예약")

alarm_time = st.datetime_input(
    "외출 시간 선택",
    value=datetime.now()
)

if st.button("알람 예약"):
    alarms.append({
        "time": alarm_time.strftime("%Y-%m-%d %H:%M")
    })

    save_alarms(alarms)

    st.success("예약 완료!")

# -----------------
# 알람 목록
# -----------------

st.subheader("📋 예약 목록")

for idx, alarm in enumerate(alarms):

    col1, col2 = st.columns([4,1])

    with col1:
        st.write(alarm["time"])

    with col2:
        if st.button("삭제", key=idx):
            alarms.pop(idx)
            save_alarms(alarms)
            st.rerun()

# -----------------
# 알람 확인
# -----------------

now = datetime.now()

funny_messages = [
    "일어나세요. 외출 시간입니다.",
    "출발하지 않으면 지각입니다.",
    "버스가 당신을 기다리지 않습니다.",
    "5분만 더는 허용되지 않습니다.",
    "오늘도 멋진 하루 시작해봅시다."
]

for alarm in alarms:

    alarm_dt = datetime.strptime(
        alarm["time"],
        "%Y-%m-%d %H:%M"
    )

    if (
        now.year == alarm_dt.year and
        now.month == alarm_dt.month and
        now.day == alarm_dt.day and
        now.hour == alarm_dt.hour and
        now.minute == alarm_dt.minute
    ):

        msg = random.choice(funny_messages)

        st.balloons()

        st.error("🚨 외출 시간입니다!")

        st.write(msg)

        tts = gTTS(
            text=msg,
            lang="ko"
        )

        tts.save("alarm.mp3")

        with open("alarm.mp3", "rb") as f:
            st.audio(
                f.read(),
                format="audio/mp3"
            )

        alarms.remove(alarm)
        save_alarms(alarms)

        break
