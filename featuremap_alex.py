class AlexNet(nn.Module):
    def __init__(self):
        super(AlexNet, self).__init__()

        self.conv1 = nn.Sequential(nn.Conv2d(3, 96, 11, 4, 2),
                                   nn.ReLU(),
                                   nn.MaxPool2d(3, 2),
                                   )

        self.conv2 = nn.Sequential(nn.Conv2d(96, 256, 5, 1, 2),
                                   nn.ReLU(),
                                   nn.MaxPool2d(3, 2),
                                   )

        self.conv3 = nn.Sequential(nn.Conv2d(256, 384, 3, 1, 1),
                                   nn.ReLU(),
                                   nn.Conv2d(384, 384, 3, 1, 1),
                                   nn.ReLU(),
                                   nn.Conv2d(384, 256, 3, 1, 1),
                                   nn.ReLU(),
                                   nn.MaxPool2d(3, 2))


        self.fc=nn.Sequential(nn.Linear(256*6*6, 4096),
                                nn.ReLU(),
                                nn.Dropout(0.5),
                                nn.Linear(4096, 4096),
                                nn.ReLU(),
                                nn.Dropout(0.5),
                                nn.Linear(4096, 100),
                                )

    def forward(self, x):
        x=self.conv1(x)
        x=self.conv2(x)
        x=self.conv3(x)
        output=self.fc(x.view(-1, 256*6*6))
        return output

model=AlexNet()
for name in model.named_children():
    print(name[0])
#同理先看网络结构
#输出
"""
conv1
conv2
conv3
fc
"""


    
path = "test.jpg"
transformss = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Resize((224, 224)),
     transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])

#注意如果有中文路径需要先解码，最好不要用中文
img = cv2.imread(path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#转换维度
img = transformss(img).unsqueeze(0)

model = AlexNet()


## 修改这里传入的字典即可

new_model = torchvision.models._utils.IntermediateLayerGetter(model, {"conv1":1,"conv2":2,"conv3":3})
out = new_model(img)

tensor_ls=[(k,v) for  k,v in out.items()]

#选取conv2的输出
v=tensor_ls[1][1]

#取消Tensor的梯度并转成三维tensor，否则无法绘图
v=v.data.squeeze(0)

print(v.shape)  # torch.Size([512, 28, 28])


#随机选取25个通道的特征图
channel_num = random_num(25,v.shape[0])
plt.figure(figsize=(10, 10))
for index, channel in enumerate(channel_num):
    ax = plt.subplot(5, 5, index+1,)
    plt.imshow(v[channel, :, :])  # 灰度图参数cmap="gray"
plt.savefig("feature.jpg",dpi=300)



