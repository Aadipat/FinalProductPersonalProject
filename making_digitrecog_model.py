import numpy as np
import tensorflow as tf

# LAODING AND PROCCESSING DATA
#Load the Data of Hand written digits
mnist = tf.keras.datasets.mnist;

#define training and Testing data
(training_data, training_labels) , (test_data, test_labels) = mnist.load_data();

print(test_data.shape);

print(test_data[0].shape);
#divide training_data and testing data to reduce noise
training_data, test_data = training_data / 255, test_data / 255;
#Reshaping data so it can be used in Keras model
training_data = training_data.reshape(training_data.shape[0], 28, 28, 1);
test_data = test_data.reshape(test_data.shape[0], 28, 28, 1);

input_shape = (28,28,1);

#DEFINING AND COMPILING MODEL
#Define tensorflow keras sequentoial Model, input (28x28) images.
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(28, kernel_size=(3,3), input_shape=input_shape),
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
    tf.keras.layers.Flatten(input_shape=input_shape),
    tf.keras.layers.Dense(128, activation=tf.nn.relu),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation=tf.nn.softmax)
]);
#print summary
model.summary();
#Compile model using optimizer adam.
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy']);


#TRAINING THE MODEL
#fit the model, train it with 5 epochs.
model.fit(training_data, training_labels, epochs=10);
#evaluate the model and see accuracy.
model.evaluate(test_data, test_labels);

#Use model to predict the test data
predictions = model.predict(test_data);
np.set_printoptions(suppress=True);

# Saving the model.
model.save("my_model");
