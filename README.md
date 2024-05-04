Project Organization
------------

    ├── LICENSE
    ├── README.md             <- The top-level README for people using this project.
    ├── data
    │   ├── 04_model_outputs  <- Tables and one-off datasets resulting from modeling. 
    │   ├── 03_analytic       <- The final data sets used for modeling.
    │   ├── 02_intermediate   <- Intermediate data that has been transformed.
    │   └── 01_raw            <- The original, immutable data dump.
    │
    ├── models                <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks_and_scripts <- Jupyter notebooks and pythong scripts. 
    │                            Naming convention is a number (for ordering), the creator's initials, 
    │                            and a short `-` delimited description, e.g. `1.0-jqp-initial-data-exploration`.
    │    
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    └── src                <- Source code for use in this project.
       ├── __init__.py    <- Makes src a Python module
       │
       ├── data           <- Scripts to download or generate data
       │   └── make_dataset.py
       │
       ├── features       <- Scripts to turn raw data into features for modeling
       │   └── build_features.py
       │
       ├── models         <- Scripts to train models and then use trained models to make
       │   │                 predictions
       │   ├── predict_model.py
       │   └── train_model.py
       │
       └── visualization  <- Scripts to create exploratory and results oriented visualizations
           └── visualize.py
