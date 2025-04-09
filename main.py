import cv2
import mediapipe as mp
import pyautogui

hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screem_width, screen_height = pyautogui.size()
# capturing the video
cap = cv2.VideoCapture(0)
cap.set(10, 100)
# displying the video
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

            for id, landmark in enumerate(landmarks):  #enumerate adds a index pointer in the list of the landmarks
             x = int(landmark.x * img_width)
             y = int(landmark.y * img_height)
             print(x, y)

             if(id == 8):
                cv2.circle(img, (x,y), 20, (255,0,0))
                index_x = screem_width/img_width*x
                index_y = screen_height/img_height*y
                pyautogui.moveTo(index_x,index_y)

             if(id == 4):
                cv2.circle(img, (x,y), 20, (255,0,0))
                thumb_x = screem_width/img_width*x
                thumb_y = screen_height/img_height*y
                if abs(index_y - thumb_y) < 20:
                   print("click")
                   pyautogui.click()
                   pyautogui.sleep(1)


    cv2.imshow("Video" , img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
