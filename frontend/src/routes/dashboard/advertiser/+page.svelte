<script>

let promise = companyId();

async function companyId(){
    const company_request = await fetch("http://localhost:8000/database/companies/");
    const response_body = await company_request.json();
    let companies_option = [];
    response_body.forEach(company => {
        companies_option.push([company["id"], company["name"]])
    });
    return companies_option;
}

let promise2 = user();
async function user() {
    const res = await fetch("http://localhost:8000/database/users/");
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
<h1> Advertiser </h1>

{#await promise2}
<p>...waiting</p>
{:then users}
{#each users.slice(0,1) as user}


<h2>hello {user.name}</h2>

<p>your ads : <br></p>

{/each}
{:catch error}
<p style="color: red">{error.message}</p>
{/await}

<!-- ///////////////// -->
<br>
<br>
<br>
<br>


<a href="http://localhost:5173/post/">
<button class="login" type="submit">Post a new ad : </button>
<!-- {/each}
{:catch error}
<p style="color: red">{error.message}</p>
{/await} -->

</main>