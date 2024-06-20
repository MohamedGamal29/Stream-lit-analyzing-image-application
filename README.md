# Image Component Analyzer

This is a Streamlit application that allows users to upload an image and, upon clicking a button, displays a list of names of each component detected in the image. The application uses a pre-trained deep learning model to analyze the image and identify its components.

## Features

- Upload an image file (JPEG, PNG).
- Analyze the uploaded image to detect various components.
- Display a list of detected components.

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

Ensure you have the following installed:

- Python 3.7 or higher
- Pip (Python package installer)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/image-component-analyzer.git
    cd image-component-analyzer
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Install additional dependencies:**

    ```bash
    pip install timm
    ```

### Running the Application

Run the Streamlit application using the following command:

```bash
streamlit run app.py
