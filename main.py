from src.data import load_data, preprocess_data
from src.models import create_model
from src.utils import shuffle_data, split_data
from src.visualize import plot_loss, plot_accuracy
#import GPT
import openai_secret_manager
import gpt_3

#import module GPT
assert "gpt" in openai_secret_manager.get_services()
secrets = openai_secret_manager.get_secrets("gpt")

print(secrets)
# Load model gpt
import openai
model_engine = "text-davinci-002"
model_prompt = (f"{model_engine} prompt: > ")

openai.api_key = secrets["api_key"]

def generate_text(prompt):
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = completions.choices[0].text
    return message.strip()

# Use gpt to generate text
generated_text = generate_text(model_prompt)
print(generated_text)
 
#gpt3
prompt = 'Il cane è il migliore amico dell'uomo.'
model = gpt_3.GPT(engine='text-davinci-002')
response = model.complete


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
