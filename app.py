import streamlit as st

st.set_page_config(
    page_title="이한빈의 스키비디 토일렛 위키",
    page_icon="🚽",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic:wght@400;700;800&family=Black+Han+Sans&display=swap');

html, body, .stApp {
    background-color: #0e0e1a !important;
    color: #f0f0ff !important;
    font-family: 'Nanum Gothic', sans-serif !important;
}

section[data-testid="stSidebar"] {
    background: #12122a !important;
    border-right: 2px solid #2e2e6e;
}
section[data-testid="stSidebar"] * { color: #d0d0ff !important; }

h1 { font-family: 'Black Han Sans', cursive !important; font-size: 2.6rem !important;
     color: #7eb3ff !important; letter-spacing: 3px; }
h2 { font-family: 'Black Han Sans', cursive !important; font-size: 1.6rem !important;
     color: #aac8ff !important; }
h3 { font-family: 'Black Han Sans', cursive !important; color: #c8dcff !important; }

/* 탭 */
.stTabs [data-baseweb="tab-list"] { background: #1a1a3a; border-radius: 10px; padding: 4px; gap: 4px; }
.stTabs [data-baseweb="tab"] { background: transparent; color: #9999cc; border-radius: 8px;
    font-family: 'Nanum Gothic', sans-serif; font-weight: 700; }
.stTabs [aria-selected="true"] { background: #2e2e7a !important; color: #aaccff !important; }

/* 입력 */
div[data-baseweb="input"] input {
    background: #1a1a3a !important; color: #d0d0ff !important;
    border: 1px solid #3a3a7a !important; border-radius: 8px !important;
}
div[data-baseweb="select"] > div {
    background: #1a1a3a !important; color: #d0d0ff !important;
    border: 1px solid #3a3a7a !important;
}

.stRadio label { color: #c0c0ee !important; }
.stRadio [data-testid="stMarkdownContainer"] p { color: #c0c0ee !important; }

/* 진행바 */
.stProgress > div > div { background: #2244aa; border-radius: 6px; }
.stProgress > div > div > div { background: linear-gradient(90deg, #4488ff, #88bbff) !important; border-radius: 6px; }

hr { border-color: #2a2a5a !important; }

/* 카드 */
.hanbin-card {
    background: #141430;
    border: 1px solid #2a2a5a;
    border-radius: 14px;
    padding: 20px 22px;
    margin-bottom: 18px;
    position: relative;
    overflow: hidden;
}
.hanbin-card::before {
    content: '';
    position: absolute; top: 0; left: 0;
    width: 4px; height: 100%;
    background: #4477ff;
}
.hanbin-card.toilet::before { background: #ff4444; }
.hanbin-card.alliance::before { background: #44aaff; }
.hanbin-card.neutral::before { background: #ffaa44; }

.char-header { display: flex; align-items: flex-start; gap: 16px; margin-bottom: 12px; }
.char-emoji-box {
    font-size: 3.2rem; width: 72px; height: 72px;
    background: #1e1e40; border-radius: 12px;
    display: flex; align-items: center; justify-content: center; flex-shrink: 0;
}
.char-name { font-family: 'Black Han Sans', cursive; font-size: 1.3rem; color: #c8dcff; margin-bottom: 4px; }
.char-sub { font-size: 0.82rem; color: #6677aa; margin-bottom: 6px; }
.badge {
    display: inline-block; padding: 3px 10px; border-radius: 20px;
    font-size: 0.72rem; font-weight: 800; margin: 2px; letter-spacing: 0.5px;
}
.badge-toilet   { background: #3a0000; border: 1px solid #ff4444; color: #ff9999; }
.badge-alliance { background: #002244; border: 1px solid #4488ff; color: #99ccff; }
.badge-neutral  { background: #2a2000; border: 1px solid #ffaa44; color: #ffdd99; }
.badge-type     { background: #1a1a3a; border: 1px solid #4455aa; color: #99aadd; }
.badge-alive    { background: #002a00; border: 1px solid #44cc44; color: #88ff88; }
.badge-dead     { background: #2a0000; border: 1px solid #cc4444; color: #ff8888; }
.badge-infected { background: #2a1500; border: 1px solid #ff8844; color: #ffcc88; }
.badge-unknown  { background: #1a1a1a; border: 1px solid #888888; color: #bbbbbb; }

.desc-box { background: #0e0e24; border-radius: 10px; padding: 12px 14px;
    font-size: 0.88rem; line-height: 1.75; color: #c0cce8; margin-bottom: 12px; }
.hanbin-quote {
    background: #111128; border-left: 3px solid #4488ff;
    border-radius: 0 8px 8px 0; padding: 10px 14px;
    font-size: 0.85rem; color: #99aacc; font-style: italic; margin-bottom: 12px;
}
.ability-tag {
    display: inline-block; background: #1c2248; border: 1px solid #334499;
    border-radius: 6px; padding: 3px 10px; margin: 3px;
    font-size: 0.78rem; color: #aabbee;
}
.weakness-box {
    background: #1e0e0e; border: 1px solid #551111; border-radius: 8px;
    padding: 8px 12px; font-size: 0.82rem; color: #ff8888; margin-bottom: 10px;
}
.stat-row { margin: 3px 0; }
.stat-label { font-size: 0.78rem; color: #8899bb; display: inline-block; width: 52px; }
.stat-val { font-size: 0.78rem; font-weight: 800; display: inline-block; width: 28px; text-align: right; }
.stat-bar { display: inline-block; height: 7px; border-radius: 4px; vertical-align: middle; margin-left: 6px; }

/* 통계 카드 */
.stat-card {
    background: #141430; border: 1px solid #2a2a5a; border-radius: 12px;
    padding: 16px; text-align: center;
}
.stat-card .num { font-family: 'Black Han Sans', cursive; font-size: 2rem; }
.stat-card .lbl { font-size: 0.8rem; color: #6677aa; margin-top: 2px; }

/* 이한빈 말풍선 */
.hanbin-talk {
    background: #111128; border: 1.5px solid #3355aa;
    border-radius: 14px 14px 14px 2px;
    padding: 14px 18px; margin-bottom: 20px;
    font-size: 0.95rem; line-height: 1.8; color: #c8d8ff;
    position: relative;
}
.hanbin-talk::before {
    content: '🎮 이한빈';
    display: block; font-weight: 800; font-size: 0.8rem;
    color: #7eb3ff; margin-bottom: 6px;
}
.section-title {
    font-family: 'Black Han Sans', cursive;
    font-size: 1.15rem; color: #7eb3ff;
    border-bottom: 2px solid #2a2a5a; padding-bottom: 6px; margin: 20px 0 14px;
}
</style>
""", unsafe_allow_html=True)

# ── 캐릭터 데이터 ──────────────────────────────────────────────────────────────
CHARS = [
    # ══ 토일렛 진영 ══
    dict(
        name="노멀 스키비디 토일렛", emoji="🚽", faction="toilet",
        status="alive", type_="기본 유닛", ep="에피소드 1",
        desc=(
            "변기 위에 사람 머리가 합체된 가장 기본적인 유닛이야. "
            "혼자면 별로 안 무섭지만 수십~수백 마리가 떼로 오면 진짜 답 없음. "
            "시리즈 초반에 카메라맨들을 완전 압도하면서 등장하는데 "
            "그 장면이 진짜 소름이었잖아. 물을 뿜거나 물어뜯는 방식으로 공격함."
        ),
        quote="야 이거 처음 봤을 때 진짜 '이게 뭐야?' 했잖아 ㅋㅋ 근데 무서움.",
        abilities=["물 분사", "물어뜯기", "떼 습격"],
        weakness="카메라맨 플래시·스피커맨 음파",
        stats=dict(공격=30, 방어=20, 속도=50, 지능=10),
    ),
    dict(
        name="라지 스키비디 토일렛", emoji="🚽", faction="toilet",
        status="alive", type_="대형 유닛", ep="에피소드 4",
        desc=(
            "노멀보다 훨씬 크고 육중한 대형 변기야. "
            "강력한 물 분사 공격이랑 돌진으로 카메라맨 여럿을 한 번에 날려버려. "
            "여러 명이 협력해야 겨우 처리할 수 있어서 중반까지 꽤 위협적인 존재임."
        ),
        quote="이 녀석은 덩치로 밀어붙이는 타입이라 카메라맨 둘이서 붙으면 위험함.",
        abilities=["강력한 물 분사", "돌진", "광역 충격"],
        weakness="집중 포화·대형 무기",
        stats=dict(공격=60, 방어=55, 속도=30, 지능=20),
    ),
    dict(
        name="자이언트 스키비디 토일렛", emoji="🏗️", faction="toilet",
        status="alive", type_="초대형 유닛", ep="에피소드 10",
        desc=(
            "건물 맞먹는 크기의 초대형 변기. 등장 자체가 이벤트야. "
            "밟기만 해도 건물이 무너지고 분사 공격 한 방이면 지역 전체가 초토화됨. "
            "G맨이나 타이탄급이 없으면 진짜 답 없는 수준의 위협."
        ),
        quote="이거 처음 나왔을 때 채팅창이 '와' 로 도배됐잖아 진짜 ㅋㅋ",
        abilities=["초대형 분사", "건물 파괴", "지진 발생", "광역 범위 공격"],
        weakness="타이탄급 동맹군·G맨 집중 공격",
        stats=dict(공격=95, 방어=85, 속도=15, 지능=35),
    ),
    dict(
        name="스트롱 스키비디 토일렛", emoji="💪", faction="toilet",
        status="alive", type_="근력 특화형", ep="에피소드 7",
        desc=(
            "근육이 이상하게 발달한 강화형 변기야. "
            "근접 전투에서 카메라맨을 진짜 가볍게 날려버리는 괴력을 가지고 있음. "
            "보기엔 웃기지만 막상 싸우면 진짜 무서운 유닛임."
        ),
        quote="이 녀석 팔뚝 보고 웃다가 카메라맨 날아가는 거 보고 ㄹㅇ 충격받음.",
        abilities=["근접 강타", "던지기", "돌진 박치기"],
        weakness="원거리 집중·스피커맨 음파",
        stats=dict(공격=75, 방어=70, 속도=35, 지능=25),
    ),
    dict(
        name="카무플라주 스키비디 토일렛", emoji="🫥", faction="toilet",
        status="alive", type_="스텔스형", ep="에피소드 12",
        desc=(
            "투명 위장 기능을 가진 은신 특화 유닛. "
            "동맹군 탐지 장비가 없으면 진짜 발견 자체가 불가능해. "
            "기습 공격에 특화되어 있고 단독 침투 임무에 자주 등장함."
        ),
        quote="이거 처음엔 진짜 몰랐음. 갑자기 카메라맨이 날아가는데 원인을 모르는 거야 ㄷㄷ",
        abilities=["투명화", "소음 제거", "기습 공격"],
        weakness="열화상 카메라·음파 탐지기",
        stats=dict(공격=55, 방어=30, 속도=70, 지능=60),
    ),
    dict(
        name="파라슈트 스키비디 토일렛", emoji="🪂", faction="toilet",
        status="alive", type_="공중 강하형", ep="에피소드 8",
        desc=(
            "낙하산을 달고 하늘에서 강하하는 유닛. "
            "하늘에서 갑자기 쏟아지는 방식으로 동맹군 기지를 기습해. "
            "낙하 시 충격으로 주변에 폭발 효과도 생기는 위험한 녀석임."
        ),
        quote="하늘에서 변기가 쏟아진다는 발상 자체가 이미 천재임 ㅋㅋㅋ",
        abilities=["공중 강하", "낙하 충격 폭발", "공중 정찰"],
        weakness="대공 무기·TV맨 레이저",
        stats=dict(공격=45, 방어=35, 속도=65, 지능=40),
    ),
    dict(
        name="제트팩 스키비디 토일렛", emoji="🚀", faction="toilet",
        status="alive", type_="비행 전투형", ep="에피소드 13",
        desc=(
            "제트팩으로 자유롭게 비행하는 고기동 유닛. "
            "빠른 속도로 동맹군 진형을 교란하고 공중에서 폭격하는 방식으로 싸워. "
            "속도가 빨라서 따라잡기도 진짜 힘들다고."
        ),
        quote="이 녀석은 진짜 빠름. 도망가는 건지 공격하는 건지 구분도 안 됨.",
        abilities=["고속 비행", "공중 폭격", "기동 회피"],
        weakness="대공 미사일·G맨 공중전",
        stats=dict(공격=60, 방어=40, 속도=85, 지능=45),
    ),
    dict(
        name="탱크 스키비디 토일렛", emoji="🛡️", faction="toilet",
        status="alive", type_="중장갑형", ep="에피소드 16",
        desc=(
            "두꺼운 장갑판을 두른 요새 같은 변기야. "
            "포탑까지 달려있어서 원거리 포격도 가능하고 정면 돌파 전술에 완전 특화됨. "
            "내구성이 말도 안 되게 높아서 왠만한 공격은 그냥 씹어버림."
        ),
        quote="이건 진짜 포탄 맞아도 멀쩡히 걸어오는 거 보고 '아 이거 답없다' 생각했음.",
        abilities=["장갑 방어", "포탑 사격", "돌격 돌파"],
        weakness="EMP 공격·강력한 폭발물",
        stats=dict(공격=80, 방어=90, 속도=20, 지능=30),
    ),
    dict(
        name="보스 스키비디 토일렛", emoji="👑", faction="toilet",
        status="alive", type_="총사령관", ep="에피소드 20",
        desc=(
            "스키비디 토일렛 군단 전체를 지휘하는 두뇌이자 최강 유닛. "
            "막대한 에너지 폭발 공격, 재생 능력, 텔레포트를 모두 보유하고 있어. "
            "다른 유닛들을 원격으로 강화시키기도 하고 "
            "G맨·TV맨이 아니면 진짜 상대 자체가 안 되는 레벨임."
        ),
        quote="이 녀석이 나오는 에피소드는 긴장감이 진짜 달라. 존재감이 다름.",
        abilities=["에너지 폭발", "재생 능력", "유닛 강화", "텔레포트", "심리 지배"],
        weakness="G맨·TV맨 동시 공격",
        stats=dict(공격=92, 방어=88, 속도=50, 지능=95),
    ),
    dict(
        name="스파이더 스키비디 토일렛", emoji="🕷️", faction="toilet",
        status="alive", type_="거미형 특수체", ep="에피소드 18",
        desc=(
            "거미 다리를 달고 벽이랑 천장을 자유롭게 이동하는 특수 유닛이야. "
            "복잡한 건물 안에서 특히 무서운데 거미줄로 적을 묶어버리고 "
            "독 공격까지 가능해서 장기전에서 진짜 짜증나는 상대임."
        ),
        quote="천장에서 뚝 떨어지는 거 보고 진짜 소름 돋았잖아. 공포물이냐고 ㄷㄷ",
        abilities=["벽·천장 이동", "거미줄 속박", "독 공격"],
        weakness="불·폭발물·넓은 공간",
        stats=dict(공격=55, 방어=45, 속도=75, 지능=50),
    ),
    dict(
        name="로봇 스키비디 토일렛", emoji="🤖", faction="toilet",
        status="alive", type_="기계 강화형", ep="에피소드 19",
        desc=(
            "기계 부품으로 온몸을 강화한 사이보그 변기. "
            "금속 장갑이랑 기계 팔 덕분에 내구성이 비약적으로 올랐고 "
            "자가 수리 기능도 있어서 왠만해서는 파괴가 안 돼."
        ),
        quote="부수면 수리하고 또 부수면 또 수리하고... TV맨 EMP 없으면 진짜 귀찮음.",
        abilities=["자가 수리", "기계 팔 공격", "중장갑"],
        weakness="EMP·TV맨 전자기 공격",
        stats=dict(공격=70, 방어=80, 속도=30, 지능=55),
    ),
    dict(
        name="사이보그 스키비디 토일렛", emoji="⚙️", faction="toilet",
        status="alive", type_="풀 사이보그형", ep="에피소드 21",
        desc=(
            "생체와 기계를 완전히 합체시킨 최첨단 유닛이야. "
            "레이저 눈, 로켓 추진, 자폭 장치까지 모두 갖추고 있어서 "
            "다양한 상황에 다 대응 가능한 올라운더 타입임."
        ),
        quote="이거 어떻게 잡냐 진짜... 각도마다 다른 무기 꺼내는 게 말이 됩니까.",
        abilities=["레이저 눈", "로켓 추진 돌격", "자폭 공격"],
        weakness="G맨·타이탄급 동맹군",
        stats=dict(공격=82, 방어=75, 속도=60, 지능=70),
    ),

    # ══ 동맹군 진영 ══
    dict(
        name="카메라맨", emoji="📷", faction="alliance",
        status="alive", type_="기본 전투원", ep="에피소드 1",
        desc=(
            "머리에 카메라를 달고 싸우는 동맹군의 기본 병사야. "
            "카메라 플래시로 스키비디 토일렛을 약화시키거나 직접 타격도 가능해. "
            "시리즈 내내 꾸준히 활약하는 진짜 주인공 같은 존재임."
        ),
        quote="카메라맨이 동맹군 핵심이지. 업그레이드될수록 점점 강해지는 성장형 캐릭터야.",
        abilities=["카메라 플래시", "근접 타격", "팀 전술 조율"],
        weakness="대형 토일렛·감염 바이러스",
        stats=dict(공격=45, 방어=40, 속도=55, 지능=60),
    ),
    dict(
        name="업그레이드 카메라맨", emoji="🔭", faction="alliance",
        status="alive", type_="강화 전투원", ep="에피소드 9",
        desc=(
            "기본 카메라맨이 각종 장비로 강화된 버전이야. "
            "레이저 조준경, 방호 장갑, 고출력 플래시를 달고 화력이 크게 올랐어. "
            "중반부 동맹군의 주력 전투원 역할을 담당함."
        ),
        quote="업글 카메라맨 나오고 나서 동맹군 전투력이 확 올라갔잖아. 변화점이 여기야.",
        abilities=["레이저 조준", "강화 플래시", "장갑 방어"],
        weakness="대형·탱크 토일렛 집중 공격",
        stats=dict(공격=58, 방어=60, 속도=50, 지능=65),
    ),
    dict(
        name="스피커맨", emoji="🔊", faction="alliance",
        status="alive", type_="음파 전투원", ep="에피소드 3",
        desc=(
            "머리에 스피커를 달고 강력한 음파와 초음파로 싸우는 전사야. "
            "카메라맨보다 전투력이 한 수 위이고 넓은 범위를 동시에 공격할 수 있어. "
            "음파 폭발은 토일렛한테 유독 효과적임."
        ),
        quote="스피커맨 음파 터지는 거 보면 진짜 시원하잖아. 속이 다 뻥 뚫림 ㅋㅋ",
        abilities=["음파 공격", "초음파 폭발", "방어막 생성"],
        weakness="대형 토일렛·보스급 유닛",
        stats=dict(공격=65, 방어=55, 속도=50, 지능=65),
    ),
    dict(
        name="TV맨", emoji="📺", faction="alliance",
        status="alive", type_="엘리트 전사", ep="에피소드 6",
        desc=(
            "머리에 TV를 달고 있는 동맹군 최고 엘리트 전사야. "
            "레이저 빔, 텔레포트, EMP 공격까지 다 갖추고 있어. "
            "G맨이랑 함께 동맹군 양대 에이스로 불리는 존재임. "
            "전략적 사고도 뛰어나서 작전 지휘도 함."
        ),
        quote="TV맨 레이저 한 방에 중형 토일렛 여럿 관통하는 거 볼 때마다 소름 ㄷㄷ",
        abilities=["레이저 빔", "텔레포트", "EMP", "전장 분석"],
        weakness="보스 스키비디 토일렛·감염",
        stats=dict(공격=85, 방어=75, 속도=80, 지능=90),
    ),
    dict(
        name="G맨", emoji="🕶️", faction="alliance",
        status="alive", type_="최강 전사", ep="에피소드 15",
        desc=(
            "선글라스 하나가 트레이드마크인 동맹군 절대 에이스야. "
            "물리적 힘, 에너지 공격, 비행 능력을 모두 갖추고 있고 "
            "보스급 토일렛이랑 1:1이 가능한 유일한 존재임. "
            "등장만으로 전세가 바뀌는 진짜 게임 체인저."
        ),
        quote="G맨 나오는 순간 다 됐다 싶잖아. 그냥 다 됨. 무조건 이김.",
        abilities=["에너지 폭발", "비행", "초강력 근접 전투", "보호막"],
        weakness="특수 감염 바이러스·집중 포화",
        stats=dict(공격=98, 방어=92, 속도=88, 지능=85),
    ),
    dict(
        name="타이탄 카메라맨", emoji="🤖", faction="alliance",
        status="alive", type_="타이탄급", ep="에피소드 25",
        desc=(
            "카메라맨이 도시 블록 크기로 강화된 타이탄 유닛이야. "
            "자이언트 토일렛이랑 맞짱 뜰 수 있는 규모로 "
            "광선 한 방에 건물이 날아가고 주먹 한 방에 지면이 갈라짐. "
            "동맹군이 열세일 때 등장해서 전세를 뒤집는 역할을 함."
        ),
        quote="이 장면 처음 봤을 때 '드디어!'라고 소리 질렀잖아 ㅋㅋ 완전 카타르시스",
        abilities=["초대형 카메라 광선", "지면 충격파", "근접 초강타"],
        weakness="타이탄급 토일렛·보스 집중 공격",
        stats=dict(공격=96, 방어=90, 속도=20, 지능=70),
    ),
    dict(
        name="타이탄 TV맨", emoji="📡", faction="alliance",
        status="alive", type_="타이탄급", ep="에피소드 27",
        desc=(
            "TV맨이 타이탄 수준으로 각성한 형태야. "
            "광역 레이저 폭격이랑 차원 이동 능력이 극대화되어서 "
            "전장 전체를 혼자 통제하는 수준의 압도적인 전투력을 가졌어."
        ),
        quote="타이탄 TV맨이랑 타이탄 카메라맨 같이 나오는 씬은 진짜 영화임.",
        abilities=["광역 레이저 폭격", "차원 이동", "전장 통제", "EMP 광역"],
        weakness="보스 스키비디 토일렛",
        stats=dict(공격=97, 방어=89, 속도=75, 지능=96),
    ),
    dict(
        name="타이탄 스피커맨", emoji="📣", faction="alliance",
        status="alive", type_="타이탄급", ep="에피소드 29",
        desc=(
            "스피커맨이 타이탄 수준으로 성장한 형태야. "
            "초음파 광역 공격으로 넓은 범위의 토일렛을 동시에 파괴할 수 있어. "
            "그 울림이 수 킬로미터 밖에서도 느껴진다는 설정이 있음."
        ),
        quote="이 소리 들리면 토일렛 입장에서는 진짜 공포겠다 ㄷㄷ",
        abilities=["광역 초음파", "음파 충격파", "광역 방어막"],
        weakness="타이탄 토일렛·특수 방음 장갑",
        stats=dict(공격=93, 방어=87, 속도=55, 지능=80),
    ),

    # ══ 중립·특수 ══
    dict(
        name="감염된 카메라맨", emoji="😈", faction="neutral",
        status="infected", type_="감염체", ep="에피소드 11",
        desc=(
            "토일렛 진영에 감염되어 적으로 돌아선 카메라맨이야. "
            "아군인 척 위장하고 내부에서 사보타주하거나 기습할 수 있어서 "
            "진짜 무서운 게 외형상으로는 구분이 잘 안 됨."
        ),
        quote="이게 진짜 충격이었어. 아군이 갑자기 내 카메라맨 때리는 거 보고 '아 이건 반칙이다' 했잖아.",
        abilities=["위장 침투", "내부 사보타주", "아군 혼란 유발"],
        weakness="G맨 식별·정화 장치",
        stats=dict(공격=55, 방어=40, 속도=55, 지능=70),
    ),
    dict(
        name="사이렌 헤드 변형체", emoji="🚨", faction="neutral",
        status="unknown", type_="사이렌형 특수체", ep="에피소드 22",
        desc=(
            "사이렌 소리를 내는 변형 스키비디 토일렛. "
            "귀를 찢는 경보음으로 동맹군을 마비시키고 주변 유리를 모두 산산조각 냄. "
            "정확한 소속이 불분명해서 더 미스터리한 존재야."
        ),
        quote="이 소리 유튜브로 들었을 때 헤드셋 낀 상태라 진짜 귀 죽는 줄 알았음.",
        abilities=["경보음 마비", "유리 파괴 음파", "공포 유발"],
        weakness="방음 장비·스피커맨 역음파",
        stats=dict(공격=65, 방어=50, 속도=40, 지능=45),
    ),
]

FACTION_INFO = {
    "toilet":   ("🚽 스키비디 토일렛", "badge-toilet"),
    "alliance": ("🤝 동맹군",          "badge-alliance"),
    "neutral":  ("❓ 중립·특수",       "badge-neutral"),
}
STATUS_INFO = {
    "alive":    ("● 생존",  "badge-alive"),
    "dead":     ("✖ 사망",  "badge-dead"),
    "infected": ("⚠ 감염", "badge-infected"),
    "unknown":  ("? 불명",  "badge-unknown"),
}
STAT_COLORS = {
    "공격": "#ff6644", "방어": "#44aaff", "속도": "#44ff88", "지능": "#ffdd44"
}

def stat_inline(name, val):
    color = STAT_COLORS.get(name, "#88aaff")
    bar_w = int(val * 1.5)
    return (
        f'<div class="stat-row">'
        f'<span class="stat-label">{name}</span>'
        f'<span class="stat-val" style="color:{color};">{val}</span>'
        f'<span class="stat-bar" style="width:{bar_w}px;background:{color};opacity:0.8;"></span>'
        f'</div>'
    )

def render_char(c):
    fl, fc = FACTION_INFO.get(c["faction"], ("?", "badge-neutral"))
    sl, sc = STATUS_INFO.get(c["status"], ("?", "badge-unknown"))
    cards_cls = c["faction"]

    abilities_html = "".join(f'<span class="ability-tag">{a}</span>' for a in c["abilities"])
    stats_html = "".join(stat_inline(k, v) for k, v in c["stats"].items())

    st.markdown(f"""
<div class="hanbin-card {cards_cls}">
  <div class="char-header">
    <div class="char-emoji-box">{c['emoji']}</div>
    <div style="flex:1;">
      <div class="char-name">{c['name']}</div>
      <div class="char-sub">첫 등장: {c['ep']}</div>
      <div>
        <span class="badge {fc}">{fl}</span>
        <span class="badge {sc}">{sl}</span>
        <span class="badge badge-type">{c['type_']}</span>
      </div>
    </div>
  </div>

  <div class="hanbin-talk">{c['quote']}</div>
  <div class="desc-box">{c['desc']}</div>

  <div class="section-title">⚔️ 보유 능력</div>
  <div style="margin-bottom:12px;">{abilities_html}</div>

  <div class="weakness-box">💀 약점: {c['weakness']}</div>

  <div class="section-title">📊 스탯</div>
  <div style="columns:2;column-gap:20px;">{stats_html}</div>
</div>
""", unsafe_allow_html=True)

# ── 사이드바 ─────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
<div style='text-align:center;padding:16px 0 8px;'>
  <div style='font-size:2.8rem;'>🚽</div>
  <div style='font-family:"Black Han Sans",cursive;font-size:1.3rem;color:#7eb3ff;letter-spacing:2px;'>이한빈의<br>스키비디 위키</div>
</div>
<hr style='border-color:#2a2a5a;margin:10px 0;'/>
""", unsafe_allow_html=True)

    search = st.text_input("🔍 캐릭터 검색", placeholder="예: 카메라맨")

    st.markdown("#### 진영 필터")
    faction_map = {"전체": "all", "🚽 토일렛 진영": "toilet",
                   "🤝 동맹군": "alliance", "❓ 중립·특수": "neutral"}
    sel_faction = faction_map[st.radio("진영", list(faction_map.keys()), label_visibility="collapsed")]

    st.markdown("#### 상태 필터")
    status_map = {"전체": "all", "생존": "alive", "감염": "infected", "불명": "unknown"}
    sel_status = status_map[st.selectbox("상태", list(status_map.keys()), label_visibility="collapsed")]

    st.markdown("---")
    st.markdown("""
<div style='font-size:0.76rem;color:#444466;text-align:center;line-height:1.7;'>
  DaFuq!?Boom! 유튜브 시리즈<br>이한빈 비공식 팬 위키<br>
  <span style='color:#223355;'>★ 내용은 팬 해석 포함 ★</span>
</div>
""", unsafe_allow_html=True)

# ── 헤더 ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center;padding:24px 0 6px;">
  <div style="font-family:'Black Han Sans',cursive;font-size:2.8rem;color:#7eb3ff;letter-spacing:3px;line-height:1.2;">
    🚽 스키비디 토일렛 위키
  </div>
  <div style="color:#445588;font-size:1rem;margin-top:6px;">
    이한빈이 직접 설명해주는 완전 정복 도감
  </div>
</div>
""", unsafe_allow_html=True)

# 이한빈 인트로 멘트
st.markdown("""
<div class="hanbin-talk" style="margin:16px 0 24px;">
야 안녕~ 나 이한빈이야! 오늘은 스키비디 토일렛 시리즈 등장인물들을 내가 직접 하나하나 다 설명해줄게.
진짜 내가 에피소드 다 보면서 정리한 거니까 믿어도 됨 ㅋㅋ
왼쪽에서 진영이랑 상태 필터 쓰면 원하는 캐릭터만 볼 수 있어. 그럼 시작해볼까?
</div>
""", unsafe_allow_html=True)

# ── 통계 ──────────────────────────────────────────────────────────────────────
t_cnt = sum(1 for c in CHARS if c["faction"] == "toilet")
a_cnt = sum(1 for c in CHARS if c["faction"] == "alliance")
n_cnt = sum(1 for c in CHARS if c["faction"] == "neutral")

c1, c2, c3, c4 = st.columns(4)
for col, num, lbl, color in [
    (c1, len(CHARS), "전체 캐릭터", "#7eb3ff"),
    (c2, t_cnt,      "🚽 토일렛 진영", "#ff6666"),
    (c3, a_cnt,      "🤝 동맹군",     "#66aaff"),
    (c4, n_cnt,      "❓ 중립·특수", "#ffaa44"),
]:
    col.markdown(
        f'<div class="stat-card"><div class="num" style="color:{color};">{num}</div>'
        f'<div class="lbl">{lbl}</div></div>',
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)

# ── 탭 ────────────────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4 = st.tabs(["🚽 전체 도감", "💀 토일렛 진영", "🤝 동맹군 진영", "❓ 중립·특수"])

def filtered(faction_filter):
    result = CHARS
    if search:
        result = [c for c in result if search.lower() in c["name"].lower()]
    if sel_faction != "all":
        result = [c for c in result if c["faction"] == sel_faction]
    else:
        if faction_filter != "all":
            result = [c for c in result if c["faction"] == faction_filter]
    if sel_status != "all":
        result = [c for c in result if c["status"] == sel_status]
    return result

with tab1:
    chars = filtered("all")
    st.markdown(f'<p style="color:#445588;font-size:0.88rem;margin-bottom:12px;">총 <strong style="color:#7eb3ff">{len(chars)}</strong>명 표시</p>', unsafe_allow_html=True)
    if not chars:
        st.warning("조건에 맞는 캐릭터가 없어. 필터를 바꿔봐!")
    for c in chars:
        render_char(c)

with tab2:
    st.markdown("""
<div class="hanbin-talk">
토일렛 진영 정리야. 이쪽이 사실상 빌런인데 진짜 다양하게 진화하면서 점점 강해지는 게 이 시리즈의 재미임!
</div>
""", unsafe_allow_html=True)
    chars = [c for c in CHARS if c["faction"] == "toilet"]
    if search:
        chars = [c for c in chars if search.lower() in c["name"].lower()]
    if sel_status != "all":
        chars = [c for c in chars if c["status"] == sel_status]
    for c in chars:
        render_char(c)

with tab3:
    st.markdown("""
<div class="hanbin-talk">
동맹군이야! 처음엔 많이 밀리다가 업그레이드되면서 점점 강해지는 성장 서사가 있어서 보는 맛이 있음.
</div>
""", unsafe_allow_html=True)
    chars = [c for c in CHARS if c["faction"] == "alliance"]
    if search:
        chars = [c for c in chars if search.lower() in c["name"].lower()]
    if sel_status != "all":
        chars = [c for c in chars if c["status"] == sel_status]
    for c in chars:
        render_char(c)

with tab4:
    st.markdown("""
<div class="hanbin-talk">
이쪽은 소속이 좀 애매하거나 특수한 케이스들이야. 감염된 캐릭터나 불명인 존재들인데 이게 또 스토리에서 중요한 포인트가 됨.
</div>
""", unsafe_allow_html=True)
    chars = [c for c in CHARS if c["faction"] == "neutral"]
    if search:
        chars = [c for c in chars if search.lower() in c["name"].lower()]
    if sel_status != "all":
        chars = [c for c in chars if c["status"] == sel_status]
    for c in chars:
        render_char(c)

# ── 푸터 ──────────────────────────────────────────────────────────────────────
st.markdown("""
<hr style="border-color:#1a1a3a;margin-top:40px;"/>
<div style="text-align:center;color:#2a2a4a;font-size:0.78rem;padding:12px 0;">
  이한빈의 스키비디 토일렛 위키 · 비공식 팬 제작 · 원작: DaFuq!?Boom!
</div>
""", unsafe_allow_html=True)
