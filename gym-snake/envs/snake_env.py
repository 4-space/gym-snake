import gym
from gym import error, spaces, utils
from gym.utils import seeding

class SnakeEnv(gym.Env):
	metadata = {'render.modes': ['']}

	action_space = ["left", "right", "up", "down", "none"]
	observation_space =

	def __init__(self, tile_size, board_size, num_agents,):
		self.tile_size = tile_size
		self.board_size = board_size

		self.num_agents = num_agents
		self.game_size = self.tile_size * self.board_size
		self.cookie_pos = []

		self.players = []
		for i in num_agents:
			new_player = []
			new_player.push(_random_position(self.board_size))
			self.players.push(new_player)

		#initialize the screen

		self.screen = pygame.display.set_mode(screen_size)

	"""
	Returns a random position, a 2-tuple representing (x,y) position

	board_size: int - a int representing the nxn size of the board
	"""
	def _random_position(board_size):
		return random.randint(0,board_size-1), random.randint(0,board_size-1)

	"""
	Given input direction, calculate the projected tile that the snake is going to go to on the next time step

	dir: string - direction that the snake is traveling

	projected_tile: 2-tuple - the projected tile that the snake will advance to given no user input
	"""
	def _calculate_proj(dir, projected_tile):
		if dir == "none":
			return projected_tile
		if dir == "up":
			return projected_tile[0], projected_tile[1]-1
		if dir == "down":
			return projected_tile[0], projected_tile[1]+1
		if dir == "left":
			return projected_tile[0]-1, projected_tile[1]
		else:
			return projected_tile[0]+1, projected_tile[1]

	def step(self, action):
		'''
		GAME LOGIC
		'''
		projected_tile = _calculate_proj(self.player_direction, self.head)

		assert(len(action) == self.num_agents)

		for i in range
			if act == "down" and player_direction != "up":
				projected_tile = head[0], head[1]+1
				player_direction = "down"
			if act == "up" and player_direction != "down":
				projected_tile = head[0], head[1]-1
				player_direction = "up"
			if act == "left" and player_direction != "right":
				projected_tile = head[0]-1, head[1]
				player_direction = "left"
			if act == "right" and player_direction != "left":
				projected_tile = head[0]+1, head[1]
				player_direction = "right"
			print(player_direction)

		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()

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

	def reset(self):
		self.__init__()
	def render(self, mode='human', close=False):
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
