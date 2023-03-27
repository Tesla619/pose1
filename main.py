from symbol import parameters
import cv2
import cv2.aruco as aruco

def findMarker(img, markerSize=6, totalMarkers=250, draw=True):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    key = getattr(aruco,f'DICT_{markerSize}X{markerSize}_{totalMarkers}')
    arucoDict = aruco.Dictionary_get(key)   
    arucoParam = aruco.DetectorParameters_create()
    bbox,ids,_=aruco.detectMarkers(imgGray,arucoDict,parameters=arucoParam)
    print(ids)

def main():
    #cap = cv2.VideoCapture(0)
    
    while True:
        #succ, img = cap.read()
        
        img = cv2.imread("3.png")
        img = cv2.resize(img,(0,0),fx=0.7,fy=0.7)        
        
        findMarker(img)        
                
        if cv2.waitKey(1) == 113:
            break
        
        cv2.imshow("img", img) 

main()
#print(cv2. __version__)