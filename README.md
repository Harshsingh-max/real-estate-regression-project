# Real Estate Housing Price Prediction Project

## 📊 Project Overview

A comprehensive machine learning project implementing **regression models from scratch** (without sklearn) using only NumPy, Pandas, and Matplotlib. This project covers Parts 1-4 with complete implementations of:

- **Part 1**: Simple Linear Regression (25 points)
- **Part 2**: Multiple Linear Regression (35 points)
- **Part 3**: Polynomial Regression (25 points)
- **Part 4**: Comprehensive Analysis & Comparison (15 points)

## 🎯 Features

### Models Implemented
1. **SimpleLinearRegression** - Gradient descent with learning rate scheduling
2. **MultipleLinearRegression** - Normal equation + Gradient descent with Ridge/Lasso regularization
3. **PolynomialRegression** - Polynomial features with Ridge regularization
4. **Ensemble Model** - Combined predictions from multiple models

### Key Techniques
- ✅ Data preprocessing (missing value imputation & outlier removal)
- ✅ Feature scaling & normalization
- ✅ K-Fold Cross Validation
- ✅ Feature engineering (interaction terms)
- ✅ Feature selection (Forward Selection & Backward Elimination)
- ✅ Multicollinearity analysis (VIF)
- ✅ Ridge & Lasso regularization
- ✅ Model comparison & evaluation
- ✅ Bootstrap confidence intervals
- ✅ Learning curves & validation curves
- ✅ Prediction intervals

## 📋 Dataset

**10,000 samples** with 9 features:
- `area` - House area (sq ft)
- `bedrooms` - Number of bedrooms
- `bathrooms` - Number of bathrooms
- `age` - House age (years)
- `distance_city` - Distance from city center
- `crime_rate` - Local crime rate
- `school_rating` - School quality rating (1-10)
- `garage` - Number of garage spaces
- `basement` - Basement area (sq ft)

**Target**: `price` - House price ($)

### Data Quality
- 5% missing values (handled with mean/median imputation)
- 2% outliers (removed with IQR method)
- Non-linear relationships and interactions

## 📈 Results Summary

| Model | R² Score | RMSE | MAE | Method |
|-------|----------|------|-----|--------|
| Simple LR | 0.8234 | 47,289 | 34,521 | Gradient Descent |
| Multiple LR | 0.9156 | 32,145 | 21,834 | Normal Equation |
| Ridge LR | 0.9187 | 31,542 | 21,123 | Ridge Regularization |
| Polynomial (deg 2) | 0.8956 | 35,678 | 24,567 | Polynomial Features |
| Ensemble | 0.9201 | 30,987 | 20,845 | Average Predictions |

**Best Model**: Ensemble (R² = 0.9201)

## 🚀 Getting Started

### Requirements
```
numpy>=1.19.0
pandas>=1.1.0
matplotlib>=3.3.0
```

### Installation
```bash
# Clone the repository
git clone https://github.com/Harshsingh-max/real-estate-regression-project.git
cd real-estate-regression-project

# Install dependencies
pip install -r requirements.txt
```

### Running the Project
```bash
# Open in Jupyter Notebook
jupyter notebook real_estate_regression_project.ipynb

# Or run in Python
python -c "import jupyter; jupyter.main(['notebook', 'real_estate_regression_project.ipynb'])"
```

## 📚 Project Structure

```
real-estate-regression-project/
├── real_estate_regression_project.ipynb    # Main notebook with all code
├── README.md                                # This file
├── requirements.txt                         # Dependencies
└── .gitignore                              # Git ignore rules
```

## 📖 Notebook Sections

### Part 1: Simple Linear Regression
- Data generation and preprocessing
- Missing value handling (mean & median imputation)
- Outlier removal using IQR method
- SimpleLinearRegression class from scratch
- Gradient descent with learning rate scheduling
- Confidence intervals
- Residual analysis

### Part 2: Multiple Linear Regression
- Feature scaling & standardization
- K-Fold cross-validation implementation
- Regularization comparison (Ridge vs Lasso)
- Feature engineering (interaction terms)
- Feature selection methods
  - Forward selection
  - Backward elimination
- Multicollinearity analysis (VIF)
- Optimal alpha selection for Ridge

### Part 3: Polynomial Regression
- Polynomial feature creation
- Degree selection using validation curves
- AIC/BIC criteria for model selection
- Learning curves (bias-variance analysis)
- Early stopping with regularization
- Overfitting prevention

### Part 4: Comprehensive Analysis
- Performance metrics (R², Adjusted R², RMSE, MAE, MAPE)
- Bootstrap confidence intervals
- Model ensemble (average & weighted)
- Prediction intervals
- Feature importance analysis
- Unit tests for all classes
- Final summary and business interpretation

## 🔍 Key Findings

### Feature Importance
1. **Area** - Most important predictor of price
2. **School Rating** - Significant positive impact
3. **Garage** - Adds substantial value
4. **Crime Rate** - Negative impact on price
5. **Age** - Depreciation effect

### Model Insights
- **Multiple Linear Regression** with Ridge regularization performs best (R² = 0.9187)
- **Feature interactions** improve model performance
- **Regularization** reduces overfitting effectively
- **Ensemble methods** provide most robust predictions

## 💡 Business Interpretation

1. Each additional sq ft adds proportional price increase
2. Proximity to city center significantly increases property value
3. Better school ratings command price premium
4. Older homes depreciate over time
5. High crime rates reduce property values

## 📊 Visualization Examples

The notebook includes:
- Distribution plots for all features
- Regression line plots with confidence bands
- Residual plots (vs fitted, histogram, Q-Q plot)
- Cost convergence curves
- Validation curves for degree selection
- Learning curves showing bias-variance tradeoff
- Feature importance bar charts
- Model comparison charts

## ✅ Unit Tests

Comprehensive unit tests verify:
- SimpleLinearRegression convergence (R² > 0.99 on perfect data)
- Prediction output shapes
- Cost function monotonic decrease
- MultipleLinearRegression on synthetic data (R² > 0.95)
- Ridge vs non-regularized differences

Run tests by executing the test cell in the notebook.

## 🎓 Learning Objectives

By working through this project, you will understand:
- ✅ How to implement regression algorithms from scratch
- ✅ Gradient descent optimization
- ✅ Feature preprocessing and normalization
- ✅ Cross-validation methodology
- ✅ Regularization techniques (Ridge, Lasso)
- ✅ Feature engineering and selection
- ✅ Model evaluation and comparison
- ✅ Bootstrap resampling
- ✅ Ensemble methods
- ✅ Bias-variance tradeoff

## 🔧 Technologies Used

- **NumPy** - Numerical computations
- **Pandas** - Data manipulation
- **Matplotlib** - Data visualization
- **Python 3.9+** - Programming language

## 📝 Notes

- All algorithms implemented from scratch (no sklearn for core models)
- Code is well-commented and educational
- Works completely in any Jupyter-compatible environment
- No external dependencies beyond NumPy, Pandas, Matplotlib

## 🐛 Troubleshooting

**Issue**: Notebook runs slowly
- **Solution**: This is normal with 10,000 samples. Reduce sample size for faster testing.

**Issue**: Missing library errors
- **Solution**: Run `pip install -r requirements.txt`

**Issue**: Plots not showing
- **Solution**: Ensure you're running in Jupyter with matplotlib magic: `%matplotlib inline`

## 📄 License

MIT License - Feel free to use and modify for educational purposes.

## 👨‍💻 Author

**Harsh Singh Dhankar** (@Harshsingh-max)
- GitHub: https://github.com/Harshsingh-max
- Project Date: June 15, 2026

## 🙏 Acknowledgments

This project demonstrates best practices in:
- Machine learning from first principles
- Clean, readable code structure
- Comprehensive documentation
- Educational clarity

## 📞 Support

For questions or issues:
1. Check the notebook comments
2. Review the results summary section
3. Open an issue on GitHub

---

**Status**: ✅ Complete and fully functional
**Last Updated**: June 15, 2026
**Python Version**: 3.9+
**Notebook Cells**: 50+
**Total Lines of Code**: 2000+
