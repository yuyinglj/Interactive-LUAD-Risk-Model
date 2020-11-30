import { writable, derived } from "svelte/store";

export const gene_data = writable({});
export var selected_genes = writable([]);
export var selected_model = writable({value:"LR", label: "Linear Regression (LASSO)"});
