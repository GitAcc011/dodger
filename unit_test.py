from leadearboard import Leaderboard
import dodger
import unittest
import pygame


class TestShop(unittest.TestCase):

    def test_leaderboard(self):
        # screen params
        pygame.init()
        width = 750
        height = 900
        main_res = (width, height)
        screen = pygame.display.set_mode(main_res)
        # leaderboard file check
        is_name_exist = False
        leaderboard = Leaderboard(screen)
        leaderboard.write_new_record(0)
        file_data = leaderboard.file_data
        for values in range(1, len(file_data)):
            current_num = int(file_data[values][1])
            if "Player" == file_data[values][0] and current_num >= 0:
                is_name_exist = True
        self.assertEqual(is_name_exist, True)
