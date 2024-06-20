import streamlit as st
from PIL import Image
import torch
from transformers import DetrImageProcessor, DetrForObjectDetection

# Load pre-trained model and processor
model = DetrForObjectDetection.from_pretrained('facebook/detr-resnet-50')
processor = DetrImageProcessor.from_pretrained('facebook/detr-resnet-50')

def analyze_image(image):
    # Prepare the image for the model
    inputs = processor(images=image, return_tensors="pt")
    
    # Forward pass
    outputs = model(**inputs)
    
    # Get the class labels
    target_sizes = torch.tensor([image.size[::-1]])
    results = processor.post_process_object_detection(outputs, target_sizes=target_sizes)[0]
    
    # Extract detected objects
    components = []
    for score, label in zip(results["scores"], results["labels"]):
        if score > 0.9:  # Threshold to filter out low-confidence detections
            components.append(model.config.id2label[label.item()])
    
    return components

st.title("Image Component Analyzer")

# Upload image widget
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

    if st.button('Analyze Image'):
        # Call the image analysis function here
        components = analyze_image(image)
        st.write("Detected components:")
        for component in components:
            st.write(component)
