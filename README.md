# Evolving research themes in animal science and veterinary journals using text mining and BERTopic

This repository contains the Python notebook and data-processing workflow supporting the manuscript **"Evolving research themes in animal science and veterinary journals using text mining and BERTopic,"** submitted to BMC Veterinary Research.

The study analyzes research trends in selected animal science and veterinary journals from 2010 to 2025 using bibliometric analysis, keyword analysis, co-occurrence network analysis, centrality analysis, and BERTopic-based semantic topic modeling.

## Repository description

Text mining and BERTopic-based analysis of evolving research themes in animal science and veterinary journals from 2010 to 2025.

## Suggested GitHub topics

`text-mining` `bibliometrics` `bertopic` `topic-modeling` `sentence-transformers` `veterinary-science` `animal-science` `co-occurrence-network` `research-trends`

## Data source

The bibliographic dataset was exported from Scopus and includes articles and reviews published from 2010 to 2025 in eight selected animal science and veterinary journals:

- *Animal*
- *Animal Nutrition*
- *International Journal of Veterinary Science and Medicine*
- *Journal of Animal Science and Biotechnology*
- *Journal of Animal Science and Technology*
- *Lab Animal*
- *Pakistan Veterinary Journal*
- *Veterinary Research*

The uploaded Scopus CSV file contains **12,937 records** and **24 columns**.

## Repository structure

```text
.
├── README.md
├── requirements.txt
├── Veterinary-Science_GitHub_ready.ipynb
├── data/
│   └── export_veterinary_science_scopus_2010_2025.csv.gz
├── results/
│   └── generated figures and tables
└── docs/
    └── manuscript or supplementary notes
```

## Main workflow

The analysis follows these steps:

1. Load and clean Scopus bibliographic records.
2. Standardize journal names, document types, citation counts, and textual fields.
3. Analyze annual publication output and citation trends.
4. Extract country information from affiliations and calculate country contribution and collaboration patterns.
5. Preprocess author and indexed keywords.
6. Construct keyword co-occurrence networks and calculate centrality measures.
7. Apply BERTopic to titles and abstracts using SentenceTransformer embeddings.
8. Evaluate reduced topic solutions using coherence, topic diversity, topic-size balance, and interpretability.
9. Visualize temporal changes in BERTopic-derived topics.

## Notebook

The main notebook is:

```text
Veterinary-Science_GitHub_ready.ipynb
```

The notebook has been cleaned for public release by removing cell outputs and replacing local file paths with relative project paths. Place the Scopus CSV file in the `data/` folder before running the notebook.

## Data file size note

The original CSV file is approximately **153.9 MiB**. A compressed version is approximately **53.4 MiB**. If uploading through the GitHub web interface, large files may fail. For public sharing, consider one of the following options:

- use Git Large File Storage (Git LFS),
- upload the dataset as a GitHub release asset,
- deposit the dataset in Zenodo, OSF, Figshare, or another repository,
- provide only the processed/derived dataset if Scopus licensing limits redistribution.

## Reproducibility

The detailed Python implementation is provided in the notebook. Package dependencies are listed in `requirements.txt`.

To install the main dependencies:

```bash
pip install -r requirements.txt
```

To run the notebook:

```bash
jupyter notebook Veterinary-Science_GitHub_ready.ipynb
```

## Data availability and licensing note

The dataset was exported from Scopus. Before public redistribution, users should check Scopus/Elsevier data-use terms and institutional license conditions. If redistribution of the full raw export is restricted, share the analysis code, a processed/derived dataset, or a metadata-limited version instead.

## Citation

If you use this repository, please cite the associated manuscript:

> Lee YJ, Kwak MJ, et al. Evolving research themes in animal science and veterinary journals using text mining and BERTopic.

## Contact

Corresponding author: Min-Jin Kwak  
Email: ics1051@kookmin.ac.kr
