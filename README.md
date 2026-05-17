# AI System Workshop (2 Hours)

This folder is a complete, ready-to-run workshop package.

## What you'll learn (by doing)
- **K-Means**: discover student personas (no labels needed)
- **Logistic Regression**: explainable dropout risk (probability + reasons)
- **Random Forest**: stronger dropout prediction for messy human behavior

---

## 1) Fresh setup (10 minutes)

### Windows (recommended for students)
1. Install **Python 3.10+** from python.org  
   ✅ Tick **“Add Python to PATH”** during install.
2. Open this folder in File Explorer.
3. Double-click: **start_windows.cmd**

If it opens a browser page (Jupyter), you're ready.

### macOS / Linux
1. Make sure Python 3 is installed.
2. Open Terminal in this folder.
3. Run:
   ```bash
   bash start_mac_linux.sh
   ```

---

## 2) Run the notebook
When Jupyter opens:
1. Click **student_dropout_system.ipynb**
2. Run cells **top to bottom**
3. Read the explanation above each code cell

---

## Troubleshooting (quick fixes)
- If `pip` is not found: restart terminal, or reinstall Python with PATH enabled.
- If Jupyter doesn’t open: run `python -m jupyter notebook`
- If a library is missing: run  
  `pip install pandas numpy scikit-learn matplotlib seaborn jupyter`

---

## Files
- `student_dropout_system.ipynb` → main notebook
- `student_data.csv` → dataset
- `start_windows.cmd` → one-click run (Windows)
- `start_mac_linux.sh` → one-click run (macOS/Linux)
