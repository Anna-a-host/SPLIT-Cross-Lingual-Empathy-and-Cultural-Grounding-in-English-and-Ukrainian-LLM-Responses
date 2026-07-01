# Research Log
The following file aims to highlight the progress made prior to this GitHub repository initialization following a consistent timeline to demonstrate the preliminary background research done, as well as consistently update the future study's current stage.


### March – April 2026
During these months, our major study's motivation was developed when working on a multilingually accessible Telegram companion Bot for Ukrainians experiencing a range of crisis situations. During the process, a range of various discrepancies was observed, thus raising a number of already existing, but highly unexplored questions regarding LLMs' ability to perform adequate NLP tasks across different languages, Ukrainian and English specifically. 

Another major observation stemmed directly from some models' partial inability to provide proper deep, culturally aware responses when trying to address a user's struggles. Seeming to be lacking deep emotional awareness, the deployed models occasionally produced robotic answers which experienced an apparent scarcity of natural and linguistic flow when answering in Ukrainian, whereas English versions of the answers were more naturally sound and idiomatically diverse.

Therefore, the objective of this study was formed. It lies directly at the intersection of several topics, such as the ability of LLMs to provide empathetic grounding being aware of the user's emotional state, produce linguistically and logically natural language generated responses, and maintain cultural awareness, thus reinforcing consistency in LLMs across mid-resource languages. 

### April – May 2026
Rigorous research has been accomplished, studying a range of related papers available on Google Scholar and consequently — arXiv. Studies have demonstrated that while an array of benchmarks have been introduced for evaluating LLMs' consistency when generating responses (regardless of the primary topic), the one which focuses specifically on evaluation of conversational discrepancies in a cultural awareness context has not been initialized yet. With this being said, we introduce a novel SPLIT benchmark, which stands for Stress, Panic, Loneliness, Internal displacement, and Tension. The fourth parameter especially showcases the current context of the current war, with thousands of Ukrainians living in the east being forced to move to the west, which puts a significant strain on people's lives. 

During this time, the overall idea of the study was fully shaped, with it being named as follows: 

**# SPLIT: Cross-Lingual Empathy and Cultural Grounding in English and Ukrainian LLMs**



### May – Early June 2026
Comprehensive research was the first and most essential part of the paper, to make sure all the peer research in this realm receives the required credit and citations for their meaningful contributions to the realm of LLMs' development and evaluation. Starting with the Transformer Architecture introduced in 2017 in the paper "Attention is all you need" which was a massive breakthrough, to the up-to-date, state-of-the-art studies for both holistic evaluations to even specific psychological papers. A range of research has been observed during this period, which is now already available in the references.bib file. Additionally, the Methodology has already been established, which is going to follow this structure:

1. 500 potential crisis-affected queries generation across 5 diverse categories, 100 queries each, standing for the SPLIT benchmark evaluation.
2. The answers to these queries are provided by three architecturally diverse models to ensure accuracy.
3. These answers are later evaluated by three other LLMs on three different parameters of a different structure to eliminate potential self-preference bias.
4. The mean outcome for each parameter of the answer is calculated to shed light on the overall picture.
5. To ensure reliability and credibility, these answers are additionally manually checked by a bilingual human evaluator, a native Ukrainian speaker with C2 English Proficiency.
6. To demonstrate the statistical alignment of human and AI jury scores, the Pearson Correlation Coefficient is adopted for further calculations.

The approach was thoroughly chosen after studying a range of peer papers and comprehending which one fits best our requirements.

### June 2026 – Current Process
Currently, the Introduction draft and Methodology section are being worked on, aiming to comprehensively describe the prior relevant data and our approach. Additionally, the Python code is at its development stage and is going to be pushed into this repository as soon as it is ready to demonstrate our progress.


### 10 - 18th of June

The Introduction and Methodology drafts have been fully established. We are going to provide access to the paper as soon as it is fully completed. 

Consequently, a dataset with 500 diverse potential user queries has been successfully generated and pushed to this GitHub repository to demonstrate our progress. The prompt for the LLM (GPT-4o) has been thoroughly written and can now be viewed by opening the SPLIT_500_BENCHMARK_PROMPT.txt file situated in the PROMPTS_TO_LLMs folder. Additionally, since this model has been proven to be an effective few-shot learner, several contextual examples in the preferred JSON format have been produced. These have been inserted into the main prompt in rotation accordingly, and they can also be accessed via the SPLIT folder.

The generated prompts are currently undergoing a manual check by a bilingual expert to ensure translation accuracy. Fifteen percent ($n = 75$) of all prompts will be adjusted if necessary.

### 19th of June

During the first stage of validation, some linguistic inconsistencies were observed in the generated queries. While they fully corresponded to the required SPLIT thematic coverage, they did not fully reflect real, human-like queries, which do not always possess highly polished or poetic phrasing.

Therefore, the prompt for the LLM was carefully adjusted, as well as the JSON format examples. Newly generated queries can now be accessed via the prompts.csv file. The prompts are still undergoing manual checks to ensure accuracy, consistency, and naturalness of the Ukrainian translations, following the rules mentioned above.


### 19-20th of June

The manual evaluation of the queries was completed; specifically, 15% of the queries generated by GPT-4o were assessed by a native Ukrainian representative. Consequently, 20% of the graded queries have been adjusted, demonstrating inaccuracies in machine translation.

Therefore, the next logical step was the evaluation of the answers by three judging models chosen to represent high technical diversity. The prompt for this assessment was manually written, providing the models with stringent rules regarding evaluation. 

The assessments were produced successfully, and the code ran without crashing. To see the big picture of these machine evaluations, the average across different categories, like Language and the model undergoing assessment, was evaluated, thus giving us the data, which can be accessed via these files:

    1. results\evaluations_by_LLMs/evaluation_claude.csv
    2. results\evaluations_by_LLMs/evaluation_gpt-4o.csv
    3. results\evaluations_by_LLMs/evaluation_mistral.csv

Please note that the averages are grouped by the judging models, rather than the evaluated ones. 
This structure is going to simplify the process of performance comparisons between the models.

Consequently, the main mean number on a (1-5) scale was calculated, showing us the final, approximate outcome of this study (specifically for LLMs). It can be accessed via this file:

    grand_average_src/grand_average.csv

The results leave a lot of space for future evaluations and, therefore, explanations. They are all going to be assessed in the paper, which is now in its active production process. 

The last stage of this specific process, before the final calculations using Pearson's Formula, is the manual evaluation of the answers. We decided to manually assess 10% of the answers, which showcases this structure: 

3000 (total answers of 3 models in 2 languages) * 0.1 = 300 (answers for manual evaluation)

Therefore, to ensure credibility, the languages and the models deployed were distributed equally among these 300. This leaves us with this math:

        1. 300 (answers for manual evaluation) / 2 (languages) = 150 (answers in one language)
        2. 150 / 3 (models) = 50 (answers of a specific model in a chosen language)

Therefore, a sample of 50 answers from each category was extracted randomly. The answers of the LLMs for human-in-the-loop assessment can be accessed via:

    human_in_the_loop_src\balanced_human_validation_subset.csv

During the next several days, the evaluation process will be finished; thus, the research process will be fully established. Our next step will be the calculation of the Pearson Correlation Coefficient ($r$) to understand the alignment between our automated AI Jury and a human.


***Note: the reason why the research is moving so quickly is our genuine desire to assess the empathy divergence in AI-generated responses. A number of papers were explored preliminarily, thus creating a strong foundation for fast research evolution. Moreover, some interesting data was gathered, only reinforcing our desire to continue dedicating 6-8 hours a day to the project.***



### 20-23rd of June

During these days, we actively worked on manually validating the 300 sample answers, equally split between 2 languages and 3 models. Once this part was completed, the next logical step was to extract identical rows from the following files:

    results/evaluations_by_LLMs/evaluation_claude.csv
    results/evaluations_by_LLMs/evaluation_gpt-4o.csv
    results/evaluations_by_LLMs/evaluation_mistral.csv

As these 300 rows were assessed by a human expert preliminarily (following the structure described above), the average AI score for every dimension for each of the answers was calculated to further find the Pearson Correlation Coefficient between human and LLMs' alignment. Average LLMs' assessments can be accessed via

300_average_evaluations_for_300_answers/AI_300_average_jury_scores.csv

Consequently, the Correlation Coefficient was successfully calculated and put into
SPLIT_Benchmark_Final_Metrics.csv file. To ensure accuracy and transparency of the current study, another formula was adopted to calculate Mean Absolute Error (MAE). Providing us with even more data, these results allow us to make more reasonable conclusions in the Results and Discussion sections.


***Overall, our findings serve as a justification of the ones preliminarily found in LLMs' abilities when adapting to specific cultures. They additionally indicate, that Empathetic accuracy and Linguistic Naturalness are vulnerable areas for a LLM-as-a-jury set-up. A comprehensive analysis is currently being held and will soon be published.***