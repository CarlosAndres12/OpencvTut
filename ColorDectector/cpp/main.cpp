#include <iostream>

#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"

using namespace std;
using namespace cv;

int main() {

//   todas las camaras conectadas tienen un ID, el 0 representa la primera.
    VideoCapture cap(0);

    Mat frame;
    Mat hsv_frame;
    Mat thresholded_frame;


//  CV_WINDOW_NORMAL permite redimensionar las ventanas
    namedWindow("frame", CV_WINDOW_NORMAL);
    namedWindow("hsv", CV_WINDOW_NORMAL);
    namedWindow("thr", CV_WINDOW_NORMAL);

// ventana que solo posee los controles, es posible colocarlos en las que fueron declaradas anteriormente.
    namedWindow("controls");


    int iLowH = 0;
    int iHighH = 0;

    int iLowS = 0;
    int iHighS = 0;

    int iLowV = 0;
    int iHighV = 0;

//    trackbars
    createTrackbar("LowH", "controls", &iLowH, 179); //Hue (0 - 179)
    createTrackbar("HighH", "controls", &iHighH, 179);

    createTrackbar("LowS", "controls", &iLowS, 255); //Saturation (0 - 255)
    createTrackbar("HighS", "controls", &iHighS, 255);

    createTrackbar("LowV", "controls", &iLowV, 255); //Value (0 - 255)
    createTrackbar("HighV", "controls", &iHighV, 255);


    while(true) {

        if(!cap.read(frame)) {
            cerr << "error reading web cam" << endl;
            break;
        }

//        cambia el espacio de color de la imagen
        cvtColor(frame, hsv_frame, COLOR_BGR2HSV);

//        realiza el filtrado
        inRange(hsv_frame, Scalar(iLowH, iLowS, iLowV), Scalar(iHighH, iHighS, iHighV), thresholded_frame);


        imshow("frame", frame);
        imshow("hsv", hsv_frame);
        imshow("thr", thresholded_frame);

//      finaliza el programa al presionar la tecla scape.
        if(waitKey(5) == 27) {
            destroyAllWindows();
            cap.release();
            break;
        }


    }




    return 0;
}