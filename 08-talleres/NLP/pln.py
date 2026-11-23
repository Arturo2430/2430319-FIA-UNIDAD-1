"""Analizador de sentimientos sencillo basado en palabras y reglas."""

import re


palabras_positivas = {
    "feliz", "alegre", "contento", "excelente", "increíble", "genial",
    "encantó", "encanta", "bueno", "buena", "maravilloso", "divertido",
    "divertida", "amo", "amé", "recomiendo", "espectacular", "bien",
}

palabras_negativas = {
    "triste", "mal", "malo", "mala", "pésimo", "horrible", "aburrido",
    "aburrida", "decepcionante", "odio", "odié", "feo", "fea",
    "terrible", "deprimido", "deprimida", "enojado", "enojada",
}

conectores_de_contraste = ["pero", "aunque", "sin embargo"]


def tokenizar(texto):
    """Convertir el texto en palabras en minúsculas, sin puntuación."""
    return re.findall(r"[^\W\d_]+", texto.lower(), flags=re.UNICODE)


def analizar_sentimiento(texto):
    """Devolver la clasificación y el puntaje según el vocabulario conocido."""
    tokens = tokenizar(texto)
    puntaje = 0
    encontro_conector = False
    index = 0

    while index < len(tokens):
        # Comparar secuencias para reconocer también "sin embargo".
        for conector in conectores_de_contraste:
            partes = conector.split()
            if tokens[index:index + len(partes)] == partes:
                encontro_conector = True
                index += len(partes)
                break
        else:
            palabra = tokens[index]
            peso = 2 if encontro_conector else 1
            if palabra in palabras_positivas:
                puntaje += peso
            elif palabra in palabras_negativas:
                puntaje -= peso
            index += 1

    if puntaje > 0:
        return "Sentimiento POSITIVO (texto feliz)", puntaje
    if puntaje < 0:
        return "Sentimiento NEGATIVO (texto triste)", puntaje
    return "Sentimiento NEUTRAL", puntaje


def main():
    print("=== Analizador de Sentimientos ===")
    print("Escribe una frase y te diré si es feliz, triste o neutral.")
    print("(Escribe 'salir' para terminar)\n")

    while True:
        try:
            texto_usuario = input("Escribe tu texto: ")
        except (EOFError, KeyboardInterrupt):
            print("\nGracias por probar el analizador.")
            break
        if texto_usuario.strip().lower() == "salir":
            print("Gracias por probar el analizador.")
            break
        resultado, puntaje = analizar_sentimiento(texto_usuario)
        print(f"Resultado: {resultado} (puntaje: {puntaje})\n")


if __name__ == "__main__":
    main()
