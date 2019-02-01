import gym
from gym import error, spaces, utils
from gym.utils import seeding

class SnakeEnv(gym.Env):
	metadata = {'render.modes': ['']}

	action_space = ["left", "right", "up", "down", "none"]

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

	"""
	action: action array where len(action) == num_agents

	Returns
	observation: array
	reward: array
	done: boolean is true if episode is over (all agents are done)
	"""
	def step(self, action):
		'''
		GAME LOGIC
		'''
		#assign actions to players

		#get projected_tiles
		for player in self.players:
			player.projected_tile = _calculate_proj(player.player_direction, player.head)
			if act == "down" and player_direction != "up":
				player.projected_tile = head[0], head[1]+1
				player.direction = "down"
			if act == "up" and player_direction != "down":
				player.projected_tile = head[0], head[1]-1
				player.direction = "up"
			if act == "left" and player_direction != "right":
				player.projected_tile = head[0]-1, head[1]
				player.direction = "left"
			if act == "right" and player_direction != "left":
				player.projected_tile = head[0]+1, head[1]
				player.player_direction = "right"
			print(player_direction)

		#check for collisions
		for player in self.players:
			if player.projected_tile in self.get_obstacles() or self._crossed_boundary(player):
				#player is eliminated
				self.players.remove(player) #fix this line of code lol
		if self.players.empty():
			done = true

		#check for cookie collisions
		for player in self.players:
			if player.projected_tile not in self.cookie_locations:
				player.player_length.pop()

		#advance players
		for player in self.players:
			player.player_length.insert(0, player.projected_tile)

		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()

		#return array of observations, one for each players
		observation = self._get_observation()


		return observation, reward, done

	def reset(self):
		self.__init__()

	def render(self, mode='human', close=False):

		if mode == 'human':
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
			pygame.display.flip()
		if mode == 'rgb':
			#get rgb array and make video 
