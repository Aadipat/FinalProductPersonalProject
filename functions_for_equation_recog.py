import numpy as np
import os
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import tensorflow as tf

def preproccess(path, image_num, flag = True):
    #CODE TO INVERT AND RESIZE image
    img = Image.open(path).convert('RGB');
    # CODE to crop if tthe image is being used the first time.
    if(flag == True):
        width,height = img.size;
        #
        left = (image_num-1)* height;
        top = 0;
        right = image_num*height;
        bottom = height;
        #
        img = img.crop((left,top,right,bottom));
    converted_image = ImageOps.invert(img);
    converted_image = converted_image.resize((round(28), round(28)))
    converted_image.save(path);
    # Using Keras Preproccessing to convert to grayscale.
    image=tf.keras.preprocessing.image.load_img(
        path, color_mode='grayscale', target_size=None,
        interpolation='nearest'
    );
    input_arr = tf.keras.preprocessing.image.img_to_array(image);
    input_arr = np.array([input_arr]);  # Convert single image to a batch.
    input_arr = input_arr.reshape(28, 28);
    #Sending back image data.
    return input_arr;

def print_prediction(confidence_array):
  max = 0;
  most_likely = 0;
  for i in range(len(confidence_array)):
      if(confidence_array[i] > max):
        max = confidence_array[i];
        most_likely = i;
  prediction = [most_likely, max];
  return prediction;

def find_class(confidence_array, class_names):
    index = 0;
    val = 0;
    for i in range(len(confidence_array)):
        if(float(confidence_array[i]) > val):
            val = confidence_array[i];
            index = i;
    predicted_class = class_names[index];
    return predicted_class;

def test_model( equation_predicted, num, digit_predictions, operator_predictions, digits_data, operators_data, class_names):
  i = 1;
  while(i <= num):
    #print(test_labels[i])
    if(i%2 == 0):
        # print(np.argmax(predictions[i]));
        index = (i/2) - 1;
        plt.imshow(operators_data[int(index)]);
        predicted_class = find_class(operator_predictions[int(index)], class_names);
        # print(predicted_class);
        # ('This Image is of digit ', most_likely
        plt.title('This is an Image of operator '+ str(predicted_class));
        equation_predicted.append(str(predicted_class));
    else:
        plt.imshow(digits_data[i-1]);
        prediction = print_prediction(digit_predictions[i-1]);
        plt.title('This is an Image of digit '+ str(prediction[0])+
            ' , I am '+ str(prediction[1]*100) + '% Sure!');
        equation_predicted.append(int(prediction[0]));
    plt.show();
    i = i + 1;

def find_equation_answer(equation):
    answer = 0;
    previous_operator = 'none';
    for i in range(len(equation)):
        if(isinstance(equation[i], str) == True):
            previous_operator = equation[i];
        elif(isinstance(equation[i], int)):
            if(previous_operator == 'plus'):
                answer = answer + equation[i];
            elif(previous_operator == 'minus'):
                answer = answer - equation[i];
            elif(previous_operator == 'multiply'):
                answer = answer*equation[i];
            elif(previous_operator == 'divide'):
                answer = answer/equation[i];
            else:
                answer = answer + equation[i];
    return answer;
