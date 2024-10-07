import pygame
from constantes import *
from classBatalhas import *
import time
class Animacao():
    def __init__(self) -> None:
        self.rect_para_att = pygame.Rect(409, 167, 3, 120)
        #infos para o ataque sludge
        self.slude = pygame.transform.scale((pygame.image.load('img/sluge.jpeg')),(30, 30))
        self.beam = pygame.transform.scale((pygame.image.load('img/psybeam.png')),(50, 50))
        self.horn = pygame.transform.scale((pygame.image.load('img/mega.png')),(200, 70))
        self.leaf = pygame.transform.scale((pygame.image.load('img/leaf_2.png')),(80, 80))
        self.chop = pygame.transform.scale((pygame.image.load('img/Karate.png')),(80, 80))
        self.dchop = pygame.transform.scale((pygame.image.load('img/DKaraye.png')),(80, 80))
        self.thunder = pygame.transform.scale((pygame.image.load('img/Thunderboltsprite.png')), (30,110))
        self.tackle = pygame.transform.scale((pygame.image.load('img/Tackle.png')), (60,60))
        self.cut1 = pygame.transform.scale((pygame.image.load('img/Cut1.png')), (100,100))
        self.cut2 = pygame.transform.scale((pygame.image.load('img/Cut2.png')), (100,100))
        self.cut3 = pygame.transform.scale((pygame.image.load('img/Cut3.png')), (100,100))
        self.cut4 = pygame.transform.scale((pygame.image.load('img/Cut4.png')), (100,100))
        self.fcut1 = pygame.transform.scale((pygame.image.load('img/FCut1.png')), (100,100))
        self.fcut2 = pygame.transform.scale((pygame.image.load('img/FCut2.png')), (100,100))
        self.fcut3 = pygame.transform.scale((pygame.image.load('img/FCut3.png')), (100,100))
        self.fcut4 = pygame.transform.scale((pygame.image.load('img/FCut4.png')), (100,100))
        self.slam1 = pygame.transform.scale((pygame.image.load('img/Slam1.png')), (100,100))
        self.slam2 = pygame.transform.scale((pygame.image.load('img/Slam2.png')), (100,100))
        self.slam3 = pygame.transform.scale((pygame.image.load('img/Slam3.png')), (100,100))
        self.slam4 = pygame.transform.scale((pygame.image.load('img/Slam4.png')), (100,100))
        self.slam5 = pygame.transform.scale((pygame.image.load('img/Tackle.png')), (135,135))
        self.facade1 = pygame.transform.scale((pygame.image.load('img/Facade1.png')), (100,100))
        self.facade2 = pygame.transform.scale((pygame.image.load('img/Facade2.png')), (100,100))
        self.facade3 = pygame.transform.scale((pygame.image.load('img/Facade3.png')), (100,100))
        self.facade4 = pygame.transform.scale((pygame.image.load('img/Facade4.png')), (100,100))
        self.facade5 = pygame.transform.scale((pygame.image.load('img/Facade5.png')), (100,100))
        self.recover1 = pygame.transform.scale((pygame.image.load('img/recover1.png')), (60,60))
        self.recover2 = pygame.transform.scale((pygame.image.load('img/recover2.png')), (60,60))
        self.recover3 = pygame.transform.scale((pygame.image.load('img/recover3.png')), (60,60))
        self.recover4 = pygame.transform.scale((pygame.image.load('img/recover4.png')), (60,60))
        self.recover5 = pygame.transform.scale((pygame.image.load('img/recover5.png')), (60,60))
        self.recover6 = pygame.transform.scale((pygame.image.load('img/recover6.png')), (60,60))
        self.metal1 = pygame.transform.scale((pygame.image.load('img/Metal1.png')), (100,100))
        self.metal2 = pygame.transform.scale((pygame.image.load('img/Metal2.png')), (100,100))
        self.metal3 = pygame.transform.scale((pygame.image.load('img/Metal3.png')), (100,100))
        self.metal4 = pygame.transform.scale((pygame.image.load('img/Metal4.png')), (100,100))
        self.metal5 = pygame.transform.scale((pygame.image.load('img/Metal5.png')), (100,100))
        self.fpunch1 = pygame.transform.scale((pygame.image.load('img/Fire.png')), (130,130))
        self.fpunch2 = pygame.transform.scale((pygame.image.load('img/FPunch.png')), (130,130))
        self.tackle_mini = pygame.transform.scale((pygame.image.load('img/Tackle.png')), (30,30))
        self.tackle_cont = 0
        self.cut_cont = 0
        self.icut_cont = 0
        self.fcut_cont = 0
        self.slam_cont = 0
        self.fpunch_cont = 0
        self.facade_cont = 0
        self.recover_cont = 0
        self.ifacade_cont = 0
        self.metal_cont = 0
        self.slude_x = 160
        self.slude_y = 330
        self.beam_x = 439
        self.beam_y = 220
        self.horn_x = 340
        self.horn_y = 120
        self.leaf_x = 160
        self.leaf_y = 330
        self.chop_x = 0
        self.chop_y = 350
        self.dchop_x = 175
        self.dchop_y = 350
        self.thunder_rect_x = 385
        self.slude_rect = self.slude.get_rect()
        self.slude_rect.topleft = (self.slude_x, self.slude_y)
        self.slud_counter = 0
        self.beam_rect = self.slude.get_rect()
        self.beam_rect.topleft = (self.beam_x, self.beam_y)
        self.beam_counter = 0
        self.horn_rect = self.horn.get_rect()
        self.horn_rect.topleft = (self.horn_x, self.horn_y)
        self.horn_counter = 0
        self.leaf_rect = self.slude.get_rect()
        self.leaf_rect.topleft = (self.leaf_x, self.leaf_y)
        self.leaf_counter = 0
        self.chop_rect = self.slude.get_rect()
        self.chop_rect.topleft = (self.chop_x, self.chop_y)
        self.chop_counter = 0
        self.dchop_rect = self.dchop.get_rect()
        self.dchop_rect.topleft = (self.dchop_x, self.dchop_y)
        self.dchop_counter = 0
        self.leaf_animation_counter = 3
        self.chop_animation_counter = 1
        self.dchop_animation_counter = 1
        self.thunder_counter = 0
        self.slud_animation_counter = 3
        self.beam_animation_counter = 3
        self.horn_animation_counter = 3
        self.thunder_animation_counter = 12
        self.tackle_counter = 0
        self.tackle_animation_counter = 6
        self.itackle_counter = 0
        self.itackle_animation_counter = 6
        self.cut_counter = 0
        self.cut_animation_counter = 5
        self.icut_counter = 0
        self.icut_animation_counter = 5
        self.fcut_counter = 0
        self.fcut_animation_counter = 4
        self.slam_counter = 0
        self.slam_animation_counter = 4
        self.fpunch_counter = 0
        self.fpunch_animation_counter = 4
        self.facade_counter = 0
        self.facade_animation_counter = 4
        self.recover_counter = 0
        self.recover_animation_counter = 3
        self.ifacade_counter = 0
        self.ifacade_animation_counter = 4
        self.metal_counter = 0
        self.metal_animation_counter = 3
        self.itackle_cont = 0
        #outro ataque aqui
    def movimenta_slude(self):
        self.slud_counter += 1
        if self.slud_counter == self.slud_animation_counter:
            self.slud_counter = 0
            self.slude_rect.x += 25
            self.slude_rect.y -= 13
    def desenha_slude(self, window, bool):
        if bool:
            self.movimenta_slude()
            window.blit(self.slude, (self.slude_rect.x, self.slude_rect.y))
        if self.slude_rect.x > 439:
            self.slude_x = 160
            self.slude_y = 330

    def movimenta_thunder(self):
        self.thunder_counter += 1
        if self.thunder_counter == self.thunder_animation_counter:
            self.thunder_counter = 0
            self.thunder_rect_x += 50

    def desenha_thunder(self, window, bool):
        if bool:
            self.movimenta_thunder()
            window.blit(self.thunder, (self.thunder_rect_x, 150))

    def desenha_tackle(self, window, bool):
        if bool:
            if self.tackle_cont == 2:
                window.blit(self.tackle_mini, (440, 235))
            else:
                window.blit(self.tackle, (425, 220))
            self.tackle_counter += 1
            if self.tackle_counter == self.tackle_animation_counter:
                self.tackle_counter = 0
                self.tackle_cont += 1

    def desenha_cut(self, window, bool):
        if bool:
            if self.cut_cont == 1:
                window.blit(self.cut1, (425, 190))
            elif self.cut_cont == 2:
                window.blit(self.cut2, (425, 190))
            elif self.cut_cont == 3:
                window.blit(self.cut3, (425, 190))
            elif self.cut_cont == 4:
                window.blit(self.cut4, (425, 190))
            self.cut_counter += 1
            if self.cut_counter == self.cut_animation_counter:
                self.cut_counter = 0
                self.cut_cont += 1
    def desenha_slam(self, window, bool):
        if bool:
            if self.slam_cont == 1:
                window.blit(self.slam1, (405, 170))
            elif self.slam_cont == 2:
                window.blit(self.slam2, (405, 170))
            elif self.slam_cont == 3:
                window.blit(self.slam3, (405, 170))
            elif self.slam_cont == 4:
                window.blit(self.slam4, (405, 170))
            elif self.slam_cont == 5 or self.slam_cont == 6:
                window.blit(self.slam5, (405, 170))
            self.slam_counter += 1
            if self.slam_counter == self.slam_animation_counter:
                self.slam_counter = 0
                self.slam_cont += 1

    def desenha_facade(self, window, bool):
        if bool:
            if self.facade_cont == 1:
                window.blit(self.facade1, (425, 190))
            elif self.facade_cont == 2:
                window.blit(self.facade2, (425, 190))
            elif self.facade_cont == 3:
                window.blit(self.facade3, (425, 190))
            elif self.facade_cont == 4:
                window.blit(self.facade4, (425, 190))
            elif self.facade_cont == 5:
                window.blit(self.facade5, (425, 190))
            self.facade_counter += 1
            if self.facade_counter == self.facade_animation_counter:
                self.facade_counter = 0
                self.facade_cont += 1
    def desenha_metal(self, window, bool):
        if bool:
            if self.metal_cont == 1:
                window.blit(self.metal1, (425, 190))
            elif self.metal_cont == 2:
                window.blit(self.metal2, (425, 190))
            elif self.metal_cont == 3:
                window.blit(self.metal3, (425, 190))
            elif self.metal_cont == 4:
                window.blit(self.metal4, (425, 190))
            elif self.metal_cont == 5:
                window.blit(self.metal5, (425, 190))
            self.metal_counter += 1
            if self.metal_counter == self.metal_animation_counter:
                self.metal_counter = 0
                self.metal_cont += 1
    def movimenta_leaf(self):
        self.leaf_counter += 1
        if self.leaf_counter == self.leaf_animation_counter:
            self.leaf_counter = 0
            self.leaf_rect.x += 25
            self.leaf_rect.y -= 13
    def desenha_leaf(self, window, bool):
        if bool:
            self.movimenta_leaf()
            window.blit(self.leaf, (self.leaf_rect.x, self.leaf_rect.y))
        if self.leaf_rect.x > 439:
            self.leaf_x = 160
            self.leaf_y = 330

    def desenha_fcut(self, window, bool):
        if bool:
            if self.fcut_cont == 1 or self.fcut_cont == 9:
                window.blit(self.cut1, (415, 175))
            elif self.fcut_cont == 2 or self.fcut_cont == 10:
                window.blit(self.cut2, (415, 175))
            elif self.fcut_cont == 3 or self.fcut_cont == 11:
                window.blit(self.cut3, (415, 175))
            elif self.fcut_cont == 4 or self.fcut_cont == 12:
                window.blit(self.cut4, (415, 175))
            if self.fcut_cont == 5 or self.fcut_cont == 13:
                window.blit(self.fcut1, (415, 175))
            elif self.fcut_cont == 6 or self.fcut_cont == 14:
                window.blit(self.fcut2, (415, 175))
            elif self.fcut_cont == 7 or self.fcut_cont == 15:
                window.blit(self.fcut3, (415, 175))
            elif self.fcut_cont == 8 or self.fcut_cont == 16:
                window.blit(self.fcut4, (415, 175))
            self.fcut_counter += 1
            if self.fcut_counter == self.fcut_animation_counter:
                self.fcut_counter = 0
                self.fcut_cont += 1

    def desenha_itackle(self, window, bool):
        if bool:
            if self.itackle_cont == 2:
                window.blit(self.tackle_mini, (90, 365))
            else:
                window.blit(self.tackle, (90, 360))
            self.itackle_counter += 1
            if self.itackle_counter == self.itackle_animation_counter:
                self.itackle_counter = 0
                self.itackle_cont += 1

    def desenha_ifacade(self, window, bool):
        if bool:
            if self.ifacade_cont == 1:
                window.blit(self.facade1, (90, 360))
            elif self.ifacade_cont == 2:
                window.blit(self.facade2, (90, 360))
            elif self.ifacade_cont == 3:
                window.blit(self.facade3, (90, 360))
            elif self.ifacade_cont == 4:
                window.blit(self.facade4, (90, 360))
            elif self.ifacade_cont == 5:
                window.blit(self.facade5, (90, 360))
            self.ifacade_counter += 1
            if self.ifacade_counter == self.ifacade_animation_counter:
                self.ifacade_counter = 0
                self.ifacade_cont += 1

    def movimenta_chop(self):
        self.chop_counter += 1
        if self.chop_counter == self.chop_animation_counter:
            self.chop_counter = 0
            self.chop_rect.x += 10
    def desenha_chop(self, window, bool):
        if bool:
            self.movimenta_chop()
            window.blit(self.chop, (self.chop_rect.x, self.chop_rect.y))
        if self.chop_rect.x > 155:
            self.chop_x = 25
            self.chop_y = 350
        
    def movimenta_beam(self):
        self.beam_counter += 1
        if self.beam_counter == self.beam_animation_counter:
            self.beam_counter = 0
            self.beam_rect.x -= 25
            self.beam_rect.y += 13
    def desenha_beam(self, window, bool):
        if bool:
            self.movimenta_beam()
            window.blit(self.beam, (self.beam_rect.x, self.beam_rect.y))
        if self.beam_rect.x < 180:
            self.beam_x = 439
            self.beam_y = 220
    def desenha_fpunch(self, window, bool):
        if bool:
            if self.fpunch_cont == 1 or self.fpunch_cont == 2:
                window.blit(self.fpunch1, (80, 320))
            elif self.fpunch_cont == 3 or self.fpunch_cont == 4:
                window.blit(self.fpunch2, (80, 320))
            elif self.fpunch_cont == 5:
                window.blit(self.tackle, (60, 320))
            self.fpunch_counter += 1
            if self.fpunch_counter == self.fpunch_animation_counter:
                self.fpunch_counter = 0
                self.fpunch_cont += 1

    def desenha_recover(self, window, bool):
        if bool:
            if self.recover_cont == 1:
                window.blit(self.recover1, (460, 180))
                window.blit(self.recover1, (430, 240))
                window.blit(self.recover1, (390, 160))
            elif self.recover_cont == 2:
                window.blit(self.recover2, (460, 180))
                window.blit(self.recover2, (430, 240))
                window.blit(self.recover2, (390, 160))
            elif self.recover_cont == 3:
                window.blit(self.recover3, (460, 180))
                window.blit(self.recover3, (430, 240))
                window.blit(self.recover3, (390, 160))
            elif self.recover_cont == 4:
                window.blit(self.recover4, (460, 180))
                window.blit(self.recover4, (430, 240))
                window.blit(self.recover4, (390, 160))
            elif self.recover_cont == 5:
                window.blit(self.recover5, (460, 180))
                window.blit(self.recover5, (430, 240))
                window.blit(self.recover5, (390, 160))
            elif self.recover_cont == 6:
                window.blit(self.recover6, (460, 180))
                window.blit(self.recover6, (430, 240))
                window.blit(self.recover6, (390, 160))
            self.recover_counter += 1
            if self.recover_counter == self.recover_animation_counter:
                self.recover_counter = 0
                self.recover_cont += 1

    def desenha_icut(self, window, bool):
        if bool:
            if self.icut_cont == 1:
                window.blit(self.cut1, (90, 360))
            elif self.icut_cont == 2:
                window.blit(self.cut2, (90, 360))
            elif self.icut_cont == 3:
                window.blit(self.cut3, (90, 360))
            elif self.icut_cont == 4:
                window.blit(self.cut4, (90, 360))
            self.icut_counter += 1
            if self.icut_counter == self.icut_animation_counter:
                self.icut_counter = 0
                self.icut_cont += 1

    def movimenta_horn(self):
        self.horn_counter += 1
        if self.horn_counter == self.horn_animation_counter:
            self.horn_counter = 0
            self.horn_rect.x -= 25
            self.horn_rect.y += 18
    def desenha_horn(self, window, bool):
        if bool:
            self.movimenta_horn()
            window.blit(self.horn, (self.horn_rect.x, self.horn_rect.y))
        if self.horn_rect.x < 80:
            self.horn_x = 340
            self.horn_y = 120

    def movimenta_dchop(self):
        self.chop_counter += 1
        if self.chop_counter == self.chop_animation_counter:
            self.chop_counter = 0
            self.chop_rect.x += 10
        self.dchop_counter += 1
        if self.dchop_counter == self.dchop_animation_counter:
            self.dchop_counter = 0
            self.dchop_rect.x -= 10
    def desenha_dchop(self, window, bool):
        if bool:
            self.movimenta_dchop()
            window.blit(self.chop, (self.chop_rect.x, self.chop_rect.y))
            window.blit(self.dchop, (self.dchop_rect.x, self.dchop_rect.y))
