# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
# import numpy as np
# import tensorflow as tf


# class KeyPointClassifier(object):
#     def __init__(
#         self,
#         # model_path='model/keypoint_classifier/keypoint_classifier.tflite',
#         model_path = 'model/keypoint_classifier/keypoint_classifier.keras',
#         num_threads=1,
#     ):
#         self.interpreter = tf.lite.Interpreter(model_path=model_path,
#                                                num_threads=num_threads)

#         self.interpreter.allocate_tensors()
#         self.input_details = self.interpreter.get_input_details()
#         self.output_details = self.interpreter.get_output_details()

#     def __call__(
#         self,
#         landmark_list,
#     ):
#         # print("this is the landmark list ", len(landmark_list)
#         input_details_tensor_index = self.input_details[0]['index']
#         self.interpreter.set_tensor(
#             input_details_tensor_index,
#             np.array([landmark_list], dtype=np.float32))
#         self.interpreter.invoke()

#         output_details_tensor_index = self.output_details[0]['index']

#         result = self.interpreter.get_tensor(output_details_tensor_index)

#         result_index = np.argmax(np.squeeze(result))

#         return result_index


################## JUST MODEL VERSION ###########################
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import tensorflow as tf


class KeyPointClassifier(object):
    def __init__(
        self,
        model_path='model/keypoint_classifier/keypoint_classifier.keras',
        num_threads=1,
    ):
        # Load the Keras model
        self.model = tf.keras.models.load_model(model_path)
    def __call__(
        self,
        landmark_list,
    ):
        # Prepare the input data
        input_data = np.array([landmark_list], dtype=np.float32)

        # Perform prediction
        result = self.model.predict(input_data)

        # Interpret the result
        result_index = np.argmax(np.squeeze(result))
        # print("the confidance or argmax",result,"\n")
        confidence_score = np.max(result)
        print("the confidance or argmax",confidence_score,"\n")

        # confidence_scores.append((predicted_class, confidence_score))
    
        # if confidence_score >= 0.98:
        #     return result_index
        # else:
        #     return 

        return result_index, confidence_score