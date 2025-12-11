import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 9 with Collision")

clock = pygame.time.Clock()  # FPS 제어 준비

#================= Player 클래스 =================
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("dukbird.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed = 3

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # 화면 경계 제한
        self.rect.clamp_ip(screen.get_rect())


#================= Enemy 클래스(추가) =================
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((255, 0, 0))           # 빨간색 박스
        self.rect = self.image.get_rect()
        self.random_position()

    def random_position(self):
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(0, HEIGHT - self.rect.height)


#================= 그룹 생성 =================
all_sprites = pygame.sprite.Group()
player = Player()
enemy = Enemy()

all_sprites.add(player)
all_sprites.add(enemy)

# 점수 변수 추가
score = 0
font = pygame.font.SysFont(None, 36)

running = True

#================= 메인 루프 =================
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    #================= 충돌 체크 (추가) =================
    if pygame.sprite.collide_rect(player, enemy):
        score += 1                 # 점수 증가!
        enemy.random_position()    # Enemy 위치 랜덤 재배치

    #================= 화면 그리기 =================
    screen.fill((170, 200, 255))
    pygame.draw.rect(screen, (80, 170, 80), (0, HEIGHT - 60, WIDTH, 60))
    pygame.draw.rect(screen, (255, 80, 80), (50, 280, 40, 40))
    pygame.draw.circle(screen, (0, 255, 0), (450, 150), 20)
    pygame.draw.line(screen, (0, 0, 0), (300, 300), (500, 300), 5)

    all_sprites.draw(screen)

    # 점수 표시
    text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
