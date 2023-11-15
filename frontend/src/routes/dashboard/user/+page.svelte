<script>
    let promise = getRandomNumber();
    
    async function getRandomNumber() {
        const res = await fetch("http://localhost:8000/database/advertisements/");
        const json = await res.json();
        console.log(json);
    
        if (res.ok) {
            return json;
        } else {
            throw new Error(json);
        }
    }
    
    async function learnmore(id) {
        const res = await fetch("http://localhost:8000/database/advertisements/" + id);
        const json = await res.json();
        console.log(json);
    
        if (res.ok) {
            document.getElementById("jobinfo").style.visibility = "visible"
            document.getElementById("title").innerText = json["title"]
            document.getElementById("salary").innerText = json["salary"]
            document.getElementById("type").innerText = json["type"]
            document.getElementById("description").innerText = json["description"]
            document.getElementById("date").innerText = json["date"]
            document.getElementById("company").innerText = json["company"]
            return json;
        } else {
            throw new Error(json);
        }
    }
    
    </script>
    
    <main>
    
    <div id="jobs">
    
    <h1> Jobs Available</h1>
    
    
    {#await promise}
    <p>...waiting</p>
    {:then advertisements}
    {#each advertisements as ad}
    
    <section id="{ad.id}">
    
        <article>
        <p><b>Title :</b> <br> {ad.title}</p>
        </article>
    
        <article>
        <p class="description"><b>Description :</b> <br> {ad.description.slice(0, 40)}</p>
        </article>
    
        
        <div>
            <button type="submit" on:click={() => learnmore(ad.id)}> Learn More </button>
        </div>
    
        <a href="http://localhost:5173/Apply/">
        <button class="button" type="submit"> Apply </button>
    
        </section>
        {/each}
        {:catch error}
        <p style="color: red">{error.message}</p>
        {/await}
    </div>
    
    
    <div id="jobinfo">
        
        <section>
    
            <article>
            <b>Title :</b> <br>
            <p id="title"></p>
            </article>
        
            <article>
            <b>Salary :</b> <br>
            <p id="salary"></p>
            </article>
        
            <article>
            <b>Type :</b> <br>
            <p id="type"></p>
            </article>
        
            <article>
            <b>Description :</b> <br>
            <p class="description" id="description"></p>
            </article>
        
            <article>
            <b>Starting date :</b> <br>
            <p id="date"></p>
            </article>
        
            <article>
            <b>Company :</b> <br>
            <p id="company"></p>
            </article>
    
        </section>
    
    </div>
    
    </main>
    
    
    <style>
    
    main {
        background-color: rgb(215, 214, 214);
        height: 100%;
        display: flex;
        flex-direction: row;
    }
    
    main div{
        width : 48%;
        flex : 1;
        height: 100%;
    }
    
    #jobs {
        background-color: pink;
    }
    
    #jobinfo{
    visibility: hidden;
    }
    
    .description{
        align-self: auto;
        word-wrap: break-word;
    }
    
    #jobs section {
        height: 30%;
    
    }
    
    section {
        width: 15vw;
        background-color: rgb(250, 249, 250);
        margin: 10px;
        display: inline-block;
    }
    
    h1{
       text-align: center;
    }
    
    .button{
        background-color: aqua;
    }
    </style>
    