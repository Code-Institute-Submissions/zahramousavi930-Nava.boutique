


const scroll = document.getElementById('my-scroll');

var isDown = false;
var scrollX;
var scrollLeft;

// Mouse Up Function
scroll.addEventListener("mouseup", () => {
  isDown = false;
  scroll.classList.remove("active");
});

// Mouse Leave Function
scroll.addEventListener("mouseleave", () => {
  isDown = false;
  scroll.classList.remove("active");
});

// Mouse Down Function
scroll.addEventListener("mousedown", (e) => {
  e.preventDefault();
  isDown = true;
  scroll.classList.add("active");
  scrollX = e.pageX - scroll.offsetLeft;
  scrollLeft = scroll.scrollLeft;
});

// Mouse Move Function
scroll.addEventListener("mousemove", (e) => {
  if (!isDown) return;
  e.preventDefault();
  var element = e.pageX - scroll.offsetLeft;
  var scrolling = (element - scrollX) * 2;
  scroll.scrollLeft = scrollLeft - scrolling;
});






// second scrool of discount

const discountcontainer = document.querySelector(".discount-container");
var isdown = false;
var scrollX;
var scrollLeft;

// Mouse Up Function
discountcontainer.addEventListener("mouseup", () => {
  isdown = false;
  discountcontainer.classList.remove("active");
});

// Mouse Leave Function
discountcontainer.addEventListener("mouseleave", () => {
  isdown = false;
  discountcontainer.classList.remove("active");
});

// Mouse Down Function
discountcontainer.addEventListener("mousedown", (e) => {
  e.preventDefault();
  isdown = true;
  discountcontainer.classList.add("active");
  scrollX = e.pageX - scroll.offsetLeft;
  scrollLeft = discountcontainer.scrollLeft;
});

// Mouse Move Function
discountcontainer.addEventListener("mousemove", (e) => {
  if (!isdown) return;
  e.preventDefault();
  var element = e.pageX - discountcontainer.offsetLeft;
  var scrolling = (element - scrollX) * 2;
  discountcontainer.scrollLeft = scrollLeft - scrolling;
});





//send mail to all

function sendMail() {
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

  const csrftoken = getCookie('csrftoken');

  let headers = {
    'Accept': 'application/json',
    'X-Requested-With': 'XMLHttpRequest', //Necessary to work with request.is_ajax()
    'X-CSRFToken': csrftoken,
  }


  fetch('sendemailtoall', {
    method: 'post',
    credentials: 'include',
    headers
  }).then(res =>{
    res.json().then(response=>{
      if (response.status ==='send'){
        Swal.fire({
  text: response.message,
  icon: "success"
});
      }

      if (response.status ==='not'){
        Swal.fire({
  text: response.message,
  icon: "error"
});
      }

    })
  })



}




function modify_order(pk){

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    const csrftoken = getCookie('csrftoken');
    let headers = {
        'Accept': 'application/json',
        'X-Requested-With': 'XMLHttpRequest', //Necessary to work with request.is_ajax()
        'X-CSRFToken': csrftoken,


    }

    fetch('modify_order_detail',{
 method: 'post',
        credentials: 'include',
        headers ,
        body : JSON.stringify({
           pk



        })
    }).then(res=>{
        res.json().then(response=>{
            if(response.status === 'del'){
                window.location.href='/user/profile'
            }
        })
    })

}










//top

var scrollToTopBtn = document.getElementById("scrollToTopBtn");

window.addEventListener("scroll", function() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    scrollToTopBtn.classList.add("show");
  } else {
    scrollToTopBtn.classList.remove("show");
  }
});

function scrollToTop() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}

