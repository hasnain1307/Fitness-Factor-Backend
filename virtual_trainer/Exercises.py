import numpy as np
import cv2
import base64
class bodyExercises:

    def curls(a,b,c,stats):
        stats = stats
        a = np.array(a)
        b = np.array(b)
        c = np.array(c)
        radians = np.arctan2(c[1]-b[1],c[0]-b[0]) - np.arctan2(a[1]-b[1],a[0]-b[0]) 
        angle = np.abs(radians*180.0/np.pi)
        if angle > 160:
            stats["state"] = "down"
            # print(angle)
        if angle < 60 and stats["state"] == 'down':
            stats["state"] = "up"
            stats["count"] +=1 
        # print(angle)    
    
        return stats

    def pushups(a,b,c,stats):
        stats = stats
        a = np.array(a)
        b = np.array(b)
        c = np.array(c)
        radians = np.arctan2(c[1]-b[1],c[0]-b[0]) - np.arctan2(a[1]-b[1],a[0]-b[0]) 
        angle = np.abs(radians*180.0/np.pi)
        # print(angle)
        if angle > 160 and stats["state"] == 'down':
            stats["state"] = "up"
            stats["count"] +=1
        if angle < 60:
            stats["state"] = "down"        
        # print(stats)    
        return stats
        
    def pullups(a,b,c,stats):
        stats = stats
        a = np.array(a)
        b = np.array(b)
        c = np.array(c)
        radians = np.arctan2(c[1]-b[1],c[0]-b[0]) - np.arctan2(a[1]-b[1],a[0]-b[0]) 
        angle = np.abs(radians*180.0/np.pi)

        if angle > 160:
            stats["state"] = "down"
            # print(angle)
        if angle < 40 and stats["state"] == 'down':
            stats["state"] = "up"
            stats["count"] +=1 
        # print(stats)    
        return stats

    def rows(a,b,c,stats):
        stats = stats
        a = np.array(a)
        b = np.array(b)
        c = np.array(c)
        radians = np.arctan2(c[1]-b[1],c[0]-b[0]) - np.arctan2(a[1]-b[1],a[0]-b[0]) 
        angle = np.abs(radians*180.0/np.pi)
        # print(angle)
        if angle < 75:
            stats["state"] = "back"
        if (angle > 180 and angle <250) and stats["state"] == "back":
            stats["state"] = "forward"
            stats["count"] +=1    
        # print(stats)    
        return stats

    def armRaises(a,b,c,stats):
        stats = stats
        a = np.array(a)
        b = np.array(b)
        c = np.array(c)
        radians = np.arctan2(c[1]-b[1],c[0]-b[0]) - np.arctan2(a[1]-b[1],a[0]-b[0]) 
        angle = np.abs(radians*180.0/np.pi)
        # print(angle)
        if angle > 115:
            stats["state"] = "up"
            print(angle)
        if angle < 20 and stats["state"] == 'up':
            stats["state"] = "down"
            stats["count"] +=1 
        # print(stats)    
        return stats

    def legs(a,b,c,stats):
        stats = stats
        a = np.array(a)
        b = np.array(b)
        c = np.array(c)
        radians = np.arctan2(c[1]-b[1],c[0]-b[0]) - np.arctan2(a[1]-b[1],a[0]-b[0]) 
        angle = np.abs(radians*180.0/np.pi)
        # print(angle)
        if angle < 70:
            stats["state"] = "down"
            # print(angle)
        if (angle >180 and angle <200) and stats["state"] == 'down':
            stats["state"] = "up"
            stats["count"] +=1 
        # print(stats)    
        return stats
    def vid(image):
        s = base64.b64encode(image)
        print(s)
        # cap = cv2.VideoCapture(image)
        # size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        #         int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        # out = cv2.VideoWriter('output2/curls.mp4',
        #                             cv2.VideoWriter_fourcc(*'MJPG'),
        #                             10, size)
        # while cap.isOpened():
        #     out.write(image)
        # pass
