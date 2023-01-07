from src.data import load_data, preprocess_data
from src.models import create_model
from src.utils import shuffle_data, split_data
from src.visualize import plot_loss, plot_accuracy

# Load and preprocess data
X, y = load_data()
X, y = preprocess_data(X, y)

# Shuffle and split data into train and test sets
X, y = shuffle_data(X, y)
X_train, X_test, y_train, y_test = split_data(X, y, test_size=0.2)

# Create model
model = create_model()

# Train model
history = model.fit(X_train, y_train, epochs=20,
                    batch_size=32, validation_data=(X_test, y_test))

# Evaluate model
score = model.evaluate(X_test, y_test, verbose=0)
print("Test loss:", score[0])
print("Test accuracy:", score[1])

# Plot loss and accuracy
plot_loss(history)
plot_accuracy(history)
