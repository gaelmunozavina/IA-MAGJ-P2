import re

def extractor_entidades_simple(texto):
    # Patrones para identificar entidades basadas en pistas lingüísticas
    # Organizaciones: Palabras que empiezan con mayúscula seguidas de S.A. o Corp.
    org_patron = r'\b[A-Z][a-z]+ (?:S\.A\.|Corp\.|Group)\b'
    # Lugares: "en [Ciudad]"
    lugar_patron = r'en ([A-Z][a-z]+(?:\s[A-Z][a-z]+)*)'
    
    organizaciones = re.findall(org_patron, texto)
    lugares = re.findall(lugar_patron, texto)
    
    return {
        "Organizaciones": organizaciones,
        "Lugares": lugares
    }

# --- ESCENARIO ---
texto_noticia = """
La empresa TechGlobal Corp. anunció hoy la apertura de su nueva sede 
en Tonalá y otra oficina en Ciudad de Mexico. 
El representante de Inversiones MAGJ Group confirmó la noticia.
"""

entidades = extractor_entidades_simple(texto_noticia)

print("Entidades Extraídas:")
for categoria, valores in entidades.items():
    print(f"  {categoria}: {valores}")
  
