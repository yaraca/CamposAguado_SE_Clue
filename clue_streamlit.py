# app.py
import streamlit as st
import random

# ---------------- CONFIGURACIÓN DE LA APP ----------------
st.set_page_config(
    page_title="Clue: El misterio de Alison",
    page_icon="🕵️‍♀️",
    layout="centered",
)

# ---------------- ESTILOS ----------------
st.markdown("""
<style>
body {
    background-color: #1b1b2f;
    color: #f8f8f2;
    font-family: 'Poppins', sans-serif;
}
.sidebar .sidebar-content {
    background-color: #2c2c7c;
}
h1, h2, h3 {
    color: #ff66b2;
}
.stButton>button {
    background-color: #ff66b2;
    color: white;
    border-radius: 10px;
    padding: 8px 16px;
    border: none;
}
.stButton>button:hover {
    background-color: #ff3385;
}
</style>
""", unsafe_allow_html=True)

# ---------------- DATOS DEL JUEGO ----------------
personajes = [
    "Spencer Hastings",
    "Emily Fields",
    "Aria Montgomery",
    "Hanna Marin",
    "Mona Vanderwaal"
]

lugares = ["Granero de Spencer", "Bosque", "Cabaña del lago", "Casa de los DiLaurentis", "Escuela de Rosewood"]
armas = ["Pala", "Cuerda", "Cuchillo", "Veneno", "Pisapapeles"]

# ---------------- NARRATIVA PRINCIPAL ----------------
st.title("🕵️‍♀️ Clue: El misterio de Alison")

st.markdown("""
## 🌙 La desaparición
Era una noche lluviosa en Rosewood. Alison y sus amigas —Spencer, Aria, Hanna y Emily— decidieron pasar la noche en el granero de Spencer.  
Entre risas, secretos y copas de alcohol, la tormenta interrumpió la luz. Cuando despertaron, **Alison había desaparecido**.  
Spencer juró haber escuchado un grito proveniente del bosque. La policía fue llamada, pero no se encontró rastro alguno.  
El caso fue **suspendido** como una desaparición sin pistas sólidas.

---

## 🪦 Un año después
Exactamente un año más tarde, un cuerpo fue encontrado y todos pensaron que era **Alison DiLaurentis**.  
Las chicas, que se habían distanciado desde su desaparición, se reunieron nuevamente para su **funeral**.  
Pero cuando creyeron que todo había terminado... cada una recibió un **mensaje anónimo**.

> “Si contaran la verdad, ya no tendría que hacerlo yo. —A”

Desde ese día, **“A” comenzó a manipularlas, a exponer sus secretos más oscuros**… los mismos que Alison conocía.  
¿Podría ser que alguna de ellas fuera “A”? ¿O acaso Alison no estaba muerta?

---

## 🤫 Los secretos
- **Spencer:** Alison la había visto besando al novio de su hermana y la chantajeaba con contárselo.  
- **Emily:** Estaba enamorada de Alison, pero Alison jugaba con sus sentimientos y la amenazaba con revelar su orientación.  
- **Aria:** Alison sabía que el padre de Aria era infiel y la presionaba para confesarlo.  
- **Hanna:** Luchaba con su inseguridad y desórdenes alimenticios causados por las burlas de Alison.  
- **Mona:** Había sido humillada por Alison durante años, y tras su desaparición se convirtió en alguien nueva… pero con sed de venganza.  

Y además, todas compartían un secreto oscuro: **el accidente de Jenna**, cuando una “broma” terminó dejando a una chica ciega.

---

## 💌 El misterio comienza
Nadie sabe quién mató a Alison...  
Ni si “A” fue su asesino, o alguien más que se esconde entre ellas.

Tu misión es **resolver el misterio**.
""")

st.divider()
st.subheader("¿Quién crees que fue el culpable?")

culpable_elegido = st.selectbox("Selecciona a la sospechosa principal:", personajes)
arma_elegida = st.selectbox("Selecciona el arma del crimen:", armas)
lugar_elegido = st.selectbox("Selecciona el lugar donde ocurrió:", lugares)

if st.button("🔍 Resolver el misterio"):
    culpable_real = random.choice(personajes)
    arma_real = random.choice(armas)
    lugar_real = random.choice(lugares)

    st.divider()
    st.subheader("🔦 Resultados del caso")

    if (culpable_elegido == culpable_real and
        arma_elegida == arma_real and
        lugar_elegido == lugar_real):
        st.success(f"¡Correcto! Descubriste la verdad. Fue {culpable_real} con {arma_real} en {lugar_real}.")
    else:
        st.error(f"No era {culpable_elegido} con {arma_elegida} en {lugar_elegido}.")
        st.info(f"La verdad salió a la luz: fue **{culpable_real}**, usando **{arma_real}**, en **{lugar_real}**.")

    # ---------------- HISTORIAS POSIBLES ----------------
    historias = {
        "Spencer Hastings": f"""
        Spencer, atormentada por la presión de ser perfecta, no soportaba que Alison la manipulara
        con el secreto del beso con el novio de su hermana. Esa noche en el {lugar_real}, discutieron.  
        En un impulso de furia, Spencer tomó la {arma_real}.  
        Nadie sabe si fue un accidente o algo más…  
        Desde entonces, A la ha mantenido bajo control.
        """,

        "Emily Fields": f"""
        Emily amaba a Alison más de lo que podía admitir. Pero Alison jugaba con sus sentimientos.  
        Cuando Alison la amenazó con revelar su secreto, Emily la enfrentó en el {lugar_real}.  
        La discusión se tornó violenta y, en un accidente con la {arma_real}, Alison desapareció.  
        A partir de entonces, Emily recibe mensajes que la atormentan cada día.
        """,

        "Aria Montgomery": f"""
        Aria había guardado silencio sobre el amorío de su padre, pero Alison amenazó con contarlo.  
        Esa noche, en el {lugar_real}, Aria la enfrentó.  
        Entre lágrimas y rabia, la {arma_real} cayó… y con ella, el silencio de Alison.  
        Al día siguiente, “A” le escribió:  
        > “Tu secreto está a salvo conmigo… por ahora.”
        """,

        "Hanna Marin": f"""
        Hanna fue quien más sufrió los comentarios crueles de Alison.  
        Cuando la volvió a humillar en el {lugar_real}, algo en Hanna se quebró.  
        Tomó la {arma_real}, sin pensar, y todo cambió.  
        Pero... ¿por qué los mensajes de A comenzaron justo después de eso?
        """,

        "Mona Vanderwaal": f"""
        Mona había sido humillada durante años.  
        Aquella noche en el {lugar_real}, vio su oportunidad. Con la {arma_real}, puso fin a la reina de Rosewood.  
        Desde ese momento, se convirtió en **“A”**, y comenzó su venganza controlando a todas las demás.  
        Pero el misterio no terminó ahí… ¿Quién controla a “A” ahora?
        """
    }

    st.divider()
    st.subheader("📜 La verdad revelada")
    st.markdown(historias[culpable_real])
    st.divider()
    st.caption("Basado en los sucesos de Pretty Little Liars — Adaptación interactiva para Sistemas Expertos 🎭")

else:
    st.info("Selecciona tus sospechas y presiona **Resolver el misterio** para descubrir la verdad.")
