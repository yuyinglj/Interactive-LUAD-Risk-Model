import { writable, derived } from "svelte/store";

// export const c_data = writable({});
// export var selected_cols = writable({});

export var selected_model = writable({value:"LR", label: "Linear Regression (LASSO)"});
