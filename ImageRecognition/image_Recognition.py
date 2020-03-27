from imageai.Prediction import ImagePrediction
import os

#This script uses Prediction classes to determine the image.
execution_path = os.getcwd()

prediction = ImagePrediction()
prediction.setModelTypeAsSqueezeNet() #Type of the model to use
prediction.setModelPath(os.path.join(execution_path, "squeezenet_weights_tf_dim_ordering_tf_kernels.h5")) #Path to the model.
prediction.loadModel()

predictions, probabilities = prediction.predictImage(os.path.join(execution_path, "maison.jpg"), result_count=5 )
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction , " : " , eachProbability)