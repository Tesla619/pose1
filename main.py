from symbol import parameters
import cv2
#import cv2.aruco as aruco  #OLD

def findMarker(img, markerSize=6, totalMarkers=250, draw=True):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    key = getattr(cv2.aruco,f'DICT_{markerSize}X{markerSize}_{totalMarkers}')
    
    #arucoDict = cv2.aruco.Dictionary_get(key)          #OLD
    arucoDict = cv2.aruco.getPredefinedDictionary(key)  #NEW
  
    #arucoParam = cv2.aruco.DetectorParameters_create() #OLD
    arucoParam = cv2.aruco.DetectorParameters()         #NEW
        
    bbox,ids,_= cv2.aruco.detectMarkers(imgGray,arucoDict,parameters=arucoParam)
    print(ids)

def main():
    #cap = cv2.VideoCapture(0)
    
    while True:
        #succ, img = cap.read()
        
        #img = cv2.imread("3.png")          #OLD
        img = cv2.imread("pose1\\3.png")    #NEW
        img = cv2.resize(img,(0,0),fx=0.7,fy=0.7)        
        
        findMarker(img)        
                
        if cv2.waitKey(1) == 113:
            img.Release()
            break
        
        cv2.imshow("img", img) 

main()
cv2.destroyAllWindows()