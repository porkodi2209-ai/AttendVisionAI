import streamlit as st
import torch
import matplotlib.pyplot as plt
from transformers import BertTokenizer, BertModel

st.set_page_config(
    page_title="AttendVision AI",
    layout="wide"
)

st.title("AttendVision AI")
st.write("Visualize how a Transformer model focuses on different words.")


@st.cache_resource
def load_model():

    tokenizer = BertTokenizer.from_pretrained(
        "prajjwal1/bert-tiny"
    )

    model = BertModel.from_pretrained(
        "prajjwal1/bert-tiny",
        output_attentions=True
    )

    model.eval()

    return tokenizer, model


tokenizer, model = load_model()


text = st.text_area(
    "Enter your sentence",
    placeholder="Example: The cat is sitting on the mat."
)


if st.button("Visualize Attention"):

    if text.strip():

        inputs = tokenizer(
            text,
            return_tensors="pt"
        )

        with torch.no_grad():
            outputs = model(**inputs)

        tokens = tokenizer.convert_ids_to_tokens(
            inputs["input_ids"][0]
        )

        attention = outputs.attentions[-1][0, 0].detach().numpy()

        st.success("Attention generated successfully!")

        st.subheader("Attention Visualization")

        fig, ax = plt.subplots(figsize=(10, 7))

        ax.imshow(attention)

        ax.set_xticks(range(len(tokens)))
        ax.set_yticks(range(len(tokens)))

        ax.set_xticklabels(tokens, rotation=90)
        ax.set_yticklabels(tokens)

        ax.set_xlabel("Key Tokens")
        ax.set_ylabel("Query Tokens")

        ax.set_title("Transformer Attention")

        plt.tight_layout()

        st.pyplot(fig)

    else:
        st.warning("Please enter a sentence.")