<script>
	import FeatSelector from "./components/FeatSelector.svelte";
	import ModelSelector from "./components/ModelSelector.svelte";
	import TrainPanel from "./components/TrainPanel.svelte";
	import {gene_data} from "./stores";

	// load data
	import * as gene_data_json from "../data/gene_data.json";
	$gene_data = gene_data_json.values;
</script>

<style>
	main {
		/* text-align: center; */
		margin: 0 auto;
		/* border: 1px solid red; */ /* for debugging spacing */
		
	}

	.header {
		min-height: 6rem;
		display: flex;
		/* width: 100%; */
		align-items: center;
	}

	.header h1 {
		text-transform: uppercase;
		font-size: 2.5rem;
		color: white;
		font-weight: 100;
		padding: 1rem;
		margin: 0rem;
	}

	.grid-box {
		display: grid;
		grid-template-columns: 1fr 1fr 1fr;
		/* grid-template-rows: 1fr 1fr; */
		height: 100%;
		grid-auto-rows: minmax(5rem, auto);
	}

	.left-top {
		grid-column-start: 1;
		grid-column-end: 2;
		grid-row-start: 1;
		/* grid-row-end: 2; */
	}

	.left-bottom {
		grid-column-start: 1;
		grid-column-end: 2;
		grid-row-start: 2;
		/* grid-row-end: 3; */
	}

	.right{
		grid-column-start: 2;
		grid-column-end: 4;
		grid-row-start: 1;
		/* grid-row-end: 3; */
	}


	/* @media (max-width: 1200px) {
		.left-half {
			width: 100%;
		}
		.right-half {
			width: 100%;
		}
	} */
</style>

<div class="header gradient">
	<h1>LUAD Risk Model Builder</h1>
</div>

<main>
	<div class="grid-box">
		<div class="left-top">
			<ModelSelector />
		</div>
		<div class="left-bottom">
			<FeatSelector />
		</div>
		<div class="right">
			<TrainPanel />
		</div>
	</div>
</main>
