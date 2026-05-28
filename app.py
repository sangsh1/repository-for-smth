import streamlit as st

# ─── 페이지 설정 ────────────────────────────────────────────────
st.set_page_config(
    page_title="Skibidi Toilet Wiki",
    page_icon="🚽",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── CSS ───────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Share+Tech+Mono&family=Exo+2:wght@400;600;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Exo 2', sans-serif;
    background-color: #0a0a0f;
    color: #d4e8ff;
}
.stApp {
    background: radial-gradient(ellipse at top, #0d1b2a 0%, #0a0a0f 60%);
}

/* 사이드바 */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0d1b2a 0%, #0a0f1a 100%);
    border-right: 1px solid #1e3a5f;
}

/* 헤더 */
.wiki-header {
    background: linear-gradient(135deg, #0d1b2a, #1a0d2e);
    border: 1px solid #1e3a5f;
    border-radius: 16px;
    padding: 32px;
    text-align: center;
    margin-bottom: 24px;
    position: relative;
    overflow: hidden;
}
.wiki-header::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: repeating-linear-gradient(
        45deg,
        transparent,
        transparent 20px,
        rgba(30,90,180,0.03) 20px,
        rgba(30,90,180,0.03) 40px
    );
}
.wiki-title {
    font-family: 'Bebas Neue', cursive;
    font-size: 4rem;
    letter-spacing: 6px;
    background: linear-gradient(90deg, #4fc3f7, #7c4dff, #4fc3f7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin: 0;
}
.wiki-subtitle {
    font-family: 'Share Tech Mono', monospace;
    color: #4fc3f7;
    font-size: 0.85rem;
    letter-spacing: 3px;
    margin-top: 8px;
}

/* 카드 */
.char-card {
    background: linear-gradient(135deg, rgba(13,27,42,0.9), rgba(10,10,20,0.95));
    border: 1px solid #1e3a5f;
    border-radius: 14px;
    padding: 20px;
    margin: 10px 0;
    transition: border-color 0.3s;
}
.char-card:hover {
    border-color: #4fc3f7;
}
.char-name {
    font-family: 'Bebas Neue', cursive;
    font-size: 1.8rem;
    letter-spacing: 3px;
    color: #4fc3f7;
    margin: 0 0 4px 0;
}
.char-faction {
    display: inline-block;
    padding: 3px 12px;
    border-radius: 20px;
    font-size: 0.75rem;
    font-family: 'Share Tech Mono', monospace;
    letter-spacing: 1px;
    margin-bottom: 12px;
}
.faction-alliance {
    background: rgba(79,195,247,0.15);
    border: 1px solid rgba(79,195,247,0.4);
    color: #4fc3f7;
}
.faction-toilet {
    background: rgba(244,67,54,0.15);
    border: 1px solid rgba(244,67,54,0.4);
    color: #ef9a9a;
}
.faction-astro {
    background: rgba(156,39,176,0.15);
    border: 1px solid rgba(156,39,176,0.4);
    color: #ce93d8;
}
.char-desc {
    color: #90aec8;
    font-size: 0.9rem;
    line-height: 1.6;
    margin-bottom: 14px;
}
.ability-tag {
    display: inline-block;
    background: rgba(124,77,255,0.2);
    border: 1px solid rgba(124,77,255,0.4);
    color: #b39ddb;
    border-radius: 6px;
    padding: 3px 10px;
    font-size: 0.75rem;
    margin: 3px 2px;
    font-family: 'Share Tech Mono', monospace;
}

/* 섹션 타이틀 */
.section-header {
    font-family: 'Bebas Neue', cursive;
    font-size: 2rem;
    letter-spacing: 4px;
    color: #4fc3f7;
    border-bottom: 2px solid #1e3a5f;
    padding-bottom: 8px;
    margin: 24px 0 16px 0;
}

/* 에피소드 카드 */
.ep-card {
    background: rgba(13,27,42,0.8);
    border: 1px solid #1e3a5f;
    border-left: 4px solid #4fc3f7;
    border-radius: 0 10px 10px 0;
    padding: 14px 18px;
    margin: 8px 0;
}
.ep-number {
    font-family: 'Share Tech Mono', monospace;
    color: #4fc3f7;
    font-size: 0.8rem;
}
.ep-title {
    font-family: 'Bebas Neue', cursive;
    font-size: 1.2rem;
    color: #d4e8ff;
    letter-spacing: 2px;
}
.ep-desc {
    color: #7899b8;
    font-size: 0.85rem;
    margin-top: 4px;
}

/* 전쟁 현황 바 */
.war-bar-container {
    background: rgba(13,27,42,0.9);
    border: 1px solid #1e3a5f;
    border-radius: 12px;
    padding: 20px;
    margin: 12px 0;
}
.war-bar-label {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.8rem;
    color: #90aec8;
    margin-bottom: 6px;
}
.war-bar-track {
    background: #0a0f1a;
    border-radius: 6px;
    height: 12px;
    overflow: hidden;
    margin-bottom: 4px;
}
.war-bar-fill {
    height: 100%;
    border-radius: 6px;
}

/* 용어 사전 */
.term-card {
    background: rgba(13,27,42,0.6);
    border: 1px solid rgba(30,58,95,0.5);
    border-radius: 10px;
    padding: 14px;
    margin: 8px 0;
}
.term-name {
    font-family: 'Bebas Neue', cursive;
    font-size: 1.2rem;
    color: #7c4dff;
    letter-spacing: 2px;
}
.term-def {
    color: #90aec8;
    font-size: 0.88rem;
    margin-top: 4px;
}

/* stat 뱃지 */
.stat-row {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    margin-top: 10px;
}
.stat-badge {
    background: rgba(10,15,26,0.9);
    border: 1px solid #2a4a6e;
    border-radius: 8px;
    padding: 6px 12px;
    text-align: center;
    min-width: 70px;
}
.stat-val {
    font-family: 'Bebas Neue', cursive;
    font-size: 1.4rem;
    color: #4fc3f7;
}
.stat-lbl {
    font-size: 0.65rem;
    color: #607d9b;
    font-family: 'Share Tech Mono', monospace;
}

/* 사이드바 메뉴 */
.stRadio > label {
    color: #90aec8 !important;
    font-family: 'Share Tech Mono', monospace !important;
}

/* divider */
.divider {
    border: none;
    border-top: 1px solid #1e3a5f;
    margin: 20px 0;
}
</style>
""", unsafe_allow_html=True)


# ─── 데이터 ────────────────────────────────────────────────────
CHARACTERS = {
    "얼라이언스 (The Alliance)": [
        {
            "name": "TITAN CAMERAMAN",
            "emoji": "📷",
            "faction": "alliance",
            "role": "얼라이언스 최강 타이탄",
            "debut": "에피소드 23",
            "status": "🟢 활동 중",
            "desc": "얼라이언스의 가장 강력한 타이탄. 거대한 카메라 머리를 가진 인간형 로봇으로, 파란색 에너지 코어를 지닌다. 원래 업그레이드를 위해 자리를 비웠다가 Episode 50에서 강화된 모습으로 복귀했다. Titan Speakerman을 정화시키고 G-Toilet을 제압한 전투의 핵심 영웅.",
            "abilities": ["🔵 에너지 코어 블라스트", "🔨 기계식 해머", "🧲 중력 건", "✊ 스파이크 주먹"],
            "stats": {"STR": "98", "AGI": "72", "DEF": "90", "INT": "75"},
            "color": "#4fc3f7",
        },
        {
            "name": "TITAN SPEAKERMAN",
            "emoji": "🔊",
            "faction": "alliance",
            "role": "얼라이언스 2번째 타이탄",
            "debut": "에피소드 26",
            "status": "🟢 활동 중 (정화 완료)",
            "desc": "두 번째로 등장한 얼라이언스 타이탄. 가장 빠르고 기동성이 뛰어나지만 세 타이탄 중 원초적 힘은 가장 약하다. Episode 32에서 감염되어 적으로 돌아섰다가 Episode 57에서 정화되었다. 에피소드 진행 중 'Everybody Wants to Rule the World' 음악과 함께 등장.",
            "abilities": ["🚀 제트팩 비행", "📢 사운드웨이브 공격", "⚡ 플라즈마 캐논 (업그레이드)"],
            "stats": {"STR": "82", "AGI": "99", "DEF": "70", "INT": "78"},
            "color": "#ff6b6b",
        },
        {
            "name": "TITAN TV MAN",
            "emoji": "📺",
            "faction": "alliance",
            "role": "얼라이언스 3번째 타이탄",
            "debut": "에피소드 42",
            "status": "🟢 활동 중",
            "desc": "세 번째 타이탄이자 가장 마지막에 참전한 강자. 처음엔 오만하고 거만했지만 점차 동료를 지키는 모습을 보인다. 텔레포트 능력과 에너지 검으로 Chief Scientist Toilet Mech를 단번에 무력화했다. G-Toilet과는 오랜 악연이 있다.",
            "abilities": ["🌀 순간이동", "⚔️ 에너지 블레이드", "📺 데스스크린 공격", "🔋 에너지 충전"],
            "stats": {"STR": "88", "AGI": "85", "DEF": "80", "INT": "95"},
            "color": "#b39ddb",
        },
        {
            "name": "CAMERAMAN",
            "emoji": "🎥",
            "faction": "alliance",
            "role": "얼라이언스 기본 병사",
            "debut": "에피소드 1",
            "status": "🟢 활동 중",
            "desc": "얼라이언스의 가장 기본 병사. 카메라 머리를 가진 인간형 존재들로, 시리즈 처음부터 스키비디 토일렛과 싸워왔다. 다양한 특수 변종(Lucky Cameraman, Cinemaman 등)이 존재한다.",
            "abilities": ["📡 레이저 공격", "🔫 무기 사용", "👊 근접 전투"],
            "stats": {"STR": "55", "AGI": "60", "DEF": "50", "INT": "65"},
            "color": "#4fc3f7",
        },
        {
            "name": "SPEAKERMAN",
            "emoji": "🔈",
            "faction": "alliance",
            "role": "얼라이언스 2군 병사",
            "debut": "에피소드 14",
            "status": "🟢 활동 중",
            "desc": "스피커 머리를 가진 얼라이언스 병사. 음파 공격을 주무기로 사용하며, Camera 군단의 지원군으로 참전했다. 빨간색 스피커를 가진 강화형 개체들도 존재한다.",
            "abilities": ["📢 음파 공격", "💨 스피커 폭발"],
            "stats": {"STR": "60", "AGI": "65", "DEF": "55", "INT": "60"},
            "color": "#ff6b6b",
        },
        {
            "name": "TV MAN",
            "emoji": "📻",
            "faction": "alliance",
            "role": "얼라이언스 3군 병사",
            "debut": "에피소드 42",
            "status": "🟢 활동 중",
            "desc": "TV 머리를 가진 얼라이언스 병사. 데스스크린으로 스키비디 토일렛을 마비시키는 능력이 있다. 단, 토일렛이 선글라스를 발명한 뒤 초반엔 무력해졌다. 전투보다 전략적·기술적 역할을 담당하며 수가 적다.",
            "abilities": ["📺 데스스크린 마비", "🔪 손목 단검", "🌀 텔레포트 (소규모)"],
            "stats": {"STR": "52", "AGI": "70", "DEF": "48", "INT": "90"},
            "color": "#b39ddb",
        },
    ],
    "스키비디 토일렛 (Skibidi Toilets)": [
        {
            "name": "G-TOILET (G-MAN SKIBIDI TOILET)",
            "emoji": "🚽",
            "faction": "toilet",
            "role": "스키비디 토일렛 현 최고 지도자",
            "debut": "에피소드 ~35",
            "status": "🟡 도주 중 / 현재 얼라이언스와 임시 동맹",
            "desc": "Chief Scientist가 사망한 이후 스키비디 토일렛의 사실상 지도자. G-Squad를 이끌고 있다. Episode 71에서 전쟁에서 도주하기 시작했고, 아스트로 토일렛의 위협 앞에 얼라이언스와 임시 동맹을 맺는 복잡한 노선을 걷고 있다.",
            "abilities": ["⚡ 레이저 캐논", "🛡️ 고급 방어력", "💀 기생체 감염"],
            "stats": {"STR": "92", "AGI": "75", "DEF": "88", "INT": "85"},
            "color": "#ef9a9a",
        },
        {
            "name": "CHIEF SCIENTIST SKIBIDI TOILET",
            "emoji": "🔬",
            "faction": "toilet",
            "role": "전(前) 스키비디 총참모장",
            "debut": "에피소드 ~48",
            "status": "🔴 사망 (Titan TV Man에게 격파)",
            "desc": "스키비디 토일렛 군의 최고 과학자이자 전략가. 거대한 메크 슈트를 착용하고 등장했다. Episode 68에서 Titan TV Man에 의해 격파되어 사망. 그의 죽음 이후 토일렛 진영은 크게 약화됐다.",
            "abilities": ["🤖 메크 슈트", "🔫 중화기", "☣️ 기생체 기술"],
            "stats": {"STR": "89", "AGI": "55", "DEF": "91", "INT": "98"},
            "color": "#ef9a9a",
        },
        {
            "name": "NORMAL SKIBIDI TOILET",
            "emoji": "🚽",
            "faction": "toilet",
            "role": "기본 병사",
            "debut": "에피소드 1",
            "status": "🟢 대규모 활동 중",
            "desc": "시리즈의 시작부터 등장하는 기본 스키비디 토일렛. 변기 안에서 머리가 튀어나와 'Skibidi Dop Dop Yes Yes' 노래를 부른다. 혼자서는 약하지만 대규모 군집을 이루며 공격한다.",
            "abilities": ["🎵 스키비디 노래", "💧 물 공격", "🦾 자폭"],
            "stats": {"STR": "30", "AGI": "40", "DEF": "25", "INT": "20"},
            "color": "#ef9a9a",
        },
    ],
    "아스트로 토일렛 (Astro Toilets)": [
        {
            "name": "DETAINER ASTRO TOILET",
            "emoji": "🛸",
            "faction": "astro",
            "role": "아스트로 토일렛 엘리트",
            "debut": "에피소드 51",
            "status": "🟢 현재 주요 위협",
            "desc": "아스트로 토일렛 진영의 강력한 엘리트 유닛. G-Toilet을 추적하는 데 배치되었으나 G-Toilet에게 큰 피해를 입어 후퇴했다. 얼라이언스와 스키비디 토일렛 모두에게 현재 가장 큰 공통 위협이다.",
            "abilities": ["🌌 우주 기동력", "⚡ 고에너지 무기", "🔗 구속/억류 클로"],
            "stats": {"STR": "95", "AGI": "88", "DEF": "93", "INT": "80"},
            "color": "#ce93d8",
        },
    ],
}

EPISODES_KEY = [
    {"num": "EP 1", "title": "시작 — 첫 번째 스키비디 토일렛 출현", "date": "2023.02.07",
     "desc": "거리에서 변기 안 머리가 노래를 부르기 시작한다. 11초짜리 쇼트. 스키비디 세계관의 시작."},
    {"num": "EP 23", "title": "Titan Cameraman 첫 등장", "date": "2023.06",
     "desc": "얼라이언스 최강 타이탄이 전쟁터에 합류. 스키비디 토일렛 군대를 압도하기 시작."},
    {"num": "EP 26", "title": "Titan Speakerman 등장", "date": "2023.07",
     "desc": "'Everybody Wants to Rule the World'와 함께 두 번째 타이탄이 전장에 나타난다."},
    {"num": "EP 32", "title": "Titan Speakerman 감염", "date": "2023.08",
     "desc": "Titan Speakerman이 토일렛 기생체에 감염되어 아군을 공격하기 시작. 최대 위기."},
    {"num": "EP 42", "title": "TV Man 진영 참전", "date": "2023.09",
     "desc": "데스스크린 능력을 지닌 TV Man들이 얼라이언스에 합류. Titan TV Man도 첫 등장."},
    {"num": "EP 51", "title": "아스트로 토일렛 첫 등장", "date": "2023.10",
     "desc": "우주에서 온 더 강력한 신세력 아스트로 토일렛 데뷔. 기존 전쟁 구도를 흔들다."},
    {"num": "EP 57", "title": "Titan Speakerman 정화 성공", "date": "2023.11",
     "desc": "Titan Cameraman이 Titan Speakerman의 기생체를 제거. TV Woman의 도움이 결정적."},
    {"num": "EP 67", "title": "Titan TV Man 화려한 복귀", "date": "2024.01",
     "desc": "부상에서 회복한 Titan TV Man이 업그레이드 후 복귀. Chief Scientist Mech를 순식간에 무력화."},
    {"num": "EP 68", "title": "Chief Scientist 사망", "date": "2024.02",
     "desc": "Titan TV Man이 Chief Scientist Skibidi Toilet Mech를 격파. 토일렛 최고 지휘부 붕괴."},
    {"num": "EP 71", "title": "토일렛 군 도주 — 새로운 국면", "date": "2024.03",
     "desc": "대부분의 스키비디 토일렛이 전쟁을 포기하고 은신. G-Toilet이 잔여 세력 이끌며 도주."},
    {"num": "EP 75+", "title": "얼라이언스 ✕ 토일렛 임시 동맹", "date": "2024.05~",
     "desc": "공통의 적 아스트로 토일렛에 맞서 얼라이언스와 스키비디 토일렛이 손을 잡기 시작."},
]

GLOSSARY = [
    ("수면 사이클", "The Alliance", "카메라맨, 스피커맨, TV맨으로 구성된 스키비디 토일렛에 대항하는 동맹 세력."),
    ("기생체 (Parasite)", "Parasitic Skibidi Toilet", "타이탄 등 강력한 유닛에 붙어 조종하는 소형 스키비디 토일렛. Titan Speakerman 감염에 사용됨."),
    ("G-Squad", "G-Squad", "G-Toilet이 이끄는 스키비디 토일렛의 정예 소대. 대규모 군대 붕괴 후에도 잔존."),
    ("아스트로 토일렛", "Astro Toilets", "Episode 51에 등장한 우주 기원의 신세력. 얼라이언스와 스키비디 토일렛 모두를 위협하는 공통의 적."),
    ("데스스크린", "Death Screen", "TV Man 계열이 사용하는 특수 공격. TV 화면에서 나오는 치명적 광선으로 토일렛을 마비·파괴."),
    ("선글라스", "Skibidi Sunglasses", "토일렛이 TV Man의 데스스크린을 막기 위해 발명한 방어 도구. Episode 43부터 등장."),
    ("Source Filmmaker", "SFM", "이 시리즈 전체가 제작된 Valve의 3D 애니메이션 툴."),
    ("DaFuq!?Boom!", "Creator", "Alexey Gerasimov의 YouTube 채널명이자 시리즈 창작자. 조지아 거주."),
]

# ─── 사이드바 ──────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="text-align:center; padding: 16px 0;">
        <div style="font-family:'Bebas Neue',cursive; font-size:2rem; color:#4fc3f7; letter-spacing:4px;">🚽 SKIBIDI</div>
        <div style="font-family:'Share Tech Mono',monospace; color:#607d9b; font-size:0.7rem; letter-spacing:2px;">TOILET WIKI</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")

    page = st.radio(
        "📂 메뉴",
        ["🏠 홈 / 개요", "👥 등장인물", "📺 주요 에피소드", "⚔️ 전쟁 현황", "📖 용어 사전"],
        label_visibility="collapsed",
    )
    st.markdown("---")
    st.markdown("""
    <div style="font-family:'Share Tech Mono',monospace; color:#2a4a6e; font-size:0.7rem; line-height:1.8;">
    Created by: DaFuq!?Boom!<br>
    플랫폼: YouTube<br>
    첫 공개: 2023.02.07<br>
    에피소드: 79+<br>
    시즌: 26<br>
    제작 툴: Source Filmmaker<br>
    </div>
    """, unsafe_allow_html=True)


# ─── 헤더 ─────────────────────────────────────────────────────
st.markdown("""
<div class="wiki-header">
    <div class="wiki-title">🚽 SKIBIDI TOILET WIKI</div>
    <div class="wiki-subtitle">// THE UNOFFICIAL ENCYCLOPEDIA OF THE SKIBIDI UNIVERSE //</div>
</div>
""", unsafe_allow_html=True)


# ════════════════════════════════════════════
#   홈 / 개요
# ════════════════════════════════════════════
if page == "🏠 홈 / 개요":
    st.markdown('<div class="section-header">OVERVIEW</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        <div class="char-card">
            <div style="font-family:'Bebas Neue',cursive; font-size:1.3rem; color:#4fc3f7; letter-spacing:3px; margin-bottom:10px;">
                📌 시리즈 소개
            </div>
            <div class="char-desc">
                <b style="color:#d4e8ff;">Skibidi Toilet</b>은 Alexey Gerasimov(DaFuq!?Boom!)이 <b>Source Filmmaker</b>로 제작한 유튜브 웹 시리즈입니다.
                2023년 2월 7일 첫 에피소드가 공개된 이후 전 세계 SNS를 강타하며 <b style="color:#4fc3f7;">2024년 7월 기준 유튜브 역대 최다 조회 미디어 1위</b>에 올랐습니다.
                <br><br>
                스토리는 변기에서 머리가 튀어나와 노래를 부르는 <b style="color:#ef9a9a;">스키비디 토일렛</b>과,
                카메라·스피커·TV를 머리에 달고 있는 인간형 로봇 <b style="color:#4fc3f7;">얼라이언스</b>의 전쟁을 중심으로 전개됩니다.
                후반부에는 <b style="color:#ce93d8;">아스트로 토일렛</b>이라는 제3세력이 등장해 판도를 뒤흔들고 있습니다.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="war-bar-container">
            <div style="font-family:'Bebas Neue',cursive; color:#4fc3f7; letter-spacing:3px; margin-bottom:16px;">📊 기본 정보</div>
            <div style="margin-bottom:12px;">
                <div class="war-bar-label">제작자</div>
                <div style="color:#d4e8ff; font-size:0.9rem;">Alexey Gerasimov<br><span style="color:#607d9b;">DaFuq!?Boom!</span></div>
            </div>
            <div style="margin-bottom:12px;">
                <div class="war-bar-label">첫 방영</div>
                <div style="color:#d4e8ff; font-size:0.9rem;">2023년 2월 7일</div>
            </div>
            <div style="margin-bottom:12px;">
                <div class="war-bar-label">총 에피소드</div>
                <div style="color:#4fc3f7; font-family:'Bebas Neue',cursive; font-size:1.8rem;">79+</div>
            </div>
            <div>
                <div class="war-bar-label">시즌</div>
                <div style="color:#4fc3f7; font-family:'Bebas Neue',cursive; font-size:1.8rem;">26</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-header">THREE FACTIONS</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        <div class="char-card" style="border-color:#4fc3f7; text-align:center;">
            <div style="font-size:2.5rem;">📷🔊📺</div>
            <div style="font-family:'Bebas Neue',cursive; font-size:1.4rem; color:#4fc3f7; letter-spacing:3px;">THE ALLIANCE</div>
            <div class="char-desc">카메라맨, 스피커맨, TV맨 + 3명의 타이탄. 스키비디 토일렛의 침공에 맞서 싸우는 주인공 진영.</div>
            <span class="char-faction faction-alliance">PROTAGONISTS</span>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="char-card" style="border-color:#ef9a9a; text-align:center;">
            <div style="font-size:2.5rem;">🚽🚽🚽</div>
            <div style="font-family:'Bebas Neue',cursive; font-size:1.4rem; color:#ef9a9a; letter-spacing:3px;">SKIBIDI TOILETS</div>
            <div class="char-desc">변기에서 머리가 튀어나와 노래를 부르는 군대. 원래 적이었지만 아스트로 토일렛 앞에 얼라이언스와 임시 동맹.</div>
            <span class="char-faction faction-toilet">ANTAGONISTS → ALLY</span>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class="char-card" style="border-color:#ce93d8; text-align:center;">
            <div style="font-size:2.5rem;">🛸🌌🔮</div>
            <div style="font-family:'Bebas Neue',cursive; font-size:1.4rem; color:#ce93d8; letter-spacing:3px;">ASTRO TOILETS</div>
            <div class="char-desc">Episode 51에 등장한 우주 기원 세력. 얼라이언스와 스키비디 토일렛 모두를 압도하는 현재 최대 위협.</div>
            <span class="char-faction faction-astro">NEW THREAT</span>
        </div>
        """, unsafe_allow_html=True)


# ════════════════════════════════════════════
#   등장인물
# ════════════════════════════════════════════
elif page == "👥 등장인물":
    st.markdown('<div class="section-header">CHARACTERS</div>', unsafe_allow_html=True)

    faction_filter = st.selectbox(
        "진영 필터",
        ["전체 보기", "얼라이언스 (The Alliance)", "스키비디 토일렛 (Skibidi Toilets)", "아스트로 토일렛 (Astro Toilets)"],
    )

    factions_to_show = list(CHARACTERS.keys()) if faction_filter == "전체 보기" else [faction_filter]

    for faction_name in factions_to_show:
        if faction_name not in CHARACTERS:
            continue
        chars = CHARACTERS[faction_name]
        st.markdown(f"""
        <div style="font-family:'Bebas Neue',cursive; font-size:1.4rem; color:#607d9b;
                    letter-spacing:3px; margin: 24px 0 12px 0; border-bottom:1px solid #1e3a5f; padding-bottom:6px;">
            ▸ {faction_name}
        </div>
        """, unsafe_allow_html=True)

        for i in range(0, len(chars), 2):
            cols = st.columns(2)
            for j, col in enumerate(cols):
                if i + j < len(chars):
                    c = chars[i + j]
                    faction_class = f"faction-{c['faction']}"
                    abilities_html = "".join(f'<span class="ability-tag">{a}</span>' for a in c["abilities"])
                    stats_html = "".join(
                        f'<div class="stat-badge"><div class="stat-val">{v}</div><div class="stat-lbl">{k}</div></div>'
                        for k, v in c["stats"].items()
                    )
                    with col:
                        st.markdown(f"""
                        <div class="char-card" style="border-left: 4px solid {c['color']};">
                            <div style="display:flex; align-items:center; gap:10px; margin-bottom:8px;">
                                <span style="font-size:2rem;">{c['emoji']}</span>
                                <div>
                                    <div class="char-name" style="color:{c['color']};">{c['name']}</div>
                                    <div style="color:#607d9b; font-size:0.75rem; font-family:'Share Tech Mono',monospace;">{c['role']}</div>
                                </div>
                            </div>
                            <span class="char-faction {faction_class}">{c['faction'].upper()}</span>
                            <span style="font-size:0.75rem; color:#607d9b; margin-left:8px; font-family:'Share Tech Mono',monospace;">
                                첫등장: {c['debut']} · {c['status']}
                            </span>
                            <div class="char-desc" style="margin-top:10px;">{c['desc']}</div>
                            <div style="margin-bottom:10px;">{abilities_html}</div>
                            <div style="font-family:'Share Tech Mono',monospace; font-size:0.7rem; color:#607d9b; margin-bottom:6px;">STATS</div>
                            <div class="stat-row">{stats_html}</div>
                        </div>
                        """, unsafe_allow_html=True)


# ════════════════════════════════════════════
#   주요 에피소드
# ════════════════════════════════════════════
elif page == "📺 주요 에피소드":
    st.markdown('<div class="section-header">KEY EPISODES</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="font-family:'Share Tech Mono',monospace; color:#607d9b; font-size:0.8rem; margin-bottom:20px;">
    // 79개 이상의 에피소드 중 스토리 핵심 전환점 정리 //
    </div>
    """, unsafe_allow_html=True)

    search = st.text_input("🔍 에피소드 검색", placeholder="에피소드 번호 또는 키워드 입력...")

    for ep in EPISODES_KEY:
        if search and search.lower() not in ep["title"].lower() and search.lower() not in ep["num"].lower() and search.lower() not in ep["desc"].lower():
            continue
        st.markdown(f"""
        <div class="ep-card">
            <div class="ep-number">[ {ep['num']} ] · {ep['date']}</div>
            <div class="ep-title">{ep['title']}</div>
            <div class="ep-desc">{ep['desc']}</div>
        </div>
        """, unsafe_allow_html=True)


# ════════════════════════════════════════════
#   전쟁 현황
# ════════════════════════════════════════════
elif page == "⚔️ 전쟁 현황":
    st.markdown('<div class="section-header">WAR STATUS</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="char-card" style="border-color:#ce93d8;">
        <div style="font-family:'Bebas Neue',cursive; font-size:1.2rem; color:#ce93d8; letter-spacing:3px; margin-bottom:10px;">
            🚨 현재 전선 상황 (Episode 75+ 기준)
        </div>
        <div class="char-desc">
            Episode 71 이후 스키비디 토일렛이 전선에서 도주하면서 기존의 <b>얼라이언스 vs 토일렛</b> 구도가 붕괴됐습니다.
            아스트로 토일렛이라는 훨씬 강력한 세력이 등장하여 두 진영 모두를 위협하고 있으며,
            역설적으로 <b style="color:#4fc3f7;">얼라이언스와 스키비디 토일렛이 임시 동맹</b>을 맺는 전황이 전개 중입니다.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<br>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="war-bar-container">
            <div style="font-family:'Bebas Neue',cursive; color:#4fc3f7; letter-spacing:3px; margin-bottom:16px;">📷 THE ALLIANCE</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("**병력 현황**")
        st.progress(72, text="전투력 (상당한 피해 후 회복 중)")
        st.progress(85, text="타이탄 전력 (3타이탄 모두 활동 중)")
        st.progress(60, text="기본 병력 (지속적 손실 발생)")
        st.progress(90, text="기술 수준 (아스트로 기술 역설계 중)")

    with col2:
        st.markdown("""
        <div class="war-bar-container">
            <div style="font-family:'Bebas Neue',cursive; color:#ef9a9a; letter-spacing:3px; margin-bottom:16px;">🚽 SKIBIDI TOILETS</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("**병력 현황**")
        st.progress(35, text="전투력 (대규모 철수 후 잔여 세력)")
        st.progress(20, text="지휘 체계 (Chief Scientist 사망)")
        st.progress(45, text="G-Squad 전력")
        st.progress(30, text="영토 (대부분 상실)")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="war-bar-container" style="border-color: rgba(156,39,176,0.4);">
        <div style="font-family:'Bebas Neue',cursive; color:#ce93d8; letter-spacing:3px; margin-bottom:16px;">🛸 ASTRO TOILETS — 현재 최강 위협</div>
    </div>
    """, unsafe_allow_html=True)
    st.progress(95, text="전투력 (압도적 우위)")
    st.progress(88, text="기술 수준")
    st.progress(80, text="점령지 확장률")

    st.markdown('<div class="section-header">TIMELINE</div>', unsafe_allow_html=True)
    phases = [
        ("1단계", "EP 1~22", "🚽 침공 시작", "스키비디 토일렛이 도시를 점령하기 시작. 카메라맨들이 저항."),
        ("2단계", "EP 23~41", "📷 타이탄 참전", "Titan Cameraman·Speakerman 등장. 얼라이언스 반격 성공."),
        ("3단계", "EP 32~57", "😈 Titan 감염 위기", "Titan Speakerman 감염으로 최대 위기. 결국 정화 성공."),
        ("4단계", "EP 42~67", "📺 TV Man 참전 & 반격", "TV Man 진영 합류, 아스트로 토일렛 출현, Chief Scientist 사망."),
        ("5단계", "EP 71~현재", "🛸 아스트로 위협", "공통의 적 앞에 얼라이언스 ✕ 스키비디 토일렛 임시 동맹."),
    ]
    for phase, eps, title, desc in phases:
        st.markdown(f"""
        <div class="ep-card" style="border-left-color:#7c4dff;">
            <div style="display:flex; justify-content:space-between;">
                <span style="font-family:'Bebas Neue',cursive; color:#7c4dff; letter-spacing:2px;">{phase} · {eps}</span>
            </div>
            <div class="ep-title">{title}</div>
            <div class="ep-desc">{desc}</div>
        </div>
        """, unsafe_allow_html=True)


# ════════════════════════════════════════════
#   용어 사전
# ════════════════════════════════════════════
elif page == "📖 용어 사전":
    st.markdown('<div class="section-header">GLOSSARY</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="font-family:'Share Tech Mono',monospace; color:#607d9b; font-size:0.8rem; margin-bottom:20px;">
    // 스키비디 토일렛 세계관 핵심 용어 정리 //
    </div>
    """, unsafe_allow_html=True)

    search_term = st.text_input("🔍 용어 검색", placeholder="검색어 입력...")

    for _, en_name, definition in GLOSSARY:
        if search_term and search_term.lower() not in en_name.lower() and search_term.lower() not in definition.lower():
            continue
        st.markdown(f"""
        <div class="term-card">
            <div class="term-name">{en_name}</div>
            <div class="term-def">{definition}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-header">QUICK FACTS</div>', unsafe_allow_html=True)
    facts = [
        ("🎵", "스키비디 토일렛이 부르는 노래는 'Give It To Me'와 'Skibidi Dop Dop Yes Yes'의 매쉬업입니다."),
        ("🌍", "시리즈 창작자 Alexey Gerasimov는 러시아 출신이지만 현재 조지아 공화국에 거주합니다."),
        ("📅", "Episode 1~9의 유튜브 설명에는 스키비디 토일렛이 'toilet in ohio'로 표기되어 있었습니다."),
        ("🏆", "2024년 7월 기준, Skibidi Toilet은 유튜브 역대 최다 조회 미디어 1위에 올랐습니다."),
        ("🔵", "얼라이언스 색상: 카메라맨=파란색, 스피커맨=빨간색, TV맨=보라색 에너지."),
        ("💀", "얼라이언스 병사는 머리 유닛이 완전히 파괴되지 않으면 부활할 수 있습니다 (Chunky Salsa Rule)."),
    ]
    for emoji, fact in facts:
        st.markdown(f"""
        <div class="tip-box" style="background:rgba(124,77,255,0.08); border-left:3px solid #7c4dff;
             border-radius: 0 10px 10px 0; padding:14px 18px; margin:8px 0;
             color:#b0bec5; font-size:0.88rem;">
            {emoji} {fact}
        </div>
        """, unsafe_allow_html=True)


# ─── 푸터 ─────────────────────────────────────────────────────
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align:center; font-family:'Share Tech Mono',monospace; color:#2a4a6e; font-size:0.7rem; padding:20px; border-top:1px solid #1e3a5f;">
    SKIBIDI TOILET UNOFFICIAL WIKI · Built with Streamlit · Series by DaFuq!?Boom! (Alexey Gerasimov)<br>
    All characters and content belong to their respective creators.
</div>
""", unsafe_allow_html=True)
