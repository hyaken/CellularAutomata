#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


class CarLine():
    def __init__(self, length, num):
        # 車列の長さ
        self.length = length
        # 車両の数
        self.num = num
        # Carクラスの入れ物
        self.cars = list()

        self.make_line()

    # 車列をつくる
    def make_line(self):
        self.cars = [Car() for var in range(self.num)]

        # 車の配置はランダムに行う
        locations = [var for var in range(self.length)]
        random_locations = random.sample(locations, self.num)
        for index in range(len(random_locations)):
            self.cars[index].set_location(random_locations[index])

        # 各車のstatusをセットする
        # 前に車がいれば止まっている。いなければ、走っている状態とする
        for current_car in self.cars:
            is_found_car_in_front = False
            for next_car in self.cars:
                # currentの位置が、末尾だった場合は、特殊対応
                # サーキット場の車列としているため、nextの位置は、先頭になる
                if current_car.location == self.length - 1:
                    # current_car の先に車がいないとき
                    if next_car.location != 0:
                        continue

                    # current_car の先に車がいるときは、進めない
                    current_car.set_status(0)
                    is_found_car_in_front = True
                    break

                # current_car の先に車がいないとき
                if next_car.location != current_car.location + 1:
                    continue

                # current_car の先に車がいるときは、進めない
                current_car.set_status(0)
                is_found_car_in_front = True
                break

            # current_car の先に車がいないことがわかったので、進める
            if not is_found_car_in_front:
                current_car.set_status(1)

    def advance(self):
        # 前に車がいたら止まる、いなかったら進む単純ケース
        car_locations = [car.location for car in self.cars]
        for current_car in self.cars:
            if current_car.location == (self.length - 1):
                if 0 in car_locations:
                    continue

                current_car.location = 0

            else:
                # 前に車がいた場合は進めない
                if (current_car.location + 1) in car_locations:
                    continue

                current_car.location += 1

    def advance_slow_start(self):
        # 前に車がいたらとまる。走っているステータスの場合は、止まるへ変える
        # いなかったら、走っているステータスに変える
        # 前に車がいない かつ、走っているステータスの場合、前に進むというケース
        None

    def print(self):
        line = [0] * self.length
        for car in self.cars:
            line[car.location] = 1
        print(line)

    def print_status(self):
        status_line = [""] * self.length
        for car in self.cars:
            status_line[car.location] = car.status
        print(status_line)


class Car():
    def __init__(self):
        # 止まっている：0、走っている：1
        self.status = int()
        # 車列のどこにいるか
        self.location = int()

    def set_location(self, location):
        self.location = location

    def set_status(self, status):
        self.status = status
