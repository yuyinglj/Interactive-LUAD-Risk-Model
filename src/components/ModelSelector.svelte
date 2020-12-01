<script>
    
    import Select from 'svelte-select';
    import {selected_model} from "../stores.js"


    let model_options = [
        {value:"LR", label: "Linear Regression (LASSO)"},
        {value:"NN", label:"Neural Network"},
        {value: "DT", label:"Decision Tree"},
        {value:"RF", label:"Random Forest"}
    ]


</script>

<style>

    #model-selector {
        /* border: 1px solid grey; */
        padding: 1rem;
    }

</style>

<div id="model-selector">
    <h1>Select Model Type:</h1>

    <Select items={model_options} bind:selectedValue={$selected_model} ></Select>

</div>
