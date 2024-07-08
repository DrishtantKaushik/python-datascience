import random

def draw_canvas():
    # Clear the canvas
    for i in range(canvas_width):
        for j in range(canvas_height):
            canvas[i][j] = '.'

def draw_ball():
    # Draw the ball
    canvas[ball_y][ball_x] = 'o'

def draw_bar():
    # Draw the bar
    for i in range(bar_width):
        canvas[bar_y][bar_x + i] = '|'

def move_ball():
    global ball_x, ball_y
    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

def move_bar():
    global bar_x
    # Move the bar
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            bar_x -= bar_speed
        elif event.key == pygame.K_RIGHT:
            bar_x += bar_speed

def check_collision():
    # Check if the ball hits the bar
    if ball_y == bar_y and ball_x >= bar_x and ball_x <= bar_x + bar_width:
        return True
    return False

def main():
    global ball_x, ball_y, bar_x, canvas_width, canvas_height, ball_speed_x, ball_speed_y, bar_width, bar_speed

    # Initialize the canvas
    canvas_width = 80
    canvas_height = 20
    canvas = [['.' for i in range(canvas_width)] for j in range(canvas_height)]

    # Initialize the ball
    ball_x = canvas_width // 2
    ball_y = 0
    ball_speed_x = random.choice([-1, 1])
    ball_speed_y = 1

    # Initialize the bar
    bar_x = canvas_width // 2
    bar_width = 5
    bar_speed = 1

    # Main loop
    while True:
        # Draw the canvas
        draw_canvas()

        # Draw the ball
        draw_ball()

        # Draw the bar
        draw_bar()

        # Move the ball
        move_ball()

        # Move the bar
        move_bar()

        # Check if the ball hits the bar
        if check_collision():
            print("Game over!")

        # Wait for a while
        time.sleep(0.1)
        
if __name__ == '_main_':  
    main()      
        
        
        
        


