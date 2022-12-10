import cv2
import mediapipe as mp
import numpy as np
# from video import Video
from virtual_trainer.Exercises import bodyExercises


class poseEstimation:
    
    def aiTrainer(img):
        mp_drawing = mp.solutions.drawing_utils
        mp_pose = mp.solutions.pose
        cap = cv2.VideoCapture(img)

        size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        out = cv2.VideoWriter('output/curls.mp4',
                                cv2.VideoWriter_fourcc(*'MJPG'),
                                10, size)

        stats ={
            "state":None,
            "count":0
        }
            # Mediapipe instance
        with mp_pose.Pose(min_detection_confidence = 0.5, min_tracking_confidence = 0.5) as pose:
            while cap.isOpened():
                ret, frame =cap.read()

                # img2=cv2.flip(frame,-1)
                img2 = frame
                # Recolor into RGB
    
                image = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
                image.flags.writeable = False

                # Make detections
                results = pose.process(image)

                # Render detections
                # mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                #                         mp_drawing.DrawingSpec(color=(245,117,66),thickness=2,circle_radius=2),
                #                         mp_drawing.DrawingSpec(color=(245,88,230),thickness=2,circle_radius=2)
                #                         )

                # Recolor back into BGR
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                # Extract landmarks

                try:
                    landmarks = results.pose_landmarks.landmark
                    # Get coordinates
                    left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                    left_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                    left_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
                    left_hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                    left_knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
                    left_ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]
                    
                    right_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
                    right_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
                    right_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                    right_hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                    right_knee = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                    right_anckle = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                    
                    #Later will add if else here
                    
                    # Get angle
                    stats = bodyExercises.curls(right_shoulder, right_elbow, right_wrist, stats)
                    # stats = bodyExercises.pushups(right_shoulder,right_elbow,right_wrist, stats)
                    # stats = bodyExercises.pullups(right_shoulder,right_elbow,right_wrist, stats)
                    # stats = bodyExercises.rows(left_shoulder, left_elbow, left_wrist, stats)
                    # stats = bodyExercises.armRaises(left_elbow, left_shoulder, left_hip, stats)
                    # stats = bodyExercises.legs(left_hip,left_knee,left_ankle,stats)
                    # print(stats)
                    
                    # cv2.putText(image, str(pushups), 
                    #            tuple(np.multiply(right_elbow, [640, 360]).astype(int)), 
                    #            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                    #                 )

                except:
                    print('Exception..')
                    pass
                # print(landmarks)
                cv2.rectangle(image, (0,0), (225,73), (245,117,16), -1)

                # Rep Data
                cv2.putText(image, 'REPS', (15,12), 
                            cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
                cv2.putText(image, str(stats["count"]), (10,60), 
                            cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)            
                
                # Stage Data
                cv2.putText(image, 'STAGE', (65,12), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
                cv2.putText(image, stats["state"], 
                            (60,60), 
                            cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
                
                cv2.imshow('Mediapipe Feed', image)
                out.write(image)
                bodyExercises.vid(np.array(image))
                ##############################################
                # cap = cv2.VideoCapture(image)
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break
            cap.release()
            cv2.destroyAllWindows()
# if __name__ == "__main__":
#     main()

