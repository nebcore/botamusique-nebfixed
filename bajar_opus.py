import urllib.request
import ssl

print("Descargando la librería Opus oficial (64-bit)...")
# Obtenemos el archivo nativo desde el código fuente del famoso proyecto MusicBot
url = "https://github.com/Just-Some-Bots/MusicBot/raw/ea5e0daebd384ec8a14c9a585da399934e2a6252/libopus-0.x64.dll"

# Ignoramos advertencias de certificados locales por seguridad
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Descargamos y guardamos con el nombre exacto que exige tu bot
with urllib.request.urlopen(url, context=ctx) as response, open("libopus-0.dll", "wb") as out_file:
    out_file.write(response.read())

print("¡Descarga lista! Archivo libopus-0.dll guardado correctamente.")
