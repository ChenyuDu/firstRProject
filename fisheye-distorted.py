import cv2
import os
import numpy as np
import math
from google.colab.patches import cv2_imshow

def transform(img, distortion_param):
    rows, cols, c = img.shape
    R = np.int(cols / 2 / math.pi)
    D = R * 2
    cx = R
    cy = R

    new_img = np.zeros((D, D, c), dtype=np.uint8)

    for i in range(D):
        for j in range(D):
            r = math.sqrt((i - cx) ** 2 + (j - cy) ** 2)
            if r > R:
                continue
            tan_inv = np.arctan((j - cy) / (i - cx + 1e-10))
            if (i < cx):
                theta = math.pi / 2 + tan_inv
            else:
                theta = math.pi * 3 / 2 + tan_inv
            xp = np.int(np.floor(theta / 2 / math.pi * cols))
            yp = np.int(np.floor(r / R * rows))
            new_img[j, i] = img[rows - yp - 1, xp]

    return new_img

# 定义鱼眼参数的列表
fisheye_params = [0, 1, 1.25, 1.5, 2, 2.25, 2.5]

# 定义输入和输出文件夹路径
input_folder = 'fisheye'
output_folder = 'fisheye-output'

# 创建输出文件夹
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# 遍历输入文件夹中的图像文件
for filename in os.listdir(input_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        input_path = os.path.join(input_folder, filename)
        img = cv2.imread(input_path)

        # 遍历不同的鱼眼参数
        for fisheye_param in fisheye_params:
            if fisheye_param >= 0:
                transformed_img = transform(img, fisheye_param)

                # 生成输出文件名
                output_filename = f'{filename}_distortion_{fisheye_param}.jpg'
                output_path = os.path.join(output_folder, output_filename)

                # 保存变换后的图像
                cv2.imwrite(output_path, transformed_img)

                # 显示图像（可选）
                cv2_imshow(transformed_img)

print('鱼眼效果处理完成！')