# Interactive LUAD Risk Modeling

This is a web app for creating risk models for Lung Adenocarcinoma patients based off of their genetic data. Data is taken from TCGA and filtered down using GSEA. It's a [Svelte](https://svelte.dev/docs) web app that talks to a python backend to run the modeling. 

## How to run

To install and run the web app you need to run the following commands. At the root level of the repo.

```bash
npm install
npm run dev
```

Or the below optimizes the build for deploying (not really necessary)

```bash
npm run dev
```

Run python server

TODO

### Code layout

Svelte app is in the `src` directory, the python server in `python-server` directory, and data stored in `data` directory.

The Svelte app looks like this at a high level

```
src
|   /components     # this containts different app components
|   App.svelte      # main app code
|   stores.js       # app wide state variables  

```

### Dev notes

If you're making change to app and get a weird Rollup error like this `[!] Error: Unexpected token (Note that you need @rollup/plugin-json to import JSON files)` you probably need to install a new npm package AND add it to the `rollup.config.js` file under plugins.