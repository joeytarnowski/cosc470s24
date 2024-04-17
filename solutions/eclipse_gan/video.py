import cv2
import os

def extract_frames(video_path, output_dir):
    # Make sure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Open the video file
    vidcap = cv2.VideoCapture(video_path)
    
    success, image = vidcap.read()
    count = 0

    while success:
        # Save frame as JPEG file
        cv2.imwrite(os.path.join(output_dir, f"frame{count:04d}.jpg"), image)
        
        success, image = vidcap.read()
        print(f'Read a new frame: {success}', end='\r')
        count += 1

# Example usage
video_path = '/Videos/solar_eclipse_vid.mov'
output_dir = '/Python/470/eclipse_gan/frames'

extract_frames(video_path, output_dir)
