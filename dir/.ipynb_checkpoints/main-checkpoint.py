import pandas as pd
import os
import cv2

files = '/home/muci/alpro/dir'

def read_files(files):
    dataframes = []
    for file in os.listdir(files):
        if file.endswith('.csv'):
            file_path = os.path.join(files, file)
            df = pd.read_csv(file_path, sep=',')
            df = df.iloc[:, 1:] 
            dataframes.append(df)
        if file.endswith('.jpg') or file.endswith('.png'):
            file_path = os.path.join(files, file)
            img = cv2.imread(file_path)
            cv2.imshow('Image', img)
            while True:
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            cv2.destroyWindow('Image')
        if file.endswith('.mp4'):
            file_path = os.path.join(files, file)
            video = cv2.VideoCapture(file_path)
            while True:
                ret, frame = video.read()
                if not ret:
                    break
                cv2.imshow('Video', frame)
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            video.release()
            cv2.destroyWindow('Video')
    add_df = pd.concat(dataframes, ignore_index=True)
    return add_df

add_df = read_files(files)
print(add_df)