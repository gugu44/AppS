import pygame
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 150, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Plotter Connect")
font = pygame.font.SysFont(None, 36)

NUM_POINTS = 5
POINT_RADIUS = 8
CLICK_RADIUS = 15


def generate_points(num):
    margin = 50
    points = []
    for _ in range(num):
        x = random.randint(margin, WIDTH - margin)
        y = random.randint(margin, HEIGHT - margin)
        points.append((x, y))
    return points


def draw_points(points, visited):
    for i, pos in enumerate(points):
        color = BLUE if i in visited else BLACK
        pygame.draw.circle(screen, color, pos, POINT_RADIUS)


def main():
    running = True
    points = generate_points(NUM_POINTS)
    current_idx = 0
    visited = []

    while running:
        screen.fill(WHITE)
        draw_points(points, visited)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = event.pos
                px, py = points[current_idx]
                if (mx - px) ** 2 + (my - py) ** 2 <= CLICK_RADIUS ** 2:
                    if visited:
                        pygame.draw.line(screen, BLUE, points[current_idx - 1], points[current_idx], 2)
                    visited.append(current_idx)
                    current_idx += 1
                    if current_idx >= len(points):
                        text = font.render("Completed!", True, BLACK)
                        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))
                        pygame.display.flip()
                        pygame.time.wait(1000)
                        points = generate_points(NUM_POINTS)
                        current_idx = 0
                        visited = []

        pygame.display.flip()
        pygame.time.Clock().tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
