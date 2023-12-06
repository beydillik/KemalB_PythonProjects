import streamlit as st
import nbformat
from nbconvert import HTMLExporter
from IPython.display import display, HTML

def main():
    # Path to your .ipynb file
    notebook_path = r"D:\SE_Projects\MachineLearning\Mubea_EnergyConsump\pages\energy_consumption_model1_RandForest.ipynb"

    # Read the .ipynb file
    with open(notebook_path, "r", encoding="utf-8") as file:
        notebook_content = file.read()

    # Convert .ipynb to HTML
    notebook = nbformat.reads(notebook_content, as_version=4)
    html_exporter = HTMLExporter()
    html_exporter.exclude_output_prompt = True
    (body, resources) = html_exporter.from_notebook_node(notebook)
    html_content = body.replace('\n', '')

    # Display the .ipynb as HTML
    st.components.v1.html(html_content, width=800, height=800, scrolling=True)

if __name__ == "__main__":
    st.set_page_config(page_title="Notebook Viewer2")
    #st.image("images/mubea2.jpg")
    main()
