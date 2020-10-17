import numpy as np
import os
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import tensorflow as tf
import functions_for_equation_recog

equation_predicted = [];

operator_class_names=["divide","minus","multiply","plus"];

reconstructed_digit_model = tf.keras.models.load_model("my_digits_model");
reconstructed_operator_model = tf.keras.models.load_model("my_operatormodel");

directory = 'C:/Users/k21pa/dev/PersonalProject/PERSONAL_PROJECT_FINAL_PRODUCT/FINAL_PRODUCT_USERDRAWN';

User_drawn_digit_data = np.empty((100, 28, 28));
User_drawn_operator_data = np.empty((100, 28, 28));

filenum = 1;
crop = True;
for filename in os.listdir(directory):
    image_data = functions_for_equation_recog.preproccess(directory + '/' + filename, filenum,crop);
    # print(image_data.shape);
    if(filenum%2 == 0):
        index = (filenum/2) - 1;
        User_drawn_operator_data[int(index)] = image_data;
    else:
        User_drawn_digit_data[filenum - 1] = image_data;
    filenum = filenum + 1;

User_drawn_digit_data = User_drawn_digit_data.reshape(User_drawn_digit_data.shape[0], 28, 28, 1);
User_drawn_operator_data = User_drawn_operator_data.reshape(User_drawn_operator_data.shape[0], 28, 28, 1);

digit_predictions = reconstructed_digit_model.predict(User_drawn_digit_data);
np.set_printoptions(suppress=True);
operator_predictions = reconstructed_operator_model.predict(User_drawn_operator_data);
np.set_printoptions(suppress=True);

num_of_files = filenum - 1;

functions_for_equation_recog.test_model(equation_predicted, num_of_files, digit_predictions, operator_predictions, User_drawn_digit_data, User_drawn_operator_data, operator_class_names);

answer = functions_for_equation_recog.find_equation_answer(equation_predicted);

for i in equation_predicted:
    print(str(i));

print(answer);
