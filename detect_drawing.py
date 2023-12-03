""" 4. lépés """

from enum import Enum
import numpy as np
import cv2
import os

class DrawingClass(Enum):
    CLEAN = "LABEL_0"
    MARKED = "LABEL_1"

class DetectDrawingSolution:
    def __init__(self) -> None:
        self.images: list = []

    def algorithm(self, image) -> DrawingClass:
        """ The algorithm to classify the drawings wether it is marked as the correct answer or not.

        Args:
            image (_type_): The image to classify.

        Returns:
            DrawingClass: The classification of the image.
        """
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        difference_threshold = 100
        difference_mask = np.any(np.abs(image - gray_image[:, :, np.newaxis]) > difference_threshold, axis=-1).astype(np.uint8)
        difference_pixel_count = np.sum(difference_mask)
        total_pixels = image.shape[0] * image.shape[1]
        difference_percentage = (difference_pixel_count / total_pixels) * 100
        # print(difference_percentage) # testing percentages
        if difference_percentage != 100:
            return DrawingClass.MARKED
        return DrawingClass.CLEAN
        
    def get_images(self, folder_path = 'tesztlap-kiertekeles\\test_data\\drawing_detection') -> list:
        """ Gets the images from the target folder.

        Args:
            folder_path (str, optional): The path of the folder. Defaults to 'tesztlap-kiertekeles\test_data\drawing_detection'.

        Returns:
            list: The list of the images.
        """
        all_files = os.listdir(folder_path)
        image_files = [file for file in all_files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
        self.images = []
        for image_file in image_files:
            image_path = os.path.join(folder_path, image_file)
            image = cv2.imread(image_path)
            self.images.append(image)
        return self.images

if __name__ == "__main__":
    example = DetectDrawingSolution()
    for image in example.get_images(folder_path='tesztlap-kiertekeles\\test_data\\drawing_detection'):
        DetectDrawingSolution().algorithm(image)
        cv2.imshow(f'test_image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()