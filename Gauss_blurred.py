import cv2
import os

# 定义参数g的列表
g_values = [0, 1, 2, 3, 4, 5]

# 定义输入和输出文件夹路径
input_folder = 'peopel'
output_folder = 'Gaussian-blurred-output'

# 创建输出文件夹
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# 遍历输入文件夹中的图像文件
for filename in os.listdir(input_folder):
    if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):
        input_path = os.path.join(input_folder, filename)
        img = cv2.imread(input_path)

        # 遍历不同的参数g
        for g in g_values:
            if g == 0:
                # 如果参数g为0，图像不变
                output_img = img
            else:
                # 使用高斯模糊来模糊图像
                output_img = cv2.GaussianBlur(img, (2 * g + 1, 2 * g + 1), 0)

            # 生成输出文件名
            output_filename = f'{filename}_g_{g}.jpg'
            output_path = os.path.join(output_folder, output_filename)

            # 保存模糊后的图像
            cv2.imwrite(output_path, output_img)

print('高斯模糊图像处理完成！')
