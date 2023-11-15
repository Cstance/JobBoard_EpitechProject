<script>
    
    let promise = getRandomNumber();

    async function getRandomNumber() {
        const res = await fetch("http://localhost:8000/database/advertisements/");
        console.log(res)
        const json = await res.json();
        console.log(json);

        if (res.ok) {
            return json;
        } else {
            throw new Error(json);
        }
    }
</script>


<main>
	<a href="http://localhost:5173/login/">
	<button class="login" type="submit">Login</button>
	</a>


	<h2>Recently posted jobs</h2>

	{#await promise}
	<p>...waiting</p>
	{:then advertisements}
	{#each advertisements.slice(0, 2) as ad}
	
	<section>
	
		<article>
		<p><b>Title :</b> <br> {ad.title}</p>
		</article>
	
		<article>
		<p><b>Salary :</b> <br> {ad.salary}</p>
		</article>
	
		<article>
		<p><b>Type :</b> <br> {ad.type}</p>
		</article>
	
		<article>
		<p><b>Description :</b> <br> {ad.description}</p>
		</article>
	
		<article>
		<p><b>Starting date :</b> <br> {ad.starting_date}</p>
		</article>
	
		<article>
		<p><b>Company :</b> <br> {ad.company}</p>
		</article>
	
		</section>
		{/each}
		{:catch error}
		<p style="color: red">{error.message}</p>
		{/await}
	

	<a href="http://localhost:5173/ads/">
	<button class="submit" type="submit">See More</button>
	</a>

</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h2 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}

	.login{
		position: absolute;
		top : 20px;
		right: 50px;
	}

	section{	
		border: solid;	
		margin-bottom: 30px;
	}
</style>