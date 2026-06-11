import streamlit as st
from google import genai

# -----------------------
# 페이지 설정
# -----------------------
st.set_page_config(
    page_title="🚽 한빈이의 스키비디 토일렛 위키",
    page_icon="🚽",
    layout="centered"
)

st.title("🚽 한빈이의 스키비디 토일렛 위키")
st.caption("스키비디 토일렛 광팬 한빈이가 설명해줌 🔥")

# -----------------------
# Gemini API Key
# -----------------------
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
    st.error("❌ Secrets에 GEMINI_API_KEY가 설정되지 않았습니다.")
    st.stop()

# -----------------------
# Gemini Client
# -----------------------
try:
    client = genai.Client(api_key=api_key)
except Exception as e:
    st.error(f"❌ Gemini 초기화 실패\n\n{e}")
    st.stop()

# -----------------------
# 채팅 기록
# -----------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "브로 🔥\n\n"
                "나는 한빈이야.\n"
                "스키비디 토일렛 관련 질문이면 뭐든 물어봐 ㅋㅋ\n\n"
                "예시:\n"
                "- 타이탄 TV맨 설명해줘\n"
                "- G맨 토일렛은 얼마나 강함?\n"
                "- 최강 캐릭터는 누구야?\n"
                "- 에피소드 77 요약해줘"
            )
        }
    ]

# -----------------------
# 이전 대화 출력
# -----------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------
# 사이드바
# -----------------------
with st.sidebar:
    st.header("⚙️ 메뉴")

    if st.button("🗑️ 대화 초기화"):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": (
                    "브로 🔥\n\n"
                    "대화 초기화 완료 ㅋㅋ\n"
                    "다시 질문해줘!"
                )
            }
        ]
        st.rerun()

# -----------------------
# 사용자 입력
# -----------------------
prompt = st.chat_input("질문 입력...")

if prompt:

    # 사용자 메시지 저장
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        try:
            history = ""

            for msg in st.session_state.messages[-20:]:
                role = "사용자" if msg["role"] == "user" else "한빈이"
                history += f"{role}: {msg['content']}\n"

            system_prompt = """
너는 '한빈이'다.

설정:
- 스키비디 토일렛을 엄청 좋아하는 광팬이다.
- 친구처럼 편하게 대화한다.
- 흥분한 팬 느낌으로 말한다.
- '브로', 'ㄹㅇ', '미쳤다', '레전드', 'GOAT', '개간지', 'ㅋㅋ' 등을 자연스럽게 사용한다.
- 하지만 설명 자체는 최대한 정확하게 한다.
- 모르는 내용은 지어내지 않는다.
- 한국어로 답한다.

예시 스타일:

"브로 그거 ㄹㅇ 레전드 캐릭터임 🔥"

"당시 팬들 반응이 진짜 미쳤었음 ㅋㅋ"

"개인적으로 GOAT 후보라고 생각함 ㄹㅇ"

답변은 너무 짧지 않게 작성한다.
"""

            full_prompt = f"""
{system_prompt}

대화 기록:
{history}

사용자 질문:
{prompt}
"""

            response = client.models.generate_content(
                model="gemini-2.5-flash-lite",
                contents=full_prompt
            )

            answer = response.text

        except Exception as e:
            answer = f"""
⚠️ 오류 발생

{str(e)}

잠시 후 다시 시도해줘 브로 😭
"""

        st.markdown(answer)

    # 응답 저장
    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )
