import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Step 10 - Collision")

clock = pygame.time.Clock() 

apple_img = pygame.image.load("apple.png")
apple_img = pygame.transform.scale(apple_img, (40, 40))

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

    self.rect.clamp_ip(screen.get_rect())

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5,20))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect(center=(x,y))
        self.speed_y = -7

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > 0:
            self.kill()

all_sprites = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

coins = []
coin_speeds = []

for _ in range(5):   # ← 사과 개수 조절
    rect = pygame.Rect(
        random.randint(0, WIDTH-40),
        random.randint(0, HEIGHT-40),
        40, 40
    )
    coins.append(rect)
    coin_speeds.append([random.choice([-2,2]), random.choice([-2,2])])


running = True
game_over = False        #추가: 게임 오버 상태 표시용 플래그

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  #변경: 게임 오버가 아닐 때만 움직임/충돌 처리
    if not game_over:
        all_sprites.update() #추가: game_over == False 일 때만 업데이트

        if event.type == pygame.KEYDOWN:
            # 총알 발사 (스페이스)
            if event.key == pygame.K_SPACE and not game_over:
                bullet = Bullet(rect.centerx , rect.top)
                all_sprites.add(bullet)
                bullet_group.add(bullet)

    
        hits = pygame.sprite.groupcollide(coins, bullet_group, True, True)
        for hit in hits:
            score += 1
            
        if pygame.sprite.spritecollide(player, coins, False):
            for hit in hits:
                score -= 1

  # ---------------- 그림 그리기 영역 ----------------
  screen.fill((170, 200, 255))  
  pygame.draw.rect(screen, (80, 170, 80), (0, HEIGHT - 60, WIDTH, 60))  # 땅

  pygame.draw.line(screen, (0, 0, 0), (300, 300), (500, 300), 5)  # 장애물 선
 
  all_sprites.draw(screen)  #추가: Sprite 그룹 그리기 (Player + Enemy)

  #추가: 점수 텍스트 출력해서 진짜 게임 느낌
  font = pygame.font.SysFont(None, 24)
  text = font.render(f"Score: {score}", True, (0, 0, 0))
  screen.blit(text, (10, 10))

  #추가: 게임오버 메시지 (플래그가 True일 때만)
  if game_over:
    over_text = font.render("GAME OVER", True, (255, 0, 0))
    over_x = (WIDTH - over_text.get_width()) // 2 #글씨 정중앙에 배치
    over_y = (HEIGHT - over_text.get_height()) // 2 
    screen.blit(over_text, (over_x, over_y))

  pygame.display.flip()
  clock.tick(60)
pygame.quit()