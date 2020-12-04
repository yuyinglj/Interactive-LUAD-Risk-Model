<script>
    
    import Select from 'svelte-select';
    import {selected_model, prediction_type} from "../stores.js"


    let model_options = [
        {value:"LR", label: "Logistic Regression"},
        {value:"NN", label:"Neural Network"},
        {value: "DT", label:"Decision Tree"},
        {value:"RF", label:"Random Forest"},
        {value:"SVM", label:"Support Vector Machine"}
    ]

    let predict_options = [
        {value:"normal_vs_tumor", label: "Normal Tissue vs. Tumor Tissue"},
        {value:"lowrisk_vs_highrisk", label:"Low vs. High Risk"},
    ]

    let select_pred_type = {value:"normal_vs_tumor", label: "Normal Tissue vs. Tumor Tissue"}
    let dt = 500;

    $: $prediction_type = {...select_pred_type, day_thresh: dt}

</script>

<style>
    .numInput {
        width: 65px;
    }

    .modelSel {
        width: 60%;
    }

    #model-selector {
        /* border: 1px solid grey; */
        padding: 1rem;
    }

</style>

<div id="model-selector">
    <h1>Select Model Options:</h1>
    <p>Grid Search is automatically run to find the best hyperparameters.</p>

    <h3>Model Type:</h3>
    <div class="modelSel">
        <Select isClearable={false} items={model_options} bind:selectedValue={$selected_model} ></Select>
    </div>

    <h3>Prediction Type:</h3>
    <p>Select an output task to model. If selecting low vs. high risk select a threshold (in days). Patients that survive beyond this threshold are "low risk".</p>
    <div class="modelSel">
        <Select isClearable={false} items={predict_options} bind:selectedValue={select_pred_type} ></Select>
    </div>
    
    {#if select_pred_type.value == "lowrisk_vs_highrisk"}
    <br>
    Threshold: <input class="numInput" type="number" bind:value={dt} min="0" />
    {/if}

</div>
