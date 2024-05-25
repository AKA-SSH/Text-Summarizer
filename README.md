# Text Summarizer

## Description
This is a dummy project based on a professional project I have worked on for Dekin's University, Australia. The project focuses on text summarization, providing abstract summaries for research papers and reports. Additionally, it includes tasks such as question generation and a QnA bot.

## Project Workflow
1. PDF -> raw text
2. Cleaned text
3. Embedding
4. Semantic chunking
5. Chunk summarization
6. Combined summarization

### Add-ons
In this version of the project, semantic chunking has replaced the original general recursive character splitting method.

## How to Run
1. Have a PDF file.
2. Set the path of the file.
3. Navigate to the root directory.
4. Set PYTHONPATH to the current directory: `set PYTHONPATH=%cd%`
5. Run `python src\main.py`

## Research Paper First Page
Cannot share the full paper due to legal reasons.
![Research Paper](https://i.imgur.com/2teAXFS.png)

## Text Summarization For Above Sampled Research Paper
The text delves into the vulnerability of machine learning (ML) models in adversarial settings and the countermeasures developed by researchers in the academic and industrial community. It recognizes the remarkable performance of ML methods in areas such as autopilot systems, facial recognition, and spam detection. With the progress in deep learning methods and hardware accessibility for training intricate models, ML has surpassed human capabilities in numerous tasks.

The interdisciplinary nature of ML is acknowledged, incorporating computer science, statistics, probability, and brain-like technologies. A security framework introduced in 2014 is highlighted, along with concerns surrounding deep learning techniques, especially deep neural networks (DNNs) excelling in multi-mode recognition tasks.

Various attack and defense methods are discussed, including universal adversarial perturbations, differential privacy, and input transformations. The usage of generative adversarial networks (GANs) for defense against adversarial perturbations is also touched upon.

The importance of acknowledging and protecting against adversarial attacks in ML models for security and robustness is stressed. The deployment of ML models in parallel distributed computing environments is explored, referencing the works of numerous authors. Discussions on feature squeezing, foveation-based methods, and GANs in the deployment of ML models are presented and validated with references to specific studies.

The text offers an extensive overview of the advancement of ML models in parallel distributed computing environments, emphasizing the significance of evaluating diverse methods for optimal performance and security. It underlines the vulnerability of ML models in adversarial settings due to carefully crafted adversarial examples that compromise their effectiveness. Various security properties in ML algorithms in adversarial settings are analyzed, emphasizing the need for interdisciplinary research to ensure secure ML models.

Future work in ML security is outlined, suggesting the development of robust defense strategies for deep learning models, addressing data privacy concerns, and establishing evaluation mechanisms to assess model security effectively. It also stresses the importance of consistently evaluating and 
enhancing ML model security to combat evolving threats.

The discussion shifts to specific techniques and studies related to ML methods and DNNs for data classification, referencing the l-bfgs method for DNN classification and datasets like mnist, ImageNet, and cifar-10. Notably, the text explores the DeepCloak technique for DNN dimensionality reduction, defense strategies using GANs, and feature squeezing methods. Additionally, the PATE algorithm is overviewed with references to relevant studies in the field of ML and DNNs, offering a technical insight into recent research and techniques in data classification.

## License
This project is licensed under the MIT License.
