# Evolving Research Themes in Veterinary Science

This repository contains the data files and Python notebook used for the study:

**Evolving Research Themes in Veterinary Science: A Bibliometric and BERTopic-Based Analysis**

The project uses a Scopus-derived bibliographic dataset to analyze publication growth, citation trends, country-level contribution, international collaboration, keyword evolution, keyword co-occurrence networks, centrality measures, and BERTopic-derived semantic research themes in veterinary science literature from 2010 to 2025.

## Repository structure

```text
BERTopic_Veterinary-science/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── raw/
│   │   ├── export_veterinary_science_scopus_2010_2025.csv.gz
│   │   ├── raw_data_manifest.json
│   │   └── README.md
│   └── processed/
│       └── README.md
├── docs/
│   ├── DATA_CHECK_REPORT.md
│   └── scopus_query.txt
├── notebooks/
│   └── Veterinary-Science_GitHub_ready.ipynb
├── results/
│   ├── bertopic/
│   │   ├── final_document_topic_assignments.csv
│   │   └── final_topic_info_raw.csv
│   ├── figures/
│   │   └── figure1_workflow.png
│   └── tables/
│       ├── Supplementary_Table_S1_BERTopic_model_selection.csv
│       ├── table4_final_bertopic_topics.csv
│       └── supplementary_final_bertopic_topics_with_representative_titles.csv
└── scripts/
    ├── quick_check.py
    └── git_upload_commands.txt
```

## Data source

Records were retrieved from Scopus on **5 September 2026**. The analysis was restricted to selected veterinary science journals, English-language articles and reviews, and publication years 2010–2025.

The complete Scopus query is provided in [`docs/scopus_query.txt`](docs/scopus_query.txt).

## Dataset summary

| Stage | Number of records/documents |
|---|---:|
| Initial merged Scopus export | 89,559 records |
| After journal selection and eligibility checking | 48,791 records |
| Final bibliometric dataset after DOI- and title-based duplicate removal | 48,768 documents |
| Final BERTopic corpus after title and abstract sufficiency filtering | 48,344 documents |
| Valid topic-assigned documents in final BERTopic model | 37,467 documents |
| Topic -1 outliers | 10,877 documents |
| Final valid BERTopic topics | 46 topics |

## Main analysis workflow

1. Import and merge Scopus CSV exports.
2. Standardize journal-title variants.
3. Apply the final veterinary science journal allowlist.
4. Check publication-year, document-type, and language eligibility.
5. Remove duplicate records based on DOI and normalized title information.
6. Construct title-abstract text fields for BERTopic modeling.
7. Perform bibliometric analysis of annual publication output and citation counts.
8. Extract country information and calculate publication count, fractional contribution score, and international collaboration ratio.
9. Normalize author and indexed keywords.
10. Perform keyword frequency analysis, keyword co-occurrence network analysis, and centrality analysis.
11. Compare candidate BERTopic models and select the final model.
12. Interpret final topics and analyze temporal topic shares.

## BERTopic model summary

The final model was selected from six candidate BERTopic configurations. The selected model was **M3_more_conservative**, which used:

- SentenceTransformer model: `sentence-transformers/all-MiniLM-L6-v2`
- Embedding normalization: enabled
- UMAP: `n_neighbors = 15`, `n_components = 5`, `min_dist = 0.0`, metric = cosine, `random_state = 42`
- HDBSCAN: `min_cluster_size = 300`, `min_samples = 10`, metric = Euclidean, cluster selection method = excess of mass, `prediction_data = True`
- CountVectorizer: English stop words + additional corpus-level stop words, n-grams of 1–2 words, `min_df = 5`, `max_df = 0.95`
- BERTopic: `top_n_words = 10`, `calculate_probabilities = False`

The model comparison table is provided as [`results/tables/Supplementary_Table_S1_BERTopic_model_selection.csv`](results/tables/Supplementary_Table_S1_BERTopic_model_selection.csv).

## Reproducibility

Create a Python environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Run a quick data check:

```bash
python scripts/quick_check.py
```

Then open and run the notebook:

```bash
jupyter lab notebooks/Veterinary-Science_GitHub_ready.ipynb
```

The notebook is configured to use relative paths, with raw data in `data/raw/`, processed data in `data/processed/`, and outputs in `results/`.

## Notes on raw data

The file `data/raw/export_veterinary_science_scopus_2010_2025.csv.gz` is a gzipped merge of six Scopus CSV export files. It contains **89,559 records** and **25 original Scopus columns** before downstream cleaning.

Because Scopus metadata can include abstracts and other database-derived bibliographic fields, users should verify that their intended public sharing complies with institutional and database-use policies.

## Citation

If you use this repository, please cite the associated manuscript:

Lee YJ, Kim T, Yang Y, Park S, Park S, Woo S, Kwak M-J. Evolving Research Themes in Veterinary Science: A Bibliometric and BERTopic-Based Analysis. 2026.

## Contact

Corresponding author: Min-Jin Kwak, Kookmin University.
