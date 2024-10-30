def calcular_media(nota1, nota2, nota3):
    # Verifica se as notas estão entre 0 e 10
    notas = [nota1, nota2, nota3]
    if any(nota < 0 or nota > 10 for nota in notas):
        raise ValueError("As notas devem estar entre 0 e 10.")
    return (nota1 + nota2 + nota3) / 3
