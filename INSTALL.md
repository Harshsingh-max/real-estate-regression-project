# Installation Guide

## Quick Start (5 minutes)

### 1. Clone Repository
```bash
git clone https://github.com/Harshsingh-max/real-estate-regression-project.git
cd real-estate-regression-project
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run Jupyter Notebook
```bash
jupyter notebook real_estate_regression_project.ipynb
```

## System Requirements
- Python 3.7 or higher
- pip (Python package manager)
- 2GB RAM minimum
- 100MB disk space

## Troubleshooting

**Problem**: `ModuleNotFoundError: No module named 'jupyter'`
**Solution**: `pip install jupyter`

**Problem**: `ModuleNotFoundError: No module named 'numpy'`
**Solution**: `pip install -r requirements.txt`

**Problem**: Port 8888 already in use
**Solution**: `jupyter notebook --port 8889`

## Verify Installation
```bash
python -c "import numpy, pandas, matplotlib; print('All packages installed!')"
```

You should see: `All packages installed!`
