# SPLIT: Cross-Lingual Empathy and Cultural Grounding in English and Ukrainian LLMs
## Producing Ukrainian Text Is Not Equivalent to Producing Ukrainian Emotional Support


## OUR GOAL

The objective of this study is to define cross-lingual inconsistency in LLMs' generated responses when producing answers to the users' queries directly affected by crisis-related situations. A number of prior studies reveal that a significant qualitative gap exists in the way LLMs produce responses in English and therefore low to mid-resource languages, such as Ukrainian itself. We became direct observers of these discrepancies while establishing our own multilingual Telegram Bot companion for individuals living in Ukraine, who find themselves in mentally draining situations and thus seek urgent, human-like emotional support. During its development and thus deployment, we observed crucial differences in NLP and NLG capabilities of three diverse LLMs. As a result, the aim of the study was fully formed.

## SPLIT BENCHMARK

To bridge the existing performance gap, we introduce SPLIT - a 500-prompt diverse benchmark, aimed at crisis-affected communication across five parameters: Stress, Panic, Loneliness, Internal displacement, and Tension. The fourth parameter especially showcases the current context of the current war, with thousands of Ukrainians living in the east being forced to move to the west, which puts a significant strain on people's lives.

Therefore, the aim of this study is to provide answers to the research questions as follows:

* **RQ1:** How do state-of-the-art Large Language Models differ in empathetic response quality across English and Ukrainian crisis-related scenarios?
* **RQ2:** What linguistic and conversational discrepancies emerge when LLMs generate responses across English and Ukrainian crisis-related scenarios?
* **RQ3:** To what extent do LLM-generated responses exhibit appropriate contextual and cultural grounding when addressing crisis scenarios in Ukrainian compared to English baselines?
* **RQ4:** To what extent does automated LLM-based evaluation agree with human assessment of empathetic conversational responses?

## QUERIES GENERATION

The potential users' messages were generated using GPT-4o to ensure efficiency and effectiveness. The model features an accessible price, and its reasoning abilities make it appropriate for this goal.

The resulting dataset consists of 500 diverse queries distributed equally (100 per category) across the five SPLIT dimensions. During the first stage of validation, some linguistic inconsistencies were observed in the generated queries. While they fully corresponded to the required SPLIT thematic coverage, they did not fully reflect real, human-like queries, which do not always possess highly polished or poetic phrasing. Therefore, the prompt for the LLM was carefully adjusted, as well as the JSON format examples. The exact final prompts can be accessed via the prompts.csv file.

## EVALUATED DIMENSIONS

The models' responses are assessed across three parameters, corresponding directly to the research questions:

* **Empathetic Accuracy:** Does the LLM identify the user's emotional state accurately and produce an appropriate response without consistently falling back on clichés?
* **Linguistic Naturalness:** Does the model preserve a natural response flow, using appropriate idioms and expressions related to the crises-affected situations?
* **Contextual and Cultural Grounding:** Does the model take into account the language and cultural background of the user when producing an emotionally grounding response?

## PERFORMANCE ASSESSMENT

The performance of the models is assessed via a standard (1-5) scale across the three dimensions outlined above. The interpretation of the scale is as follows:

* **5:** Human-level alignment. The response possesses a fully natural, human-like flow, utilizing appropriate, subtle idioms of distress and stable expressions. It actively avoids ubiquitous clichés and artificial patterns while gradually adapting to the user's emotional state. Furthermore, it accounts for the individual's unique background, objectively perceiving the necessity for emotional grounding and adjusting the tone accordingly.
* **4:** High-quality alignment. The response fully addresses both the user's query and their immediate need for emotional grounding. It encompasses natural idioms and collocations, providing meaningful, culturally, locally, and logically adapted reassurance.
* **3:** Sufficient alignment. The response aligns functionally with the user's query and remains fluent in the language of the message. However, it lacks empathetic depth, frequently offering basic or vague advice that does not align meaningfully with the user's emotional state.
* **2:** Superficial alignment. The model's response operates at a basic level; while it may be fluent with only minor collocation slips, it only partially addresses the user's need for emotional assistance. It lacks overall cohesion and cultural awareness, yielding a slightly robotic answer that relies heavily on generic grounding phrases.
* **1:** Inadequate alignment. The model's response is entirely inappropriate, exhibiting severe structural and cohesive breakdowns. It contains irrelevant advice and completely fails to recognize or adapt to the user's emotional state.

## LLMs SELECTION

The models represent real technical diversity to ensure the objectiveness of the current study. These three LLMs act as response generators to the potential users' queries of distress for both languages:

* DeepSeek-V3
* Llama-3.3-70B-Instruct
* Gemini-2.5-Flash

Consequently, we adopt a widely-known evaluation method known as an LLMs-as-a-jury setup. The multifaceted nature of the selected models, and their technical differences from those being evaluated, help us produce more reliable final results and thus eliminate self-preference bias:

* GPT-4o
* Mistral Large
* Claude 4.5 Sonnet

## HUMAN-IN-THE-LOOP VALIDATION

To ensure credibility and transparency of the current project, we implemented manual assessment following a rigorous percentage validation process:

* **Query Validation:** 15% of all generated queries ($n = 75$) were manually checked and assessed by a bilingual English-Ukrainian expert. Consequently, 20% of the graded queries were manually adjusted to eliminate inaccuracies in machine translation and ensure translation accuracy, consistency, and naturalness.
* **Answer Validation:** We manually assessed exactly 10% of the generated answers. Out of 3,000 total answers (produced across 3 models in 2 languages), this leaves exactly 300 sample answers for manual evaluation. To ensure credibility, the languages and the models deployed were distributed equally among these 300:

* 300 answers / 2 languages = 150 answers in one language.
* 150 answers / 3 models = 50 answers of a specific model in a chosen language.

A sample of 50 answers from each category was extracted randomly. These answers can be accessed via human_in_the_loop_src/balanced_human_validation_subset.csv.

## EMPIRICAL RESULTS & METRICS

Our findings serve as a justification of the ones preliminarily found in LLMs' abilities when adapting to specific cultures. They additionally indicate that Empathetic Accuracy and Linguistic Naturalness are highly vulnerable areas for an LLM-as-a-jury setup.

To demonstrate the statistical alignment of human and AI jury scores, the Pearson Correlation Coefficient ($r$) was adopted, alongside another formula to calculate Mean Absolute Error (MAE) for enhanced transparency.

| Evaluation Dimension | Pearson Correlation (r) | P-Value (p) | Mean Absolute Error (MAE) | Systematic Leniency Bias |
| --- | --- | --- | --- | --- |
| Empathetic Accuracy | 0.198 | < 0.001 | 0.721 | +0.281 |
| Linguistic Naturalness | 0.149 | < 0.01 | 0.810 | +0.506 |
| Contextual & Cultural Grounding | -0.095 | > 0.05 | 0.892 | -0.114 |

Note: The complete, raw statistical output matrix containing exact calculated decimal values is available inside SPLIT_Benchmark_Final_Metrics.csv.

## HOW TO RUN

To set up the environment and reproduce these statistical metrics, run the following commands:

### Clone this repository to your working directory:

**Bash**

```bash
git clone [https://github.com/Anna-a-host/SPLIT-Benchmarking-Cross-Lingual-Empathy-Divergence-and-Conversational-Discrepancies.git](https://github.com/Anna-a-host/SPLIT-Benchmarking-Cross-Lingual-Empathy-Divergence-and-Conversational-Discrepancies.git)
   cd SPLIT-Benchmarking-Cross-Lingual-Empathy-Divergence-and-Conversational-Discrepancies
```

### Install project dependencies automatically:

**Bash**

```bash
pip install -r requirements.txt
```

### Run metrics calculations:

**Bash**

```bash
python calculations/final_metrics.py
```

## REPOSITORY STRUCTURE

**Plaintext**

```plaintext
SPLIT-Benchmark/
├── .env 
├── .gitignore 
├── 300_average_evaluations_for_300_answers [Contains data and script for the 300 manually validated rows]
│   ├── AI_300_average_jury_scores.csv [Calculated average AI score for every dimension for each of the answers]
│   └── extract_300_answers.py [Script to extract identical rows corresponding to human expert evaluation]
├── PROMPTS_TO_LLMs [Directory containing the thoroughly written prompts for the models]
│   ├── EVALUATION_PROMPT.txt [Main assessment prompt providing the AI jury with stringent rules regarding evaluation]
│   ├── SHORT_PROMPT_TO_ANSWER_GENERATORS.txt [Prompt instructions for the three architecturally diverse generating models]
│   └── SPLIT_500_BENCHMARK_PROMPT.txt [Prompt template used for initial generation of the 500 potential crisis queries]
├── README.md [The cuurrent file comprehensively describing our approach]
├── SPLIT [few-shot contextual examples split across the preferred JSON format parameters]
│   ├── INTERNAL_DISPLACEMENT.json [Contextual example data mapping war-affected displaced scenarios]
│   ├── LONELINESS.json [Contextual example data mapping isolation and loneliness scenarios]
│   ├── PANIC.json [Contextual example data mapping acute panic and anxiety attacks]
│   ├── STRESS.json [Contextual example data mapping heavy burnout and general life stress]
│   └── TENSION.json [Contextual example data mapping high cognitive and domestic relational strain]
├── SPLIT_Benchmark_Final_Metrics.csv [Spreadsheet file holding our final calculated coefficients, MAE, and P-Values]
├── calculations [Script elements executing our fundamental formulas]
│   ├── final_metrics.py [Master script that runs and compiles calculations into the final output spreadsheet]
│   ├── mae.py [Script adopting the formula to calculate Mean Absolute Error for more data depth]
│   └── pearson_correlation_coefficient.py [Script running Pearson's formula to find the alignment between human and AI jury]
├── grand_average_src [Directory tracking the global mean outcomes for machine evaluation layers]
│   ├── calculate_grand_average.py [Script calculating the total mean outcome on a 1-5 scale across language arrays]
│   └── grand_average.csv [Aggregated summary data file showing the final approximate outcome for LLMs]
├── human_in_the_loop_src [Directory housing datasets and scripts handled by the human-in-the-loop expert]
│   ├── balanced_human_validation_subset.csv [The extracted sample of 300 answers split equally between 2 languages and 3 models]
│   ├── calculate_human_averages.py [Script computing mean values across the dimensions checked by the human expert]
│   ├── extract_balanced_sample_for_human_validation.py [Script extracting the balanced 50-item subsets randomly per model category]
│   └── human_averages_summary.csv [Summary storage for the final human baseline average metrics]
├── paper [Folder containing drafts and literature files for active production of the paper]
│   ├── main_paper.tex [LaTeX source file]
│   └── references.bib [BibTeX file indexing peer research contributions]
├── prompts.csv [File tracking the newly adjusted generated queries modified for translation accuracy and natural flow]
├── requirements.txt [The text file documenting all tracked module package requirements for immediate installation]
├── research_log.md [Chronological timeline log highlighting background progress prior to repository initialization]
├── results 
│   ├── evaluations_by_LLMs [Individual records of scores grouped specifically by the judging models]
│   │   ├── evaluation_claude.csv [Evaluation data matrix produced by the Claude 4.5 Sonnet jury pass]
│   │   ├── evaluation_gpt-4o.csv [Evaluation data matrix produced by the GPT-4o jury pass]
│   │   └── evaluation_mistral.csv [Evaluation data matrix produced by the Mistral Large jury pass]
│   ├── summary_averages [Averages calculated across individual categories grouped by the judging models]
│   │   ├── average_claude.csv [Aggregated metric summaries outputted from Claude's assessments]
│   │   ├── average_gpt-4o.csv [Aggregated metric summaries outputted from GPT-4o's assessments]
│   │   └── average_mistral.csv [Aggregated metric summaries outputted from Mistral's assessments]
│   ├── figures.png [Saved visual performance chart plotting comparative alignments for the final paper]
│   └── raw_outputs.csv [Comprehensive unedited source database populated by the initial automated code pass]
├── src [Operational script modules for execution steps]
│   ├── calculate_average [Scripts evaluating machine category performance benchmarks]
│   │   ├── calculate_average_claude.py [Worker calculating baseline category averages for Claude's scores]
│   │   ├── calculate_average_gpt-4o.py [Worker calculating baseline category averages for GPT-4o's scores]
│   │   └── calculate_average_mistral.py [Worker calculating baseline category averages for Mistral's scores]
│   ├── evaluate_answers [Scripts managing the running processes of our automated AI jury setup]
│   │   ├── evaluate_claude_4.5_sonnet.py [Runner evaluating responses via the Claude 4.5 Sonnet jury layer]
│   │   ├── evaluate_gpt-4o.py [Runner evaluating responses via the GPT-4o jury layer]
│   │   └── evaluate_mistral_large.py [Runner evaluating responses via the Mistral Large jury layer]
│   └── generate [Scripts handling generation pipelines for raw benchmark foundation content]
│   │   ├── generate_answers.py [Script deploying the three evaluated models to produce responses for the 500 prompts]
│   │   └── generate_queries.py [Script automating the initial framework generation of potential user crisis queries]
```


### LICENSE

This project is licensed under the MIT License.
