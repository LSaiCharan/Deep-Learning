<center> <h3> Auto-Encoders </h3> </center>

Autoencoders are a type of neural network architecture used for unsupervised learning and dimensionality reduction. They consist of two main components: an encoder and a decoder.

The encoder takes an input data sample and maps it to a lower-dimensional representation called the "encoded" or "latent" space. This is achieved through a series of hidden layers that gradually reduce the dimensionality of the input. Each hidden layer typically applies a non-linear activation function, such as ReLU, to introduce non-linearity into the model.

The decoder, on the other hand, takes the encoded representation and maps it back to the original input space. It has a structure similar to the encoder, but with layers that gradually increase the dimensionality of the representation. The final output of the decoder aims to reconstruct the input data as accurately as possible.

The goal of the autoencoder is to minimize the reconstruction error between the original input and the output of the decoder. By doing so, it learns to capture the most salient features of the input data in the encoded representation. Autoencoders are often used for tasks such as dimensionality reduction, anomaly detection, denoising, and generative modeling.
