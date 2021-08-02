import pygame
import os

YELLOW = 'yellow'
GREEN = (143, 221, 143)
UPGRADE_BTN_IMAGE = pygame.transform.scale(pygame.image.load('images/upgrade.png'), (45, 35))
SELL_BTN_IMAGE = pygame.transform.scale(pygame.image.load('images/sell.png'), (35, 35))
MENU_BTN_IMAGE = pygame.transform.scale(pygame.image.load('images/upgrade_menu.png'), (180, 180))


class UpgradeMenu:
    def __init__(self, x, y):
        self.x = x      # the tower center x
        self.y = y      # the tower center y
        self.__buttons = [Button(UPGRADE_BTN_IMAGE, "upgrade", self.x, self.y - 75),
                          Button(SELL_BTN_IMAGE, "sell", self.x, self.y + 75)]
        # (Q2) Add buttons here, button upgrade and sell
        self.menu = MENU_BTN_IMAGE              # menu image
        self.upgrade = UPGRADE_BTN_IMAGE        # upgrade image
        self.sell = SELL_BTN_IMAGE              # sell image

    def draw(self, win):
        """
        (Q1) draw menu itself and the buttons
        (This method is call in draw() method in class TowerGroup)
        :return: None
        """
        # draw menu
        win.blit(self.menu, (self.x-90, self.y-90))
        # draw button
        # (Q2) Draw buttons here
        win.blit(self.upgrade, (self.x - 23, self.y - 82))
        win.blit(self.sell, (self.x - 20, self.y + 50))

        pass

    def get_buttons(self):
        """
        (Q1) Return the button list.
        (This method is call in get_click() method in class TowerGroup)
        :return: list
        """
        # Getter, let get button list
        return self.__buttons
        pass


class Button:
    def __init__(self, image, name, x, y):
        self.name = name                    # button name
        self.image = image                  # button image
        self.rect = self.image.get_rect()   # get button image rect
        self.rect.center = (x, y)           # the rect center (x, y)

    def clicked(self, x, y):
        """
        (Q2) Return Whether the button is clicked
        (This method is call in get_click() method in class TowerGroup)
        :param x: mouse x
        :param y: mouse y
        :return: bool
        """
        if self.rect.collidepoint(x, y):        # determined mouse click in button image or not
            return True
        else:
            return False
        pass

    def response(self):
        """
        (Q2) Return the button name.
        (This method is call in get_click() method in class TowerGroup)
        :return: str
        """
        # print(self.name)      # use to test
        return self.name        # return you click button's name
        pass






