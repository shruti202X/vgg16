from keras.applications.vgg16 import VGG16
from keras.models import Model

# Load the pre-trained VGG model without the top (fully connected) layers
base_model = VGG16(weights=None, include_top=True, input_shape=(224, 224, 3))

# Create a new model with the VGG base model's input and output
vgg = Model(inputs=base_model.input, outputs=base_model.output)

# Load weights from the H5 file
vgg.load_weights('/kaggle/input/vgg16-weights-tf-keras-with-top/vgg16_weights_tf_dim_ordering_tf_kernels.h5')

# Example usage: extracting features from an image
import numpy as np
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input

# Load and preprocess an image
img_path = '/kaggle/input/fracatlas/FracAtlas/images/Fractured/IMG0000019.jpg'
img = image.load_img(img_path, target_size=(224, 224))
x_img = image.img_to_array(img)
x_img = np.expand_dims(x_img, axis=0)
x_imp = preprocess_input(x_img)

# Extract features using the VGG model
features = vgg.predict(x_img)

print(features.shape) #(1, 1000)
print(sum(features[0])) #0.999999942553643
print(max(features[0])) #0.21049187
