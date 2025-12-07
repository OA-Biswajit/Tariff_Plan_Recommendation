# PriceApp (npn-hackthon)

Short project README for the PriceApp repository used in the OA-Biswajit hackathon.

**Live App:** https://tariffplanrecommendation.streamlit.app/

**Project:** Price prediction and recommendation utilities used for hackathon demos and analysis.

**Contents:**
- `main.py` - Entry point for running the primary script.
- Notebooks: `EDA_Biswajit.ipynb`, `Final_good_Recom.ipynb` for exploration and recommendations.
- `requirements.txt` - Python dependencies for the project.
- `env/` - Optional local virtual environment (do not commit if you create your own).

## Requirements
- Python 3.10+ recommended
- See `requirements.txt` for specific packages and versions.

## Setup
1. Create and activate a virtual environment (recommended):

	 ```bash
	 python -m venv .venv
	 source .venv/Scripts/activate  # on Windows (bash)
	 # or: source .venv/bin/activate  # on Unix-like
	 ```

2. Install dependencies:

	 ```bash
	 pip install -r requirements.txt
	 ```

3. (Optional) If you already have an `env/` folder included, you can reuse it by activating the environment in that folder.

## Running
- To run the Streamlit app:

	```bash
	streamlit run main.py
	```
	The app will open in your browser at `http://localhost:8501`.

### Sample Login Credentials (for developers)
If the app has login enabled, use these sample credentials:
- **Mobile Number:** `382-4657`
- **Password:** `pass123`

- To open the notebooks for interactive analysis, start Jupyter or open them in VS Code:

	```bash
	jupyter notebook
	```

## Development notes
- Keep the `requirements.txt` up to date when adding packages.
- Avoid committing large environment folders; prefer listing dependencies instead.

## Contributing
- Create a new branch for features or fixes and open a pull request against `main`.
- Add short, focused commits and include tests or notebook examples when relevant.

## License
This repository includes a `LICENSE` file. Follow its terms for reuse and distribution.

---
If you'd like, I can also add badges (CI, license), expand the Usage examples, or generate a minimal contributing guide — tell me which you'd prefer next.
