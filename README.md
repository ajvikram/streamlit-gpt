# Streamlit-GPT : Run Free Open Chat GPT 4(GPT4All-J) with Streamlit

We have many open chat GPT models available now, but only few, we can use for commercial purpose. 
We can run one of that chat GPT model known as GPT4ALL specially GPT4ALL-J which is good for commercial use.

We need to install few packages -

It is a good practice to use python virtual environment.

Create project directory and create sub directory as model.

Download model file from — https://gpt4all.io/models/ggml-gpt4all-j.bin

And put into model directory.

Once it s done, install python packages

`pip install -r requirement.txt`

then run -

`./run.sh`

or

`streamlit run main.py --server.port=8080 --server.address=0.0.0.0`


![Alt text](./image/streamlit-gpt.gif?raw=true "Streamlit GPT")

