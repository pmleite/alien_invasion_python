class Settings:

    def __init__(self):
        self.screen_width       = 0
        self.screen_heigth      = 0
        self.bg_image           = "images/background.jpg"
        self.alien_image        = "images/alien.png"
        self.ship_image         = "images/ship.png"
        self.caption            = "Alien Invasion by Paulo Leite"
        self.ship_speed         = 0.8


        self.bullet_speed       = 1.0
        self.bullet_width       = 900
        self.bullet_height      = 25
        self.bullet_color       = (83,220,83)
        self.bullets_allowed    = 10

        self.alien_speed        = 0.5
        self.fleet_drop_speed   = 10
        self.fleet_direction    = 1
        self.ship_limit         = 3
        self.speedup_scale      = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed     = 1.5
        self.bullet_speed   = 3.0
        self.alien_speed    = 1.0
        self.fleet_direction = 1
    
    def increase_speed(self):
        self.ship_speed     *= self.speedup_scale
        self.bullet_speed   *= self.speedup_scale
        self.alien_speed    *= self.speedup_scale







 
