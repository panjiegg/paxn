import pygame
import random

# 初始化pygame库，必须在使用pygame的其他功能之前调用
pygame.init()

# 定义颜色常量，使用RGB颜色模式
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 设置游戏窗口的宽度和高度
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
# 创建游戏窗口并设置窗口标题
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("贪吃蛇")

# 定义蛇身方块的大小和蛇的移动速度
BLOCK_SIZE = 20
SNAKE_SPEED = 15

# 定义字体样式，用于在游戏中显示文本
FONT_STYLE = pygame.font.SysFont(None, 50)


def draw_text(text, font, color, surface, x, y):
    """
    在指定的表面（surface）上绘制文本

    参数：
    text (str)：要绘制的文本内容
    font (pygame.font.Font)：字体对象
    color (tuple)：文本颜色，格式为(R, G, B)
    surface (pygame.Surface)：要绘制文本的表面，通常是游戏窗口
    x (int)：文本在表面上的水平中心位置
    y (int)：文本在表面上的垂直中心位置
    """
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)


def generate_food(snake_body):
    """
    生成食物的位置，确保食物位置不与蛇身重叠

    参数：
    snake_body (list)：蛇身的坐标列表，每个元素是一个包含[x, y]坐标的列表

    返回：
    tuple：食物的[x, y]坐标
    """
    food_x = random.randint(0, (SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
    food_y = random.randint(0, (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
    while [food_x, food_y] in snake_body:
        food_x = random.randint(0, (SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        food_y = random.randint(0, (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
    return food_x, food_y


class SnakeGame:
    def __init__(self):
        """
        初始化游戏状态
        """
        self.game_over = False
        self.game_close = False

        # 蛇的初始位置，位于屏幕中心
        self.snake_x = SCREEN_WIDTH / 2
        self.snake_y = SCREEN_HEIGHT / 2

        # 蛇的初始移动方向，初始为静止（0, 0）
        self.snake_x_change = 0
        self.snake_y_change = 0

        # 蛇的身体列表，初始为空
        self.snake_body = []
        self.snake_length = 1

        # 生成食物的初始位置，确保不与蛇身重叠
        self.food_x, self.food_y = generate_food(self.snake_body)

        # 创建一个时钟对象，用于控制游戏帧率
        self.clock = pygame.time.Clock()

    def handle_events(self):
        """
        处理游戏中的各种事件，如按键按下和窗口关闭事件
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # 如果用户点击关闭窗口，设置游戏结束标志为True
                self.game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    # 如果按下左键，设置蛇的移动方向向左
                    self.snake_x_change = -BLOCK_SIZE
                    self.snake_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    # 如果按下右键，设置蛇的移动方向向右
                    self.snake_x_change = BLOCK_SIZE
                    self.snake_y_change = 0
                elif event.key == pygame.K_UP:
                    # 如果按下上键，设置蛇的移动方向向上
                    self.snake_y_change = -BLOCK_SIZE
                    self.snake_x_change = 0
                elif event.key == pygame.K_DOWN:
                    # 如果按下下键，设置蛇的移动方向向下
                    self.snake_y_change = BLOCK_SIZE
                    self.snake_x_change = 0

    def move_snake(self):
        """
        根据当前的移动方向更新蛇的位置
        """
        self.snake_x += self.snake_x_change
        self.snake_y += self.snake_y_change

    def check_collisions(self):
        """
        检查蛇是否与边界或自身发生碰撞
        """
        # 检查蛇是否撞到边界
        if (self.snake_x >= SCREEN_WIDTH or self.snake_x < 0 or
                self.snake_y >= SCREEN_HEIGHT or self.snake_y < 0):
            self.game_close = True

        # 检查蛇是否撞到自己，通过比较蛇头位置与蛇身其他部分的位置
        snake_head = [self.snake_x, self.snake_y]
        if snake_head in self.snake_body[:-1]:
            self.game_close = True

    def update_snake_body(self):
        """
        更新蛇的身体列表，添加蛇头位置并删除蛇尾位置（如果蛇身长度未增加）
        """
        self.snake_body.append([self.snake_x, self.snake_y])
        if len(self.snake_body) > self.snake_length:
            del self.snake_body[0]

    def check_food_collision(self):
        """
        检查蛇是否吃到食物，如果吃到则更新食物位置并增加蛇的长度
        """
        if self.snake_x == self.food_x and self.snake_y == self.food_y:
            self.food_x, self.food_y = generate_food(self.snake_body)
            self.snake_length += 1

    def draw_game_objects(self):
        """
        绘制游戏中的所有对象，包括背景、食物和蛇身
        """
        screen.fill(WHITE)
        pygame.draw.rect(screen, GREEN, [self.food_x, self.food_y, BLOCK_SIZE, BLOCK_SIZE])
        for segment in self.snake_body:
            pygame.draw.rect(screen, BLACK, [segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE])

    def display_message(self, text, color):
        """
        在屏幕中心显示指定文本和颜色的消息

        参数：
        text (str)：要显示的文本内容
        color (tuple)：文本颜色，格式为(R, G, B)
        """
        draw_text(text, FONT_STYLE, color, screen, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    def run_game(self):
        """
        游戏的主循环，包含游戏的主要逻辑
        """
        while not self.game_over:
            while self.game_close:
                screen.fill(WHITE)
                self.display_message("你输了！按Q-退出或C-重新开始", RED)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            self.game_over = True
                            self.game_close = False
                        if event.key == pygame.K_c:
                            return self.run_game()

            self.handle_events()
            self.move_snake()
            self.check_collisions()
            self.update_snake_body()
            self.check_food_collision()
            self.draw_game_objects()
            pygame.display.update()
            self.clock.tick(SNAKE_SPEED)

        pygame.quit()
        quit()


if __name__ == "__main__":
    game = SnakeGame()
    game.run_game()
