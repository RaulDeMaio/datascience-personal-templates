# 📓 Jupyter Notebooks

This directory is for **exploratory analysis**, **data preprocessing**, and **experiments** before formalizing the code in the `src/` directory.

---

## ✅ Guidelines

### 📁 Naming Convention
Please follow a numeric prefix to maintain order:

- 01_data_exploration.ipynb 
- 02_feature_engineering.ipynb 
- 03_model_training.ipynb 
- 04_model_evaluation.ipynb


### 🧼 Best Practices
- Keep notebooks **lightweight** and **modular**
- Refactor production code into `src/` when stabilized
- Use **Markdown cells** generously to document insights
- Avoid hardcoding paths; prefer using variables or relative paths
- Restart the kernel before saving/committing to avoid output clutter

---

## 🧪 Version Control with Pre-commit (Optional)

If you enabled `nbQA` in pre-commit, your notebooks will be linted automatically:
- `black`, `flake8`, `mypy` checks via `nbQA`

---

## 📦 Example Workflow

1. Explore or preprocess data here
2. Validate ideas
3. Move reusable code to `src/` for productionization
4. Re-run notebook from top and clean outputs before committing

---

## 🔒 Commit Policy

✅ Clean notebooks: no large outputs  
✅ Modular structure  
✅ Descriptive filenames  
✅ Clear titles and documented steps

---

