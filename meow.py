import pygame
import sys
import math
import os

# Inicializar pygame
pygame.init()

# Verificar si el archivo de sonido existe
sonido = "hana.wav"  # 👈 CAMBIA ESTO si usas .mp3
if not os.path.exists(sonido):
    print(f"⚠️  Advertencia: No se encontró '{sonido}' en esta carpeta.")
    print("📁 Asegúrate de que el archivo esté aquí y tenga la extensión correcta (.wav o .mp3).")

# Configurar ventana
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐱 Holograma de Gato Giratorio - By Daira")

# Colores tipo holograma
BACKGROUND = (5, 0, 20)
HOLO_COLOR = (0, 255, 200)  # Cian brillante

clock = pygame.time.Clock()
angle = 0

# Intentar reproducir sonido
if os.path.exists(sonido):
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(sonido)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)  # Repetir
        print("🔊 Música de fondo activada.")
    except Exception as e:
        print(f"❌ Error al cargar el sonido: {e}")

# Gato en ASCII (versión compacta)
cat_lines = [
    "  /\\_/\\  ",
    " ( o w o )",
    "  > ^ <   ",
    " ( Daira )"
]

font = pygame.font.SysFont('Courier New', 22, bold=True)

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    angle += 0.03
    radius = 120 + 40 * math.sin(angle * 0.7)
    x = WIDTH // 2 + radius * math.cos(angle)
    y = HEIGHT // 2 + radius * math.sin(angle)

    screen.fill(BACKGROUND)

    # Dibujar gato con efecto de brillo
    for i, line in enumerate(cat_lines):
        glow = 150 + 100 * math.sin(angle + i * 0.5)
        color = (0, min(255, glow), min(255, glow // 2 + 100))
        text = font.render(line, True, color)
        screen.blit(text, (x - text.get_width() // 2, y - 50 + i * 30))

    # Título
    title = pygame.font.SysFont('Arial', 26).render("🌀 CUTE", True, (100, 255, 255))
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()