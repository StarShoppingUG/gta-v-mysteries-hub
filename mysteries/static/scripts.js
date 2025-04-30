document.addEventListener('DOMContentLoaded', function() {
    
    HighlightSelected();
    ToggleMysteriesCheats();


});
 //toggle mysteries and cheat codes
function ToggleMysteriesCheats(){
    const mysteriesBtn = document.getElementById();
    const cheatsBtn = document.getElementById();
    mysteriesBtn.addEventListener("click", ()=>{
        document.querySelector("#mysteries").style.display = "block";
        document.querySelector("#cheats").style.display = "none";
    })
    cheatsBtn.addEventListener("click", ()=>{
        document.querySelector("#cheats").style.display = "block";
        document.querySelector("#mysteries").style.display = "none";
    })
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