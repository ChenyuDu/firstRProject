import cv2
import os
import numpy as np

# 定义参数v的列表
v_values = [0, 0.05, 0.1, 0.15, 0.2, 0.25]

# 定义输入和输出文件夹路径
input_folder = 'mushroom'
output_folder = 'Gaussian white noise-output'

# 创建输出文件夹
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# 遍历输入文件夹中的图像文件
for filename in os.listdir(input_folder):
    if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):
        input_path = os.path.join(input_folder, filename)
        img = cv2.imread(input_path)

        # 遍历不同的参数v
        for v in v_values:
            if v == 0:
                # 如果参数v为0，图像不变
                output_img = img
            else:
                # 生成与图像大小相同的高斯噪声
                noise = np.random.normal(0, v * 255, img.shape).astype(np.uint8)

                # 将噪声添加到图像中
                noisy_img = cv2.add(img, noise)

                output_img = noisy_img

            # 生成输出文件名
            output_filename = f'{filename}_v_{v}.jpg'
            output_path = os.path.join(output_folder, output_filename)

            # 保存添加噪声后的图像
            cv2.imwrite(output_path, output_img)

print('高斯白噪声图像处理完成！')
