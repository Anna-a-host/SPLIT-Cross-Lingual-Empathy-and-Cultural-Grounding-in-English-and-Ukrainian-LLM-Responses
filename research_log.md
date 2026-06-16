# Research Log

The following file aims to highlight the progress made prior to this GitHub repository initialization following a consistent timeline to demonstrate the preliminary background research done, as well as consistently update the future study's current stage.


### March – April 2026
During these months, our major study's motivation was developed when working on a multilingually accessible Telegram companion Bot for Ukrainians experiencing a range of crisis situations. During the process, a range of various discrepancies was observed, thus raising a number of already existing, but highly unexplored questions regarding LLMs' ability to perform adequate NLP tasks across different languages, Ukrainian and English specifically. 

Another major observation stemmed directly from some models' partial inability to provide proper deep, culturally aware responses when trying to address a user's struggles. Seeming to be lacking deep emotional awareness, the deployed models occasionally produced robotic answers which experienced an apparent scarcity of natural and linguistic flow when answering in Ukrainian, whereas English versions of the answers were more naturally sound and idiomatically diverse.

Therefore, the objective of this study was formed. It lies directly at the intersection of several topics, such as the ability of LLMs to provide empathetic grounding being aware of the user's emotional state, produce linguistically and logically natural language generated responses, and maintain cultural awareness, thus reinforcing consistency in LLMs across mid-resource languages. 

### April – May 2026
Rigorous research has been accomplished, studying a range of related papers available on Google Scholar and consequently — arXiv. Studies have demonstrated that while an array of benchmarks have been introduced for evaluating LLMs' consistency when generating responses (regardless of the primary topic), the one which focuses specifically on evaluation of conversational discrepancies in a cultural awareness context has not been initialized yet. With this being said, we introduce a novel SPLIT benchmark, which stands for Stress, Panic, Loneliness, Internal displacement, and Tension. The fourth parameter especially showcases the current context of the current war, with thousands of Ukrainians living in the east being forced to move to the west, which puts a significant strain on people's lives. 

During this time, the overall idea of the study was fully shaped, with it being named as follows: 

**SPLIT: Benchmarking Cross-Lingual Empathy Divergence and Conversational Discrepancies in English and Ukrainian LLM Responses**



### May – Early June 2026
Comprehensive research was the first and most essential part of the paper, to make sure all the peer research in this realm receives the required credit and citations for their meaningful contributions to the realm of LLMs' development and evaluation. Starting with the Transformer Architecture introduced in 2017 in the paper "Attention is all you need" which was a massive breakthrough, to the up-to-date, state-of-the-art studies for both holistic evaluations to even specific psychological papers. A range of research has been observed during this period, which is now already available in the references.bib file. Additionally, the Methodology has already been established, which is going to follow this structure:

1. 500 potential crisis-affected queries generation across 5 diverse categories, 100 queries each, standing for the SPLIT benchmark evaluation.
2. The answers to these queries are provided by three architecturally diverse models to ensure accuracy.
3. These answers are later evaluated by three other LLMs on three different parameters of a different structure to eliminate potential self-preference bias.
4. The mean outcome for each parameter of the answer is calculated to shed light on the overall picture.
5. To ensure reliability and credibility, these answers are additionally manually checked by a bilingual human evaluator, a native Ukrainian speaker with C2 English Proficiency.
6. To demonstrate the statistical alignment of human and AI jury scores, the Cohen’s Kappa formula is adopted for further calculations.

The approach was thoroughly chosen after studying a range of peer papers and comprehending which one fits best our requirements.

### June 2026 – Current Process
Currently, the Introduction draft and Methodology section are being worked on, aiming to comprehensively describe the prior relevant data and our approach. Additionally, the Python code is at its development stage and is going to be pushed into this repository as soon as it is ready to demonstrate our progress.