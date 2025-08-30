# Shipment Analytics — Project

**One-line:** ETL + Validation pipeline, KPI dashboard, and an interactive Streamlit demo for logistics shipment data.

---

## Project story (Problem → Approach → Results)

**Problem**  
Raw logistics data often contains invalid tracking numbers, missing or inconsistent dates, and non-numeric weights. These issues make operational reporting and decision-making unreliable for courier companies.

**Approach**  
- Built a production-style ETL notebook (`ETL_shipment_pro.ipynb`) that: validates tracking numbers (regex), enforces a branch whitelist, parses dates robustly, coerces numeric weights, flags duplicates, and exports invalid rows to `errors.csv`.  
- Created a dashboard notebook (`Dashboard_shipment_pro.ipynb`) that computes KPIs (claims per 100 shipments, delivered ratio, average transit days) and saves clear charts + a PDF report.  
- Added a small Streamlit app (`app.py`) so hiring managers can interact with the KPIs without opening notebooks.  
- Included a synthetic demo dataset (`shipments_raw_demo.csv`) and the produced `cleaned_shipments.csv` and `errors.csv` so the app runs immediately.

**Results**  
- Cleaned dataset and error isolation for QA.  
- Six chart PNGs and a multi-page PDF report for recruiter review.  
- Interactive Streamlit dashboard for quick exploration.

---

## Files in this repo
- `ETL_shipment_pro.ipynb` — ETL + validation pipeline (run this first).  
- `Dashboard_shipment_pro.ipynb` — KPIs, charts, and PDF report (run after ETL).  
- `app.py` — Streamlit interactive dashboard (reads `cleaned_shipments.csv`).  
- `shipments_raw_demo.csv` — Synthetic raw demo data.  
- `cleaned_shipments.csv` — Clean data produced by ETL (included).  
- `errors.csv` — Rows that failed critical validations (included).  
- `README.md` — This file.  
- `requirements.txt` — Minimal Python deps to run notebooks and app.

---

## Quickstart (macOS / Linux)

1. (optional) Add pip --user bin to PATH if you use --user installations:
```bash
USER_BASE=$(python3 -m site --user-base)
echo 'export PATH="$PATH:'$USER_BASE'/bin"' >> ~/.zshrc
source ~/.zshrc
```

2. Install Python packages (minimal):
```bash
python3 -m pip install --upgrade pip --user
python3 -m pip install --user pandas numpy matplotlib nbformat
# install streamlit only if your network is stable:
python3 -m pip install --user streamlit
```

3. Open Jupyter Notebook or Lab in this folder:
```bash
python3 -m notebook        # or: python3 -m jupyterlab
```

4. Run `ETL_shipment_pro.ipynb` (Kernel → Restart & Run All). This creates/overwrites `cleaned_shipments.csv` and `errors.csv`.

5. Run `Dashboard_shipment_pro.ipynb` to generate charts and `shipment_report.pdf`.

6. Run the Streamlit app (optional):
```bash
python3 -m streamlit run app.py
```

---

## Git & GitHub — push to your repo (copy-paste)
Replace `<GIT_URL>` with your repo URL, e.g. `https://github.com/ABDURAHM4M/All-my-projects-.git`.

```bash
cd path/to/shipment_project_repaired        # local folder
git init
git add .
git commit -m "feat: add shipment analytics ETL, dashboard, and Streamlit demo"
git branch -M main
git remote add origin <GIT_URL>
git push -u origin main
```

If your remote already has content, run instead:
```bash
git remote add origin <GIT_URL>
git fetch origin
git branch -M main
git pull --rebase origin main   # careful: resolves conflicts if any
git add .
git commit -m "feat: add shipment analytics ETL, dashboard, and Streamlit demo"
git push -u origin main
```

---

## Suggested GitHub README blurb (short, one-paragraph)
**Shipment Analytics** — ETL pipeline, data validation, KPI dashboard, and interactive Streamlit app for logistics operations. Demonstrates data cleaning, validation rules, KPI calculations, charting, and a recruiter-friendly PDF report. Built with Python (Pandas, Matplotlib) and Streamlit.

---

## Suggested LinkedIn project blurb (1-2 lines)
Built an end-to-end shipment analytics demo: ETL + validation (cleaned data + error isolation), KPI dashboard, and an interactive Streamlit app for quick stakeholder review.

---

## Contact / Notes
If anything fails (missing packages or PATH issues), run the commands in the Quickstart section above.  
If you want, I can also push this repo to GitHub for you *if* you provide a personal access token (PAT) or give me permission to open a GitHub repo name to push to; otherwise I’ll provide the exact commands and confirm each step.
