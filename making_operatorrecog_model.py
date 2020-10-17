import pathlib
import tensorflow as tf

#DEFINING DATA and USING KERAS TO PREPROCCESS the data, splitting into training and validation.

data_dir = pathlib.Path('C:/Users/k21pa/dev/PersonalProject/FINAL_PRODUCT/selfmade_hand_drawn_dataset/operators/');
image_count = len(list(data_dir.glob('*/*.jpg')));

print("Detected " + str(image_count) +" images");

train_ds = tf.keras.preprocessing.image_dataset_from_directory(
  data_dir,
  labels="inferred",
  color_mode='grayscale',
  validation_split=0.2,
  subset="training",
  seed=123,
  image_size=(28, 28));
val_ds = tf.keras.preprocessing.image_dataset_from_directory(
  data_dir,
  labels="inferred",
  color_mode='grayscale',
  validation_split=0.2,
  subset="validation",
  seed=123,
  image_size=(28, 28));

# Creating the class anmes (labels).
class_names = train_ds.class_names;
print("Detected "+str(class_names)+" classes");
# from tensorflow.keras import layers
# normalization_layer = tf.keras.layers.experimental.preprocessing.Rescaling(1./255);
# Build sequential model
model = tf.keras.Sequential([
  tf.keras.layers.experimental.preprocessing.Rescaling(1./255, input_shape=(28, 28, 1)),
  tf.keras.layers.Conv2D(28, 3, padding='same', activation='relu'),
  tf.keras.layers.MaxPooling2D(),
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(128, activation='softmax'),
  tf.keras.layers.Dense(len(class_names))
])

model.compile(
  optimizer='adam',
  loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True),
  metrics=['accuracy']);

model.fit(
  train_ds,
  validation_data=val_ds,
  epochs=20
)

model.evaluate(val_ds);

model.save("my_operatormodel")
print(" Saved operator model")
