import cv2
import math
import numpy as np

class Counting():

    def setCalibration(self,device_calibration_value,image):
        self.gridStartX = int((3264-(1000/device_calibration_value))/2)
        self.gridStartY = int((2448-(1000/device_calibration_value))/2)
        self.gridSmallSquareSize = int(250/device_calibration_value)
        self.device_calibration = device_calibration_value
        self.orginal_image = image
        self.result_color_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)




    def HelaCellCount(self):
        self.dead_cell_contour=[]
        self.live_cell_contour=[]
        self.live_cell_diameter=[]
        self.dead_cell_diameter = []
        self.total_cell_diameter = []
        self.ellipse_contour = []

        threshold_value_hela = 75
        image = self.orginal_image.copy()
        result_image = self.orginal_image.copy()
        #gray_image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        self.after_background_image = cv2.GaussianBlur(image, (7, 7), 0)

        self.analysis_image = self.background_subtraction(self.after_background_image)
        print("background subscraption:")
        print(self.analysis_image[0,:])



        ###İMAGE PROCESSİNG#####

        self.analysis_image = cv2.bitwise_not(self.analysis_image.astype("uint8"))
        print("bitwise:")
        print(self.analysis_image[0, :])
        self.analysis_image = cv2.GaussianBlur(self.analysis_image,(3,3),0)
        print("blur:")
        print(self.analysis_image[0,:])
        ret, self.threshold = cv2.threshold(self.analysis_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        self.analysis_image_forCircle = self.threshold
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
        self.close = cv2.morphologyEx(self.threshold, cv2.MORPH_CLOSE, kernel, iterations=2)
        self.contours, hierarchy = cv2.findContours(self.close, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for i in range(len(self.contours)):
            area = cv2.contourArea(self.contours[i])
            contour_diameter = math.sqrt(area/math.pi)*2*self.device_calibration
            if(area>150 and area<1700):
                if(self.isHelaHıghEllipticty(self.contours[i])):
                    M = cv2.moments(self.contours[i])
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])
                    if(cX>self.gridStartX-(2*self.gridSmallSquareSize) and cX< self.gridStartX+(6*self.gridSmallSquareSize)):
                        if(cY>self.gridStartY-(self.gridSmallSquareSize) and cY< self.gridStartY+(5*self.gridSmallSquareSize)):
                            contour_viability_flag = self.HelaCellViability_contour(self.contours[i],self.after_background_image,threshold_value_hela)
                            if(contour_viability_flag):
                                cv2.drawContours(self.result_color_image, self.contours[i], -1, (0, 255, 0), 3)
                                self.live_cell_contour.append(self.contours[i])
                                self.live_cell_diameter.append(contour_diameter)
                                self.total_cell_diameter.append(contour_diameter)
                            else:
                                self.dead_cell_contour.append(self.contours[i])
                                self.dead_cell_diameter.append(contour_diameter)
                                self.total_cell_diameter.append(contour_diameter)
                                cv2.drawContours(self.result_color_image, self.contours[i], -1, (0, 0, 255), 3)
                else:
                    self.ellipse_contour.append(self.contours[i])
            else:
                if(area<4000):
                    self.ellipse_contour.append(self.contours[i])

        self.circles = cv2.HoughCircles(self.analysis_image_forCircle, cv2.HOUGH_GRADIENT, 1, 21,  param1=100, param2=10, minRadius=9, maxRadius=17)

        self.live_points=[]
        self.dead_points=[]

        for i in self.circles[0,:]:
            for j in range(len(self.ellipse_contour)):
                distance = cv2.pointPolygonTest(self.ellipse_contour[j], (i[0],i[1]), False)
                if(distance>0):
                    if (i[0] > self.gridStartX - (2 * self.gridSmallSquareSize) and i[0] < self.gridStartX + (6 * self.gridSmallSquareSize)):
                        if (i[1] > self.gridStartY - (self.gridSmallSquareSize) and i[1] < self.gridStartY + (5 * self.gridSmallSquareSize)):
                            circle_viability_flag = self.HelaCellViability_circle(self.ellipse_contour[j],i,self.after_background_image,threshold_value_hela)
                            if(circle_viability_flag):
                                self.live_points.append(i)
                                self.live_cell_diameter.append(i[2]*2*self.device_calibration)
                                self.total_cell_diameter.append(i[2]*2*self.device_calibration)
                            else:
                                self.dead_points.append(i)
                                self.dead_cell_diameter.append(i[2] * 2 * self.device_calibration)
                                self.total_cell_diameter.append(i[2] * 2 * self.device_calibration)

        for i in self.live_points:
            cv2.circle(self.result_color_image,(int(i[0]),int(i[1])) ,int(i[2]),(0,255,0), 3)
            cv2.circle(self.result_color_image, (int(i[0]), int(i[1])), 1, (0, 255, 0), 2)
        for i in self.dead_points:
            cv2.circle(self.result_color_image, (int(i[0]), int(i[1])), int(i[2]), (0, 0, 255), 3)
            cv2.circle(self.result_color_image, (int(i[0]), int(i[1])), 1, (0, 0, 255), 2)

        return self.result_color_image,self.live_cell_contour,self.dead_cell_contour,self.live_cell_diameter,self.dead_cell_diameter,



    def HelaCellViability_contour(self,contour,image,threshold_value):
        x, y, w, h = cv2.boundingRect(contour)
        intensity_list=[]
        for i in range(h):
            for j in range(w):
                distance = cv2.pointPolygonTest(contour, (x+j, y+i), False)
                if(distance>0):
                    intensity = image[y+i,x+j]
                    intensity_list.append(intensity)
        total_intensity = 0
        for i in range(len(intensity_list)):
            total_intensity=total_intensity+intensity_list[i]
        average_intensity = total_intensity/len(intensity_list)
        if(average_intensity>=threshold_value):
            return True
        if(average_intensity<threshold_value):
            return False

    def HelaCellViability_circle(self,contour,circle,image,threshold_value):
        intensity_list=[]
        x, y, w, h = cv2.boundingRect(contour)
        cX = int(circle[0]-(circle[2]/2))
        cY = int(circle[1]-(circle[2]/2))

        for i in range(int(circle[2])):
            for j in range(int(circle[2])):
                distance = cv2.pointPolygonTest(contour, (x + j, y + i), False)  ######## Bİr farklılık var rectangelde x+j burda x+i ?
                if(distance>0):
                    if(cY+i<2448 and cX+j<3264):
                        intensity = image[cY+i,cX+j]
                        intensity_list.append(intensity)
        total_intensity = 0
        for i in range(len(intensity_list)):
            total_intensity = total_intensity + intensity_list[i]
        if(len(intensity_list)!=0):
            average_intensity = total_intensity / len(intensity_list)
        else:
            average_intensity=0
        if (average_intensity >= threshold_value):
            return True
        if (average_intensity < threshold_value):
            return False

    def isHelaHıghEllipticty(self,contour):
        M = cv2.moments(contour)
        cX = int(M["m10"]/M["m00"])
        cY = int(M["m01"]/M["m00"])
        min_dist = math.sqrt(((contour[0][0][0]-cX)**2)+((contour[0][0][1]-cY)**2))
        max_dist=min_dist
        for i in contour:
            temp_distance = math.sqrt(((i[0][0]-cX)**2)+((i[0][1]-cY)**2))
            if(temp_distance>max_dist):
                max_dist=temp_distance
            if(temp_distance<min_dist):
                min_dist=temp_distance
        ellipticty=0
        if(max_dist!=0 and min_dist!=0):
             ellipticty = ((max_dist**2)-(min_dist**2))/(max_dist*min_dist)

        if(ellipticty>0.70):
            return True
        else:
            return False




    def background_subtraction(self,image):
        background = cv2.imread("background.jpeg")
        gray_background = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)
        background_blur = cv2.GaussianBlur(gray_background, (1001, 1001), 0)
        gray_background = background_blur / gray_background.max()
        result_image = image / gray_background
        cv2.imwrite('b_result.jpeg', result_image)
        return result_image

