import streamlit as st
import random
import hashlib
import time

st.set_page_config(
    page_title="💘 Match de Almas | Encuentra tu Match",
    page_icon="💘",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ============ CSS DISEÑO PREMIUM / VIRAL ============
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    .stApp {
        background: radial-gradient(circle at 0% 0%, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    }
    
    /* Fondo animado de partículas (estilo disco) */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: radial-gradient(rgba(255,255,255,0.08) 1px, transparent 1px);
        background-size: 40px 40px;
        pointer-events: none;
        z-index: 0;
    }
    
    .main-title {
        text-align: center;
        background: linear-gradient(135deg, #FF6B6B, #FF8E53, #FF6B6B);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 0;
        text-shadow: 0 0 30px rgba(255,107,107,0.5);
        letter-spacing: -0.5px;
        animation: glow 2s ease-in-out infinite alternate;
    }
    
    @keyframes glow {
        from { text-shadow: 0 0 10px #FF6B6B; }
        to { text-shadow: 0 0 30px #FF8E53, 0 0 40px #FF6B6B; }
    }
    
    .subtitle {
        text-align: center;
        color: rgba(255,255,255,0.8);
        margin-bottom: 2rem;
        font-size: 0.9rem;
        font-weight: 300;
    }
    
    .badge-neon {
        background: linear-gradient(135deg, #FF6B6B, #FF8E53);
        color: white;
        padding: 0.4rem 1.2rem;
        border-radius: 40px;
        display: inline-block;
        font-size: 0.7rem;
        font-weight: 600;
        margin-bottom: 1rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 0 20px rgba(255,107,107,0.4);
    }
    
    .question-card {
        background: rgba(255,255,255,0.08);
        backdrop-filter: blur(20px);
        border-radius: 32px;
        padding: 2rem 1.5rem;
        margin: 1.5rem 0;
        border: 1px solid rgba(255,255,255,0.15);
        box-shadow: 0 25px 45px rgba(0,0,0,0.3), 0 0 30px rgba(255,107,107,0.2);
        transition: all 0.3s ease;
    }
    
    .question-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 30px 55px rgba(0,0,0,0.4), 0 0 40px rgba(255,107,107,0.3);
    }
    
    .question-text {
        font-size: 1.4rem;
        font-weight: 700;
        color: white;
        margin-bottom: 0.5rem;
        text-align: center;
        background: linear-gradient(135deg, #fff, #FFD6A5);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
    }
    
    .question-icon {
        font-size: 2.5rem;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    .option-btn {
        width: 100%;
        padding: 0.9rem;
        margin: 0.6rem 0;
        border-radius: 60px;
        border: none;
        background: rgba(255,255,255,0.1);
        color: white;
        font-weight: 500;
        font-size: 1rem;
        text-align: center;
        transition: all 0.3s ease;
        cursor: pointer;
        backdrop-filter: blur(5px);
        border: 1px solid rgba(255,255,255,0.1);
    }
    
    .option-btn:hover {
        background: linear-gradient(135deg, #FF6B6B, #FF8E53);
        transform: scale(1.02);
        box-shadow: 0 10px 25px rgba(255,107,107,0.4);
        border: 1px solid rgba(255,255,255,0.3);
    }
    
    .match-card {
        background: linear-gradient(135deg, rgba(255,255,255,0.12), rgba(255,255,255,0.05));
        backdrop-filter: blur(15px);
        border-radius: 28px;
        padding: 1.2rem;
        margin: 0.8rem 0;
        border: 1px solid rgba(255,107,107,0.3);
        transition: all 0.3s ease;
        cursor: pointer;
    }
    
    .match-card:hover {
        transform: translateX(8px);
        border-color: #FF6B6B;
        box-shadow: 0 0 25px rgba(255,107,107,0.3);
    }
    
    .match-percent {
        font-size: 2rem;
        font-weight: 800;
        background: linear-gradient(135deg, #FF6B6B, #FF8E53);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
    }
    
    .profile-link {
        background: #1877F2;
        color: white;
        padding: 0.45rem 1rem;
        border-radius: 40px;
        text-decoration: none;
        display: inline-block;
        margin: 0.2rem;
        font-size: 0.75rem;
        font-weight: 500;
        transition: all 0.2s;
    }
    
    .profile-link:hover {
        transform: scale(1.05);
        background: #0d6bdf;
    }
    
    .instagram-link {
        background: linear-gradient(45deg, #f09433, #d62976, #962fbf);
        color: white;
        padding: 0.45rem 1rem;
        border-radius: 40px;
        text-decoration: none;
        display: inline-block;
        margin: 0.2rem;
        font-size: 0.75rem;
        font-weight: 500;
    }
    
    .instagram-link:hover {
        transform: scale(1.05);
    }
    
    .result-card {
        background: linear-gradient(135deg, rgba(255,255,255,0.15), rgba(255,255,255,0.05));
        backdrop-filter: blur(20px);
        border-radius: 40px;
        padding: 2rem;
        text-align: center;
        border: 1px solid rgba(255,107,107,0.4);
        box-shadow: 0 20px 40px rgba(0,0,0,0.3);
    }
    
    .result-emoji {
        font-size: 4.5rem;
        animation: bounce 0.6s ease;
    }
    
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-15px); }
    }
    
    .result-title {
        font-size: 1.8rem;
        font-weight: 800;
        margin: 0.5rem 0;
    }
    
    .progress-bar-container {
        background: rgba(255,255,255,0.15);
        border-radius: 30px;
        height: 10px;
        overflow: hidden;
    }
    
    .progress-fill {
        background: linear-gradient(90deg, #FF6B6B, #FF8E53);
        width: 0%;
        height: 100%;
        border-radius: 30px;
        transition: width 0.3s ease;
    }
    
    .progress-text {
        text-align: center;
        color: rgba(255,255,255,0.7);
        margin: 0.5rem 0;
        font-size: 0.8rem;
    }
    
    .code-badge {
        background: linear-gradient(135deg, #FF6B6B, #FF8E53);
        padding: 0.8rem 1.5rem;
        border-radius: 60px;
        display: inline-block;
        font-weight: 700;
        letter-spacing: 2px;
        font-size: 1.3rem;
        color: white;
    }
    
    .share-btn-wa {
        background: #25D366;
        color: white;
        padding: 0.9rem;
        border-radius: 60px;
        text-decoration: none;
        display: block;
        text-align: center;
        font-weight: 700;
        transition: all 0.2s;
    }
    
    .share-btn-wa:hover {
        transform: scale(1.02);
        background: #128C7E;
    }
    
    .share-btn-ig {
        background: linear-gradient(45deg, #f09433, #d62976, #962fbf);
        color: white;
        padding: 0.9rem;
        border-radius: 60px;
        text-decoration: none;
        display: block;
        text-align: center;
        font-weight: 700;
    }
    
    .footer {
        text-align: center;
        color: rgba(255,255,255,0.4);
        margin-top: 2rem;
        font-size: 0.7rem;
    }
    
    hr {
        border-color: rgba(255,255,255,0.1);
    }
    
    /* Inputs personalizados */
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input,
    .stTextArea > div > textarea {
        background: rgba(255,255,255,0.1) !important;
        border: 1px solid rgba(255,255,255,0.2) !important;
        border-radius: 30px !important;
        color: white !important;
        padding: 0.7rem 1rem !important;
    }
    
    .stTextInput label, .stNumberInput label, .stTextArea label {
        color: rgba(255,255,255,0.8) !important;
    }
</style>
""", unsafe_allow_html=True)

# ============ BANCO DE PREGUNTAS ============
preguntas = [
    {"pregunta": "🎵 ¿Qué género musical prefieres?", "icono": "🎵", "opciones": ["Reggaetón", "Rock", "Pop", "Corridos/Banda", "Electrónica", "Indie"]},
    {"pregunta": "🍕 ¿Cuál es tu comida favorita?", "icono": "🍕", "opciones": ["Pizza", "Tacos", "Sushi", "Hamburguesas", "Comida china", "Pasta"]},
    {"pregunta": "📺 ¿Qué tipo de series ves?", "icono": "📺", "opciones": ["Drama", "Comedia", "Terror", "Ciencia ficción", "Romance", "Documentales"]},
    {"pregunta": "🌍 ¿Qué harías con $10,000?", "icono": "💰", "opciones": ["Viajar", "Invertir", "Comprar ropa", "Comprar tecnología", "Fiesta", "Ahorrar"]},
    {"pregunta": "🐕 ¿Mascota favorita?", "icono": "🐕", "opciones": ["Perro", "Gato", "Ninguna", "Hámster", "Pájaro", "Pez"]},
    {"pregunta": "🎮 ¿Qué haces en tu tiempo libre?", "icono": "🎮", "opciones": ["Videojuegos", "Salir con amigos", "Ver series", "Hacer ejercicio", "Leer", "Dormir"]},
    {"pregunta": "💍 ¿Qué buscas aquí?", "icono": "💍", "opciones": ["Algo serio", "Amistad", "Algo casual", "Conocer gente", "Ver qué pasa", "Romance"]},
    {"pregunta": "🏖️ ¿Vacaciones ideales?", "icono": "🏖️", "opciones": ["Playa", "Montaña", "Ciudad", "Campo", "Aventura", "Todo incluido"]}
]

# ============ INICIALIZAR ============
if "paso" not in st.session_state:
    st.session_state.paso = 0
if "respuestas" not in st.session_state:
    st.session_state.respuestas = []
if "terminado" not in st.session_state:
    st.session_state.terminado = False
if "perfil" not in st.session_state:
    st.session_state.perfil = {
        "nombre": "", "edad": 0, "ciudad": "", "facebook": "", "instagram": "", "bio": ""
    }

# ============ HEADER ============
st.markdown('<div style="text-align: center;"><span class="badge-neon">✨ ENCUENTRA TU ALMA GEMELA ✨</span></div>', unsafe_allow_html=True)
st.markdown('<h1 class="main-title">💘 Match de Almas</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Responde preguntas y encuentra personas con tus mismos gustos</p>', unsafe_allow_html=True)

# ============ REGISTRO ============
if st.session_state.paso == 0 and not st.session_state.terminado:
    st.markdown(f'''
    <div class="question-card">
        <div class="question-icon">📝✨</div>
        <div class="question-text">Cuéntanos quién eres</div>
    </div>
    ''', unsafe_allow_html=True)
    
    nombre = st.text_input("👤 ¿Cómo te llamas?")
    edad = st.number_input("🎂 Edad", min_value=15, max_value=99, value=20)
    ciudad = st.text_input("📍 ¿Dónde vives?")
    facebook = st.text_input("📘 Facebook (usuario)", placeholder="Opcional")
    instagram = st.text_input("📸 Instagram (@usuario)", placeholder="Opcional")
    bio = st.text_area("💬 Una frase sobre ti", placeholder="Soy una persona...", height=80)
    
    if st.button("✨ COMENZAR ✨", use_container_width=True):
        if nombre:
            st.session_state.perfil = {"nombre": nombre, "edad": edad, "ciudad": ciudad, "facebook": facebook, "instagram": instagram, "bio": bio}
            st.session_state.paso = 1
            st.rerun()
        else:
            st.warning("Escribe tu nombre")

# ============ PREGUNTAS ============
elif not st.session_state.terminado and st.session_state.paso <= len(preguntas):
    if st.session_state.paso <= len(preguntas) and st.session_state.paso > 0:
        idx = st.session_state.paso - 1
        if idx < len(preguntas):
            # Barra de progreso
            progress = (st.session_state.paso - 1) / len(preguntas)
            st.markdown(f'<div class="progress-text">💘 Pregunta {st.session_state.paso} de {len(preguntas)}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="progress-bar-container"><div class="progress-fill" style="width: {progress*100}%;"></div></div>', unsafe_allow_html=True)
            
            pregunta_actual = preguntas[idx]
            st.markdown(f'''
            <div class="question-card">
                <div class="question-icon">{pregunta_actual["icono"]}</div>
                <div class="question-text">{pregunta_actual["pregunta"]}</div>
            </div>
            ''', unsafe_allow_html=True)
            
            for opcion in pregunta_actual["opciones"]:
                if st.button(opcion, key=f"q{idx}_{opcion}", use_container_width=True):
                    st.session_state.respuestas.append(opcion)
                    st.session_state.paso += 1
                    st.rerun()

# ============ RESULTADOS ============
elif st.session_state.paso > len(preguntas) and not st.session_state.terminado:
    st.session_state.terminado = True
    st.rerun()

elif st.session_state.terminado:
    codigo = hashlib.md5("".join(st.session_state.respuestas).encode()).hexdigest()[:6]
    matches_simulados = [
        {"nombre": "Sofía", "edad": 22, "ciudad": st.session_state.perfil["ciudad"] or "tu ciudad", "facebook": "sofi.love", "instagram": "@sofi_love", "match": random.randint(75, 99)},
        {"nombre": "Mateo", "edad": 23, "ciudad": st.session_state.perfil["ciudad"] or "tu ciudad", "facebook": "mateo.dev", "instagram": "@mateo_d", "match": random.randint(70, 96)},
        {"nombre": "Valentina", "edad": 21, "ciudad": st.session_state.perfil["ciudad"] or "tu ciudad", "facebook": "valentina.m", "instagram": "@vale_m", "match": random.randint(82, 98)},
    ]
    
    st.markdown(f'''
    <div class="result-card">
        <div class="result-emoji">💘✨</div>
        <div class="result-title" style="background: linear-gradient(135deg, #FF6B6B, #FF8E53); -webkit-background-clip: text; background-clip: text; color: transparent;">¡Hola {st.session_state.perfil["nombre"]}!</div>
        <div style="margin: 1rem 0;"><span class="code-badge">#{codigo}</span></div>
        <p style="color: rgba(255,255,255,0.8);">Tu código único • Compártelo y haz match</p>
    </div>
    ''', unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown('<h3 style="color: white; text-align: center;">💕 Personas compatibles cerca de ti</h3>', unsafe_allow_html=True)
    
    for match in matches_simulados:
        st.markdown(f'''
        <div class="match-card">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap;">
                <div>
                    <span style="font-size: 1.3rem; font-weight: 700; color: white;">{match["nombre"]}</span>
                    <span style="color: rgba(255,255,255,0.6);">, {match["edad"]} años</span>
                    <div style="font-size: 0.8rem; color: rgba(255,255,255,0.5);">📍 {match["ciudad"]}</div>
                </div>
                <div class="match-percent">{match["match"]}%<br><span style="font-size: 0.7rem;">Match</span></div>
            </div>
            <div style="margin-top: 0.8rem; display: flex; gap: 0.5rem; flex-wrap: wrap;">
                <a href="https://facebook.com/{match['facebook']}" target="_blank" class="profile-link">📘 Facebook</a>
                <a href="https://instagram.com/{match['instagram'].replace('@', '')}" target="_blank" class="instagram-link">📸 Instagram</a>
            </div>
            <div style="margin-top: 0.8rem; font-size: 0.75rem; color: rgba(255,255,255,0.4);">
                ✨ Gustos en común: {", ".join(random.sample(st.session_state.respuestas, 3))}
            </div>
        </div>
        ''', unsafe_allow_html=True)
    
    st.markdown("---")
    st.subheader("🔍 Buscar por código")
    codigo_buscar = st.text_input("Ingresa el código de alguien")
    if codigo_buscar:
        st.success(f"✅ Código válido. ¡Encontramos a alguien compatible!")
    
    st.markdown("---")
    st.subheader("📱 Comparte tu perfil")
    share_text = f"💘 Mi código es {codigo} en Match de Almas. ¿Cuál es el tuyo?"
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f'<a href="https://wa.me/?text={share_text}" target="_blank" class="share-btn-wa">📱 WhatsApp</a>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<a href="https://www.instagram.com/" target="_blank" class="share-btn-ig">📸 Instagram</a>', unsafe_allow_html=True)
    
    if st.button("🔄 Jugar de nuevo", use_container_width=True):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

st.markdown('<div class="footer">💘 Match de Almas • Encuentra a tu persona ideal 🔥</div>', unsafe_allow_html=True)