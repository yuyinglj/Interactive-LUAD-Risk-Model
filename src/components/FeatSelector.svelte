<script>
    import { Datatable, rows } from "svelte-simple-datatables";
    // import { selected_model } from "../stores";

    const settings = {
        sortable: true,
        pagination: true,
        rowPerPage: 5,
        columnFilter: false,
        css: true,
    };

    let data = [
        {
            gene: "ABBA1",
            score: 0.999,
        },
        {
            gene: "QWWWL2",
            score: 0.9,
        },
        {
            gene: "HI883",
            score: 0.729,
        },
        {
            gene: "QWWWL4",
            score: 0.9,
        },
        {
            gene: "HI885",
            score: 0.729,
        },
        {
            gene: "QWWWL6",
            score: 0.9,
        },
        {
            gene: "HI887",
            score: 0.729,
        },
        {
            gene: "QWWW8L",
            score: 0.9,
        },
        {
            gene: "HI898",
            score: 0.729,
        },
        {
            gene: "HI1088",
            score: 0.729,
        },
        {
            gene: "QWW11WL",
            score: 0.9,
        },
        {
            gene: "HI1288",
            score: 0.729,
        },
        {
            gene: "QWW13WL",
            score: 0.9,
        },
        {
            gene: "HI1488",
            score: 0.729,
        },
    ];

    let selected_genes = [];

    $: {
        console.log(selected_genes);
    }
</script>

<style>
    #feat-selector {
        border: 1px solid rgb(192, 57, 57);
        padding: 1rem;
        max-width: 500px;
    }

    table.simple-table {
        width: 100%;
        height: 200px;
        text-align: left;
        border-collapse: collapse;
    }
    table.simple-table td,
    table.simple-table th {
        border: 1px solid #000000;
        padding: 6px 6px;
    }
    table.simple-table tbody td {
        font-size: 13px;
    }
    table.simple-table tr:nth-child(even) {
        background: #efefef;
    }
    table.simple-table thead {
        background: #cfcfcf;
    }
    table.simple-table thead th {
        font-size: 15px;
        font-weight: bold;
        color: #000000;
        text-align: center;
    }
    table.simple-table tfoot td {
        font-size: 14px;
    }
</style>

<div id="feat-selector">
    <h1>Select Genes:</h1>
    <p>Selected these genes: {selected_genes}</p>

    <Datatable {settings} {data}>
        <thead>
            <th data-key="gene">Gene</th>
            <th data-key="score">Score</th>
            <th>Check?</th>
        </thead>
        <tbody>
            {#each $rows as row}
                <tr>
                    <td>{row.gene}</td>
                    <td>{row.score}</td>
                    <td>
                        <input
                            type="checkbox"
                            bind:group={selected_genes}
                            value={row.gene} />
                    </td>
                </tr>
            {/each}
        </tbody>
    </Datatable>

    <!-- <table>
        <thead>
            <th data-key="gene">Gene</th>
            <th data-key="score">Score</th>
            <th>Check?</th>
        </thead>
        <tbody>
            {#each data as d}
                <tr>
                    <td>{d.gene}</td>
                    <td>{d.score}</td>
                    <td>
                        <input
                            type="checkbox"
                            bind:group={selected_genes}
                            value={d.gene} />
                    </td>
                </tr>
            {/each}
        </tbody>

    </table> -->
</div>
