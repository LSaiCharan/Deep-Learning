## LeNet-5 Demonstration and OCR Implementation using LeNet-5
he LeNet-5 architecture is a pioneering convolutional Neural Network (CNN) designed by Yann LeCun et al. in 1998. It was specifically developed for handwritten digit recognition tasks, such as the recognition of characters in the MNIST dataset. LeNet-5 played a significant role in popularizing deep learning and CNNs.

The architecture of LeNet-5 consists of seven layers, including three convolutional layers, two average pooling layers, and two fully connected layers. Here's a brief description of each layer:

Convolutional Layer 1: The first layer applies six filters of size 5x5 to the input image. The filters extract low-level features and generate six feature maps.

Average Pooling Layer 1: A 2x2 average pooling layer follows the first convolutional layer. It reduces the spatial dimensions of the feature maps while preserving the important features.

Convolutional Layer 2: The second layer applies 16 filters of size 5x5 to the output of the first pooling layer. It extracts higher-level features and generates 16 feature maps.

Average Pooling Layer 2: Another 2x2 average pooling layer follows the second convolutional layer, further reducing the spatial dimensions.

Flatten Layer: The output of the second pooling layer is flattened into a vector to be fed into the fully connected layers.

Fully Connected Layer 1: This layer consists of 120 neurons and applies the rectified linear unit (ReLU) activation function. It learns complex combinations of features.

Fully Connected Layer 2: The final fully connected layer has 84 neurons with ReLU activation. It further processes the learned features.

