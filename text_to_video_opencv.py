import cv2
import numpy


# Функция для создания видео с бегущей строкой
def text_to_video(message: str) -> None:
    """
    Generates a video from text (ticker)
    :param message: string
    :return:
    """
    video_width: int = 100
    video_height: int = 100
    framerate: int = 12

    video = cv2.VideoWriter("text_to_video.mp4", cv2.VideoWriter_fourcc(*'mp4v'), framerate, (video_width, video_height))

    # Создаем кадр с черным фоном
    frame = numpy.zeros((video_width, video_height, 3), dtype=numpy.uint8)

    # Начальные координаты для бегущей строки
    text_coordinate_x, text_coordinate_y = video_width, video_height // 2

    # Установим параметры шрифта
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_thickness = 2
    font_color = (255, 255, 255)  # Белый цвет текста

    for t in range(120):  # 10 секунд с частотой 12 кадра/сек
        # Очистка кадра
        frame.fill(0)  # 0 - black, 255 - white


        # Новые координаты для бегущей строки
        text_coordinate_x -= 10  # Скорость бегущей строки

        # Вот тут добавим текст
        cv2.putText(frame, message, (text_coordinate_x, text_coordinate_y), font, font_scale, font_color, font_thickness, cv2.LINE_AA)

        # Тут запишем кадр
        video.write(frame)

    # Закроем тут видеопоток
    video.release()


text_to_video('foobar текст на русском ***11!!,')
