import cv2
import os
import numpy as np

# 定义模糊参数的列表
blur_lengths = [0, 5, 10, 15, 20, 25]

# 定义输入和输出文件夹路径
input_folder = 'butterfly'
output_folder = 'motion-blurred-output'

# 创建输出文件夹
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# 遍历输入文件夹中的图像文件
for filename in os.listdir(input_folder):
    if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):
        input_path = os.path.join(input_folder, filename)
        img = cv2.imread(input_path)

        # 遍历不同的模糊参数
        for blur_length in blur_lengths:
            if blur_length > 0:
                # 创建运动模糊核
                kernel = np.zeros((blur_length, blur_length))
                kernel[int((blur_length-1)/2), :] = np.ones(blur_length)
                kernel /= blur_length

                # 应用运动模糊
                img_blurred = cv2.filter2D(img, -1, kernel)

                # 保存模糊图像到输出文件夹
                output_filename = f'{filename}_blur_{blur_length}.jpg'
                output_path = os.path.join(output_folder, output_filename)
                cv2.imwrite(output_path, img_blurred)

            else:
                # 如果参数为0，直接复制原图像
                output_path = os.path.join(output_folder, filename)
                cv2.imwrite(output_path, img)

print('运动模糊完成！')
