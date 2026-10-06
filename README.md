# AttendVision AI

## Overview

AttendVision AI is an interactive application that visualizes how a Transformer model focuses on different words in a sentence using attention mechanisms.

The application uses a lightweight BERT model to generate attention scores and represents them as a heatmap for easy understanding.

## Features

* Enter a custom sentence
* Generate Transformer attention scores
* Visualize attention using a heatmap
* Uses a lightweight BERT model
* Interactive Streamlit interface
* Displays query and key tokens

## Technologies Used

* Python
* Streamlit
* Hugging Face Transformers
* PyTorch
* Matplotlib
* BERT

## Model Used

The application uses:

```text
prajjwal1/bert-tiny
```

This lightweight BERT model is used to generate attention information efficiently.

## Project Structure

```text
AttendVision-AI/
│
├── attention.py
└── README.md
```

## How It Works

1. Enter a sentence in the application.
2. The sentence is tokenized using the BERT tokenizer.
3. The BERT model processes the tokens.
4. Attention scores are generated from the Transformer model.
5. The attention values are converted into a heatmap.
6. The heatmap shows how the model focuses on different tokens.

## Installation

Install the required libraries:

```bash
pip install streamlit
pip install transformers
pip install torch
pip install matplotlib
```

## Run the Application

```bash
py -m streamlit run .\attention.py
```

## Demo
## Screenshot

<img width="1920" height="1080" alt="Screenshot (139)" src="https://github.com/user-attachments/assets/822de212-0391-425e-acef-80e971ac9bbb" />

<img width="1920" height="1080" alt="Screenshot (140)" src="https://github.com/user-attachments/assets/12966b52-d478-4b88-a5ac-b86a92b5d3f8" />

<img width="1920" height="1080" alt="Screenshot (141)" src="https://github.com/user-attachments/assets/c6c3487a-6aec-457f-9aeb-d3f750bb1393" />


## Output

The application generates an attention heatmap where the tokens are displayed on the X-axis and Y-axis. The heatmap represents the attention relationships between the tokens.

## Applications

* Understanding Transformer attention
* NLP model visualization
* Educational demonstrations
* Exploring BERT-based models
* Learning how attention mechanisms work

## Conclusion

AttendVision AI demonstrates the working of Transformer attention mechanisms through an interactive visualization. By using a lightweight BERT model and attention heatmaps, the application provides a simple way to understand how different words in a sentence are related during Tra
