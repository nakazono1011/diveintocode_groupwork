#!/usr/bin/env python
#! -*- coding: utf-8 -*-

import os
import argparse
parser = argparse.ArgumentParser(description='shutter_image.')
parser.add_argument('--bottle_name', default=None, help="path to bottle_name")


import pygame.mixer
import numpy as np
import picamera
from PIL import Image
from time import sleep

def shutter(save_path):
    # pi camera 用のライブラリーを使用して、画像を取得
    # 音声再生
    pygame.mixer.init(frequency = 44100)    # 初期設定
    pygame.mixer.music.load("./Camera-Phone03-5.mp3")
    pygame.mixer.music.play(1)
    sleep(1)
    # 再生の終了
    pygame.mixer.music.stop()
    with picamera.PiCamera() as camera:
        #camera.resolution = (640,480)
        camera.resolution = (300,400)
        camera.start_preview()
        sleep(1.000)
        camera.capture(save_path)

import datetime

def main():
    args = parser.parse_args()
    if args.bottle_name is None:
        print('--bottle_nameを指定してください')
    else:
        try:
            os.makedirs(args.bottle_name, exist_ok=True)
        except:
            pass
        key = input('写真をとる場合は"y"を押して下さい')
        i = 0
        while key=="y":
            dt_now = datetime.datetime.now()
            file_name = str(args.bottle_name) + '_' + dt_now.strftime('%Y%m%d%H%M%S') + '.jpg'
            save_path = os.path.join(args.bottle_name, file_name)
            # 写真撮影
            shutter(save_path)
            i += 1
            print('{}枚目の写真を {} へ保存しました'.format(i, save_path))
            key = input('続けて写真をとる場合は「y」を、終了する場合は「n」を押して下さい')
            if key == 'n':
                print("写真撮影を終了しました")
                break
            
if __name__ == '__main__':
    main()