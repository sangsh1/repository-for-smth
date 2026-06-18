import streamlit as st
import json
import os
from datetime import datetime
from gtts import gTTS
from streamlit_autorefresh import st_autorefresh
import speech_recognition as sr

ALARM_FILE = "alarms.json"

# 자동 새로고침
st_autorefresh(interval=5000, key="alarm_refresh")

st.title("🎒 외출시간 음성 알람")

# --------------------
# 알람 저장/불러오기
# --------------------
def load_alarms():
    if os.path.exists(ALARM_FILE):
        with open(ALARM_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_alarms(data):
    with open(ALARM_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)

alarms = load_alarms()

# --------------------
# 음성 입력
# --------------------
st.header("🎤 음성으로 알람 설정")

audio_file = st.file_uploader(
    "음성을 녹음해서 업로드하세요 (wav 권장)",
    type=["wav"]
)

if audio_file:
    recognizer = sr.Recognizer()

    with open("temp.wav", "wb") as f:
        f.write(audio_file.read())

    with sr.AudioFile("temp.wav") as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio, language="ko-KR")

        st.success(f"인식 결과: {text}")

        # 간단 예시
        if "7시" in text:
            alarm_time = (
                datetime.now()
                .replace(hour=7, minute=0, second=0)
            )

            alarms.append({
                "time": alarm_time.strftime("%Y-%m-%d %H:%M"),
                "message": "외출 준비하세요!"
            })

            save_alarms(alarms)

            st.success("알람 설정 완료!")

    except Exception as e:
        st.error("음성 인식 실패")

# --------------------
# 수동 설정
# --------------------
st.header("⏰ 직접 설정")

alarm_datetime = st.datetime_input(
    "외출 시간 선택"
)

if st.button("알람 추가"):
    alarms.append({
        "time": alarm_datetime.strftime("%Y-%m-%d %H:%M"),
        "message": "외출 준비하세요!"
    })

    save_alarms(alarms)
    st.success("추가 완료")

# --------------------
# 예약 목록
# --------------------
st.header("📋 예약된 알람")

for idx, alarm in enumerate(alarms):
    st.write(alarm["time"])

    if st.button(f"삭제 {idx}"):
        alarms.pop(idx)
        save_alarms(alarms)
        st.rerun()

# --------------------
# 알람 체크
# --------------------
now = datetime.now()

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

        st.error("🚨 외출 시간입니다!")

        text = (
            "일어나세요! 외출 시간입니다! "
            "지금 출발하지 않으면 지각할 수 있습니다!"
        )

        tts = gTTS(
            text=text,
            lang="ko"
        )

        tts.save("alarm_voice.mp3")

        audio_file = open(
            "alarm_voice.mp3",
            "rb"
        )

        st.audio(
            audio_file.read(),
            format="audio/mp3",
            autoplay=True
        )
