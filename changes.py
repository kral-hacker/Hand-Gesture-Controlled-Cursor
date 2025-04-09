import cv2
import mediapipe as mp
import pyautogui

hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screem_width, screen_height = pyautogui.size()

cap = cv2.VideoCapture(0)
cap.set(10, 110)

index_y = 0
while True:
    _, img = cap.read()
    img = cv2.flip(img, 1)
    img_height, img_width, _ = img.shape
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb)
    hands = output.multi_hand_landmarks

 
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(img, hand)
            landmarks = hand.landmark

            index_tip_y = landmarks[8].y
            index_base_y = landmarks[6].y
            middle_tip_y = landmarks[12].y
            middle_base_y = landmarks[10].y
            ring_tip_y = landmarks[16].y
            ring_base_y = landmarks[14].y
            little_tip_y = landmarks[20].y
            little_base_y = landmarks[18].y
            thumb_tip_y = landmarks[4].y
            thumb_base_y = landmarks[2].y
            thumb_tip_x = landmarks[4].x
            thumb_base_x = landmarks[2].x

            if(index_tip_y < index_base_y and middle_tip_y < middle_base_y and ring_tip_y < ring_base_y and little_tip_y > little_base_y and thumb_tip_x < thumb_base_x):
               print("Successful Tab Change.")  
               pyautogui.hotkey('alt', 'tab', interval = 0.1)

            if(index_tip_y < index_base_y and middle_tip_y < middle_base_y and ring_tip_y < ring_base_y and little_tip_y < little_base_y and thumb_tip_x < thumb_base_x):
               print("Successful volume up.")
               pyautogui.hotkey('volumeup', interval = 0.1)
               
            if(index_tip_y > index_base_y and middle_tip_y > middle_base_y and ring_tip_y > ring_base_y and little_tip_y > little_base_y and thumb_tip_x < thumb_base_x):
               print("Successful volume Down")
               pyautogui.hotkey('volumedown', interval = 0.1)
               

            for id, landmark in enumerate(landmarks):  #enumerate adds a index pointer in the list of the landmarks
             x = int(landmark.x * img_width)
             y = int(landmark.y * img_height)
             print(x, y)

             if(id == 8 and middle_tip_y > middle_base_y and ring_tip_y > ring_base_y and little_tip_y > little_base_y):
                cv2.circle(img, (x,y), 30, (255,0,0))
                index_x = screem_width/img_width*x
                index_y = screen_height/img_height*y
                pyautogui.moveTo(index_x,index_y)

             if(id == 4 and thumb_tip_x > thumb_base_x and middle_tip_y > middle_base_y and ring_tip_y > ring_base_y and little_tip_y > little_base_y):
                cv2.circle(img, (x,y), 30, (255,0,0))
                thumb_x = screem_width/img_width*x
                thumb_y = screen_height/img_height*y
                if abs(index_y - thumb_y) < 50:
                   print("click")
                   pyautogui.click()
                   pyautogui.sleep(0.1)
            
             


    cv2.imshow("Video" , img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
