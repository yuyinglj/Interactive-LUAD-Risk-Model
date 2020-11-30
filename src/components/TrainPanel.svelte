<script>
    import { selected_model, selected_genes } from "../stores.js";

    const url_base = "http://127.0.0.1:8000"

    async function hitAPI() {
        const res = await self.fetch(url_base + "/delay/45");

        if (res.ok) {
            return res.json();
        } else {
            throw new Error(res);
        }
    }

	let promise = Promise.resolve([]); // trick the dum dum computer

    function handleClick() {
        promise = hitAPI();
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
    {:then number}
        <p>The number is {number.item_id}</p>
    {:catch error}
        <p style="color: red">{error.message}</p>
    {/await}
</div>
