import streamlit as st
import pandas as pd
from datetime import datetime, date, time, timedelta
import os

# 1. 페이지 기본 설정 및 프리미엄 테마 적용
st.set_page_config(
    page_title="SnoozeWise | 데일리 수면 루틴 트래커",
    page_icon="🌙",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 눈이 편안한 인디고 로열 다크 테마와 세련된 그라데이션 커스텀 CSS
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700&family=Playfair+Display:ital,wght=0,600;1,400&display=swap');
    
    /* 기본 폰트 및 모션 백그라운드 디자인 */
    html, body, [class*="css"] {
        font-family: 'Noto Sans KR', sans-serif;
    }
    
    /* 스무스 애니메이션 정의 */
    @keyframes fadeInDown {
        0% { opacity: 0; transform: translateY(-20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    @keyframes fadeInUp {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    @keyframes pulseGlow {
        0%, 100% { border-color: rgba(99, 102, 241, 0.3); box-shadow: 0 0 15px rgba(99, 102, 241, 0.1); }
        50% { border-color: rgba(99, 102, 241, 0.6); box-shadow: 0 0 25px rgba(99, 102, 241, 0.25); }
    }

    /* 메인 브랜딩 컨테이너 */
    .header-container {
        text-align: center;
        padding: 2rem 1rem 1.5rem 1rem;
        animation: fadeInDown 1.2s cubic-bezier(0.16, 1, 0.3, 1);
    }
    
    .brand-logo {
        font-size: 3.2rem;
        font-family: 'Playfair Display', serif;
        font-weight: 600;
        letter-spacing: -1px;
        background: linear-gradient(135deg, #a5b4fc 0%, #818cf8 50%, #6366f1 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    
    .brand-desc {
        font-size: 1.1rem;
        color: #94a3b8;
        font-weight: 300;
        letter-spacing: 1px;
    }

    /* 입체감 있는 글래스모피즘 박스 */
    .glass-card-premium {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.6) 0%, rgba(15, 23, 42, 0.8) 100%);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 24px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        animation: fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) both;
    }
    
    .glass-card-premium:hover {
        transform: translateY(-4px);
        border-color: rgba(99, 102, 241, 0.3);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.3);
    }

    /* 루틴 달성률 게이지 바 */
    .routine-progress-container {
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
        height: 10px;
        width: 100%;
        margin-top: 1rem;
        margin-bottom: 1rem;
        overflow: hidden;
    }

    .routine-progress-fill {
        background: linear-gradient(90deg, #818cf8 0%, #6366f1 100%);
        height: 100%;
        border-radius: 10px;
        transition: width 0.6s ease-in-out;
    }

    /* 커스텀 라벨 및 글꼴 색상 */
    .section-title {
        color: #c7d2fe;
        font-weight: 600;
        font-size: 1.3rem;
        margin-bottom: 1.2rem;
    }

    /* 스트림릿 기본 버튼 커스텀 */
    div.stButton > button {
        background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%) !important;
        border: none !important;
        color: #fff !important;
        padding: 0.7rem 2rem !important;
        border-radius: 12px !important;
        font-weight: 600 !important;
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.2) !important;
        width: 100% !important;
    }
    div.stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(99, 102, 241, 0.45) !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 2. 프리미엄 헤더 세션
st.markdown(
    """
    <div class="header-container">
        <div class="brand-logo">SnoozeWise</div>
        <div class="brand-desc">🌙 DAILY SLEEP ROUTINE TRACKER</div>
    </div>
    """,
    unsafe_allow_html=True
)

st.write(" ")

# 3. 로컬 데이터 관리 엔진 (안정적인 데이터 관리)
DATA_FILE = "sleep_data.csv"

if os.path.exists(DATA_FILE):
    try:
        df = pd.read_csv(DATA_FILE)
    except Exception:
        df = pd.DataFrame(columns=["date", "target", "actual", "score", "routine_rate"])
else:
    df = pd.DataFrame(columns=["date", "target", "actual", "score", "routine_rate"])

# 4. 레이아웃 분할을 통한 프리미엄 공간 구성
col_left, col_right = st.columns([1.1, 0.9])

with col_left:
    st.markdown(
        """
        <div class="glass-card-premium">
            <div class="section-title">⏱️ 오늘 밤 수면 타깃 및 패턴 입력</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    col_input1, col_input2 = st.columns(2)
    with col_input1:
        target_time = st.time_input(
            "🎯 목표로 하는 취침 시간",
            value=time(22, 30)
        )
    with col_input2:
        actual_time = st.time_input(
            "🛏️ 실제 잠자리에 든 시간",
            value=time(23, 0)
        )

    # 5. 자기 전 루틴 체크박스 그룹화 및 시각 게이지 구축
    st.markdown("<div style='margin-bottom: 1.5rem;'></div>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class="glass-card-premium">
            <div class="section-title">✅ 프리미엄 취침 전 루틴 관리</div>
            <p style="color: #94a3b8; font-size: 0.85rem; margin-top: -0.5rem; margin-bottom: 1.5rem;">
                수면 호르몬 분비와 심부 체온 조절을 위해 검증된 5대 기초 루틴입니다.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    col_r1, col_r2 = st.columns(2)
    with col_r1:
        phone = st.checkbox("📱 취침 30분 전 스마트폰 멀리하기")
        water = st.checkbox("💧 신체 이완을 돕는 미온수 한 모금")
        stretch = st.checkbox("🧘 굳어 있던 척추 가볍게 풀어주기")
    with col_r2:
        light = st.checkbox("💡 방 조명 어둡고 은은하게 세팅")
        alarm = st.checkbox("⏰ 내일 아침 알람 확인 및 소리 조율")

    # 루틴 달성도 계산
    routines = [phone, water, stretch, light, alarm]
    completed_count = sum(routines)
    routine_rate = int((completed_count / len(routines)) * 100)

    # 게이지 시뮬레이션바 동적 표출
    st.markdown(
        f"""
        <p style="color: #a5b4fc; font-size: 0.9rem; font-weight: 500; margin-bottom: 0.2rem;">루틴 성취도: {routine_rate}% 완료</p>
        <div class="routine-progress-container">
            <div class="routine-progress-fill" style="width: {routine_rate}%;"></div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # 기록 및 저장 처리 (자정 근처 시간 역산 버그 예방 알고리즘 포함)
    if st.button("🌟 오늘의 수면 습관 데이터 기록하기"):
        # 자정 전후의 분 단위 계산 최적화 알고리즘
        target_minutes = target_time.hour * 60 + target_time.minute
        actual_minutes = actual_time.hour * 60 + actual_time.minute

        # 만약 실제 취침 시간이 새벽이고 (예: 01:00 = 60분) 목표 취침 시간이 늦은 밤인 경우 (예: 23:00 = 1380분)
        # 실제 취침 시간을 다음 날로 환산하여 24시간을 가산
        if actual_minutes < 360 and target_minutes > 1080:
            actual_minutes += 24 * 60
        elif target_minutes < 360 and actual_minutes > 1080:
            target_minutes += 24 * 60

        diff = abs(actual_minutes - target_minutes)
        
        # 수면 부합도 점수 산출 (최대 100점)
        score = max(0, 100 - diff)
        
        # 루틴 추가 보너스 점수 가산 적용 (루틴 1개당 2점 보너스 제공)
        bonus_points = completed_count * 2
        final_score = min(100, score + bonus_points)

        new_data = pd.DataFrame([{
            "date": date.today().strftime("%Y-%m-%d"),
            "target": target_time.strftime("%H:%M"),
            "actual": actual_time.strftime("%H:%M"),
            "score": final_score,
            "routine_rate": routine_rate
        }])

        df = pd.concat([df, new_data], ignore_index=True)
        # 중복 기록 방지를 위해 동일 날짜는 갱신 처리
        df = df.drop_duplicates(subset=["date"], keep="last")
        df.to_csv(DATA_FILE, index=False)

        st.session_state["saved_now"] = True
        st.session_state["recent_score"] = final_score
        st.session_state["recent_rate"] = routine_rate

with col_right:
    st.markdown(
        """
        <div class="glass-card-premium" style="min-height: 200px;">
            <div class="section-title">📊 실시간 분석 피드백 보고서</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # 방금 저장했거나 세션 상태에 저장 데이터가 있는 경우 메인 리포트 카드 전송
    if "saved_now" in st.session_state and st.session_state["saved_now"]:
        recent_score = st.session_state["recent_score"]
        recent_rate = st.session_state["recent_rate"]
        
        if recent_score >= 90:
            glow_border = "rgba(16, 185, 129, 0.4)"
            accent_color = "#10b981"
            title_msg = "🟢 퍼펙트: 매우 규칙적인 수면 리듬!"
            desc_msg = "목표한 시간에 거의 정확하게 취침하고 수면 루틴도 훌륭하게 완수하셨습니다. 완벽한 바이오리듬이 보장된 하루입니다."
        elif recent_score >= 70:
            glow_border = "rgba(245, 158, 11, 0.4)"
            accent_color = "#f59e0b"
            title_msg = "🟡 보통: 안정성 유지 단계"
            desc_msg = "약간의 취침 격차가 있으나 양호하게 선방하셨습니다. 잠자리에 들기 전 스마트폰 사용 제한율만 높여도 더 가뿐해질 것입니다."
        else:
            glow_border = "rgba(239, 68, 68, 0.4)"
            accent_color = "#ef4444"
            title_msg = "🔴 주의: 수면 불일치 신호 감지"
            desc_msg = "설정한 목표와 실제 누운 시각의 편차가 큽니다. 생체 시계가 무너지지 않도록 취침 목표 타깃을 20분만 앞당겨 실행해 보세요."

        st.markdown(
            f"""
            <div class="glass-card-premium" style="border-color: {glow_border}; box-shadow: 0 0 25px {glow_border};">
                <span style="font-size: 0.85rem; color: #94a3b8; letter-spacing: 1px; display: block;">TODAY'S RECORD</span>
                <h1 style="color: {accent_color}; margin: 0.5rem 0 0.2rem 0; font-size: 3.5rem; font-weight: 800;">{recent_score}점</h1>
                <p style="font-size: 1.05rem; color: #f1f5f9; font-weight: 600; margin-top: 0.5rem;">{title_msg}</p>
                <p style="font-size: 0.88rem; color: #94a3b8; line-height: 1.6; margin-bottom: 0;">{desc_msg}</p>
                <hr style="border-color: rgba(255, 255, 255, 0.08); margin: 1rem 0;">
                <p style="font-size: 0.85rem; color: #c7d2fe; margin: 0;">🎯 당일 루틴 달성 기여 보너스 반영 완료 ({recent_rate}%)</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            """
            <div class="glass-card-premium" style="background: rgba(255, 255, 255, 0.01); text-align: center; padding: 3rem 1.5rem;">
                <span style="font-size: 2.5rem; display: block; margin-bottom: 1rem;">✍️</span>
                <p style="color: #cbd5e1; font-weight: 500; margin-bottom: 0.5rem;">기록 데이터 대기 중</p>
                <p style="color: #64748b; font-size: 0.85rem; line-height: 1.5; margin: 0;">좌측 폼에 오늘의 취침 기록과 미라클 루틴 이행 내역을 채우고 저장 버튼을 눌러주시면 프리미엄 점수 카드가 생성됩니다.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

# 6. 통계 및 누적 시각 차트 (최대 7일간의 루틴 지향 가이드)
if not df.empty:
    st.markdown("---")
    st.markdown(
        """
        <div class="glass-card-premium" style="margin-bottom: 1rem;">
            <div class="section-title">📊 나의 수면 트렌드 분석 (최근 7일 기록)</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    recent_df = df.tail(7).copy()
    
    col_chart, col_table = st.columns([1.2, 0.8])
    
    with col_chart:
        # 차트 예외 처리 및 수면 변동 점수 시각화
        st.line_chart(
            data=recent_df.set_index("date")["score"],
            use_container_width=True,
            height=250
        )
        
    with col_table:
        # 가독성이 높은 반응형 테이블 정밀 배치
        display_df = recent_df[["date", "target", "actual", "score"]].rename(
            columns={
                "date": "날짜",
                "target": "목표 취침",
                "actual": "실제 취침",
                "score": "종합 점수"
            }
        )
        st.dataframe(display_df, use_container_width=True, hide_index=True)

else:
    st.markdown("---")
    st.info("💡 꾸준히 수면 루틴을 기록하시면 이곳에 주간 변동을 보여주는 누적 흐름 통계 차트와 도표가 활성화됩니다.")

st.markdown("<br><hr style='border-color: rgba(255,255,255,0.05);'><br>", unsafe_allow_html=True)

# 7. 명품 하단 푸터 영역
st.markdown(
    """
    <div style="text-align:center; color:#64748b; font-size:0.85rem; padding-bottom:2rem;">
        <p>SnoozeWise Sleep Routine Tracker — 균형 잡힌 규칙성은 숙면을 부르는 가장 위대한 마법입니다.</p>
        <p style="margin-top:0.3rem; font-family:'Playfair Display', serif; font-style:italic; color:#818cf8;">Consistency builds tranquility.</p>
    </div>
    """,
    unsafe_allow_html=True
)
