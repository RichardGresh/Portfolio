# Richard Gresham
# CPSC 386-01
# 2021-11-29
# rgresham@csu.fullerton.edu
# @RichardScience
#
# Lab Snake
#
# This is where my Scenes are stored
#

"""This is my Scene File"""
import os
import json
import datetime
import pygame
import snakeplayer
import fruit


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
        # text_font = pygame.font.Font(pygame.font.get_default_font(), self._title_size - 5)
        # instructions1 = text_font.render('Instructions to Play: ', True, self.def_color)
        # instructions1_pos = instructions1.get_rect(center = (400, 250))
        # self._screen.blit(instructions1, instructions1_pos)

    def instructions(self):
        """This is user instruction"""
        text_font = pygame.font.Font(
            pygame.font.get_default_font(), self._title_size - 5
        )
        instructionlist = [
            "Instructions to Play: ",
            "Use the arrow keys to move the snake,",
            "Score points by eating apples and staying",
            "alive. You lose if your snake collides",
            "with itself or the boundary",
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
        self.w = w
        self.h = h
        self._snake = snakeplayer.Snake(screen, 1, self._frame_rate)
        self._fruit = fruit.Fruit(screen)
        self._changed_direction = False
        self._score = 0

    def draw(self):
        """This draws my pygame"""
        super().draw()
        bound1 = pygame.Surface([800, 40])
        bound1.fill((255, 255, 0))
        self._screen.blit(bound1, (0, 0))
        bound2 = pygame.Surface([40, 800])
        bound2.fill((255, 255, 0))
        self._screen.blit(bound2, (0, 0))
        bound3 = pygame.Surface([800, 760])
        bound3.fill((255, 255, 0))
        self._screen.blit(bound3, (0, 760))
        bound4 = pygame.Surface([760, 800])
        bound4.fill((255, 255, 0))
        self._screen.blit(bound4, (760, 0))
        self._snake.draw()
        self._fruit.draw()

    def process_event(self, event):
        """This processes keyboard movement"""
        super().process_event(event)
        print("hi this is game")
        if event.type == pygame.KEYDOWN:
            if not self._changed_direction:
                if event.key == pygame.K_DOWN:
                    if self._snake.direction != 3:
                        print("pressed down")
                        self._snake.move_down()
                        self._changed_direction = True
                elif event.key == pygame.K_UP:
                    if self._snake.direction != 4:
                        print("pressed up")
                        self._snake.move_up()
                        self._changed_direction = True
                elif event.key == pygame.K_LEFT:
                    if self._snake.direction != 2:
                        print("pressed left")
                        self._snake.move_left()
                        self._changed_direction = True
                elif event.key == pygame.K_RIGHT:
                    if self._snake.direction != 1:
                        print("pressed right")
                        self._snake.move_right()
                        self._changed_direction = True

    def update(self):
        """This updates the display"""
        fruitcheck = True
        self._snake.movement()
        self._snake.update()
        self.snake_collision()
        self._changed_direction = False
        if self.munch():
            self._snake.addlength()
            self._fruit.update()
            self._score = self._score + 5
            while fruitcheck:
                for i in range(0, len(self._snake.list_snake)):
                    if self._fruit.fruit_rect.collidepoint(
                        self._snake.list_snake[i][0], self._snake.list_snake[i][1]
                    ):
                        print("insidethesnake")
                        self._fruit.update()
                        fruitcheck = True
                        break
                    else:
                        fruitcheck = False

    def munch(self):
        """This goes through munch command"""
        if self._snake.list_snake[0][0] >= self._fruit.x and self._snake.list_snake[0][
            0
        ] < self._fruit.x + (self.w // 20):
            if self._snake.list_snake[0][1] >= self._fruit.y and self._snake.list_snake[
                0
            ][1] < self._fruit.y + (self.h // 20):
                print("collision occurred")
                return True

    def snake_collision(self):
        """This handles snake collision"""
        for i in range(1, len(self._snake.list_snake)):
            if self._snake.list_snake[0][0] >= self._snake.list_snake[i][
                0
            ] and self._snake.list_snake[0][0] < self._snake.list_snake[i][0] + (
                self.w // 20
            ):
                if self._snake.list_snake[0][1] >= self._snake.list_snake[i][
                    1
                ] and self._snake.list_snake[0][1] < self._snake.list_snake[i][1] + (
                    self.h // 20
                ):
                    self._is_valid = False


class TimedGameScreen(GameScene):
    """This is the Timed GameScene Class"""

    def __init__(self, screen, background_color):
        """This is my initialization of Class"""
        super().__init__(screen, background_color)
        self.currenttime = 0
        (w, h) = self._screen.get_size()
        self._x_boundary = (0, w)
        self._y_boundary = (0, h)
        self._previnttime = 0
        self._timestart = 0
        self._font = pygame.font.Font(pygame.font.get_default_font(), 24)
        self._timer = self._font.render(
            "Time: {}".format(self.currenttime), True, (0, 0, 0)
        )
        self._timer_pos = self._timer.get_rect(center=(600, 20))
        self._scorefont = self._font.render(
            "Score: {}".format(self._score), True, (0, 0, 0)
        )
        self._score_pos = self._scorefont.get_rect(center=(160, 20))

    def displayscore(self):
        """This displays score"""
        self._scorefont = self._font.render(
            "Score: {}".format(self._score), True, (0, 0, 0)
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
            "Time: {}".format(self.currenttime), True, (0, 0, 0)
        )
        if (
            int(self.currenttime) % 3 == 0
            and int(self.currenttime) != self._previnttime
        ):
            self._previnttime = int(self.currenttime)
            self._score = self._score + 1

    def start(self, score, time):
        """This is the starting data."""
        self._timestart = pygame.time.get_ticks()

    def boundary(self):
        """This creates my game boundary"""

        if self._snake.list_snake[0][0] > 720:
            self._snake.list_snake[0][0] = 720
            self._is_valid = False
        elif self._snake.list_snake[0][0] < 40:
            self._snake.list_snake[0][0] = 40
            self._is_valid = False
        if self._snake.list_snake[0][1] > 720:
            self._snake.list_snake[0][1] = 720
            self._is_valid = False
        elif self._snake.list_snake[0][1] < 40:
            self._snake.list_snake[0][1] = 40
            self._is_valid = False

    def end(self):
        """This end function of my class"""
        i = [self.currenttime, self._score, self._restart]
        return i

    def update(self):
        """This updates the display"""
        super().update()
        self.settime()
        self.displayscore()
        self.boundary()

    def draw(self):
        """This draws my pygame"""
        super().draw()
        self._screen.blit(self._timer, self._timer_pos)
        self._screen.blit(self._scorefont, self._score_pos)


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

    def sort_scores(self, json):
        """This sorts my score"""
        sorted_list = list()
        sorted_list = json
        sorted_list.sort(reverse=True)
        print(sorted_list)
        for i in range(0, len(json)):
            for j in range(0, len(json) - i - 1):
                if json[j][0] < json[j + 1][0]:
                    temp = json[j]
                    json[j] = json[j + 1]
                    json[j + 1] = temp
                elif json[j][0] == json[j + 1][0]:
                    if json[j][1] > json[j + 1][1]:
                        temp = json[j]
                        json[j] = json[j + 1]
                        json[j + 1] = temp
        print(json)
        return json

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
