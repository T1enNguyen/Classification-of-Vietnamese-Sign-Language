import gradio as gr
import tensorflow as tf
import numpy as np
from PIL import Image

# Class labels for Vietnamese Sign Language - 25 classes
CLASS_LABELS = ['A', 'AA', 'B', 'C', 'D', 'DD', 'E', 'G', 'H', 'I', 'K', 'L', 'M',
                'N', 'O', 'OOO', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y']

# Global variable for lazy loading
model = None

def load_model():
    global model
    if model is None:
        print("Loading model...")
        model = tf.keras.models.load_model('model/mobilenet_vsl.keras')
        print("Model loaded successfully!")
    return model

def predict_sign(image):
    # Load model if not already loaded
    mdl = load_model()

    # Preprocess image
    img = Image.fromarray(image.astype('uint8'), 'RGB')
    img = img.resize((224, 224))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    predictions = mdl.predict(img_array, verbose=0)

    # Create result dictionary
    result = {CLASS_LABELS[i]: float(predictions[0][i]) for i in range(len(CLASS_LABELS))}

    return result

# Create Gradio interface
demo = gr.Interface(
    fn=predict_sign,
    inputs=gr.Image(),
    outputs=gr.Label(num_top_classes=5),
    title="Vietnamese Sign Language Classification",
    description="Upload an image of a Vietnamese Sign Language hand gesture to classify it. The model recognizes 25 classes including A, AA, B, C, D, DD, E, G, H, I, K, L, M, N, O, OOO, P, Q, R, S, T, U, V, X, Y.",
    examples=[
        ["examples/C.jpg"],
        ["examples/D.jpg"],
        ["examples/H.jpg"],
        ["examples/O.jpg"]
    ]
)

if __name__ == "__main__":
    demo.launch()
