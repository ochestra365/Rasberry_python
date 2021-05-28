import pygame
import RPi.GPIO as GPIO
import time

pygame.init()
pygame.display.set_mode((300, 300))
pygame.key.set_repeat(100, 100)

pinPiezo = 15
Melody3 = [131, 147, 165, 175, 196, 220, 247, 262]
Melody4 = [262, 294, 330, 349, 392, 440, 494, 523]
Melody5 = [523, 587, 659, 699, 784, 880, 988, 1047]
Mel_Han = ['도','레', '미', '파', '솔', '라', '시', '도']

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinPiezo, GPIO.OUT)

# 음계 주파수 : 기본음(440Hz) 기준
Buzz = GPIO.PWM(pinPiezo, 440)

rec_val = []
rec_time = []
rec_flag = False
play_flag = False
curr_time = time.time()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # Ctrl + c를 누르면 종료
            if event.key == pygame.K_c and pygame.key.get_mods() & pygame.KMOD_CTRL:
                GPIO.cleanup()
                exit()
            # r 키를 누르면 녹음 시작
            elif event.key == pygame.K_r:
                print('녹음 시작')
                rec_flag = True
                curr_time = time.time()
                rec_val = []
                rec_time = []
                continue
            # s 키를 누르면 녹음 종료
            elif event.key == pygame.K_s and rec_flag:
                print('녹음 종료')
                rec_flag = False
                play_flag = True
                continue
            # p 키를 누르면 (이전 녹음) 재생
            elif event.key == pygame.K_p and play_flag:
                print('재생 시작')
                curr_time = time.time()
                for i in range(len(rec_val)):
                    while rec_time[i] > time.time() - curr_time:
                        pass
                    Buzz.start(50)
                    Buzz.ChangeFrequency(rec_val[i])
                    time.sleep(0.3)
                    Buzz.stop()
                print('재생 종료')
                break

            Buzz.start(50)
            Buzz.ChangeFrequency(Melody4[(int(event.key) - 49) % 8])
           
            if rec_flag:
                tmp_val = (int(event.key) - 49) % 8
                tmp_time = time.time() - curr_time
                rec_val.append(Melody4[tmp_val])
                rec_time.append(tmp_time)
                print('{0:.3f} (sec) : {1}'.format(tmp_time, Mel_Han[tmp_val]))

            time.sleep(0.3)
            Buzz.stop()



