
import cv2
import os

# 定义参数(τ, ω)的列表
# parameters = [(0, 0), (8, 0.6), (9, 0.7), (10, 0.8), (11, 0.9), (12, 1)]
parameters = [(0, 0), (50, 0.2), (70, 0.3), (90, 0.4), (110, 0.5), (130, 0.6)]

# 定义输入和输出文件夹路径
input_folder = 'blimp'
output_folder = 'lighting-output'

# 创建输出文件夹
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# 遍历输入文件夹中的图像文件
for filename in os.listdir(input_folder):
    if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):
        input_path = os.path.join(input_folder, filename)
        img = cv2.imread(input_path)

        # 遍历不同的参数
        for tau, omega in parameters:
            if tau == 0 and omega == 0:
                # 如果参数为(0, 0)，图片不变
                output_img = img
            else:
                # 计算光线变暗的效果
                output_img = cv2.convertScaleAbs(img, alpha=omega, beta=tau)

            # 生成输出文件名
            output_filename = f'{filename}_tau_{tau}_omega_{omega}.jpg'
            output_path = os.path.join(output_folder, output_filename)

            # 保存变换后的图像
            cv2.imwrite(output_path, output_img)

print('光线变暗处理完成！')
