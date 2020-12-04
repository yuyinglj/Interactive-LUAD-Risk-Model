import { writable, derived } from "svelte/store";

export const gene_data_tvh = writable({});
export const gene_data_risk = writable({});
export var selected_genes = writable([]);
export var selected_model = writable({value:"LR", label: "Logistic Regression"});
export var prediction_type = writable({value:"normal_vs_tumor", label: "Normal Tissue vs. Tumor Tissue", day_thresh: 500});

