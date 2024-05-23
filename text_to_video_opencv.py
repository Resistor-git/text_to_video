# TODO
# проверять, что запрос длиннее 0 и короче 999 (drf?)

import cv2
import numpy


def text_to_video(message: str) -> None:
    """
    Generates a video from text (ticker)
    :param message: string
    :return:
    """
    video_width: int = 100
    video_height: int = 100
    framerate: int = 12
    filename: str = message[:8].replace(' ', '_')

    video = cv2.VideoWriter(f"videos/{filename}.mp4", cv2.VideoWriter_fourcc(*'mp4v'), framerate, (video_width, video_height))
    frame = numpy.zeros((video_width, video_height, 3), dtype=numpy.uint8)
    text_coordinate_x, text_coordinate_y = video_width, video_height // 2

    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_thickness = 2
    font_color = (255, 255, 255)

    text_size_pixels = cv2.getTextSize(message, font, font_scale, font_thickness)

    for _ in range(framerate * len(message)):
        frame.fill(0)  # 0 - black, 255 - white
        text_coordinate_x -= 10  # speed of text moving
        cv2.putText(frame, message, (text_coordinate_x, text_coordinate_y), font, font_scale, font_color, font_thickness, cv2.LINE_AA)
        if text_coordinate_x + text_size_pixels[0][0] < 0:
            break
        video.write(frame)

    video.release()


text_to_video('foobar текст на русском ***11!!,')
text_to_video('0123456789')
text_to_video('A')
