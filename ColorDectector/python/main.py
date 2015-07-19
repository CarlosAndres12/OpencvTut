__author__ = 'carlos'

import cv2
import sys
import numpy as np


#   callback, no usado por ahora.
def nothing(x):
    pass


def main():
    #   todas las camaras conectadas tienen un ID, el 0 representa la primera.
    cap = cv2.VideoCapture(0)

    #  WINDOW_NORMAL permite redimensionar las ventanas
    cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
    cv2.namedWindow("hsv", cv2.WINDOW_NORMAL)
    cv2.namedWindow("thr", cv2.WINDOW_NORMAL)

    # ventana que solo posee los controles, es posible colocarlos en las que fueron declaradas anteriormente.
    cv2.namedWindow("controls", cv2.WINDOW_NORMAL)

    #   trackbars
    cv2.createTrackbar("LowH", "controls", 0, 179, nothing)  # Hue [0 - 179]
    cv2.createTrackbar("HighH", "controls", 0, 179, nothing)

    cv2.createTrackbar("LowS", "controls", 0, 255, nothing)  # Saturation [0 - 255]
    cv2.createTrackbar("HighS", "controls", 0, 255, nothing)

    cv2.createTrackbar("LowV", "controls", 0, 255, nothing)  # Value [0 - 255]
    cv2.createTrackbar("HighV", "controls", 0, 255, nothing)

    while True:

        success, frame = cap.read()

        if not success:
            print("error reading web cam", file=sys.stderr)

        # cambia el espacio de color de la imagen
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_bound = np.array([cv2.getTrackbarPos("LowH", "controls"), cv2.getTrackbarPos("LowS", "controls"),
                                cv2.getTrackbarPos("LowV", "controls")])
        upper_bound = np.array([cv2.getTrackbarPos("HighH", "controls"), cv2.getTrackbarPos("HighS", "controls"),
                                cv2.getTrackbarPos("HighV", "controls")])

        # realiza el filtrado
        thresholded_frame = cv2.inRange(hsv_frame, lower_bound, upper_bound)

        cv2.imshow("frame", frame)
        cv2.imshow("hsv", hsv_frame)
        cv2.imshow("thr", thresholded_frame)

        #   finaliza el programa al presionar la tecla scape.
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break


if __name__ == '__main__':
    main()
