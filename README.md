# Interactive LUAD Risk Modeling

This is a web app for creating risk models for Lung Adenocarcinoma patients based off of their genetic data. Data is taken from TCGA and filtered down using GSEA. It's a [Svelte](https://svelte.dev/docs) web app that talks to a python backend to run the modeling. 

## Install

To install and run the web app dependencies run this at root of repo...

```bash
npm install
```
then install server libraries

```bash
pip install fastapi unicorn
```

## Run

Run server
```bash
cd python-server
uvicorn main:app --reload
```

Run web app (from repo root)
```bash
npm run dev
```

## Data

Not all data is not in git because some of it is too big. All of the data is downloadable at [this link](https://drive.google.com/drive/folders/1QFeCGAeGQZr-mFbi77dTB5pNmRMO8eGm?usp=sharing)


`gene_data.json` should be in data folder already (but if not is at url above)
`risk_expression_data.txt`
`filtered_all_data_merged.csv`


## Code layout

Svelte app is in the `src` directory, the python server in `python-server` directory, and data stored in `data` directory.

The Svelte app looks like this at a high level

```
/src
   /components     # this containts different app components
   App.svelte      # main app code
   stores.js       # app wide state variables  

```

## Dev notes

- If you're making change to app and get a weird Rollup error like this `[!] Error: Unexpected token (Note that you need @rollup/plugin-json to import JSON files)` you probably need to install a new npm package AND add it to the `rollup.config.js` file under plugins.