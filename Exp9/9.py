import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)

model = models.Sequential([
    layers.Input(shape=(28, 28, 1)),
    layers.Conv2D(32, (3, 3), activation="relu", name="conv1"),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation="relu", name="conv2"),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation="relu"),
    layers.Dense(10, activation="softmax")
])

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

model.fit(
    x_train,
    y_train,
    epochs=5,
    batch_size=64,
    validation_split=0.1,
    verbose=1
)

probabilities = model.predict(x_test, verbose=0)
y_pred = probabilities.argmax(axis=1)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average="macro", zero_division=0)
recall = recall_score(y_test, y_pred, average="macro", zero_division=0)
f1 = f1_score(y_test, y_pred, average="macro", zero_division=0)

print("\nEvaluation Metrics")
print("-" * 58)
print(f"{'Metric':<20}{'Value':>12}")
print("-" * 58)
print(f"{'Accuracy':<20}{accuracy:>12.4f}")
print(f"{'Precision (macro)':<20}{precision:>12.4f}")
print(f"{'Recall (macro)':<20}{recall:>12.4f}")
print(f"{'F1-score (macro)':<20}{f1:>12.4f}")
print("-" * 58)

kernel, bias = model.get_layer("conv1").get_weights()

print("\nFirst convolution layer: kernel for filter 1")
print("-" * 36)

for row in kernel[:, :, 0, 0]:
    print(" ".join(f"{value:8.4f}" for value in row))