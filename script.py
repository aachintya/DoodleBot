import cv2
import numpy as np
from typing import List, Tuple

def detect_colored_points(image_path: str) -> Tuple[List[Tuple[int, int]], List[Tuple[int, int]], List[Tuple[int, int]]]:
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Could not read the image")

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    red_lower = np.array([150, 0, 0])
    red_upper = np.array([255, 100, 100])
    green_lower = np.array([0, 100, 0])
    green_upper = np.array([150, 255, 150])
    blue_lower = np.array([0, 0, 100])
    blue_upper = np.array([120, 120, 255])

    red_mask = cv2.inRange(img_rgb, red_lower, red_upper)
    green_mask = cv2.inRange(img_rgb, green_lower, green_upper)
    blue_mask = cv2.inRange(img_rgb, blue_lower, blue_upper)

    kernel = np.ones((7,7), np.uint8)
    red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN, kernel)
    green_mask = cv2.morphologyEx(green_mask, cv2.MORPH_OPEN, kernel)
    blue_mask = cv2.morphologyEx(blue_mask, cv2.MORPH_OPEN, kernel)

    red_contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    green_contours, _ = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    blue_contours, _ = cv2.findContours(blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    min_area = 50

    def get_centroids(contours):
        centroids = []
        for contour in contours:
            if cv2.contourArea(contour) > min_area:
                M = cv2.moments(contour)
                if M["m00"] != 0:
                    cx = int(M["m10"] / M["m00"])
                    cy = int(M["m01"] / M["m00"])
                    centroids.append((cx, cy))
        return centroids

    red_coords = get_centroids(red_contours)
    green_coords = get_centroids(green_contours)
    blue_coords = get_centroids(blue_contours)

    return red_coords, green_coords, blue_coords

def determine_direction(curr_point: Tuple[int, int], next_point: Tuple[int, int]) -> str:
    dx = next_point[0] - curr_point[0]
    dy = next_point[1] - curr_point[1]

    if abs(dx) > abs(dy):
        return '+x' if dx > 0 else '-x'
    else:
        return '+y' if dy > 0 else '-y'

def generate_path_sequence(red_points: List[Tuple[int, int]], green_points: List[Tuple[int, int]], blue_points: List[Tuple[int, int]]) -> List[str]:
    if not red_points or not green_points:
        raise ValueError("Start or end point not detected!")

    path_sequence = ['S']

    current_point = red_points[0]

    sorted_blue_points = []
    remaining_blue_points = blue_points.copy()

    while remaining_blue_points:
        next_point = min(remaining_blue_points, key=lambda p: (p[0] - current_point[0])**2 + (p[1] - current_point[1])**2)
        sorted_blue_points.append(next_point)
        current_point = next_point
        remaining_blue_points.remove(next_point)

    green_point = green_points[0]
    ordered_points = red_points + sorted_blue_points + [green_point]

    current_point = ordered_points[0]
    for next_point in ordered_points[1:]:
        direction = determine_direction(current_point, next_point)
        path_sequence.append(direction)
        current_point = next_point

    path_sequence.append('F')

    return path_sequence

def main():
    image_path = "YOUR_PATH"
    try:
        red_points, green_points, blue_points = detect_colored_points(image_path)
        path_sequence = generate_path_sequence(red_points, green_points, blue_points)
        print("Path Sequence:", path_sequence)
    except Exception as e:
        print(f"Error processing image: {str(e)}")

if __name__ == "__main__":
    main()
