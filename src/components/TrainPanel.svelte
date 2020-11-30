<script>
    import { selected_model, selected_genes } from "../stores.js";

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
        let request_data = {
            "model_type": $selected_model.value,
            "genes": $selected_genes
        }
        promise = postAPI(request_data);
    }
</script>

<style>
    #feat-selector {
        border: 1px solid rgb(87, 130, 209);
        padding: 1rem;
    }
</style>

<div id="feat-selector">
    <h1>Train Model:</h1>
    <p>Model type: {$selected_model.label}</p>
    <p>Features: {$selected_genes}</p>

    <button on:click={handleClick}> hit API</button>

    {#await promise}
        <p>...waiting...</p>
    {:then respObj}
        <p>The response is {JSON.stringify(respObj)}</p>
    {:catch error}
        <p style="color: red">{error.message}</p>
    {/await}
</div>
