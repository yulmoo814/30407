import streamlit as st

st.set_page_config(
    page_title='이유리의 자기소개',
    page_icon='●',
    layout='wide',
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Noto+Sans+KR:wght@400;500;600;700;800&display=swap');

    :root {
        --ink: #171717;
        --muted: #686866;
        --line: #dededb;
    }

    .stApp {
        background: linear-gradient(180deg, #fafaf8 0%, #f1f1ee 100%);
        color: var(--ink);
        font-family: 'Noto Sans KR', sans-serif;
    }

    [data-testid='stHeader'] { background: transparent; }
    [data-testid='stToolbar'] { right: 1rem; }
    .block-container { max-width: 1040px; padding-top: 3rem; padding-bottom: 4rem; }

    .intro {
        position: relative;
        overflow: hidden;
        padding: clamp(1.6rem, 4vw, 3rem);
        border: 1px solid #171717;
        border-radius: 6px;
        background: #171717;
        color: #fff;
        animation: appear .7s ease-out both;
    }

    [data-testid='stImage'] img {
        border: 1px solid #d5d5d1;
        border-radius: 6px;
        pointer-events: none;
        user-select: none;
        -webkit-user-drag: none;
    }

    .eyebrow {
        color: #bdbdb8;
        font-size: .88rem;
        font-weight: 500;
        letter-spacing: 0;
    }

    .intro h1 {
        margin: .65rem 0 .25rem;
        color: #fff;
        font-family: 'Noto Sans KR', sans-serif;
        font-size: clamp(2.5rem, 6vw, 4rem);
        font-weight: 700;
        letter-spacing: 0;
        line-height: 1.12;
    }

    .intro .subtitle { margin: .8rem 0 1.5rem; color: #d0d0cc; font-size: 1.08rem; }
    .tags { display: flex; flex-wrap: wrap; gap: .55rem; }
    .tag {
        display: inline-block;
        padding: .48rem .85rem;
        border: 1px solid #555;
        border-radius: 3px;
        background: transparent;
        color: #f1f1ef;
        font-size: .9rem;
    }

    .section-title {
        margin: 2.4rem 0 1rem;
        color: var(--ink);
        font-family: 'Noto Sans KR', sans-serif;
        font-size: 1.65rem;
        font-weight: 700;
        letter-spacing: 0;
    }

    .info-card {
        height: 260px;
        padding: 1.35rem 1.45rem;
        box-sizing: border-box;
        border: 1px solid var(--line);
        border-radius: 6px;
        background: rgba(255, 255, 255, .82);
    }

    .info-card .icon { color: #777; font-family: 'DM Sans', sans-serif; font-size: .82rem; font-weight: 700; }
    .info-card h3 { margin: .55rem 0 .4rem; color: var(--ink); font-family: 'Noto Sans KR', sans-serif; font-size: 1.15rem; font-weight: 600; letter-spacing: 0; }
    .info-card h3 a, .info-card [data-testid='stHeaderActionElements'] { display: none !important; }
    .info-card p { margin: 0; color: var(--muted); line-height: 1.7; }

    .note {
        margin-top: 1.4rem;
        padding: 1.2rem 1.4rem;
        border: 1px solid var(--line);
        border-left: 3px solid #171717;
        border-radius: 0 4px 4px 0;
        background: rgba(255, 255, 255, .7);
        color: #454543;
        line-height: 1.8;
    }

    .footer { margin-top: 2.4rem; color: #777773; text-align: center; font-size: .9rem; }

    @keyframes appear {
        from { opacity: 0; transform: translateY(12px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @media (max-width: 640px) {
        .block-container { padding-top: 1.5rem; }
        .info-card { height: auto; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

intro_text, intro_photo = st.columns([2, 0.7])

with intro_text:
    st.markdown(
        """
        <section class="intro">
            <div class="eyebrow"></div>
            <h1>안녕하세요.<br>이유리입니다.</h1>
            <p class="subtitle">배움과 도전을 통해 저만의 진로를 찾아가고 있습니다.</p>
            <div class="tags">
                <span class="tag">경복비즈니스고등학교</span>
                <span class="tag">IT비즈니스과</span>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )

with intro_photo:
    st.image("img/unnamed.jpg", width=260)

st.markdown(
    '<div class="section-title">자기소개</div>',
    unsafe_allow_html=True,
)

first, second, third = st.columns(3)

with first:
    st.markdown(
        """
        <article class="info-card">
            <div class="icon"></div>
            <h3>학교생활</h3>
            <p>경복비즈니스고등학교 IT비즈니스과 3학년에 재학 중입니다. <br>
            다양한 지식과 기술을 익히며 꾸준히 성장하고 있습니다.</p>
        </article>
        """,
        unsafe_allow_html=True,
    )

with second:
    st.markdown(
        """
        <article class="info-card">
            <div class="icon"></div>
            <h3>좋아하는 것</h3>
            <p>음악 감상이 취미입니다. <br>
            좋아하는 음악을 들으며 일상의 여유를 찾고 새로운 에너지를 얻습니다.</p>
        </article>
        """,
        unsafe_allow_html=True,
    )

with third:
    st.markdown(
        """
        <article class="info-card">
            <div class="icon"></div>
            <h3>앞으로의 꿈</h3>
            <p>공무원과 취업을 진로 선택지로 고려하고 있습니다. <br>
            제 적성과 강점을 살릴 수 있는 길을 찾으며 차근차근 준비하고 있습니다.</p>
        </article>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <div class="note">
        <strong>다짐</strong><br>
        작은 경험에서도 배우는 자세를 잃지 않고, 맡은 일은 책임감 있게 완수하겠습니다.<br>
        꾸준히 노력하며 한 걸음씩 성장해 나가겠습니다.
    </div>
    <div class="footer"></div>
    """,
    unsafe_allow_html=True,
)
