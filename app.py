# Vercel serverless Python function

programs = {
    "1": """import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('shiv.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

equalized = cv2.equalizeHist(gray)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
edges = cv2.Canny(gray, 100, 200)

flip = cv2.flip(img, 1)
rotate = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

kernel = np.ones((5,5), np.uint8)
erosion = cv2.erode(thresh, kernel, iterations=1)
dilation = cv2.dilate(thresh, kernel, iterations=1)

images = [img, gray, equalized, thresh, edges, flip, rotate, erosion, dilation]
titles = ["Original", "Grayscale", "Histogram Eq", "Threshold",
          "Edges", "Flipped", "Rotated", "Erosion", "Dilation"]

plt.figure(figsize=(12,10))

for i in range(len(images)):
    plt.subplot(3,3,i+1)

    if len(images[i].shape) == 2:
        plt.imshow(images[i], cmap='gray')
    else:
        plt.imshow(images[i])

    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()""",

    "2": """from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris = load_iris()
X = iris.data[:, :2]
y = iris.target

y = [1 if label == 0 else -1 for label in y]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

w1, w2 = 0.0, 0.0
b = 0.0
lr = 0.1

for _ in range(50):
    for i in range(len(X_train)):
        x1, x2 = X_train[i]
        z = w1*x1 + w2*x2 + b

        y_pred = 1 if z >= 0 else -1

        if y_train[i] != y_pred:
            w1 += lr * y_train[i] * x1
            w2 += lr * y_train[i] * x2
            b += lr * y_train[i]

y_pred = []
for i in range(len(X_test)):
    x1, x2 = X_test[i]
    z = w1*x1 + w2*x2 + b
    y_pred.append(1 if z >= 0 else -1)

print("Accuracy:", accuracy_score(y_test, y_pred) * 100, "%")"""
}

def handler(request):
    path = request.path.split("/")[-1]
    code = programs.get(path, "Program not found")

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/plain"},
        "body": code
    }