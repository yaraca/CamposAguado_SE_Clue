import random
import time
import sys

# --- CONFIGURACIÓN DE LA CONSOLA PARA UNA MEJOR EXPERIENCIA ---
def imprimir_pausado(texto, pausa=0.03):
    """Imprime el texto letra por letra para un efecto narrativo."""
    for caracter in texto:
        sys.stdout.write(caracter)
        sys.stdout.flush()
        time.sleep(pausa)
    print()

def esperar_confirmacion():
    """Pausa la ejecución para que el jugador lea la narrativa."""
    input("\n[Presiona ENTER para continuar...]\n")

# --- 1. DEFINICIÓN DE ELEMENTOS DEL JUEGO ---

PERSONAJES = [
    "Spencer Hastings (Académica)",
    "Emily Fields (Atleta)",
    "Aria Montgomery (Artista)",
    "Hanna Marin (Reina de la Moda)",
    "Mona Vanderwaal ('A' Inicial)"
]

ARMAS = [
    "Trofeo de Natación (Contundente)",
    "Palanca de Neumáticos (De metal)",
    "Candelabro Antiguo (De bronce)",
    "Cuerda de Violonchelo (Estrangulamiento)",
    "Jeringa con Sedante (Dosis fatal)"
]

LOCACIONES = [
    "Granero de Spencer",
    "Habitación de Alison",
    "Estacionamiento del Instituto",
    "Salón de Arte de la Escuela",
    "Muelle del Lago"
]

# --- 2. DEFINICIÓN DE CASOS (Respuestas Correctas y Narrativa) ---

# Formato: (Culpable, Arma, Locación, ID)
CASOS = [
    ("Spencer Hastings (Académica)", "Candelabro Antiguo (De bronce)", "Granero de Spencer", 1),
    ("Emily Fields (Atleta)", "Trofeo de Natación (Contundente)", "Muelle del Lago", 2),
    ("Aria Montgomery (Artista)", "Cuerda de Violonchelo (Estrangulamiento)", "Salón de Arte de la Escuela", 3),
    ("Hanna Marin (Reina de la Moda)", "Palanca de Neumáticos (De metal)", "Estacionamiento del Instituto", 4),
    ("Mona Vanderwaal ('A' Inicial)", "Jeringa con Sedante (Dosis fatal)", "Habitación de Alison", 5)
]

# --- 3. FUNCIONES DE NARRATIVA ---

def narrar_introduccion():
    """Muestra la historia de inicio completa."""
    print("=" * 70)
    imprimir_pausado("          CLUE: PRETTY LITTLE SECRETS - EL SISTEMA EXPERTO          ", 0.01)
    print("=" * 70)
    time.sleep(1)
    
    narrativa_completa = """
    Rosewood, una noche de tormenta. Cuatro amigas, Spencer, Emily, Aria y Hanna, se reúnen
    en el Granero de Spencer para una pijamada, esperando a la reina indiscutible, Alison.
    La luz se fue; el alcohol fluyó. Alison llegó cargada de secretos, los de ellas.

    Alison conocía el romance prohibido de Spencer con el novio de su hermana. Sabía de la 
    confusión sexual de Emily y coqueteaba cruelmente con ella. Vio la infidelidad del padre 
    de Aria y la tenía chantajeada. Antes de su cambio, acosó a Hanna, apodándola "la Fortachona".

    Pero el secreto que las unía a todas era el accidente de Jenna. Una "broma" que la dejó 
    ciega, y un as bajo la manga de Alison para mantenerlas controladas. Esa noche, Alison
    desapareció tras un grito.

    Un año después, se encuentra un cuerpo (erróneamente identificado como Alison) y el terror
    comienza: todas reciben un mensaje simultáneo de **"A"**. Alguien conoce todos sus secretos
    y los está usando para atormentarlas. 'A' podría ser el culpable, o solo un vigilante que 
    sabe quién de ellas finalmente estalló.

    Tu misión es descifrar: ¿Quién, con qué y dónde se cometió el crimen?
    """
    imprimir_pausado(narrativa_completa, 0.01)
    esperar_confirmacion()
    
def narrar_final(id_caso, C_x, A_x, L_x):
    """Muestra la historia final completa basada en el ID del caso correcto."""
    print("\n" + "=" * 70)
    imprimir_pausado(f"          LA VERDAD SECRETA DE ROSEWOOD: CASO {id_caso}          ", 0.01)
    print("=" * 70)
    time.sleep(1)

    print(f"\nLA VERDAD ES: {C_x} usó {A_x} en el {L_x}.")

    if id_caso == 1:
        imprimir_pausado("""
        *** SPENCER HASTINGS: LA FURIA DE LA CHANTAGEADA ***
        
        Spencer estaba al límite, sintiendo que Alison tenía el control total de su vida, 
        amenazándola con su secreto y con exponer su participación en el accidente de Jenna. 
        En el granero, después de haber bebido, confrontó a Alison por última vez. Alison se 
        burló y la empujó emocionalmente. En un arrebato ciego de desesperación, Spencer tomó 
        el Candelabro Antiguo que adornaba una mesa cercana y golpeó a la persona que creía 
        era Alison. 
        
        El sistema experto revela que la víctima no era Alison, sino **Bethany Young**, 
        quien había sido manipulada para vestirse de manera similar. El pánico hizo que Spencer 
        huyera, dejando el arma en el lugar. **Mona (la primera 'A')**, que estaba observando 
        y buscando venganza, encontró la escena, aprovechó la confusión para enterrar el cuerpo y 
        comenzar su juego de terror, sabiendo que Spencer siempre sería la principal sospechosa.
        """, 0.01)
    elif id_caso == 2:
        imprimir_pausado("""
        *** EMILY FIELDS: EL GOLPE DE LA DECEPCIÓN ***
        
        Emily, profundamente enamorada de Alison pero confundida por su manipulación constante 
        y sus coqueteos vacíos, la citó en el Muelle del Lago esa noche, buscando una 
        respuesta real. Llevaba su Trofeo de Natación, un recuerdo de cuando no era esclava 
        de los juegos de Alison. Alison se rió de la confesión de amor de Emily y la amenazó
        con revelar su sexualidad a todo Rosewood de la manera más cruel.
        
        Desesperada y sintiéndose totalmente rechazada, Emily forcejeó con Alison. El **Trofeo
        de Natación** impactó la cabeza de Alison. Emily, en shock, creyó haberla matado, 
        tirándola al lago para ocultar la evidencia y cayendo en una profunda negación sobre 
        el evento. La posterior aparición de los mensajes de 'A' solo sirvió para que su mente
        culpable la atormentara constantemente.
        """, 0.01)
    elif id_caso == 3:
        imprimir_pausado("""
        *** ARIA MONTGOMERY: LA DEFENSA FAMILIAR ***
        
        Aria valoraba la imagen de su familia sobre todas las cosas. El chantaje de Alison 
        sobre la infidelidad de su padre la estaba destruyendo. Aria la siguió hasta el **Salón 
        de Arte de la Escuela**, un lugar que Alison pensó que sería el último donde la 
        buscarían. Aria rogó a Alison que se detuviera, pero la rubia solo sonrió y dijo que 
        lo contaría esa misma noche.
        
        En un momento de desesperación, Aria tomó una **Cuerda de Violonchelo** que estaba allí
        por un proyecto de arte. La usó para silenciarla. Fue un acto impulsivo para proteger 
        a su madre. El crimen fue rápido, impulsado por una lealtad familiar mal dirigida. 
        Cuando 'A' apareció, Aria supo que su secreto más oscuro no solo lo conocía Alison, 
        sino alguien más, volviéndose paranoica y sospechando de todos a su alrededor.
        """, 0.01)
    elif id_caso == 4:
        imprimir_pausado("""
        *** HANNA MARIN: LA VENGANZA SILENCIOSA ***
        
        Hanna, la más herida por el acoso de Alison sobre su peso, se sintió manipulada hasta 
        el hartazgo. Decidió enfrentarla con firmeza en el **Estacionamiento del Instituto**, 
        un lugar oscuro y aislado. Llevaba en el maletero la **Palanca de Neumáticos**, 
        simplemente para asustarla. Cuando Alison empezó a burlarse de ella y de su actual
        amistad con Mona, Hanna estalló.
        
        En la confrontación, Hanna golpeó a la figura en la oscuridad. El sistema revela que 
        esta persona era realmente **Bethany Young**, la víctima que se confundió con Alison. 
        Hanna, al darse cuenta de lo que había hecho, entró en pánico y huyó. La manipulación 
        de Alison finalmente la rompió, y el peso de su crimen, aunque no fue contra Alison, 
        fue la base que 'A' usó para iniciar su juego, apuntando directamente a la culpa de Hanna.
        """, 0.01)
    elif id_caso == 5:
        imprimir_pausado("""
        *** MONA VANDERWAAL: LA CREACIÓN DE UNA VILLANA ***
        
        Mona no quería asesinar a Alison, sino eliminarla de Rosewood para siempre. Después de 
        años de acoso, Mona se convirtió en la primera **"A"**. Su plan era inmovilizar a Alison, 
        robar sus diarios y obligarla a huir. Mona la atrajo a la **Habitación de Alison**.
        
        Allí, Mona usó una **Jeringa con Sedante** con una dosis peligrosamente alta (o que reaccionó 
        mal con el alcohol). El objetivo era dejarla inconsciente, pero la dosis resultó fatal 
        o la combinó con un fármaco que causó la muerte. Mona ocultó el cuerpo (que era 
        Bethany Young) y aprovechó la huida de la verdadera Alison para consolidar su poder como
        la mente maestra. El juego de 'A' nació de la necesidad de venganza de Mona contra la 
        persona que la había humillado y de su deseo de transformarse en una chica popular.
        """, 0.01)
    
    print("\n" + "=" * 70)
    imprimir_pausado("--- FIN DEL ARCHIVO DE INFORMES: EL CASO HA SIDO RESUELTO ---", 0.01)
    print("=" * 70)

# --- 4. LÓGICA DEL JUEGO (SISTEMA EXPERTO) ---

def obtener_eleccion(elementos):
    """Muestra una lista de opciones y pide al jugador que ingrese un número."""
    while True:
        try:
            print("-" * 70)
            for i, item in enumerate(elementos):
                print(f"{i+1}. {item}")
            
            eleccion = input("Ingresa el número de tu elección: ")
            
            # Intenta convertir la entrada a entero
            num_eleccion = int(eleccion)
            
            if 1 <= num_eleccion <= len(elementos):
                return elementos[num_eleccion - 1]
            else:
                imprimir_pausado("Número no válido. Inténtalo de nuevo.", 0.01)
        except ValueError:
            imprimir_pausado("Entrada no válida. Por favor, ingresa un número.", 0.01)

def jugar():
    """Función principal que ejecuta el simulador."""
    
    # 4.1. Selección aleatoria de la respuesta correcta al inicio (Motor de Inferencia)
    CASO_CORRECTO = random.choice(CASOS)
    C_x, A_x, L_x, ID_x = CASO_CORRECTO
    
    # 4.2. Presentar la historia inicial
    narrar_introduccion()

    # 4.3. Recoger la acusación del jugador (Botones de elección simulados)
    
    print("\n>>> PASO 1: ¿QUIÉN FUE EL CULPABLE? <<<")
    C_j = obtener_eleccion(PERSONAJES)

    print(f"\nHas acusado a: **{C_j}**")
    time.sleep(1)

    print("\n>>> PASO 2: ¿CON QUÉ ARMA SE COMETIÓ EL CRIMEN? <<<")
    A_j = obtener_eleccion(ARMAS)

    print(f"\nHas elegido el arma: **{A_j}**")
    time.sleep(1)

    print("\n>>> PASO 3: ¿EN QUÉ LOCACIÓN OCURRIÓ? <<<")
    L_j = obtener_eleccion(LOCACIONES)
    
    print(f"\nHas elegido la locación: **{L_j}**")
    time.sleep(1)

    # 4.4. Evaluación del sistema experto
    
    print("\n" + "=" * 70)
    imprimir_pausado("PROCESANDO LA ACUSACIÓN...", 0.05)
    time.sleep(2)
    
    # Comparación de las 3 variables (La lógica del sistema experto)
    if (C_j == C_x) and (A_j == A_x) and (L_j == L_x):
        imprimir_pausado("\n¡ACUSACIÓN CORRECTA! Has resuelto el misterio de Alison DiLaurentis. Ahora, mira los detalles de la verdad.", 0.01)
    else:
        imprimir_pausado("\nACUSACIÓN INCORRECTA. La verdad es más retorcida de lo que crees. A continuación, el informe del caso real:", 0.01)
    
    time.sleep(2)
    
    # 4.5. Revelación de la Historia Final (Independiente de si acertó)
    narrar_final(ID_x, C_x, A_x, L_x)

# --- EJECUCIÓN ---
if __name__ == "__main__":
    jugar()
    