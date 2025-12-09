import cv2 as cv
import mediapipe as mp
import math
#pip install mediapipe

mp_drawing =mp.solutions.drawing_utils  #No se usa
mp_pose=mp.solutions.pose

cap = cv.VideoCapture(0)

with mp_pose.Pose(
    static_image_mode=False,
    model_complexity=0) as pose:
    
    while True:
        ret, frame = cap.read()
        if ret == False:
            break
        
        frame=cv.flip(frame,1)
        frame_rgb=cv.cvtColor(frame,cv.COLOR_BGR2RGB)
        height, width, _=frame.shape
        results = pose.process(frame_rgb)
    
        if results.pose_landmarks is not None:
            #Puntos Indipendientes
            x1=int(results.pose_landmarks.landmark[11].x*width)
            y1=int(results.pose_landmarks.landmark[11].y*height)
            
            x2=int(results.pose_landmarks.landmark[13].x*width)
            y2=int(results.pose_landmarks.landmark[13].y*height)
            
            x3=int(results.pose_landmarks.landmark[15].x*width)
            y3=int(results.pose_landmarks.landmark[15].y*height)
            
            Dx1=(x2-x1)
            Dx2=(x3-x2)
            if (Dx1 ==0 or Dx2==0):
                Dx1=0.1
                Dx2=0.1
            th1=math.atan((y2-y1)/Dx1)
            th2=math.atan((y3-y2)/Dx2)
            
            
            #print(str(int(th1*57.29))+","+str(int(th2*57.29)))
            
            cv.line(frame,(x1,y1),(x2,y2),(255,255,255),3)
            cv.line(frame,(x2,y2),(x3,y3),(255,255,255),3)
            cv.circle(frame,(x1,y1),6,(128,0,255),-1)
            cv.circle(frame,(x2,y2),6,(128,0,255),-1)
            cv.circle(frame,(x3,y3),6,(128,0,255),-1)

    

        #Cuerpo
        """
        mp_drawing.draw_landmarks(
        frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
        mp_drawing.DrawingSpec(color=(128,0,255),thickness=2,circle_radius=1),
        mp_drawing.DrawingSpec(color=(0,255,0),thickness=2)
        )
        """

        cv.imshow("Frame",frame)
        if(cv.waitKey(20)==ord("q")): break
        
cap.release()   
cv.destroyAllWindows()
