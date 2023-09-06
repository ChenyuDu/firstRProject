import cv2
import os

# 定义参数f的列表
f_values = [0, 4, 8, 12, 16, 20]

# 定义输入和输出文件夹路径
input_folder = 'goat'
output_folder = 'low-resolution-output'

# 创建输出文件夹
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# 遍历输入文件夹中的图像文件
for filename in os.listdir(input_folder):
    if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):
        input_path = os.path.join(input_folder, filename)
        img = cv2.imread(input_path)

        # 遍历不同的参数f
        for f in f_values:
            if f == 0:
                # 如果参数f为0，图像不变
                output_img = img
            else:
                # 计算新的图像分辨率
                new_width = img.shape[1] // f
                new_height = img.shape[0] // f

                # 使用图像缩放来降低分辨率
                output_img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

                # 将低分辨率图像调整回原始大小
                output_img = cv2.resize(output_img, (img.shape[1], img.shape[0]), interpolation=cv2.INTER_LINEAR)

            # 生成输出文件名
            output_filename = f'{filename}_f_{f}.jpg'
            output_path = os.path.join(output_folder, output_filename)

            # 保存降低分辨率后的图像
            cv2.imwrite(output_path, output_img)

print('低分辨率图像处理完成，并调整为原始大小！')
