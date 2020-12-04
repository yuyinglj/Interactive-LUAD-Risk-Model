<script>
    import { selected_genes, gene_data } from "../stores";

    let gene_arr = $gene_data.map((item) => item.GENE);

    let start_index = 0;
    let end_index = 0;

    function selectByIndex() {
        start_index = Math.max(0, start_index); // make sure at least 0
        console.log("Selecting from " + start_index + " to " + end_index);

        $selected_genes = gene_arr.slice(start_index, end_index);
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

    <div class="blockDiv">
            Start:&nbsp;&nbsp;<input class="numInput" type="number" bind:value={start_index} min="0" />&nbsp;
            End:&nbsp;&nbsp;<input class="numInput" type="number" bind:value={end_index} min="0" />        
    </div>
    <div class="blockDiv">
        <button class="" on:click={selectByIndex}>Select</button>
        <button class="" on:click={clearSelection}>Clear</button>
    </div>
    <div class="tableWrapper">
        <table class="simple-table">
            <thead>
                <th>Gene</th>
                <th>Score</th>
                <th>Select</th>
            </thead>
            <tbody>
                {#each $gene_data as d}
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
