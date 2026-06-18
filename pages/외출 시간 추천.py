import streamlit as st
from streamlit_autorefresh import st_autorefresh
from streamlit_mic_recorder import mic_recorder
from datetime import datetime
from gtts import gTTS
import json
import random
import os
import re

# --------------------
# 설정
# --------------------

ALARM_FILE = "alarms.json"

st.set_page_config(
    page_title="외출시간 알람",
    page_icon="⏰"
)

st.title("⏰ 외출시간 음성 알람")

# 5초마다 새로고침
st_autorefresh(interval=5000, key="alarm_refresh")

# --------------------
# 저장 함수
# --------------------

def load_alarms():
    if os.path.exists(ALARM_FILE):
        with open(ALARM_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_alarms(data):
    with open(ALARM_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

alarms = load_alarms()

# --------------------
# 음성 인식 (간단 버전)
# --------------------

def parse_time(text):

    hour_match = re.search(r"(\d+)시", text)

    if hour_match:
        hour = int(hour_match.group(1))

        tomorrow = datetime.now()

        alarm_time = tomorrow.replace(
            hour=hour,
            minute=0,
            second=0,
            microsecond=0
        )

        if alarm_time < datetime.now():
            from datetime import timedelta
            alarm_time += timedelta(days=1)

        return alarm_time

    return None

# --------------------
# 음성 알람 등록
# --------------------

st.subheader("🎤 음성으로 알람 설정")

audio = mic_recorder(
    start_prompt="녹음 시작",
    stop_prompt="녹음 종료",
    key="recorder"
)

st.info(
    "예시: 내일 7시 알람 설정해줘"
)

if audio:

    st.success("음성 녹음 완료")

    # Streamlit Cloud에서 STT가 제한적이라
    # 텍스트 입력 대체

    voice_text = st.text_input(
        "인식된 문장을 입력해보세요",
        placeholder="내일 7시 알람 설정"
    )

    if st.button("음성 알람 등록"):

        alarm_dt = parse_time(voice_text)

        if alarm_dt:

            alarms.append({
                "time": alarm_dt.strftime("%Y-%m-%d %H:%M")
            })

            save_alarms(alarms)

            st.success(
                f"알람 등록 완료 : {alarm_dt}"
            )

        else:
            st.error("시간을 찾을 수 없습니다.")

# --------------------
# 수동 등록
# --------------------

st.subheader("📅 직접 알람 등록")

alarm_datetime = st.datetime_input(
    "외출 시간"
)

if st.button("알람 추가"):

    alarms.append({
        "time": alarm_datetime.strftime("%Y-%m-%d %H:%M")
    })

    save_alarms(alarms)

    st.success("등록 완료")

# --------------------
# 알람 목록
# --------------------

st.subheader("📋 예약 목록")

for idx, alarm in enumerate(alarms):

    col1, col2 = st.columns([5,1])

    with col1:
        st.write(alarm["time"])

    with col2:

        if st.button(
            "삭제",
            key=f"del_{idx}"
        ):

            alarms.pop(idx)

            save_alarms(alarms)

            st.rerun()

# --------------------
# 알람 실행
# --------------------

now = datetime.now()

funny_messages = [
    "일어나라 인간이여. 외출 시간이다.",
    "지금 안 나가면 지각이다.",
    "버스는 당신을 기다리지 않는다.",
    "5분만 더는 금지다.",
    "오늘도 힘내서 출발해보자."
]

for alarm in alarms:

    alarm_time = datetime.strptime(
        alarm["time"],
        "%Y-%m-%d %H:%M"
    )

    if (
        now.year == alarm_time.year and
        now.month == alarm_time.month and
        now.day == alarm_time.day and
        now.hour == alarm_time.hour and
        now.minute == alarm_time.minute
    ):

        st.balloons()

        msg = random.choice(
            funny_messages
        )

        st.error("🚨 외출 시간!")

        st.write(msg)

        tts = gTTS(
            text=msg,
            lang="ko"
        )

        tts.save("alarm.mp3")

        with open(
            "alarm.mp3",
            "rb"
        ) as f:

            st.audio(
                f.read(),
                format="audio/mp3"
            )

        alarms.remove(alarm)

        save_alarms(alarms)

        break
