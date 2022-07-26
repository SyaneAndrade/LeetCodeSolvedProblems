# -*- coding: utf-8 -*-

from distutils.command.build import build
from turtle import right


class Solution:
    def getSkyline(self, buildings):

        skyline = [[buildings[0][0], buildings[0][2]]]
        amount_builds = len(buildings)
        size_skyline = 1
        build_now = self.create_dict_build(buildings[0])
        for i in range(1 , amount_builds):
        # estão merged se o inicio ou final do proximo predio esta dentro do intervalo do anterior
            build_now = self.create_dict_build(buildings[i])
            build_before = self.create_dict_build(buildings[i-1])
            line_now = self.create_dict_line([build_now['left'], build_now['height']])
            line_before = self.create_dict_line(skyline[size_skyline-1])
            is_merged = self.merged(build_now, build_before)
            if is_merged:
                self.begin_line(build_now, build_before, line_now)
            else:
                self.create_ground(build_before['height'], skyline, size_skyline)
            is_insert = self.can_insert_line(line_now, line_before)
            if is_insert:
                skyline.append([line_now['begin'], line_now['height']])
                size_skyline+=1
            elif self.is_modify_skyline:
                skyline[size_skyline-1] = [line_now['begin'], line_now['height']]
            #inicio_fim(buildings[i-1], buildings[i])
            # mesmo_inicio_fim_diferente
            # mesmo_inicio_mesmo_fim
            # inicio_diferente_mesmo_fim
            #     se_altura_e_igual
        self.create_ground(build_now['right'], skyline, size_skyline)
        return skyline
    
    def merged(self, build_now, build_before):
        is_merged = False
        if build_before['right'] >= build_now['left']:
            is_merged = True
        return is_merged

    def begin_line(self, build_now, build_before, line):
        if build_now['left'] > build_before['left']:
            if build_now['height'] < build_before['height']:
                line['begin'] = build_before['right']
        
    def create_ground(self, point, skyline, size_skyline):
        skyline.append([point, 0])
        size_skyline+=1
    
    def same_begin_more_height(self, build_now, build_before):
        if ((build_now['left'] == build_before['left']) and
            (build_now['height'] > build_before['height'])):
            return True
        return False
        
    def same_height_diferent_begin(self, build_now, build_before):
        if ((build_now['height'] == build_before['height']) and
            (build_now['left'] < build_before['left'])):
            return True
        return False
        
    def is_modify_skyline(self, build_now, build_before):
        if self.same_begin_more_height or self.same_height_diferent_begin:
            return True
        return False

    def can_insert_line(self, line_now, line_before):
        return ((line_now['begin'] != line_before['begin']) 
                and (line_now['height'] != line_before['height']))

    def create_dict_build(self, build):
        build = {
            'left': build[0],
            'right': build[1],
            'height': build[2]
        }
        return build

    def create_dict_line(self, line):
        dict = {
            'begin': line[0],
            'height': line[1]
        }
        return dict

if __name__ == '__main__':
    sol = Solution()
    buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    # answer [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
    skyline = sol.getSkyline(buildings)
    print(buildings)
    print(skyline)
    buildings = [[0,2,3],[2,5,3]]
    # answer [[0,3],[5,0]]
    skyline = sol.getSkyline(buildings)
    print(buildings)
    print(skyline)
    buildings = [[1,2,1],[1,2,2],[1,2,3]]
    skyline = sol.getSkyline(buildings)
    print(buildings)
    print(skyline)
    # answer [[1,3],[2,0]]















