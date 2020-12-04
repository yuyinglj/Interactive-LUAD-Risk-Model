<script>
    import { selected_model, selected_genes, prediction_type } from "../stores.js";

    // base URL of server
    const url_base = "http://127.0.0.1:8000"

    async function postAPI(r_data) {

        // stringify
        let processed_data = JSON.stringify(r_data);
        console.log(processed_data)

        // send to server
        const res = await self.fetch(url_base + "/model", {
            method: "POST",
            headers: { 'Content-Type': 'application/json'},
            body: JSON.stringify(r_data),
        });

        if (res.ok) {
            return res.json();
        } else {
            throw new Error(res);
        }
    }

	let promise = Promise.resolve([]); // trick the dum dum computer

    function handleClick() {
        // Validate data a little

        if (!$selected_genes.length) {
            console.log("Error!")

            promise = Promise.resolve("Uh oh! Please select at least 1 gene to train a model."); // trick the dum dum computer

        } else { // is valid

            let request_data = {
            "classifier_name": $selected_model.value,
            "genelist": $selected_genes,
            "prediction_type": $prediction_type.value,
            "day_thresh": $prediction_type.day_thresh
            }

            promise = postAPI(request_data);

        }
    }
</script>

<style>
    #feat-selector {
        /* border: 1px solid rgb(87, 130, 209); */
        padding: 1rem;
    }
</style>

<div id="feat-selector">
    <h1>Train Model:</h1>
    <p>Model type: {$selected_model.label}</p>
    <p>Num Features: {$selected_genes.length}</p>
    <p>Features: {$selected_genes}</p>

    <p>Pred type: {JSON.stringify($prediction_type)}</p>

    <button on:click={handleClick}> hit API</button>

    {#await promise}
        <p>...waiting...</p>
    {:then respObj}
        <p>The response is {JSON.stringify(respObj)}</p>
    {:catch error}
        <p style="color: red">{error.message}</p>
    {/await}
</div>
