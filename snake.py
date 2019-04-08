import sys, pygame, time
import random

pygame.init()



"""
Returns a random position, a 2-tuple representing (x,y) position

board_size: int - a int representing the nxn size of the board
"""
def random_position(board_size):
	return random.randint(0,board_size-1), random.randint(0,board_size-1)


"""
Given input direction, calculate the projected tile that the snake is going to go to on the next time step

dir: string - direction that the snake is traveling

projected_tile: 2-tuple - the projected tile that the snake will advance to given no user input
"""
def calculate_proj(dir, projected_tile):
	if dir == "None":
		return projected_tile
	if dir == "Up":
		return projected_tile[0], projected_tile[1]-1
	if dir == "Down":
		return projected_tile[0], projected_tile[1]+1
	if dir == "Left":
		return projected_tile[0]-1, projected_tile[1]
	else:
		return projected_tile[0]+1, projected_tile[1]

def main():
	tile_size = 36 #px
	board_size = 16 #16 x 16 board
	wh = tile_size * board_size

	screen_size = wh, wh

	#head = 0, 0, 0
	background = 0x0B, 0x3A, 0x39
	head = 0xF0, 0xC7, 0x4B
	print(head)
	body = 0x71, 0xBE, 0xA2

	screen = pygame.display.set_mode(screen_size)
	#initialize snake somewhere randomly
	pos = random_position(board_size)

	#initialize the cookie somewhere randomly
	cookie_pos = random_position(board_size)

	my_font = pygame.font.SysFont('Consolas', 10)
	player_length = [pos]
	head = pos
	game_over = False
	player_direction = "None"
	target = 1/5
	while True:
		begin = time.time()
		'''
		GAME LOGIC
		'''
		projected_tile = calculate_proj(player_direction, head)
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_DOWN and player_direction != "Up":
					projected_tile = head[0], head[1]+1
					player_direction = "Down"
				if event.key == pygame.K_UP and player_direction != "Down":
					projected_tile = head[0], head[1]-1
					player_direction = "Up"
				if event.key == pygame.K_LEFT and player_direction != "Right":
					projected_tile = head[0]-1, head[1]
					player_direction = "Left"
				if event.key == pygame.K_RIGHT and player_direction != "Left":
					projected_tile = head[0]+1, head[1]
					player_direction = "Right"
				print(player_direction)


		#check for collisions
		if projected_tile[0] >= board_size or projected_tile[0] < 0: #wall collision
			game_over=True
		if projected_tile[1] >= board_size or projected_tile[1] < 0:
			game_over=True

		if projected_tile in player_length: #self collision
			game_over=True

		if projected_tile != cookie_pos:
			player_length.pop()
		else:
			cookie_pos = random_position(board_size)

		player_length.insert(0, projected_tile)
		print("player_length: ", player_length)
		print("cookie_pos:", cookie_pos)
		head = projected_tile
		print(projected_tile)

		'''
		DRAWING THE BOARD
		'''

		#clear screen
		screen.fill(background)

		#draw the player
		for pos in player_length:
			rect = pygame.Rect(pos[0]*tile_size, pos[1]*tile_size, tile_size-2, tile_size-2)
			screen.fill(color=body, rect=rect)
		pygame.display.flip()
		#draw the cookie
		rect1 = pygame.Rect(cookie_pos[0]*tile_size, cookie_pos[1]*tile_size, tile_size-2, tile_size-2)
		screen.fill( color=(255,0,0), rect=rect1)
		#draw the score
		#font_screen = my_font.render(score_text, color=black)
		#screen.blit(font_screen, font_position)

		pygame.display.flip()

		nums = time.time() - begin
		if nums < target:
			print("waiting: ", target-nums)
			time.sleep(target-nums)
main()
