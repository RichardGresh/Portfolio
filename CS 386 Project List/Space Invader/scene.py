# Richard Gresham
# CPSC 386-01
# 2021-12-13
# rgresham@csu.fullerton.edu
# @RichardScience
#
# Lab spaceinvaders
#
# This is where my Scenes are.
#


"""This is my Scene File"""
import os
import json
import datetime
import pygame
import random
from laser import Laser
import obstacle
import ship
import alien
import explosion


class Scene:
    """This is the Scene Class"""

    def __init__(self, screen, background_color):
        """This is my initialization of Class"""
        self._is_valid = True
        self._frame_rate = 60
        self._screen = screen
        self._background = pygame.Surface(self._screen.get_size())
        self._background_color = background_color
        self._background.fill(self._background_color)
        self._restart = False

    def is_valid(self):
        """This returns if the key is valid"""
        return self._is_valid

    def frame_rate(self):
        """This returns my framerate"""
        return self._frame_rate

    def draw(self):
        """This draws my pygame"""
        self._screen.blit(self._background, (0, 0))

    def start(self, score, time):
        """This is the starting data"""
        print("scene start")

    def end(self):
        """This is the end function of my class"""
        i = [0, 0, self._restart]
        return i

    def update(self):
        """This updates the display"""
        pygame.display.update()

    def process_event(self, event):
        """This processes keyboard movement"""
        if event.type == pygame.QUIT:
            print("exitgame")
            self._is_valid = False


class TitleScene(Scene):
    """This is the TitleScene Class"""

    def __init__(self, screen, background_color, title, title_color, title_size):
        """This is my initialization of Class"""
        super().__init__(screen, background_color)
        self._title_size = title_size
        title_font = pygame.font.Font(pygame.font.get_default_font(), title_size)
        self._title = title_font.render(title, True, title_color)
        (w, h) = self._screen.get_size()
        self._title_pos = self._title.get_rect(center=(w / 2, h / 4))

    def draw(self):
        """This draws my pygame"""
        super().draw()
        self._screen.blit(self._title, self._title_pos)

    def process_event(self, event):
        """This updates the display"""
        if event.type == pygame.KEYDOWN:
            print("pressed any key")
            self._is_valid = False


class BlinkingTitleScene(TitleScene):
    """This is the BlinkingTitleScene Class"""

    def __init__(self, screen, background_color, title, title_color, title_size):
        """This is my initialization of Class"""
        super().__init__(screen, background_color, title, title_color, title_size)
        self._title_complement_color = (
            255 - title_color[0],
            255 - title_color[1],
            255 - title_color[2],
        )
        self._counter = 0
        self._message = title
        self.color_speed = 1
        self.color_direction = [-1, 1, -1]
        self.def_color = [120, 120, 240]
        self.minimum_color = 0
        self.maximum_color = 255

    def update(self):
        """This updates the display"""
        super().update()
        self.color_change()

    def draw(self):
        """This draws my pygame"""
        title_font = pygame.font.Font(pygame.font.get_default_font(), self._title_size)
        self._title = title_font.render(self._message, True, self.def_color)
        self._screen.blit(self._title, self._title_pos)
        super().draw()
        self.instructions()

    def instructions(self):
        """This is user instruction"""
        text_font = pygame.font.Font(
            pygame.font.get_default_font(), self._title_size - 5
        )
        instructionlist = [
            "Instructions to Play: ",
            "Use the left and right arrow keys to move the tank,",
            "Press space to fire, Score points by",
            "blowing up aliens and staying alive. You lose if you",
            "run out of lives or you collide with the alien ship",
        ]
        locationlist = [(400, 250), (400, 300), (400, 350), (400, 400), (400, 450)]
        for i in range(0, len(instructionlist)):
            instructions1 = text_font.render(instructionlist[i], True, self.def_color)
            instructions1_pos = instructions1.get_rect(center=locationlist[i])
            self._screen.blit(instructions1, instructions1_pos)

    def color_change(self):
        """This causes color change"""
        for i in range(3):
            self.def_color[i] += self.color_speed * self.color_direction[i]
            if (
                self.def_color[i] >= self.maximum_color
                or self.def_color[i] <= self.minimum_color
            ):
                self.color_direction[i] *= -1


class GameScene(Scene):
    """This is the GameScene Class"""

    def __init__(self, screen, background_color):
        """This is my initialization of Class"""
        super().__init__(screen, background_color)
        (w, h) = self._screen.get_size()
        self._score = 0
        self.main_dir = os.path.split(os.path.abspath(__file__))[0]
        self._congrats = False
        self.Audio_dir = os.path.join(self.main_dir, "Audio")
        self.image_dir = os.path.join(self.main_dir, "image")
        sound = os.path.join(self.Audio_dir, "Laser.wav")
        self.lasersound = pygame.mixer.Sound(sound)
        sound = os.path.join(self.Audio_dir, "Explosion.wav")
        self.Explosionsound = pygame.mixer.Sound(sound)
        sound = os.path.join(self.Audio_dir, "MerryChristmas.wav")
        self.MerryChristmas = pygame.mixer.Sound(sound)
        self.lasersound.set_volume(0.2)
        self.Explosionsound.set_volume(0.2)
        self.MerryChristmas.set_volume(0.4)
        self.players = pygame.sprite.GroupSingle()
        self._player = ship.Player(screen, self.main_dir, self.Audio_dir, (w // 2, h))
        self.players.add(self._player)
        main_dir = os.path.split(os.path.abspath(__file__))[0]
        image_dir = os.path.join(self.main_dir, "image")
        file = os.path.join(main_dir, "image", "snowyday.png")
        self._background = pygame.image.load(file).convert_alpha()
        self._background = pygame.transform.scale(self._background, (w, h))

    def start(self, score, time):
        """This calls a previous start function"""
        print("hi")
        sound = os.path.join(self.Audio_dir, "ChristmasMelody.wav")
        pygame.mixer.music.load(sound)
        pygame.mixer.music.set_volume(0.30)
        pygame.mixer.music.play(-1)

    def draw(self):
        """This draws my pygame"""
        self._screen.blit(self._background, (0, 0))
        self._player.lasers.draw(self._screen)
        self.players.draw(self._screen)

    def process_event(self, event):
        """This processes keyboard movement"""
        super().process_event(event)

    def update(self):
        """This updates the display"""
        self._player.player_input()
        self._player.boundary()
        self._player.lasercharger()
        self._player.lasers.update()


class ObstGameScene(GameScene):
    """This is the obstacle add-in"""

    def __init__(self, screen, background_color):
        """This initializes my obstacles"""
        super().__init__(screen, background_color)
        self.shape = [
            "     00     ",
            "    0300    ",
            "   020030   ",
            "  00030000  ",
            " 0020002000 ",
            "003000000200",
            "    1111    ",
            "    1111    ",
        ]
        self.cube_size = 8
        self.bobthebuilderblocks = pygame.sprite.Group()
        self.createobstacle(150, 600, (0, 200, 400))

    def buildingblocks(self, xbegin, ybegin, locations):
        """This creates the blocks of my tree."""
        for row_index, row in enumerate(self.shape):
            for column_index, column in enumerate(row):
                if column == "0":
                    xcoord = xbegin + column_index * self.cube_size + locations
                    ycoord = ybegin + row_index * self.cube_size
                    self.bobthebuilderblocks.add(
                        obstacle.Obstacle(self.cube_size, (66, 105, 47), xcoord, ycoord)
                    )
                if column == "1":
                    xcoord = xbegin + column_index * self.cube_size + locations
                    ycoord = ybegin + row_index * self.cube_size
                    self.bobthebuilderblocks.add(
                        obstacle.Obstacle(self.cube_size, (150, 75, 0), xcoord, ycoord)
                    )
                elif column == "2":
                    xcoord = xbegin + column_index * self.cube_size + locations
                    ycoord = ybegin + row_index * self.cube_size
                    self.bobthebuilderblocks.add(
                        obstacle.Obstacle(self.cube_size, (255, 0, 0), xcoord, ycoord)
                    )
                elif column == "3":
                    xcoord = xbegin + column_index * self.cube_size + locations
                    ycoord = ybegin + row_index * self.cube_size
                    self.bobthebuilderblocks.add(
                        obstacle.Obstacle(self.cube_size, (0, 0, 255), xcoord, ycoord)
                    )

    def createobstacle(self, x_begin, y_begin, locations):
        """This is the set up that says make it in three locations."""
        for xoffset in locations:
            self.buildingblocks(x_begin, y_begin, xoffset)

    def draw(self):
        """Draws the trees"""
        super().draw()
        self.bobthebuilderblocks.draw(self._screen)

    def update(self):
        """updates everything"""
        super().update()

    def process_event(self, event):
        """Processes previous events"""
        super().process_event(event)


class AlienGameScreen(ObstGameScene):
    """This sets up the alien board and movement"""

    def __init__(self, screen, background_color):
        """Initializes the board and alien"""
        super().__init__(screen, background_color)
        self.alienshape = [
            "00000000000",
            "00000000000",
            "00000000000",
            "00000000000",
            "00000000000",
        ]
        self._aliensize = (60, 30)
        self.alienspeed = 1
        self.aliengroup = pygame.sprite.Group()
        self.alienboard(75, 100)
        self.aliendirection = 1
        (w, h) = self._screen.get_size()
        self.h = h

    def alienboard(self, xbegin, ybegin):
        """This provides placement for my alien in a row/column setup"""
        for row_index, row in enumerate(self.alienshape):
            for column_index, column in enumerate(row):
                if column == "0":
                    xcoord = xbegin + column_index * self._aliensize[0]
                    ycoord = ybegin + row_index * self._aliensize[1]
                    position = (xcoord, ycoord)
                    self.aliengroup.add(
                        alien.Alien(
                            self._screen,
                            self.main_dir,
                            position,
                            self._aliensize,
                            self.alienspeed,
                        )
                    )

    def alienmove(self):
        """This tells the alien that when it reaches a border move opposite direction"""
        aliengroup = self.aliengroup.sprites()
        for alien in aliengroup:
            if alien.rect.left <= 0:
                self.aliendirection = 1
            if alien.rect.right >= 800:
                self.aliendirection = -1

    def draw(self):
        """draws my aliens"""
        super().draw()
        self.aliengroup.draw(self._screen)

    def update(self):
        """updates alien movement"""
        super().update()
        self.alienmove()
        self.aliengroup.update(self.aliendirection)

    def process_event(self, event):
        """Processes previous events."""
        super().process_event(event)


class Alienbulletcollision(AlienGameScreen):
    """This controls my alien bullet and collision detection"""

    def __init__(self, screen, background_color):
        """This initializes my alien bullet and sets up collision"""
        super().__init__(screen, background_color)
        (w, h) = self._screen.get_size()
        self.w = w
        self.h = h
        self.alienlaser = pygame.sprite.Group()
        self._lasercharged = True
        self._alienlag = 500
        self._lasertime = 0
        self.playerlives = 3
        self.lifegoal = 40
        self._font = pygame.font.Font(pygame.font.get_default_font(), 24)
        self._life = self._font.render(
            "Lives: {}".format(self.playerlives), True, (255, 255, 255)
        )
        self._life_pos = self._life.get_rect(center=(400, 20))
        self.explosion = pygame.sprite.Group()

    def alienShoot(self):
        """This gives a random chance of which alien will shoot every 500ms"""
        if self.aliengroup.sprites() and self._lasercharged:
            alienshooter = random.choice(self.aliengroup.sprites())
            laser = Laser(alienshooter.rect.center, (255, 0, 0), self._screen, False)
            self.alienlaser.add(laser)
            self.lasersound.play()
            self._lasercharged = False
            self._lasertime = pygame.time.get_ticks()

    def lifeupdate(self):
        """This updates the life totals in my game"""
        self._life = self._font.render(
            "Lives: {}".format(self.playerlives), True, (255, 255, 255)
        )

    def lasercharger(self):
        """This checks the time to see if it should allow my alien to fire its laser again"""
        if self._lasercharged == False:
            current_time = pygame.time.get_ticks()
            if current_time - self._lasertime >= self._alienlag:
                self._lasercharged = True

    def draw(self):
        """This draws all of my images"""
        super().draw()
        self.alienlaser.draw(self._screen)
        self._screen.blit(self._life, self._life_pos)
        self.explosion.draw(self._screen)

    def update(self):
        """Updates my life total alien, and alien laser, as well as my explosion."""
        super().update()
        self.lasercharger()
        self.alienShoot()
        self.alienlaser.update()
        self.spritecollision()
        self.lifeupdate()
        self.explosion.update()

    def process_event(self, event):
        """Processes previous events."""
        super().process_event(event)

    def spritecollision(self):
        """Tests collision between objects"""
        if self.alienlaser.sprites():
            for laser in self.alienlaser:
                if pygame.sprite.spritecollide(laser, self.bobthebuilderblocks, True):
                    print("collide with block")
                    laser.kill()
                if pygame.sprite.spritecollide(laser, self.players, True):
                    laser.kill()
                    print("collide with player")
                    self.playerlives = self.playerlives - 1
                    if self.playerlives != 0:
                        self.explosion.add(
                            explosion.Explosion(
                                self.main_dir, laser.rect.x, laser.rect.y, 3
                            )
                        )
                        self._player = ship.Player(
                            self._screen,
                            self.main_dir,
                            self.Audio_dir,
                            (self.w // 2, self.h),
                        )
                        self.players.add(self._player)
                        self.Explosionsound.play()
                    if self.playerlives <= 0:
                        pygame.mixer.music.fadeout(3000)
                        self._is_valid = False
        if self._player.lasers.sprites():
            for laser in self._player.lasers:
                if pygame.sprite.spritecollide(laser, self.bobthebuilderblocks, True):
                    print("collide with block")
                    laser.kill()
                for alien in self.aliengroup:
                    if pygame.sprite.collide_rect(laser, alien):
                        self.explosion.add(
                            explosion.Explosion(
                                self.main_dir, laser.rect.x, laser.rect.y, 3
                            )
                        )
                        laser.kill()
                        alien.kill()
                        self.Explosionsound.play()
                        self._score = self._score + 1
                        if self._score == self.lifegoal:
                            self.playerlives = self.playerlives + 1
                            self.lifegoal = self.lifegoal + 40
        if self.aliengroup.sprites():
            for alien in self.aliengroup:
                if pygame.sprite.spritecollide(alien, self.players, True):
                    alien.kill()
                    self.playerlives = 0
                    if self.playerlives <= 0:
                        pygame.mixer.music.fadeout(3000)
                        self._is_valid = False


class TimedGameScreen(Alienbulletcollision):
    """This is the Timed GameScene Class"""

    def __init__(self, screen, background_color):
        """This is my initialization of Class"""
        super().__init__(screen, background_color)
        self.currenttime = 0
        (w, h) = self._screen.get_size()
        self._x_boundary = (0, w)
        self._y_boundary = (0, h)
        self._timestart = 0
        self._font = pygame.font.Font(pygame.font.get_default_font(), 24)
        self._timer = self._font.render(
            "Time: {}".format(self.currenttime), True, (255, 255, 255)
        )
        self._timer_pos = self._timer.get_rect(center=(600, 20))
        self._scorefont = self._font.render(
            "Score: {}".format(self._score), True, (255, 255, 255)
        )
        self._score_pos = self._scorefont.get_rect(center=(160, 20))
        self.background_color = background_color

    def displayscore(self):
        """This displays score"""
        self._scorefont = self._font.render(
            "Score: {}".format(self._score), True, (255, 255, 255)
        )

    def settime(self):
        """This sets initial time"""
        pygame.time.Clock().tick(60)
        timer = pygame.time.get_ticks()
        finaltime = timer - self._timestart
        finaltime = finaltime / 1000
        finaltime = round(finaltime, 2)
        self.currenttime = finaltime
        self._timer = self._font.render(
            "Time: {}".format(self.currenttime), True, (255, 255, 255)
        )

    def start(self, score, time):
        """This is the starting data."""
        super().start(score, time)
        self._timestart = pygame.time.get_ticks()

    def end(self):
        """This end function of my class"""
        i = [self.currenttime, self._score, self._restart]
        return i

    def update(self):
        """This updates the display"""
        super().update()
        self.settime()
        self.displayscore()
        if not self.aliengroup.sprites():
            self.roundovercheck()

    def draw(self):
        """This draws my pygame"""
        super().draw()
        self._screen.blit(self._timer, self._timer_pos)
        self._screen.blit(self._scorefont, self._score_pos)

    def roundovercheck(self):
        """This is a side screen to Congratulate the player."""
        (w, h) = self._screen.get_size()
        pausetime = self.currenttime
        pausescore = self._score
        pauselives = self.playerlives
        pausegoal = self.lifegoal
        second_surface = pygame.Surface(self._screen.get_size())
        second_surface.fill((0, 0, 0))
        font = self._font
        congrats = font.render(
            "Congratulations you finished the round", True, (255, 255, 255)
        )
        congrats_pos = congrats.get_rect(center=(w / 2, h / 4))
        instruct = font.render(
            "Press any key to play next round.", True, (255, 255, 255)
        )
        instruct_pos = instruct.get_rect(center=(w / 2, h / 4 + h / 8))

        run = True
        self.MerryChristmas.play()
        while run:
            self._screen.blit(second_surface, (0, 0))
            self._screen.blit(congrats, congrats_pos)
            self._screen.blit(instruct, instruct_pos)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    print("pressed any key")
                    run = False
            if run == False:
                self.__init__(self._screen, self.background_color)
                self._score = pausescore
                self.currenttime = pausetime
                self.playerlives = pauselives
                self.lifegoal = pausegoal
                self.alienspeed = self.alienspeed + pausescore // 100
                self._alienlag = self._alienlag - pausescore // 10


class EndScene(Scene):
    """This is the EndScene Class"""

    def __init__(self, screen, background_color):
        """This is my initialization of Class"""
        super().__init__(screen, background_color)
        self._finalscore = 0
        self._finaltime = 0
        self._endfont = pygame.font.Font(pygame.font.get_default_font(), 31)
        self._endmessage = self._endfont.render("Game Over!", True, (0, 0, 0))
        self._endmessage_pos = self._endmessage.get_rect(center=(400, 100))
        self._endfont2 = pygame.font.Font(pygame.font.get_default_font(), 24)
        self._endscoremessage = self._endfont2.render(
            "Final Score: {} points.".format(self._finalscore), True, (0, 0, 0)
        )
        self._endscoremessage_pos = self._endscoremessage.get_rect(center=(600, 150))
        self._endtimemessage = self._endfont2.render(
            "Final Time: {} seconds.".format(self._finaltime), True, (0, 0, 0)
        )
        self._endtimemessage_pos = self._endtimemessage.get_rect(center=(200, 150))

    def start(self, score, time):
        """This is the starting data"""
        self._finalscore = score
        self._finaltime = time

    def update(self):
        """This updates the display"""
        self._endscoremessage = self._endfont2.render(
            "Final Score: {} points.".format(self._finalscore), True, (0, 0, 0)
        )
        self._endtimemessage = self._endfont2.render(
            "Final Time: {} seconds.".format(self._finaltime), True, (0, 0, 0)
        )

    def draw(self):
        """This draws my pygame"""
        self._screen.blit(self._background, (0, 0))
        self._screen.blit(self._endmessage, self._endmessage_pos)
        self._screen.blit(self._endscoremessage, self._endscoremessage_pos)
        self._screen.blit(self._endtimemessage, self._endtimemessage_pos)
        lastmessage = self._endfont2.render(
            "Press e to exit or r to restart the game", True, (0, 0, 0)
        )
        lastmessage_pos = lastmessage.get_rect(center=(400, 200))
        self._screen.blit(lastmessage, lastmessage_pos)

    def process_event(self, event):
        """This processes keyboard movement"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                self._is_valid = False
            if event.key == pygame.K_r:
                self._is_valid = False
                self._restart = True


class Leaderboard(EndScene):
    """This is the Leaderboard Class"""

    def __init__(self, screen, background_color):
        """This is my initialization of Class"""
        super().__init__(screen, background_color)
        self.file_score = self._finalscore
        self.file_time = self._finaltime
        self.font = pygame.font.Font(pygame.font.get_default_font(), 15)
        file_name = "highscore.json"
        self.file_name = file_name
        self.scores = None
        if not os.path.isfile(self.file_name):
            self.empty_file()
        if os.path.getsize(self.file_name) == 0:
            self.empty_file()
        print("leaderboard")

    def empty_file(self):
        """This is used if file is empty"""
        empty_score_file = open(self.file_name, "w")
        empty_score_file.write("[]")
        empty_score_file.close()

    def start(self, score, time):
        """This is the starting data"""
        super().start(score, time)
        self.file_score = score
        self.file_time = time
        self.save_score()

    def save_score(self):
        """This saves my score to the file"""
        if not self.scores is None:
            new_json_score = [
                self.file_score,
                self.file_time,
                str(datetime.datetime.now()),
            ]
            self.scores.append(new_json_score)
            self.scores = self.sort_scores(self.scores)
            highscore_file = open(self.file_name, "r+")
            highscore_file.write(json.dumps(self.scores))
        else:
            self.load_previous_scores()
            self.save_score()

    def sort_scores(self, scores):
        """This sorts my score"""
        sorted_list = list()
        sorted_list = scores
        sorted_list.sort(reverse=True)
        for i in range(0, len(scores)):
            for j in range(0, len(scores) - i - 1):
                if scores[j][0] < scores[j + 1][0]:
                    temp = scores[j]
                    scores[j] = scores[j + 1]
                    scores[j + 1] = temp
                elif scores[j][0] == scores[j + 1][0]:
                    if scores[j][1] > scores[j + 1][1]:
                        temp = scores[j]
                        scores[j] = scores[j + 1]
                        scores[j + 1] = temp
        return scores

    def load_previous_scores(self):
        """This loads my previous score"""
        with open(self.file_name, "r") as highscore_file:

            self.scores = json.load(highscore_file)
            self.scores = self.scores

    def draw(self):
        """This draws my pygame"""
        super().draw()
        yinc = 0
        max_scores = 20
        scoreranks = 1
        for score in self.scores:
            if scoreranks <= max_scores:
                self._screen.blit(self.font.render("Rank", 1, (0, 0, 0)), (210, 280))
                self._screen.blit(self.font.render("Score", 1, (0, 0, 0)), (270, 280))
                self._screen.blit(self.font.render("time", 1, (0, 0, 0)), (330, 280))
                self._screen.blit(self.font.render("Date", 1, (0, 0, 0)), (390, 280))
                self._screen.blit(
                    self.font.render("| ", 1, (0, 0, 0)), (200, 300 + yinc)
                )
                self._screen.blit(
                    self.font.render(str(scoreranks) + ". ", 1, (0, 0, 0)),
                    (210, 300 + yinc),
                )
                self._screen.blit(
                    self.font.render(" | ", 1, (0, 0, 0)), (260, 300 + yinc)
                )
                self._screen.blit(
                    self.font.render(str(score[0]), 1, (0, 0, 0)), (270, 300 + yinc)
                )
                self._screen.blit(
                    self.font.render(" | ", 1, (0, 0, 0)), (320, 300 + yinc)
                )
                self._screen.blit(
                    self.font.render(str(score[1]), 1, (0, 0, 0)), (330, 300 + yinc)
                )
                self._screen.blit(
                    self.font.render(" | ", 1, (0, 0, 0)), (380, 300 + yinc)
                )
                self._screen.blit(
                    self.font.render(str(score[2]), 1, (0, 0, 0)), (390, 300 + yinc)
                )
                self._screen.blit(
                    self.font.render(" | ", 1, (0, 0, 0)), (600, 300 + yinc)
                )
                yinc += 20
                scoreranks += 1
