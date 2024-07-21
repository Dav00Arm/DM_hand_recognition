import os
import cv2 as cv
import copy
import itertools
from collections import deque
import csv
import argparse
import mediapipe as mp

from utils import CvFpsCalc
from model import KeyPointClassifier, PointHistoryClassifier

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset_path", help='Path to the dataset', type=str, required=True)
    parser.add_argument("--output_csv", help='Output CSV file', type=str, default='output.csv')
    args = parser.parse_args()
    return args

def main():
    args = get_args()
    dataset_path = os.path.abspath(args.dataset_path)
    output_csv = args.output_csv

    # Initialize MediaPipe Hand model
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(
        static_image_mode=True,
        max_num_hands=1,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.5
    )

    # Initialize KeyPoint and PointHistory classifiers
    keypoint_classifier = KeyPointClassifier()
    point_history_classifier = PointHistoryClassifier()

    # Process each image in the dataset
    for label_folder in os.listdir(dataset_path):
        print(label_folder,"  -----------  ", dataset_path)
        label_path = os.path.join(dataset_path, label_folder)
        if os.path.isdir(label_path):
            for img_file in os.listdir(label_path):
                img_path = os.path.join(label_path, img_file)
                print(f"Processing file: {img_path}")  # Debug print
                process_image(img_path, label_folder, hands, keypoint_classifier, point_history_classifier, output_csv)

def process_image(img_path, label, hands, keypoint_classifier, point_history_classifier, output_csv):
    # Ensure the image path is correct
    if not os.path.exists(img_path):
        print(f"File not found: {img_path}")
        return

    # Read image
    image = cv.imread(img_path)
    if image is None:
        print(f"Failed to read image: {img_path}")
        return

    image = cv.flip(image, 1)  # Mirror image for correct hand orientation
    debug_image = copy.deepcopy(image)

    # Convert the image color space from BGR to RGB
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = hands.process(image)
    image.flags.writeable = True

    if results.multi_hand_landmarks is not None:
        for hand_landmarks in results.multi_hand_landmarks:
            landmark_list = calc_landmark_list(debug_image, hand_landmarks)
            pre_processed_landmark_list = pre_process_landmark(landmark_list)
            pre_processed_point_history_list = pre_process_point_history(debug_image, deque([landmark_list], maxlen=1))
            logging_csv(label, 2, pre_processed_landmark_list, pre_processed_point_history_list, output_csv)

def calc_landmark_list(image, landmarks):
    image_width, image_height = image.shape[1], image.shape[0]
    landmark_point = []
    for landmark in landmarks.landmark:
        landmark_x = min(int(landmark.x * image_width), image_width - 1)
        landmark_y = min(int(landmark.y * image_height), image_height - 1)
        landmark_point.append([landmark_x, landmark_y])
    return landmark_point

def pre_process_landmark(landmark_list):
    temp_landmark_list = copy.deepcopy(landmark_list)
    base_x, base_y = 0, 0
    for index, landmark_point in enumerate(temp_landmark_list):
        if index == 0:
            base_x, base_y = landmark_point[0], landmark_point[1]
        temp_landmark_list[index][0] -= base_x
        temp_landmark_list[index][1] -= base_y
    temp_landmark_list = list(itertools.chain.from_iterable(temp_landmark_list))
    max_value = max(map(abs, temp_landmark_list))
    if max_value != 0:
        temp_landmark_list = [x / max_value for x in temp_landmark_list]
    return temp_landmark_list

def pre_process_point_history(image, point_history):
    image_width, image_height = image.shape[1], image.shape[0]
    temp_point_history = copy.deepcopy(point_history)
    base_x, base_y = temp_point_history[0][0], temp_point_history[0][1]
    for point in temp_point_history:
        point[0] = (point[0] - base_x) / image_width
        point[1] = (point[1] - base_y) / image_height
    temp_point_history = list(itertools.chain.from_iterable(temp_point_history))
    return temp_point_history

def logging_csv(label, mode, landmark_list, point_history_list, output_csv):
    if mode == 2:
        with open(output_csv, 'a', newline="") as f:
            writer = csv.writer(f)
            writer.writerow([label, *landmark_list, *point_history_list])

if __name__ == '__main__':
    main()
