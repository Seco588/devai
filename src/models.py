import tensorflow as tf


def create_model(input_shape, num_classes):
    # Define model architecture here
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(
        10, input_shape=input_shape, activation='relu'))
    model.add(tf.keras.layers.Dense(num_classes, activation='softmax'))
    return model


def compile_model(model, optimizer, loss, metrics):
    # Compile model with specified optimizer, loss function, and evaluation metrics
    model.compile(optimizer=optimizer, loss=loss, metrics=metrics)
