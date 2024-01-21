- [Repository](#repository)
- [Requirements](#requirements)
- [Directory structure](#directory-structure)
- [Installation](#installation)
  - [Before installing](#before-installing)
- [Install](#install)
  - [Analysis Topics:](#analysis-topics)


## Repository
This publicly available [GitHub repository](https://github.com/nguyenhy/US-accidents) provides detailed insights, visualizations, and code related to the study of accidents in the United States.

## Requirements
For more information check out [requirements.txt](./requirements.txt)

**Note**: The code has been developed and tested with Python 3.12.1.
While it is expected to work with any version of Python 3, the author has specifically used and verified it with Python 3.12.1.

```
python: 3 (3.12.1)
pandas: 2.1.4
holidays: 0.40
seaborn: 0.13.1
plotly: 5.18.0
ipykernel: 6.28.0
nbformat: 5.9.2
```

## Directory structure
```
.
└── root/
    ├── config/             # shareable configuration
    │   ├── ...
    │   └── const.py
    ├── data/
    │   ├── processed/      # save file after processing by `preprocess.ipynb`
    │   └── raw/            # save raw csv file
    ├── dist/               # hidden directory to save bundled files
    ├── explore/            # for data exploration purposes
    │   └── notebook.ipynb
    ├── images/
    ├── scripts/
    │   ├── ...
    │   └── pack.sh         # bundle repo into `./dist dir`
    ├── utils/
    │   ├── ...
    │   └── convert.py      # shareable, simple function
    ├── ...
    ├── main.ipynb          # main file that processes data
    ├── preprocess.ipynb    
    ├── README.md           # here we are
    └── setup.py
```
- `config`: main



## Installation
### Before installing
- Due to the nature of file size, we would not commit the raw data file here.
Instead, we can be downloaded as a document [available here](./data/README.md#source).
- Download, extract the file, and place it in the `<root>/data/raw` directory with the name:
  - `full.csv` for full version of dataset
  - `sample.csv` for sample 500K-rows version of dataset
- Open and run file `preprocess.ipynb`, to split the data into multiple individual files based on the year of the accidents.
## Install
make sure that you installs all the necessary libraries that are mentioned in the [Requirements](#requirements)

### Analysis Topics:

1. **Accident Trends by DateTime:**
   Explore patterns and trends in accidents based on the date and time.

2. **Association Between Accident Trends and Holidays:**
   Investigate the correlation between accident trends by datetime and holidays.

3. **Accident Trends by Year, Month, Hour vs State:**
   Analyze how accident rates vary across different states based on factors such as year, month, and hour.

4. **Accident DateTime and Daylight:**
   Examine the relationship between accident occurrences and daylight conditions at the time of the incident.

