import pygame
import random
from utils import blit_text_center
from elements import AbstractElement, Chase, Random, Escape
from game_info import GameInfo

pygame.init()
pygame.font.init()
MAIN_FONT = pygame.font.SysFont("comicsans", 44)
SCORE_FONT = pygame.font.Font('freesansbold.ttf', 32)
SCORE_X = 10
SCORE_Y = 10
FPS = 60
SECOND = 1000
WAIT_TIME = 5000
SCREEN = pygame.display.set_mode((800, 600))
CHASE_NAME = "Chase"
ESCAPE_NAME = "Escape"
RANDOM_NAME = "Random"

# set the caption of the game
pygame.display.set_caption("Mouse Race")
# load the images for the shapes
chase_shape = pygame.image.load('rectangle.png')
escape_shape = pygame.image.load('square.png')
random_shape = pygame.image.load('circle.png')

'''Draw the elements to the screen'''
def draw(elements, game_info):
    SCREEN.fill("white")
    # go over the list of elements
    for elem in elements:
        # call the move direction for each element
        elem.move_direction()
        # draw each element
        elem.draw_element()
        # show the score
        show_score(game_info)


'''Show the score to the screen'''
def show_score(game_info):
    score = SCORE_FONT.render("Score :" + str(game_info.score), True, (0, 0, 0))
    SCREEN.blit(score, (SCORE_X, SCORE_Y))


def main():
    # time to help keep track of when to update the score
    update_time = 0
    # list to hold the elements
    list_of_elems = []
    # initialize the pygame
    game_info = GameInfo()
    # Game Loop
    running = True
    clock = pygame.time.Clock()

    # loop to run the game
    while running:
        # control the speed of the game so that it won't run too fast
        clock.tick(FPS)

        # check of the game has started
        while not game_info.started:
            # start of game logic
            SCREEN.fill('white')
            blit_text_center(SCREEN, MAIN_FONT, "Press any key to start to Start")
            pygame.display.update()
            # follow the pygame events
            for event in pygame.event.get():
                # check if the quit button was pressed
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                # if a button was pressed start the game
                if event.type == pygame.KEYDOWN:
                    # update the time for the seconds timer to keep score
                    update_time = pygame.time.get_ticks()
                    game_info.start_game()
                    SCREEN.fill('white')
                    # create the elements
                    chase_elem1 = Chase(CHASE_NAME, chase_shape, random.uniform(0, 2), random.randint(2, 4), SCREEN,
                                        game_info)
                    # add element to array of elements
                    list_of_elems.append(chase_elem1)
                    # we can create and add more elements if we want to
                    # chase_elem2 = Chase(CHASE_NAME, chase_shape, random.uniform(0, 2), random.randint(2, 4),
                    # SCREEN, game_info)
                    # chase_elem3 = Chase(CHASE_NAME, chase_shape, random.uniform(0, 2), random.randint(2, 4),
                    # SCREEN, game_info)
                    # list_of_elems.append(chase_elem2)
                    # list_of_elems.append(chase_elem3)
                    random_elem1 = Random(RANDOM_NAME, random_shape, random.uniform(0, 2), random.randint(2, 4), SCREEN,
                                          game_info)
                    # add element to array of elements

                    list_of_elems.append(random_elem1)
                    # random_elem2 = Random(RANDOM_NAME, random_shape, random.uniform(0, 2), random.randint(2, 4),
                    # SCREEN, game_info)
                    # list_of_elems.append(random_elem2)
                    # random_elem3 = Random(RANDOM_NAME, random_shape, random.uniform(0, 2), random.randint(2, 4),
                    # SCREEN, game_info)
                    # list_of_elems.append(random_elem3)
                    escape_elem1 = Escape(ESCAPE_NAME, escape_shape, random.randint(0, 2), random.randint(1,5), SCREEN,
                                          game_info)
                    # add element to array of elements
                    list_of_elems.append(escape_elem1)
        # check if quit was pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
        # draw everything to the screen
        draw(list_of_elems, game_info)
        # get the current time
        current_time = pygame.time.get_ticks()
        # timer to update the score
        if current_time - update_time > SECOND:
            game_info.update_score()
            update_time = current_time
        # display the screen
        pygame.display.update()
        # ending the game
        if game_info.ended:
            blit_text_center(SCREEN, MAIN_FONT, f"Game Over! Your score is {game_info.score}")
            pygame.display.update()
            # pause for 5 seconds to let the play see what is written on the screen
            pygame.time.wait(WAIT_TIME)
            # clear the list of elements
            list_of_elems.clear()
            continue

    pygame.quit()


if __name__ == '__main__':
    main()
