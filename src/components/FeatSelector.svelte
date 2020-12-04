<script>
    import { selected_genes, gene_data_tvh, gene_data_risk} from "../stores";
    import Select from 'svelte-select';

    // local variables
    let gene_arr_tvh = $gene_data_tvh.map((item) => item.GENE);
    let gene_arr_risk = $gene_data_risk.map((item) => item.GENE);


    let curr_gene_data = $gene_data_tvh;
    let curr_gene_arr = gene_arr_tvh;

    let selected_data = "tvh";

    let start_index = 0;
    let end_index = 0;

    let data_options = [
        {value:"tvh", label: "GSEA: Tissue Type"},
        {value:"risk", label:"GSEA: 600 Day Risk"},
    ]

    // funcs

    $: {
        if (selected_data == "tvh") {
            curr_gene_data = $gene_data_tvh;
            curr_gene_arr = gene_arr_tvh;
            clearSelection();
        } else {
            curr_gene_data = $gene_data_risk;
            curr_gene_arr = gene_arr_risk;
            clearSelection();
        }
    }

    function selectByIndex() {
        start_index = Math.max(0, start_index); // make sure at least 0
        console.log("Selecting from " + start_index + " to " + end_index);

        $selected_genes = curr_gene_arr.slice(start_index, end_index);
    }

    function clearSelection() {
        $selected_genes = [];
        start_index = 0;
        end_index = 0;
    }
</script>

<style>
    #feat-selector {
        /* border: 1px solid rgb(192, 57, 57); */
        padding: 1rem;
    }

    .tableWrapper { 
        max-height: 750px;
        overflow: auto;
    }

    .numInput {
        width: 75px;
    }

    .blockDiv {
        display: inline-block;
    }
  

    /* table styles generated from  https://divtable.com/table-styler/ */

    table.simple-table {
        border: 1px solid #ebebeb;
        width: 100%;
        text-align: center;
        /* border-collapse: collapse; */
        border-radius:6px;
        
    }
    table.simple-table td {
        padding: 3px 4px;
    }
    table.simple-table tbody td {
        font-size: .75rem;
    }
    /* table.simple-table tr:nth-child(odd) {
        background: #ebebeb;
    } */
    table.simple-table thead th {
        font-size: 15px;
        font-weight: bold;
        color: #333333;
        text-align: center;
        padding: 10px 4px;
    }
</style>

<div id="feat-selector">
    <h1>Select Genes:</h1>
    <!-- <Select isClearable={false} items={data_options} bind:selectedValue={selected_data} ></Select> -->
    <!-- on:change="{() => answer = ''}" -->

    <table>
        <tbody>
            <tr>
                <td>
                    <select bind:value={selected_data} >
                        {#each data_options as d}
                            <option value={d.value}>
                                {d.label}
                            </option>
                        {/each}
                    </select>
                </td>
                <td></td>

            </tr>

            <tr>
                <td>
                    <input class="numInput" type="number" bind:value={start_index} min="0" /> - 
                    <input class="numInput" type="number" bind:value={end_index} min="0" />   
                </td>
                <td>
                    <button class="" on:click={selectByIndex}>Go!</button>     
                    <button class="" on:click={clearSelection}>Clear</button>
                </td>
            </tr>

        </tbody>
    </table>
    <!-- <div class="blockDiv">
        Select Ranking List:
        <select bind:value={selected_data} >
            {#each data_options as d}
                <option value={d.value}>
                    {d.label}
                </option>
            {/each}
        </select>
    </div> -->
    
    <!-- <p>{JSON.stringify(curr_gene_data.slice(0, 10))}</p> -->


    <!-- <div class="blockDiv">
            Start:&nbsp;&nbsp;<input class="numInput" type="number" bind:value={start_index} min="0" />&nbsp;
            End:&nbsp;&nbsp;<input class="numInput" type="number" bind:value={end_index} min="0" />   
            <button class="" on:click={selectByIndex}>Select</button>     
    </div>
    <div class="blockDiv">
        <button class="" on:click={clearSelection}>Clear Selection</button>
    </div> -->
    <div class="tableWrapper">
        <table class="simple-table">
            <thead>
                <th>Gene</th>
                <th>Score</th>
                <th>Select</th>
            </thead>
            <tbody>
                {#each curr_gene_data as d}
                    <tr>
                        <td>{d.GENE}</td>
                        <td>{d.SCORE}</td>
                        <td>
                            <input
                                type="checkbox"
                                bind:group={$selected_genes}
                                value={d.GENE} />
                        </td>
                    </tr>
                {/each}
            </tbody>
        </table>
    </div>

</div>
