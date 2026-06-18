import streamlit as st
from datetime import datetime, timedelta, time
import random

# 페이지 설정 (다중 페이지 앱의 경우 메인에서 이미 설정했다면 생략 가능)
st.set_page_config(page_title="출발해라 인간", page_icon="⏰", layout="centered")

# 세션 상태 초기화 (재미있는 멘트 재생성용)
if "nag_message" not in st.session_state:
    st.session_state.nag_message = ""

# 헤더 영역
st.title("⏰ 집돌이·집순이 탈출 타이머")
st.subheader("계획대로 나가본 적이 없는 당신을 위한 맞춤형 출발 가이드")

# 입력 구역
st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    appointment_time = st.time_input("약속 시간은 언제인가요?", time(18, 0))
    travel_time = st.number_input("이동 시간 (분 단위)", min_value=5, max_value=300, value=30, step=5)

with col2:
    purpose = st.selectbox(
        "오늘의 외출 목적은?",
        ["중요한 비즈니스", "이성과의 데이트", "친구들과의 소소한 모임", "귀찮지만 가야 하는 출근/등교", "숨쉬듯 자연스러운 덕질"]
    )
    persona = st.radio(
        "알림 스타일 선택",
        ["팩트폭행형", "둥둥이 응원형", "스파르타 교관형"]
    )

# 계산 로직 (에러 수정 지점)
now = datetime.now()
appointment_datetime = datetime.combine(now.date(), appointment_time)

# 약속 시간이 이미 지났다면 내일로 처리
if appointment_datetime < now:
    appointment_datetime += timedelta(days=1)

# 출발해야 하는 시간 계산
departure_datetime = appointment_datetime - timedelta(minutes=travel_time)
time_left = departure_datetime - now
minutes_left = int(time_left.total_seconds() / 60)

# 결과 출력 구역
st.markdown("---")
st.markdown(f"### 🚀 당신이 현관문을 열고 나가야 할 시간: **{departure_datetime.strftime('%H시 %M분')}**")

# 동적 UI 및 잔소리 로직
if minutes_left > 60:
    st.success(f"여유 부릴 시간 딱 {minutes_left // 60}시간 {minutes_left % 60}분 남았습니다. 아직은 침대와 한 몸이어도 무죄.")
elif 0 <= minutes_left <= 60:
    st.warning(f"🚨 긴급! 출발까지 **{minutes_left}분** 남았습니다. 양치하면서 옷 고르세요.")
else:
    st.error(f"☠️ 이미 {abs(minutes_left)}분 전에 나갔어야 했습니다. 카카오T를 부르거나 대가리 박고 사과문부터 작성하세요.")

# 재미있는 맞춤형 잔소리 생성기
nags = {
    "팩트폭행형": [
        f"누가 보면 {purpose}에 목숨 안 건 줄 알겠어요. 지금 안 나가면 늦습니다.",
        "당신의 '지금 나감'은 거짓말인 거 온 세상이 다 압니다. 빨리 신발 신으세요.",
        f"이동 시간 {travel_time}분은 축지법 기준이 아닙니다. 인간계의 물리 법칙을 따르세요."
    ],
    "둥둥이 응원형": [
        f"오늘 {purpose} 목적으로 엄청 빛나실 예정! 늦어서 허둥대면 아쉽잖아요. 무브무브!",
        "할 수 있다! 씻는 것부터 옷 입기까지 10분 컷 도전!",
        "지각해서 미안해하는 눈빛보다 정시 도착해서 당당한 미소가 더 아름답습니다 ✨"
    ],
    "스파르타 교관형": [
        f"정신 안 차립니까? {purpose}(이)가 장난입니까? 당장 침대에서 인공위성처럼 사출되십시오.",
        "당신의 나태함이 약속을 파괴하고 있습니다. 3분 내로 양말 안 신으면 탈락입니다.",
        "움직여라 인간! 패배자는 침대에 누워있고, 승리자는 약속 장소에 10분 먼저 도착한다!"
    ]
}

if st.button("🔥 내 정신을 깨우는 한마디 보기"):
    st.session_state.nag_message = random.choice(nags[persona])

if st.session_state.nag_message:
    st.info(f"💬 **[{persona}]** {st.session_state.nag_message}")
    이것도
