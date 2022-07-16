//print date to log
const d = Date();
console.log(d);

//pull the pathname from window location
const activePage = window.location.pathname;
console.log(window);
console.log(window.location);
console.log(activePage);

/*create an arey of the links in nav, 
compare each to pathname and mark the one that is active
*/ 
const navLinks = document.querySelectorAll('nav a').forEach(link => {    
  if(link.href.includes(`${activePage}`)){
    link.classList.add('active');
  }
});

function changeImage() {
    var image = document.getElementById('woman');
    if (image.src.match("../static/womanMoney.jpg")) {
        image.src = "../static/MoneyCow.jpg";
    }
    else {
        image.src = "../static/womanMoney.jpg";
    }
}

function sayThankU() {
    var input = document.getElementById("firstName");
    alert(`Thank you!
     we've got your details and we will contact you ASAP :)`);
    }



document.querySelector('#outer-source__form')?.addEventListener('submit',(e)=> {
    e.preventDefault()
    const id = e.target.id.value
    fetch('https://reqres.in/api/users/' + id)
        .then(results => results.json())
        .then(json => {
            const image = document.querySelector('#outer-source__image1')
            image.classList.remove('invisible')
            image.src = json.data.avatar
        })
        .catch((e) => {
        console.log(e)
        })
})
