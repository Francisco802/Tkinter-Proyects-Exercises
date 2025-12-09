import PIL
from PIL import ImageTk
import cv2
import tkinter as tk
import mediapipe as mp


mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

cap = cv2.VideoCapture(0)

def show_frame():
    global c

    ret , frame = cap.read()
    frame=cv2.flip(frame,1)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(frame)
    
    mp_drawing.draw_landmarks(
        frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
        mp_drawing.DrawingSpec(color=(128,0,255),thickness=2,circle_radius=1),
        mp_drawing.DrawingSpec(color=(255,255,255),thickness=2)
    )

    img = PIL.Image.fromarray(frame)
    imgtk = ImageTk.PhotoImage(image=img)
    c.config(image=imgtk)
    c.image=imgtk
    
    c.after(10, show_frame)

root = tk.Tk()
root.geometry("700x500")

c = tk.Label(root, bg = 'black')
c.pack(expand=True,fill="both")

global pose
pose = mp_pose.Pose(
        min_detection_confidence = 0.5, 
        min_tracking_confidence = 0.5,
        model_complexity = 0
        )

show_frame()

root.mainloop()