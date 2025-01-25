# screen resolution, can adapt
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

#game constsants
ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 0.8  # seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS

PLAYER_RADIUS = 20 #player will secretly be a circle to make the calculus a little bit easier
PLAYER_SPEED = 200
PLAYER_TURN_SPEED = 300 #the player rotation speed when moving, can be changed later after testing (as well as player speed)

SHOT_RADIUS = 5
PLAYER_SHOOT_SPEED = 500
PLAYER_SHOOT_COOLDOWN = 0.3 #seconds