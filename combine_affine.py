import cv2
import numpy as np

def translate_image(image, dx, dy):
    rows, cols, _ = image.shape
    M = np.float32([[1, 0, dx], [0, 1, dy]])
    translated_image = cv2.warpAffine(image, M, (cols, rows))
    return translated_image

def scale_image(image, scale_x, scale_y):
    rows, cols, _ = image.shape
    scaled_image = cv2.resize(image, None, fx=scale_x, fy=scale_y)
    return scaled_image

def flip_image(image, flip_code):
    flipped_image = cv2.flip(image, flip_code)
    return flipped_image

def rotate_image(image, angle):
    rows, cols, _ = image.shape
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    rotated_image = cv2.warpAffine(image, M, (cols, rows))
    return rotated_image

def shear_image(image, shear_factor_x, shear_factor_y):
    rows, cols, _ = image.shape
    M = np.float32([[1, shear_factor_x, 0], [shear_factor_y, 1, 0]])
    sheared_image = cv2.warpAffine(image, M, (cols, rows))
    return sheared_image

# def apply_image_transformations(image, translation=True, scaling=True, flipping=True, rotation=True, shearing=True):
#     """
#     对图片应用组合变换
#     :param image: 输入图片
#     :param translation: 是否进行平移变换
#     :param scaling: 是否进行缩放变换
#     :param flipping: 是否进行翻转变换
#     :param rotation: 是否进行旋转变换
#     :param shearing: 是否进行错切变换
#     :return: 组合变换后的图片
#     """
#     transformed_image = image.copy()
#
#     if translation:
#         dx, dy = np.random.randint(-50, 50, 2)  # 随机生成平移量
#         transformed_image = translate_image(transformed_image, dx, dy)
#
#     if scaling:
#         scale_x, scale_y = np.random.uniform(0.8, 1.2, 2)  # 随机生成缩放因子
#         transformed_image = scale_image(transformed_image, scale_x, scale_y)
#
#     if flipping:
#         flip_code = np.random.randint(-1, 2)  # 随机生成翻转类型
#         transformed_image = flip_image(transformed_image, flip_code)
#
#     if rotation:
#         angle = np.random.randint(-30, 30)  # 随机生成旋转角度
#         transformed_image = rotate_image(transformed_image, angle)
#
#     if shearing:
#         shear_factor_x, shear_factor_y = np.random.uniform(-0.3, 0.3, 2)  # 随机生成错切因子
#         transformed_image = shear_image(transformed_image, shear_factor_x, shear_factor_y)
#
#     return transformed_image

def apply_image_transformation(image, beta):
    transformed_image = image.copy()

    if beta == 1:
        dx, dy = np.random.randint(-50, 51, 2)
        transformed_image = translate_image(transformed_image, dx, dy)
    elif beta == 2:
        scale_x, scale_y = np.random.uniform(0.8, 1.2, 2)
        transformed_image = scale_image(transformed_image, scale_x, scale_y)
    elif beta == 3:
        flip_code = np.random.randint(-1, 2)
        transformed_image = flip_image(transformed_image, flip_code)
    elif beta == 4:
        angle = np.random.randint(-30, 31)
        transformed_image = rotate_image(transformed_image, angle)
    elif beta == 5:
        shear_factor_x, shear_factor_y = np.random.uniform(-0.3, 0.3, 2)
        transformed_image = shear_image(transformed_image, shear_factor_x, shear_factor_y)

    return transformed_image

# 读取输入图片
input_image_path = 'grapes.jpeg'  # 替换为你的输入图片路径
original_image = cv2.imread(input_image_path)


def generate_transformed_image(image, beta):
    translation = True
    scaling = True
    flipping = True
    rotation = True
    shearing = True

    transformed_image = image.copy()

    if beta > 0:
        # dx, dy = np.random.randint(-50 * beta, 50 * beta, 2)
        # scale_x, scale_y = np.random.uniform(0.8 * beta, 1.2 * beta, 2)
        # flip_code = np.random.randint(-1 * beta, 2 * beta)
        # angle = np.random.randint(-30 * beta, 30 * beta)
        # shear_factor_x, shear_factor_y = np.random.uniform(-0.3 * beta, 0.3 * beta, 2)
        max_translation = min(70, beta * 15)
        dx, dy = np.random.randint(-max_translation, max_translation, 2)
        scale_x, scale_y = np.random.uniform(0.9, 1.1, 2)
        flip_code = np.random.randint(-1, 2)
        angle = np.random.randint(-20, 20)
        shear_factor_x, shear_factor_y = np.random.uniform(-0.15, 0.15, 2)

        transformed_image = translate_image(transformed_image, dx, dy)
        transformed_image = scale_image(transformed_image, scale_x, scale_y)
        transformed_image = flip_image(transformed_image, flip_code)
        transformed_image = rotate_image(transformed_image, angle)
        transformed_image = shear_image(transformed_image, shear_factor_x, shear_factor_y)

    return transformed_image

# 初始化一个空白画布，用于存放生成的扭曲图像
canvas = np.zeros((original_image.shape[0], original_image.shape[1] * 6, 4), dtype=np.uint8)  # 使用四个通道，最后一个通道表示透明度

# # 生成并排列六张不同扭曲程度的图像
# for i in range(6):
#     transformed_image = apply_image_transformations(original_image, translation=True, scaling=True, flipping=True, rotation=True, shearing=True)
#     transformed_image_resized = cv2.resize(transformed_image, (original_image.shape[1], original_image.shape[0]))
#     canvas[:, i * original_image.shape[1] : (i + 1) * original_image.shape[1], :3] = transformed_image_resized  # 前三个通道为图像数据
#     canvas[:, i * original_image.shape[1] : (i + 1) * original_image.shape[1], 3] = 255  # 设置完全不透明的透明度值
# 生成并排列六张不同扭曲程度的图像
for i, beta in enumerate([0, 1, 2, 3, 4, 5]):
    transformed_image = generate_transformed_image(original_image, beta)
    transformed_image_resized = cv2.resize(transformed_image, (original_image.shape[1], original_image.shape[0]))
    canvas[:, i * original_image.shape[1] : (i + 1) * original_image.shape[1], :3] = transformed_image_resized  # 前三个通道为图像数据
    canvas[:, i * original_image.shape[1] : (i + 1) * original_image.shape[1], 3] = 255  # 设置完全不透明的透明度值

# 保存合并后的图片为 PNG 格式（支持透明通道）
cv2.imwrite('combined_transformed_images.png', canvas)
# 在这段代码中，将画布的通道数设置为 4，分别表示图像的 RGB 通道以及透明度通道。将每张扭曲图像的 RGB 数据放入前三个通道，将透明度通道设置为完全不透明（值为 255）。然后，将合并后的图像保存为 PNG 格式，以保留透明通道。





