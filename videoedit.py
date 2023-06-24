import os
import cv2  # Библиотека opencv-python для создания скриншотов
import shutil  # Библиотека для создания zip файлов
import datetime  # Библиотека для работы с временным форматом
import ntpath  # Получение имени файла
from skimage.metrics import structural_similarity

def compare(first, second):

    first_gray = cv2.cvtColor(first, cv2.COLOR_BGR2GRAY)
    second_gray = cv2.cvtColor(second, cv2.COLOR_BGR2GRAY)

    # SSIM проверка между двумя изображениями
    score, diff = structural_similarity(first_gray, second_gray, full=True)
    print("Similarity Score: {:.3f}%".format(score * 100))
    return score

directory = ''
temp_directory = './data/'
path_to_video = './video.mp4'
intvl = 5


def get_screens(path_to_video, interval, temp_directory='./data/', work_directory=''):

    videofilename = ntpath.basename(os.path.splitext(path_to_video)[0])
    print(videofilename)
    cam = cv2.VideoCapture(path_to_video)
    intvl = interval/2  # Интервал записи скриншотов в секнду

    try:
        if not os.path.exists(temp_directory):
            os.makedirs(temp_directory)


    except OSError:
        print('Error: Creating directory of data')

    fps = int(cam.get(cv2.CAP_PROP_FPS))  # Количество кадров в секунду

    print("fps : ", fps)

    cam.set(2,0)
    ret, temp_frame = cam.read()
    currentframe = 1
    start_cadr = 0
    # check_screen = False
    while (True):
        ret, frame = cam.read()
        if ret:
            duration = currentframe / fps
            # if (currentframe % (fps * intvl) == 0):
            #
            #     framedate = str(datetime.timedelta(seconds=round(duration))).replace(':', '_')
            #     name = temp_directory+'img_' + videofilename + '_' + str(framedate) + '.jpg'
            #     print('Creating...' + name)
            #     cv2.imwrite(name, frame)
            if currentframe % (fps) == 0: # Кадр каждую секунду
                if compare(temp_frame, frame)>=0.9 and duration-start_cadr<interval:
                    pass
                elif compare(temp_frame, frame)>=0.9 and duration-start_cadr>=interval: #and check_screen == False:
                    startframe = str(datetime.timedelta(seconds=round(start_cadr))).replace(':', '_')
                    endframe = str(datetime.timedelta(seconds=round(duration))).replace(':', '_')
                    name = temp_directory+'img_' + videofilename + '_' +str(startframe)+'-'+str(endframe)+'.jpg'
                    print('Creating...' + name)
                    cv2.imwrite(name, frame)
                    start_cadr = duration
                    temp_frame = frame
                    # check_screen = True
                elif compare(temp_frame, frame)<0.9: # Если кадр изменился меняется и время начала отсчета кадра
                    temp_frame = frame
                    start_cadr = duration
                    # check_screen = False
            currentframe += 1
        else:
            break



    cam.release()
    cv2.destroyAllWindows()

    shutil.make_archive('screen_archive', 'zip', 'data')
    shutil.rmtree('./data/')


get_screens(path_to_video, intvl)