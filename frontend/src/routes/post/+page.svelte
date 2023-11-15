<script>

let promise = companyIdToDropboxOption();

async function companyIdToDropboxOption(){
    const company_request = await fetch("http://localhost:8000/database/companies/");
    const response_body = await company_request.json();
    let companies_option = [];
    response_body.forEach(company => {
        companies_option.push([company["id"], company["name"]])
    });
    return companies_option;
}

async function postAd(data) {
    const res = await fetch("http://localhost:8000/database/advertisements/", {
        method: "POST",
        body : JSON.stringify(data)
    });
    const response_body = await res.json();
    console.log(response_body)

    if (res.ok) {
        window.location.replace("/post/posted")
    } else {
        for(let key in response_body){        
            document.getElementById(key+"_error").textContent = response_body[key]
        }
    }

}

function post(){
    
    let Ad = { 
            title : document.getElementById('title').value, 
            salary : document.getElementById('salary').value,
            type : document.getElementById('type').value,
            description : document.getElementById('description').value,
            starting_date : document.getElementById('starting_date').value,
            company : document.getElementById('company').value,
    }


    postAd(Ad)
}



</script>


<main>
<h1>Post your annonce</h1>

<form method="post">
    <label for="company"> Company name*</label><div id="company_error"></div>
    <select id="company" name="company">
        {#await promise}
        <option>Loading companies...</option>
        {:then companies} 
            
        {#each companies as company}<option value={company[0]}>{company[1]}</option>{/each}
        {/await}
    </select><br>

    <label for="title">Title*</label>
    <div id="title_error"></div>
    <input type="text" id="title" name="title"><br>

    <label for="description">Job description*</label>
    <div id="description_error"></div>
    <textarea rows="16" cols="64" id="description" name="description"></textarea><br>

    <label for="salary">Average Salary (per month)*</label>
    <div id="salary_error"></div>
    <input type="number" id="salary" name="salary"><br>

    <label for="type">Type*</label>
    <div id="type_error"></div>
    <select id="type" name="type">
        <option value="CDI">CDI</option>
        <option value="CDD">CDD</option>
        <option value="Alternance">Alternance</option>
        <option value="Stage">Stage</option>
    </select>    
    <br>

    <label for="starting_date">Starting date*</label>
    <div id="starting_date_error"></div>
    <input type="date" id="starting_date" name="starting_date" min="2023-10-20" max="2025-12-31" />

    <br>
    <br>

    <button type="button" on:click={() => post()}>Post your ad</button>

    <div id="error"> </div>

</form>
</main>

<style>
    form div{
        color: red;
        font-size: 10px;
    }

    form input{
        width: 128px;
    }
    form select{
        width: 128px;
    }
</style>
