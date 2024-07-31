



import time
import numpy as np
import random
import random
import cv2 as cv

# Example motivational phrases
motivational_phrases = [
    "Great job!",
    "You're doing fantastic!",
    "Keep up the good work!",
    "Excellent!",
    "You're on fire!"
]


def overlay_image(background, overlay, x, y):
    """
    Overlay an image onto another image at the specified position.

    Args:
        background (np.ndarray): The background image.
        overlay (np.ndarray): The image to overlay.
        x (int): The x-coordinate for the top-left corner of the overlay.
        y (int): The y-coordinate for the top-left corner of the overlay.

    Returns:
        np.ndarray: The combined image with the overlay.
    """
    bg_h, bg_w = background.shape[:2]
    ol_h, ol_w = overlay.shape[:2]

    # Ensure the overlay is within the bounds of the background
    if x + ol_w > bg_w or y + ol_h > bg_h:
        raise ValueError("Overlay image exceeds the background dimensions")

    # Overlay the image
    combined_image = background.copy()
    combined_image[y:y+ol_h, x:x+ol_w] = overlay

    return combined_image


# def Show_Sign_Learn(image,model_out, confidence):
#     """
#     Show the user sign language letters and ask them to copy them.
#     Uses the model to verify the user's attempt.

#     Args:
#         model: The trained sign language recognition model.
#         sign_data: Dictionary of sign data (letters as keys and corresponding image/keypoints as values).
#     """

#     sign_list = random.choices(range(0, 26), k=50)

#     #50 iterations of learning signs

#     for sign in sign_list:
#         # reading the name of the nth leter form labels, and using that below
#         # path = r"C:\Users\Marianna\Desktop\DM_hand_recognition\letters\"+ "\\"  + str(sign) + ".jpg"
#         # path = r"C:\Users\Marianna\Desktop\DM_hand_recognition\letters" + "\\" + str(sign) + ".jpg"
#         # sign_photo = cv.imread(path)
#         # print(f"Please show the sign for: {sign}")
#         cv.putText(image, "Show this gesture:", (10, 30), cv.FONT_HERSHEY_SIMPLEX,
#                1.0, (0, 0, 0), 4)
#         # overlay_image(image,sign_photo,30,30)
#         start_time = time.time()
#         correct = False
        
#         while not correct:
#             # Capture the user's attempt (this should be replaced with actual data capturing logic)
#             user_attempt = model_out
#               # Replace with actual capturing function

#             # Use the model to predict the sign
#             # prediction 
            
#             # Check if the prediction matches the expected sign with a certain confidence threshold
#             if user_attempt == sign and confidence > 0.999:
#                 phr = Good_job()
                
#                 cv.putText(image,phr,(10, 10),cv.FONT_HERSHEY_SIMPLEX,
#                1.0, (0, 255, 0), 4)
#                 correct = True
                
#             else:
#                 if time.time() - start_time > 15:
#                     phr = Try_more()
#                     cv.putText(image,phr,(10, 10),cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 4)
#                     time.sleep(5)
#                     start_time = time.time()  # Reset the timer
#         return image


def Good_job(image,hand,sign,conf,correct):
    """
    Randomly provide motivational feedback to the user.
    """
    phrase = random.choice(motivational_phrases)
    if sign == hand and conf > 0.999:    
        cv.putText(image,phrase,(10, 10),cv.FONT_HERSHEY_SIMPLEX,
               1.0, (0, 255, 0), 4)
        correct = True
        sign = random.randint(0,26)


        print(phrase)
    return image,correct,sign

def Try_more(image):
    """
    Encourage the user to try again after 15 seconds of incorrect attempts.
    """
    print("Noo, you can do better! Keep trying.") 
    cv.putText(image,"Noo, you can do better! Keep trying.",(10, 10),cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 4)
    return image

# def capture_user_sign():
#     """
#     Placeholder function to capture user's sign attempt.
#     This function should be replaced with actual logic to capture and process the user's sign.

#     Returns:
#         np.ndarray: The captured sign data (keypoints).
#     """
#     # Replace this with actual capturing logic
#     return np.random.rand(1, 42)

# def predict_sign(model, input_data):
#     """
#     Predict the sign using the provided model.

#     Args:
#         model: The trained sign language recognition model.
#         input_data: The input data for prediction (keypoint representations).

#     Returns:
#         tuple: Predicted sign and its confidence score.
#     """
#     predictions = model.predict(input_data)
#     predicted_class = np.argmax(predictions)
#     confidence_score = np.max(predictions)
#     return predicted_class, confidence_score

# Example usage



