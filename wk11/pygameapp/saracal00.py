import pygame

pygame.init()
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# 1. โหลดภาพ Spritesheet มาก่อน
full_sheet = pygame.image.load("sara/sara-cal1.png")

# 2. คำนวณขนาด (สมมติว่าภาพรวมคือ 150x100 และมี 3 คอลัมน์ 2 แถว)
# เราจะตัดเอาแค่สี่เหลี่ยมผืนผ้า (x, y, width, height)
# ลองปรับตัวเลข 50, 50 ให้พอดีกับขนาดตัวละครจริงของคุณนะครับ
char_width = full_sheet.get_width() // 3  # หาร 3 เพราะมี 3 คอลัมน์
char_height = full_sheet.get_height() // 2 # หาร 2 เพราะมี 2 แถว
sara = full_sheet.subsurface(pygame.Rect(0, 0, char_width, char_height))

# เตรียม Font
font = pygame.font.SysFont("Arial", 24)

x, y = 50, 50
speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # การเคลื่อนที่
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: x -= speed
    if keys[pygame.K_RIGHT]: x += speed
    if keys[pygame.K_UP]: y -= speed
    if keys[pygame.K_DOWN]: y += speed

    screen.fill((255, 255, 255))
    
    # วาดตัวละครที่ตัดมาแล้ว
    screen.blit(sara, (x, y))
    
    # แสดง FPS
    fps_text = font.render(f"FPS: {clock.get_fps():.0f}", True, (100, 100, 100))
    screen.blit(fps_text, (300, 260))

    pygame.display.update()
    clock.tick(60)

pygame.quit()