# Speech to text conversion with sentence correction
Install all the dependencies in conda environment
to navigate to the project directory as follows
```bash
cd nlp_project/speech-to-text
```
after successfully navigating to the main directory run the following command
```bash
conda activate aind-vui
```
this will now activate the conda environment
you can notice the change in the prompt <br/>
Run the following command after the environment is activated
```bash
jupyter notebook
```
To test the deepspeech model
Navigate to the following directory from user directory
```bash
cd acc_ind
```
```bash
deepspeech --model output_graph.pbmm --lm lm.binary --trie trie --audio sample-5.wav
```
