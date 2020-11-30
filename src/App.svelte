<script>
	import FeatSelector from "./components/FeatSelector.svelte";
	import ModelSelector from "./components/ModelSelector.svelte";
	import TrainPanel from "./components/TrainPanel.svelte";
</script>

<style>
	main {
		/* text-align: center; */
		margin: 0 auto;
		border: 1px solid grey;
	}

	.header {
		min-height: 4rem;
	}

	.header h1 {
		text-transform: uppercase;
		font-size: 2rem;
		color: white;
		font-weight: 100;
		padding: 1rem;
		margin: 0rem;
	}

	.left-half {
		float: left;
		width: 40%;
	}

	.right-half {
		width: 60%;
		float: left;
	}

	@media (max-width: 1200px) {
		.left-half {
			width: 100%;
		}
		.right-half {
			width: 100%;
		}
	}
</style>

<div class="header gradient">
	<h1>LUAD Risk Model Builder</h1>
</div>

<main>
	<div class="left-half">
		<ModelSelector />
		<FeatSelector />
	</div>
	<div class="right-half">
		<TrainPanel />
	</div>
</main>
