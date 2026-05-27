import streamlit as st
import random
import json
from datetime import datetime

# Configuración de la página
st.set_page_config(
    page_title="Guess The Movie - Adivina la película",
    page_icon="🎬",
    layout="centered"
)

# CSS personalizado para mejor apariencia
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .main-title {
        text-align: center;
        color: white;
        font-size: 3rem;
        margin-bottom: 0;
    }
    .subtitle {
        text-align: center;
        color: #e0e0e0;
        margin-bottom: 2rem;
    }
    .emoji-display {
        text-align: center;
        font-size: 5rem;
        background: white;
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 10px 40px rgba(0,0,0,0.2);
    }
    .result-box {
        text-align: center;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .correct {
        background-color: #d4edda;
        color: #155724;
        border: 1px solid #c3e6cb;
    }
    .incorrect {
        background-color: #f8d7da;
        color: #721c24;
        border: 1px solid #f5c6cb;
    }
    .score-box {
        background: rgba(255,255,255,0.2);
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# ============ BASE DE DATOS DE PELÍCULAS ============
peliculas = [
    # Emojis, Película, Pista
    ("🕷️🏠", "Spider-Man: No Way Home", "Peter Parker lucha contra villanos de otros universos"),
    ("👑🦁", "El Rey León", "Simba debe reclamar su lugar como rey"),
    ("🚢❤️", "Titanic", "Amor en el barco más famoso del mundo"),
    ("🧙‍♂️💍", "El Señor de los Anillos", "Un anillo para gobernarlos a todos"),
    ("🍫🏭", "Charlie y la Fábrica de Chocolate", "Willy Wonka es el dueño"),
    ("🔫🐶", "John Wick", "No mates al perro de este hombre"),
    ("🤖💙", "Wall-E", "Un robot limpia la Tierra y se enamora"),
    ("🦇🗿", "Batman", "El caballero de la noche protege Gotham"),
    ("🚀🌌", "Interestelar", "Viaje a través de un agujero de gusano"),
    ("🐠🌊", "Buscando a Nemo", "Un pez payaso busca a su hijo"),
    ("🦸‍♂️🔨", "Thor: Love and Thunder", "El dios del trueno con su martillo"),
    ("🧜‍♀️🌊", "La Sirenita", "Ariel quiere ser humana"),
    ("🐭🍳", "Ratatouille", "Una rata que quiere ser chef"),
    ("🎪🔪", "El Orfanato", "Terror en un antiguo orfanato"),
    ("🚗⚡", "Regreso al Futuro", "Un DeLorean viaja en el tiempo"),
    ("👻🔫", "Cazafantasmas", "¿A quién vas a llamar?"),
    ("🦖🌲", "Parque Jurásico", "Dinosaurios clonados en una isla"),
    ("😈👗", "El Diablo Viste a la Moda", "Una joven trabaja para una jefa cruel"),
    ("🏃‍♂️⚙️", "Corazón de Metal", "Boxeo y un robot llamado Atom"),
    ("🎄🏠", "Mi Pobre Angelito", "Un niño se queda solo en Navidad"),
]

# ============ INICIALIZAR ESTADO ============
if "puntaje" not in st.session_state:
    st.session_state.puntaje = 0
if "jugadas" not in st.session_state:
    st.session_state.jugadas = 0
if "pelicula_actual" not in st.session_state:
    st.session_state.pelicula_actual = random.choice(peliculas)
if "respuesta_usuario" not in st.session_state:
    st.session_state.respuesta_usuario = ""
if "mostrar_resultado" not in st.session_state:
    st.session_state.mostrar_resultado = False
if "ultimo_acierto" not in st.session_state:
    st.session_state.ultimo_acierto = None
if "usar_pista" not in st.session_state:
    st.session_state.usar_pista = False

# ============ FUNCIONES ============
def verificar_respuesta():
    if st.session_state.respuesta_usuario.strip().lower() == st.session_state.pelicula_actual[1].lower():
        st.session_state.puntaje += 1
        st.session_state.ultimo_acierto = True
        st.session_state.mostrar_resultado = True
    else:
        st.session_state.ultimo_acierto = False
        st.session_state.mostrar_resultado = True
    st.session_state.jugadas += 1

def siguiente_pelicula():
    st.session_state.pelicula_actual = random.choice(peliculas)
    st.session_state.respuesta_usuario = ""
    st.session_state.mostrar_resultado = False
    st.session_state.ultimo_acierto = None
    st.session_state.usar_pista = False
    st.rerun()

def reiniciar_juego():
    st.session_state.puntaje = 0
    st.session_state.jugadas = 0
    siguiente_pelicula()

# ============ INTERFAZ PRINCIPAL ============
st.markdown('<h1 class="main-title">🎬 Guess The Movie</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Adivina la película usando emojis</p>', unsafe_allow_html=True)

# Mostrar puntaje
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f'<div class="score-box">🎯 Puntaje: {st.session_state.puntaje}</div>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="score-box">🎮 Jugadas: {st.session_state.jugadas}</div>', unsafe_allow_html=True)
with col3:
    porcentaje = (st.session_state.puntaje / st.session_state.jugadas * 100) if st.session_state.jugadas > 0 else 0
    st.markdown(f'<div class="score-box">📊 Aciertos: {porcentaje:.0f}%</div>', unsafe_allow_html=True)

st.markdown("---")

# Mostrar emojis
st.markdown(f'<div class="emoji-display">{st.session_state.pelicula_actual[0]}</div>', unsafe_allow_html=True)

# Pista (opcional)
if st.button("💡 ¿Necesitas una pista?"):
    st.session_state.usar_pista = True

if st.session_state.usar_pista:
    st.info(f"🔍 Pista: {st.session_state.pelicula_actual[2]}")

# Input para respuesta
respuesta = st.text_input(
    "Escribe tu respuesta:",
    value=st.session_state.respuesta_usuario,
    key="respuesta_usuario",
    placeholder="Ej: Titanic, El Rey León, etc."
)

# Botones
col1, col2 = st.columns(2)

with col1:
    if st.button("✅ Verificar respuesta", use_container_width=True):
        if st.session_state.respuesta_usuario:
            verificar_respuesta()
            st.rerun()
        else:
            st.warning("Escribe una respuesta primero")

with col2:
    if st.button("🎲 Siguiente película", use_container_width=True):
        siguiente_pelicula()

# Mostrar resultado
if st.session_state.mostrar_resultado:
    if st.session_state.ultimo_acierto:
        st.markdown(
            f'<div class="result-box correct">🎉 ¡CORRECTO! Era "{st.session_state.pelicula_actual[1]}" 🎉</div>',
            unsafe_allow_html=True
        )
        st.balloons()
    else:
        st.markdown(
            f'<div class="result-box incorrect">❌ INCORRECTO. Era "{st.session_state.pelicula_actual[1]}" ❌</div>',
            unsafe_allow_html=True
        )

# Botón reiniciar
st.divider()
if st.button("🔄 Reiniciar juego", use_container_width=True):
    reiniciar_juego()

# ============ SECCIÓN PARA COMPARTIR ============
st.divider()
st.subheader("📱 Comparte con amigos")

share_text = f"🎬 ¡Adiviné {st.session_state.puntaje} películas! ¿Puedes vencerme? Juega aquí:"

# Botones para compartir
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f'<a href="https://wa.me/?text={share_text}" target="_blank"><button style="width:100%;background:#25D366;color:white;padding:0.5rem;border:none;border-radius:5px;">📱 WhatsApp</button></a>', unsafe_allow_html=True)

with col2:
    st.markdown(f'<a href="https://twitter.com/intent/tweet?text={share_text}" target="_blank"><button style="width:100%;background:#1DA1F2;color:white;padding:0.5rem;border:none;border-radius:5px;">🐦 Twitter</button></a>', unsafe_allow_html=True)

with col3:
    st.markdown(f'<a href="https://www.facebook.com/sharer/sharer.php?u=https://guessmovie.streamlit.app" target="_blank"><button style="width:100%;background:#1877F2;color:white;padding:0.5rem;border:none;border-radius:5px;">📘 Facebook</button></a>', unsafe_allow_html=True)

# Footer
st.divider()
st.caption("🎬 Guess The Movie - Juego infinito para adivinar películas con emojis")
st.caption("💡 Consejo: Si no sabes, usa la pista o pasa a la siguiente")