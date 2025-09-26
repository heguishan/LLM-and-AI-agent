import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')  # 在 import matplotlib.pyplot 之前
import matplotlib.pyplot as plt
import numpy as np

# 数据预处理和加载
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
train_dataset = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transform)
test_dataset = torchvision.datasets.MNIST(root='./data', train=False, download=True, transform=transform)

train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)

# 模型定义：简单多层感知机 (MLP)
class SimpleMLP(nn.Module):
    def __init__(self):
        super(SimpleMLP, self).__init__()
        self.fc1 = nn.Linear(28*28, 128)  # 输入层：784 -> 128
        self.fc2 = nn.Linear(128, 64)     # 隐藏层：128 -> 64
        self.fc3 = nn.Linear(64, 10)      # 输出层：64 -> 10 (数字0-9)

    def forward(self, x):
        x = x.view(-1, 28*28)  # 展平图像
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x

# 实例化模型、损失函数和优化器
model = SimpleMLP()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 训练模型
epochs = 3  # 少量epoch以便快速运行；实际可增加到10+
for epoch in range(epochs):
    model.train()
    running_loss = 0.0
    for images, labels in train_loader:
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        running_loss += loss.item()
    print(f"Epoch {epoch+1}/{epochs}, Loss: {running_loss/len(train_loader):.4f}")

# 评估模型
model.eval()
correct = 0
total = 0
with torch.no_grad():
    for images, labels in test_loader:
        outputs = model(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
print(f"Accuracy on test set: {100 * correct / total:.2f}%")

# 可视化部分预测结果
def visualize_predictions():
    dataiter = iter(test_loader)
    images, labels = next(dataiter)
    outputs = model(images)
    _, predicted = torch.max(outputs, 1)

    fig = plt.figure(figsize=(10, 10))
    for idx in range(9):
        ax = fig.add_subplot(3, 3, idx+1)
        img = images[idx][0].numpy() * 0.5 + 0.5  # 反归一化
        ax.imshow(img, cmap='gray')
        ax.set_title(f"Pred: {predicted[idx].item()}\nTrue: {labels[idx].item()}")
        ax.axis('off')
    plt.show()

visualize_predictions()