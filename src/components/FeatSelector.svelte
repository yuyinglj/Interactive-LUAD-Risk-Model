<script>
    import { selected_genes, gene_data} from "../stores";

    /*

    TODO here
        - Add clear selection
        - Add range selection so can choose genes 0-100 or 100-500

    */
    
</script>

<style>
    #feat-selector {
        border: 1px solid rgb(192, 57, 57);
        padding: 1rem;
        max-width: 500px;
        max-height: 750px;
        overflow: auto;
    }

    /* table styles generated from  https://divtable.com/table-styler/ */
    table.simple-table {
        border: 2px solid #ffffff;
        width: 100%;
        text-align: center;
        border-collapse: collapse;
    }
    table.simple-table td,
    table.simple-table th {
        border: 1px solid #ffffff;
        padding: 3px 4px;
    }
    table.simple-table tbody td {
        font-size: 13px;
    }
    table.simple-table tr:nth-child(even) {
        background: #ebebeb;
    }
    table.simple-table thead {
        background: #ffffff;
        border-bottom: 2px solid #333333;
    }
    table.simple-table thead th {
        font-size: 15px;
        font-weight: bold;
        color: #333333;
        text-align: center;
    }
</style>

<div id="feat-selector">
    <h1>Select Genes:</h1>
    
    <table class="simple-table">
        <thead>
            <th data-key="gene">Gene</th>
            <th data-key="score">Score</th>
            <th>Check?</th>
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
