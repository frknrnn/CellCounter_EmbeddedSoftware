import sys
import platform
from PySide2 import  QtCore,QtGui,QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import cv2
import numpy as np
# GUI FILE
from ui_main_ui import Ui_MainWindow
from ui_splash_screen import Ui_SplashScreen
from counting_functions import Counting
# IMPORT FUNCTIONS
import time
import serial
from serial.tools import list_ports

calibration_data=" "
serial_port = serial.Serial()
counter =0
flag=True
orginal_image=""


class VideoThread(QThread):
    change_pixmap_signal = Signal(np.ndarray)
    change_pixmap_signal_focus = Signal(np.ndarray)
    _running = True
    def createCamera(self,width,heıght):
        self.camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.camera.set(cv2.CAP_PROP_FPS, 30.0)
        self.camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('m', 'j', 'p', 'g'))
        self.camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('M', 'J', 'P', 'G'))
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH,width )
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, heıght)
        self.camera.set(12, 0)

    def terminate(self):
        self._running = False


    def run(self):
        while self._running:
            ret, cv_img = self.camera.read()
            cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
           #print(np.array(cv_img).shape)
            if ret:
                self.change_pixmap_signal.emit(cv_img)



class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.splash_ui = Ui_SplashScreen()
        self.splash_ui.setupUi(self)
        ## REMOVE TİTLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        ##DropShadowEffect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0,0,0,60))
        self.splash_ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ###QTİMER
        self.connectSerial()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)
        self.show()
        ####Function




    def progress(self):
        global counter
        self.splash_ui.progressBar_2.setValue(counter)
        if counter > 100:
            self.timer.stop()
            ###Show MainWindow
            self.close()
            self.main = MainWindow()
            self.main.show()
        counter+=1
    def connectSerial(self):
        global serial_port
        global calibration_data
        serial_list = list_ports.comports()
        for i in serial_list:
            if(i.manufacturer=="Arduino LLC (www.arduino.cc)"):
                port = i.device
                serial_port = serial.Serial(
                    port=port,
                    baudrate=38400,
                    parity=serial.PARITY_ODD,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                )
                if(serial_port.isOpen()):
                    serial_port.close()
                serial_port.open()
                serial_port.write("4".encode())
                line=[]
                serial_flag=True
                while serial_flag:
                    for data in serial_port.read().decode():
                        line.append(data)
                        if data == '\n':
                            break
                    if len(line)>=17:
                        if line[8]=='c':
                            serial_flag=False
                            calibration_data=line
                            serial_port.write("=".encode())


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.disply_width = 510
        self.display_height = 382
        self.focusDelay = 5
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)



        ############ BUTTON CONTROL###############

        ######MAİNWİNDOW#########

        self.ui.pushButton_preview.clicked.connect(self.showPreview)
        self.ui.pushButton_result.clicked.connect(self.showResult)
        self.ui.pushButton_settings.clicked.connect(self.showSettings)
        self.ui.pushButton_exit.clicked.connect(self.appExit)

        #######PREVİEW############
        self.ui.pushButton_up.pressed.connect(self.focusStartUp)
        self.ui.pushButton_up.released.connect(self.focusStopUp)
        self.ui.pushButton_down.pressed.connect(self.focusStartDown)
        self.ui.pushButton_down.released.connect(self.focusStopDown)
        self.ui.pushButton_coarse_fine.clicked['bool'].connect(self.coarseFine)
        self.ui.pushButton_auto_focus.clicked.connect(self.startFocus)
        # self.ui.pushButton_capture.clicked.connect(self.captureButton)
        self.ui.pushButton_count.clicked.connect(self.start_count)
        # self.ui.pushButton_grid_2.clicked.connect(self.loadingPage)
        self.ui.pushButton_viability.clicked.connect(self.setViabilityForCount)
        self.ui.pushButton_autoFocus_count.clicked.connect(self.setAutoFocusForCount)

        #########RESULT###########

        self.ui.pushButton_showTotal.clicked.connect(self.showTotalCell)
        self.ui.pushButton_showLive.clicked.connect(self.showLiveCell)
        self.ui.pushButton_showDead.clicked.connect(self.showDeadCell)

        self.ui.pushButton_histogram.clicked.connect(self.showHistogram)
        self.ui.pushButton_image.clicked.connect(self.showResultImage)

        self.ui.verticalSlider_min.valueChanged.connect(self.minSliderChangedValue)
        self.minSliderValue=0
        self.ui.verticalSlider_max.valueChanged.connect(self.maxSliderChangedValue)
        self.maxSliderValue=60

        self.ui.horizontalSlider_zoom.valueChanged.connect(self.zoomResultImage)

        ############# INIT SETTİNGS ################
        self.ui.stackedWidget.setCurrentIndex(0)
        self.resolution_switch = 0
        self.viabilityFlagForCount=False
        self.autoFocusFlagForCount=False
        self.focusFlag=False
        self.capture_flag=False
        self.counting_flag=False
        self.denemeFlag=False
        self.resultViabilityPushButtons=1
        self.contrastValue = 0
        self.startCam(640,480)
        #self.goUpSwitchLimit()

        # connect its signal to the update_image slot
        # start the thread
        self.show()
    def showHistogram(self):
        self.ui.stackedWidget_2.setCurrentIndex(1)
        self.ui.pushButton_histogram.setStyleSheet(u"QPushButton{\n"
                                                 "background-color: rgba(0, 122, 204,150);\n"
                                                 "border:none;\n"
                                                 "font: 14pt \"Calibri\";\n"
                                                 "color:rgb(255, 255, 255);\n"
                                                 "\n"
                                                 "}\n"
                                                 "QPushButton::hover{\n"
                                                 "	background-color: rgba(0, 122, 204, 150);\n"
                                                 "}\n"
                                                 "\n"
                                                 "")
        self.ui.pushButton_image.setStyleSheet(u"QPushButton{\n"
                                                "background-color: rgb(49, 51, 50);\n"
                                                "border:none;\n"
                                                "font: 14pt \"Calibri\";\n"
                                                "color:rgb(255, 255, 255);\n"
                                                "\n"
                                                "}\n"
                                                "QPushButton::hover{\n"
                                                "	background-color: rgba(0, 122, 204, 150);\n"
                                                "}\n"
                                                "\n"
                                                "")
    def showResultImage(self):
        self.ui.stackedWidget_2.setCurrentIndex(0)
        self.ui.pushButton_image.setStyleSheet(u"QPushButton{\n"
                                                 "background-color: rgba(0, 122, 204,150);\n"
                                                 "border:none;\n"
                                                 "font: 14pt \"Calibri\";\n"
                                                 "color:rgb(255, 255, 255);\n"
                                                 "\n"
                                                 "}\n"
                                                 "QPushButton::hover{\n"
                                                 "	background-color: rgba(0, 122, 204, 150);\n"
                                                 "}\n"
                                                 "\n"
                                                 "")
        self.ui.pushButton_histogram.setStyleSheet(u"QPushButton{\n"
                                                "background-color: rgb(49, 51, 50);\n"
                                                "border:none;\n"
                                                "font: 14pt \"Calibri\";\n"
                                                "color:rgb(255, 255, 255);\n"
                                                "\n"
                                                "}\n"
                                                "QPushButton::hover{\n"
                                                "	background-color: rgba(0, 122, 204, 150);\n"
                                                "}\n"
                                                "\n"
                                                "")

    def appExit(self):
        self.close()

    def loadingPage(self):
        self.loading_timer = QtCore.QTimer()
        self.loading_timer.timeout.connect(self.loadingProgressBar)
        self.loadingProgressValue=0
        self.loading_timer.start(10)
        self.ui.stackedWidget.setCurrentIndex(1)

    def loadingProgressBar(self):
        self.loadingProgressValue = self.loadingProgressValue+1
        if(self.loadingProgressValue==100):
            self.loadingProgressValue=0
        styleSheet1 = """
        QFrame{
            border-radius:140px;
            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP1_1} rgba(255, 0, 127, 0), stop:{STOP1_2} rgba(85, 170, 255, 255));

        }
        """
        progress=(100-self.loadingProgressValue)/100.0
        STOP1_1 = str(progress-0.001)
        STOP1_2 = str(progress)

        newStyleSheet1 = styleSheet1.replace("{STOP1_1}",STOP1_1).replace("{STOP1_2}",STOP1_2)
        self.ui.circularProgress.setStyleSheet(newStyleSheet1)

        styleSheet2 = """
                QFrame{
                    border-radius:120px;
                    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:270, stop:{STOP2_1} rgba(255, 0, 127, 0), stop:{STOP2_2} rgba(85, 170, 255, 255));

                }
                """
        STOP2_1 = str(progress - 0.001)
        STOP2_2 = str(progress)

        newStyleSheet2 = styleSheet2.replace("{STOP2_1}", STOP2_1).replace("{STOP2_2}", STOP2_2)
        self.ui.circularProgress2.setStyleSheet(newStyleSheet2)




    def captureButton(self):
        self.capture_flag=True
        self.loadingPage()
        self.startFocus()

    def start_count(self):
        self.counting_flag=True
        self.loadingPage()
        self.startFocus()



    def captureImage(self):
      self.stopCameraThread()
      self.fullResolutionImage = self.hıghResolutıonImage()
      return self.fullResolutionImage

    def counting(self):
        C = Counting()
        image = self.captureImage()
        C.setCalibration(0.661, image)
        result_image,live_contour,dead_contour,live_diameter,dead_diameter = C.HelaCellCount()
        self.qt_fullResolutionimg = self.convert_cv_qt_count(result_image)
        self.ui.pictureBox_result.loadImageFromFile(self.qt_fullResolutionimg)
        self.ui.label_total_cell.setText(str(len(live_diameter)+len(dead_diameter))+" TOTAL CELL DETECTED")
        self.ui.label_live_cell.setText(str(len(live_diameter))+" LİVE CELL DETECTED")
        self.ui.label_dead_cell.setText(str(len(dead_diameter))+" DEAD CELL DETECTED")
        self.ui.label_averageCellSize.setText(str(int((sum(live_diameter)+sum(dead_diameter))/(len(live_diameter)+len(dead_diameter))))+u"\u03bcm")

        self.ui.progressBar_liveCell.setValue(int((len(live_diameter)/(len(live_diameter)+len(dead_diameter)))*100))
        self.ui.progressBar_deadCell.setValue(int((len(dead_diameter) / (len(live_diameter) + len(dead_diameter))) * 100))

        #self.scene = QGraphicsScene()
        #self.scene.addPixmap(self.qt_fullResolutionimg)
        #self.ui.pictureBox_result.setScene(self.scene)
        #self.ui.pictureBox_result.fitInView(self.ui.pictureBox_result.sceneRect(), Qt.KeepAspectRatio)
        self.ui.stackedWidget.setCurrentIndex(2)
        #self.ui.label_total_cell.setText(+"")




        self.showResult()
        self.startCam(640, 480)



    def new_contrast(self,image):
        contrast_value = np.std(image)
        return contrast_value

    def automatedFocus(self):
        global serial_port
        self.stopCameraThread()
        self.goUpSwitchLimit()
        self.goStartPointForFocus()
        camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        camera.set(cv2.CAP_PROP_FPS, 30.0)
        camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('m', 'j', 'p', 'g'))
        camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('M', 'J', 'P', 'G'))
        camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        camera.set(12, 0)
        contrast_list=[]
        for i in range(200):
            serial_port.write("2/n".encode())
            ret, cv_img = camera.read()
            cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)

            contrast_list.append(self.new_contrast(cv_img))
        focusMaxValue = max(contrast_list)
        print(focusMaxValue)
        focusLimit = (focusMaxValue) - (focusMaxValue * (1 / 100))
        for i in range(200):
            serial_port.write("1/n".encode())
            ret, cv_img = camera.read()
            cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)

            if self.new_contrast(cv_img)>=focusLimit:
                break
        fullResolutionImage = self.hıghResolutıonImage()
        print(np.array(fullResolutionImage).shape)
        camera.release()
        self.startCam(640, 480)


    def hıghResolutıonImage(self):
        camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        camera.set(cv2.CAP_PROP_FPS, 30.0)
        camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('m', 'j', 'p', 'g'))
        camera.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('M', 'J', 'P', 'G'))
        camera.set(cv2.CAP_PROP_FRAME_WIDTH, 10000)
        camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 10000)
        camera.set(12, 0)
        time.sleep(3)
        ret, cv_img = camera.read()
        cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
        return cv_img




    def startCam(self,width,heıght):
        self.thread = VideoThread()
        self.thread.change_pixmap_signal.connect(self.update_image)
        self.thread.createCamera(width,heıght)
        self.thread.start()

    def stopCameraThread(self):
        self.thread.terminate()





    def changeResolution_low(self):
        self.thread.terminate()
        self.resolution_switch = 0
        self.startCam()


    def goStartPointForFocus(self):
        global serial_port
        for i in range(20):
            for i in range(10):
                serial_port.write("2/n".encode())
            time.sleep(0.005)

    def startFocus(self):
        self.focusFlag=True
        self.autoFocus_timer = QtCore.QTimer()
        self.autoFocus_timer.timeout.connect(self.scanFocus)
        self.focus_count = 0
        self.contras_list = []
        if self.focusFlag:
            self.goUpSwitchLimit()
            self.goStartPointForFocus()
            self.autoFocus_timer.start(30)



    def goFocusPoint(self):
        self.focusMaxValue = max(self.contras_list)
        print(self.focusMaxValue)
        self.focusLimit = (self.focusMaxValue)-(self.focusMaxValue*(1/100))
        self.focus_count=0
        self.absluteFocusPoint_timer=QtCore.QTimer()
        self.absluteFocusPoint_timer.timeout.connect(self.goAbsluteFocusPoint)
        self.absluteFocusPoint_timer.start(30)






    def goAbsluteFocusPoint(self):
        global serial_port
        if self.focus_count!=200:
            serial_port.write("1/n".encode())
            self.contras_list.append(self.getContrast())
            if self.getContrast()>=self.focusLimit:
                print(self.getContrast())
                self.absluteFocusPoint_timer.stop()
                if(self.capture_flag):
                    self.captureImage()
                    self.capture_flag=False
                if (self.counting_flag):
                    self.counting()
                    self.counting_flag = False

            self.focus_count+=1
        else:
            self.absluteFocusPoint_timer.stop()
            if self.capture_flag:
                self.captureImage()
                self.capture_flag=False
            if (self.counting_flag):
                self.counting()
                self.counting_flag = False


    def scanFocus(self):
        global serial_port
        if self.focus_count!=200:
            serial_port.write("2/n".encode())
            self.contras_list.append(self.getContrast())
            self.focus_count+=1
        else:
            self.autoFocus_timer.stop()
            self.goFocusPoint()




    def coarseFine(self,state):
        print(state)
        if state:
            self.focusDelay=50
            self.ui.pushButton_coarse_fine.setText("FINE")
        else:
            self.focusDelay=5
            self.ui.pushButton_coarse_fine.setText("COARSE")


    def focusStartUp(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.focusMoveUp)
        self.timer.start(self.focusDelay)

    def focusStopUp(self):
        self.timer.stop()

    def focusMoveUp(self):
        global serial_port
        serial_port.write("1/n".encode())

    def focusStartDown(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.focusMoveDown)
        self.timer.start(self.focusDelay)

    def focusStopDown(self):
        self.timer.stop()

    def focusMoveDown(self):
        global serial_port
        serial_port.write("2/n".encode())

    def showPreview(self):
        self.ui.stackedWidget.setCurrentIndex(0)

        self.ui.pushButton_preview.setStyleSheet(u"QPushButton{\n"
                                              "background-color: rgba(0, 122, 204,150);\n"
                                              "border:none;\n"
                                              "font: 14pt \"Calibri\";\n"
                                              "color:rgb(255, 255, 255);\n"
                                              "\n"
                                              "}\n"
                                              "QPushButton::hover{\n"
                                              "	background-color: rgba(0, 122, 204, 150);\n"
                                              "}\n"
                                              "\n"
                                              "")
        self.ui.pushButton_result.setStyleSheet(u"QPushButton{\n"
                                                 "background-color: rgb(49, 51, 50);\n"
                                                 "border:none;\n"
                                                 "font: 14pt \"Calibri\";\n"
                                                 "color:rgb(255, 255, 255);\n"
                                                 "\n"
                                                 "}\n"
                                                 "QPushButton::hover{\n"
                                                 "	background-color: rgba(0, 122, 204, 150);\n"
                                                 "}\n"
                                                 "\n"
                                                 "")
    def showResult(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.pushButton_result.setStyleSheet(u"QPushButton{\n"
                                                "background-color: rgba(0, 122, 204,150);\n"
                                                "border:none;\n"
                                                "font: 14pt \"Calibri\";\n"
                                                "color:rgb(255, 255, 255);\n"
                                                "\n"
                                                "}\n"
                                                "QPushButton::hover{\n"
                                                "	background-color: rgba(0, 122, 204, 150);\n"
                                                "}\n"
                                                "\n"
                                                "")
        self.ui.pushButton_preview.setStyleSheet(u"QPushButton{\n"
                                                 "background-color: rgb(49, 51, 50);\n"
                                                 "border:none;\n"
                                                 "font: 14pt \"Calibri\";\n"
                                                 "color:rgb(255, 255, 255);\n"
                                                 "\n"
                                                 "}\n"
                                                 "QPushButton::hover{\n"
                                                 "	background-color: rgba(0, 122, 204, 150);\n"
                                                 "}\n"
                                                 "\n"
                                                 "")



    def getContrast(self):
        contrast = np.std(self.orginal_image)
        return  contrast

    def update_image(self, cv_img):
            """Updates the picturebox with a new opencv image"""
            self.orginal_image = cv_img

            qt_img = self.convert_cv_qt(cv_img)
            self.ui.picture_box.setPixmap(qt_img)

    def convert_cv_qt(self, cv_img):
            """Convert from an opencv image to QPixmap"""
            h, w = cv_img.shape
            bytes_per_line =  w
            convert_to_Qt_format = QtGui.QImage(cv_img.data, w, h, bytes_per_line, QtGui.QImage.Format_Grayscale8)
            p = convert_to_Qt_format.scaled(self.disply_width, self.display_height, Qt.KeepAspectRatio)
            return QPixmap.fromImage(p)

    def convert_cv_qt_count(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        h, w, s= cv_img.shape
        bytes_per_line = 3*w
        convert_to_Qt_format = QtGui.QImage(cv_img.data, w, h, bytes_per_line, QtGui.QImage.Format_BGR888)
        #p = convert_to_Qt_format.scaled(self.ui.pictureBox_result.width(), self.ui.pictureBox_result.height(), Qt.KeepAspectRatio)
        return convert_to_Qt_format

    def goUpSwitchLimit(self):
        global serial_port

        for i in range(12):
            for i in range(30):
                serial_port.write("1/n".encode())

            time.sleep(0.001)

    def setViabilityForCount(self):
        if  self.viabilityFlagForCount == True:
            self.viabilityFlagForCount=False
            self.ui.pushButton_viability.setStyleSheet(u"QPushButton{\n"
                                                      "background-color: rgb(255, 255, 255);\n"
                                                      "border-radius:10px;\n"
                                                      "}\n"
                                                      "")
        else:
            self.viabilityFlagForCount=True
            self.ui.pushButton_viability.setStyleSheet(u"QPushButton{\n"
                                                       "background-color: rgb(0, 0, 0);\n"
                                                       "border-color: rgb(255,255, 255);\n"
	                                                   "border-width :4px;\n"
	                                                   "border-style:inset;\n"
                                                       "border-radius:10px;\n"
                                                       "}\n"
                                                       "")

    def setAutoFocusForCount(self):
        if  self.autoFocusFlagForCount == True:
            self.autoFocusFlagForCount=False
            self.ui.pushButton_autoFocus_count.setStyleSheet(u"QPushButton{\n"
                                                      "background-color: rgb(255, 255, 255);\n"
                                                      "border-radius:10px;\n"
                                                      "}\n"
                                                      "")
        else:
            self.autoFocusFlagForCount=True
            self.ui.pushButton_autoFocus_count.setStyleSheet(u"QPushButton{\n"
                                                       "background-color: rgb(0, 0, 0);\n"
                                                       "border-color: rgb(255,255, 255);\n"
	                                                   "border-width :4px;\n"
	                                                   "border-style:inset;\n"
                                                       "border-radius:10px;\n"
                                                       "}\n"
                                                       "")
    def showSettings(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def minSliderChangedValue(self):
        if(self.ui.verticalSlider_min.value()>=self.ui.verticalSlider_max.value()):
            self.ui.verticalSlider_min.setValue(self.maxSliderValue-1)
        self.minSliderValue = self.ui.verticalSlider_min.value()
        self.ui.label_minValue.setText(str(self.minSliderValue) + " \u00B5m")


    def maxSliderChangedValue(self):
        if(self.ui.verticalSlider_max.value()<=self.ui.verticalSlider_min.value()):
            self.ui.verticalSlider_max.setValue(self.minSliderValue + 1)
        self.maxSliderValue = self.ui.verticalSlider_max.value()
        self.ui.label_maxValue.setText(str(self.maxSliderValue)+" \u00B5m")

    def zoomResultImage(self):
        self.ui.label_zoom.setText(str(self.ui.horizontalSlider_zoom.value())+"X")
        self.ui.pictureBox_result.zoom(self.ui.horizontalSlider_zoom.value())

    def changeResultPageViabilityButtonsİcon(self):
        if(self.resultViabilityPushButtons==1):
            self.ui.pushButton_showTotal.setStyleSheet(u"QPushButton{\n"
                                                  "  border:none;\n"
                                                  "\n"
                                                  "  background-image: url(:/icons/whitePressed.png);\n"
                                                  "}")
            self.ui.pushButton_showLive.setStyleSheet(u"QPushButton{\n"
                                                       "  border:none;\n"
                                                       "\n"
                                                       "  background-image: url(:/icons/greenUnPressed.png);\n"
                                                       "}")
            self.ui.pushButton_showDead.setStyleSheet(u"QPushButton{\n"
                                                       "  border:none;\n"
                                                       "\n"
                                                       "  background-image: url(:/icons/redUnPressed.png);\n"
                                                       "}")


        if (self.resultViabilityPushButtons == 2):
            self.ui.pushButton_showTotal.setStyleSheet(u"QPushButton{\n"
                                                       "  border:none;\n"
                                                       "\n"
                                                       "  background-image: url(:/icons/whiteUnpressed.png);\n"
                                                       "}")
            self.ui.pushButton_showLive.setStyleSheet(u"QPushButton{\n"
                                                      "  border:none;\n"
                                                      "\n"
                                                      "  background-image: url(:/icons/greenPressed.png);\n"
                                                      "}")
            self.ui.pushButton_showDead.setStyleSheet(u"QPushButton{\n"
                                                      "  border:none;\n"
                                                      "\n"
                                                      "  background-image: url(:/icons/redUnPressed.png);\n"
                                                      "}")

        if (self.resultViabilityPushButtons == 3):
            self.ui.pushButton_showTotal.setStyleSheet(u"QPushButton{\n"
                                                       "  border:none;\n"
                                                       "\n"
                                                       "  background-image: url(:/icons/whiteUnpressed.png);\n"
                                                       "}")
            self.ui.pushButton_showLive.setStyleSheet(u"QPushButton{\n"
                                                      "  border:none;\n"
                                                      "\n"
                                                      "  background-image: url(:/icons/greenUnPressed.png);\n"
                                                      "}")
            self.ui.pushButton_showDead.setStyleSheet(u"QPushButton{\n"
                                                      "  border:none;\n"
                                                      "\n"
                                                      "  background-image: url(:/icons/redPressed.png);\n"
                                                      "}")

    def showTotalCell(self):
        self.resultViabilityPushButtons=1
        self.changeResultPageViabilityButtonsİcon()

    def showLiveCell(self):
        self.resultViabilityPushButtons = 2
        self.changeResultPageViabilityButtonsİcon()
    def showDeadCell(self):
        self.resultViabilityPushButtons = 3
        self.changeResultPageViabilityButtonsİcon()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())

