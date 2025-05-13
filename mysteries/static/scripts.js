document.addEventListener('DOMContentLoaded', function() {

    HighlightSelected();
    ToggleMysteriesCheats();
    FilterPlatformCheats();
    DeleteMystery();
    NavigateMystery();
    ReadMore();
    NavigateMysteriesCheats();
    ToggleNavbar();
    ToggleTheme();

});
 //toggle mysteries and cheat codes
function ToggleMysteriesCheats(){
    const mysteriesBtn = document.getElementById("mysteries-btn");
    const cheatsBtn = document.getElementById("cheats-btn");
    if (mysteriesBtn){
    mysteriesBtn.addEventListener("click", ()=>{
        document.querySelector("#mysteries-container").style.display = "block";
        document.querySelector("#cheats-container").style.display = "none";
        mysteriesBtn.classList.add("mysteries-cheats-selected");
        cheatsBtn.classList.remove("mysteries-cheats-selected");
    })
    }
    if(cheatsBtn){
    cheatsBtn.addEventListener("click", ()=>{
        document.querySelector("#cheats-container").style.display = "block";
        document.querySelector("#mysteries-container").style.display = "none";
        mysteriesBtn.classList.remove("mysteries-cheats-selected");
        cheatsBtn.classList.add("mysteries-cheats-selected");
    })
    }
}
//Highlight selected page.
function HighlightSelected(){
     // Get all navigation links
     const navLinks = document.querySelectorAll('.nav-links a');
     const currentPath = window.location.pathname;
 
     // Add active class to current page link
     navLinks.forEach(link => {
         if (link.getAttribute('href') === currentPath) {
             link.classList.add('active');
         }
      
     });
}
//Display cheats for specific platforms.
function FilterPlatformCheats(){
    const platform = document.getElementById("platform-choice")
    
    if(platform){
    platform.addEventListener("change", async ()=>{
        const response = await fetch(`/filter-cheats/?platform=${platform.value}`);
        const result = await response.text()
        document.getElementById("cheats-list").innerHTML = result
    } )
    }
    
}
//Get CSRFtoken
function GetCSRFToken(){
    return document.querySelector('meta[name="csrf-token"]').getAttribute('content')
}
//Delete mystery
function DeleteMystery(){
    const deleteBtns = document.querySelectorAll(".delete-mystery");
    deleteBtns.forEach(button => {
        button.addEventListener("click", function (){
            if (!confirm("Are you sure you want to delete this mystery?")) return;
            const mystery = this.closest(".user-mystery-card");
            const mysteryId = mystery.getAttribute("data-id");
            fetch(`/delete-mystery/${mysteryId}`, {
                method: 'POST',
                headers : {
                    'X-CSRFToken' : GetCSRFToken(),
                    'Content-Type' : 'application/json'}, }).then(response => {
                        if(response.ok){
                            mystery.remove();
                        }
                        else{
                            alert("Delete failed")
                        }
                        
                    })
                 }) })
                       
}

function NavigateMystery(){
    document.querySelectorAll(".view-mystery").forEach(
        btn => {
            btn.addEventListener("click", function(){
                const id = this.dataset.id
                window.location.href = `/browse/#mystery-${id}`;
            })
        }
    )
}
function ReadMore(){
    document.querySelectorAll(".more-text-btn").forEach(btn =>{
        btn.addEventListener("click", function(){
            const id = this.dataset.id
            const desc = document.getElementById(`desc-${id}`);
            const moreText = desc.querySelector(".more-text");
            if(moreText.style.display === 'none'){
                moreText.style.display = "inline";
                this.textContent = "Read Less"
            }
            else{
                moreText.style.display = "none";
                this.textContent = "Read More";
            }
        })
    })
}
function NavigateMysteriesCheats(){
    const hash = window.location.hash
    const cheatSection = document.querySelector("#cheats-container");
    const mysteriesSection = document.querySelector("#mysteries-container");
    if (hash === "#cheats"){
        cheatSection.style.display = "block";
        mysteriesSection.style.display = "none";
        document.getElementById("mysteries-btn").classList.remove("mysteries-cheats-selected");
        document.getElementById("cheats-btn").classList.add("mysteries-cheats-selected");

    }
}
function ToggleNavbar(){
    const navBtn = document.getElementById("toggle-navbar");
    const nav = document.querySelector(".nav-links");
    navBtn.addEventListener("click", function (e){
        e.stopPropagation();
        nav.classList.toggle("show");
    })
    document.addEventListener("click", (e)=>{
        if(!nav.contains(e.target) && ! navBtn.contains(e.target)){
            nav.classList.remove("show")
        }
    })

}
function ToggleTheme(){
    const btn = document.getElementById("toggle-theme");
    const body = document.body;
    if (localStorage.getItem("theme") == "light"){
        body.classList.add("light-mode");
    }
    btn.addEventListener("click", ()=> {
        body.classList.toggle("light-mode");
        const theme = body.classList.contains('light-mode') ? 'light' : "dark";
        localStorage.setItem("theme", theme);
    })
}