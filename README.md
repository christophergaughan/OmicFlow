# OmicFlow

**OmicFlow** is a domain-specific assistant designed to help biologists, researchers, and data scientists parse, transform, and analyze TCGA and other omics-related datasets – without requiring advanced coding skills.

Unlike general-purpose AI models, OmicFlow integrates domain knowledge, understands file structures, and automates bioinformatics data preparation tasks with rigor and reproducibility in mind.

## Why Use OmicFlow Instead of General ChatGPT?

OmicFlow provides:

- Accurate TCGA clinical and expression data parsing
- Reliable JSON flattening and schema-aware merging
- Automatic column mapping and metadata standardization
- Pre-processed outputs formatted for ML workflows (for example, XGBoost, SageMaker)

General-purpose models often hallucinate columns, misinterpret file structures, or require extensive back-and-forth to correct errors. OmicFlow avoids these pitfalls by using tested logic and reproducible workflows.

## Quantitative Comparison

OmicFlow's capabilities have been benchmarked and summarized in the included graphs:

- Parsing accuracy across different file types
- Workflow time savings compared to manual and generic AI workflows
- Robustness and output quality versus input complexity

See `/graphs/methodology.md` for detailed descriptions and test case documentation.

## Example Prompts Where OmicFlow Excels

| Example Prompt                                    | General ChatGPT         | OmicFlow                | Why OmicFlow Wins                       |
|--------------------------------------------------|-------------------------|------------------------|----------------------------------------|
| Flatten TCGA JSON into CSV                       | Often incorrect         | Accurate               | Schema-aware parsing                   |
| Convert clinical data to `.parquet`             | Needs guidance          | Automated              | Built-in column type optimization      |
| Standardize missing exposure data               | Requires manual setup   | Domain defaults applied | Uses bioinformatics best practices     |
| Prepare file for XGBoost training               | Incomplete              | Ready-to-use           | Integrated ML pipeline logic           |
| Merge expression and clinical by barcode        | Fails or misaligns      | Correct               | Uses TCGA-specific merge keys          |
| Detect outliers in expression matrix            | Weak or missing logic   | Reliable              | IQR and PCA-based checks              |
| Generate heatmap for top 20 expressed genes     | May misplot             | Clean visualizations  | Validated plotting and feature logic  |

## Outputs and File Support

- CSV and Parquet exports
- Ready for downstream ML training
- Clear logs and file processing summaries

## Build Log and Timeline

A detailed build timeline, elapsed time per segment, lessons learned, and version tagging are provided in `/project_logs/omicflow_build_log.md`. A Gantt-style project graphic is also included.

## Hosting Options

OmicFlow can be used as a GPT in the ChatGPT store or deployed as a standalone web app via Streamlit. Full instructions and starter code are provided.

## Statement of Authorship and Intended Use

OmicFlow was conceptualized, designed, and authored by Christopher Gaughan, Ph.D., in 2025. All design decisions, graphs, benchmarks, and workflow logic were independently created and documented in the build log and accompanying timeline graphics.

This tool is shared publicly to support the bioinformatics community, especially for researchers and students who lack access to advanced data preparation resources. It is intended for academic and research use and may be adapted with proper attribution. Commercial use or significant derivative works should explicitly credit the original author and source repository.

## About

OmicFlow was developed using OpenAI's GPT architecture, enhanced with domain-specific workflows for bioinformatics and clinical data. All results are evidence-based and supported by reproducible tests.

Christopher Gaughan, Ph. D., produced all Notebooks produced herein. These notebooks are meant to guide you on deploying OmicFlow and are used as pedagogical resources. If they can help you, please feel free to build upon them.

Further, we employ some "sanity checks" on well-established, publicly available data sets. See the notebooks and data folder to check them out yourself to benchmark your data.

Version: v1.0.0 – July 6, 2025

## License

This project is licensed under the MIT License. You are welcome to use, modify, and distribute this software for academic and research purposes, given proper attribution to the original author. Explicit credit and adherence to the MIT License terms are required for commercial use or significant derivative works.

See the full license text in the `LICENSE` file.

