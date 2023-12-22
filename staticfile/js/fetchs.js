// add comments

function add_commentt(id) {
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


    const email = document.getElementById('id_email').value
    const text = document.getElementById('id_text').value
    const rate = document.getElementById('rate').value
    const frm = document.getElementById('frm')


    fetch('/add_comments', {
        method: 'post',
        credentials: 'include',
        headers,
        body: JSON.stringify({
            email, text, id, rate
        })
    }).then(response => {
        frm.reset()
        response.json().then(res => {
                if (res.status === 'ok') {
                    Swal.fire({
                        text: res.message,
                        icon: "success"
                    });
                }
                if (res.status === 'no') {
                    Swal.fire({
                        text: res.message,
                        icon: "error"
                    });
                }
            }
        )

    })
}


function add_to_cart(pk) {
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


    const size = document.querySelector('input[name="options"]:checked').value
    const color = document.querySelector('input[name="color"]:checked').value
    const count=document.getElementById("counter").innerText



    fetch('/addtocart', {
        method: 'post',
        credentials: 'include',
        headers,
        body: JSON.stringify({
            pk, size, color,count
        })
    }).then(res => {
        res.json().then(response => {
            if (response.status === 'success') {
                Swal.fire({

                    text: response.message,
                    icon: "success"
                }).then(function() {
                     window.location = document.URL})

            }
            if (response.status === 'not_found') {
                Swal.fire({

                    text: response.message,
                    icon: "error"
                });
            }
            if (response.status === 'not_auth') {
                Swal.fire({

                    text: response.message,
                    icon: "error"
                });
            }

        })
    })
}


let counter = 1; // Start with 1 instead of 0

function updateCounter() {
    document.getElementById("counter").innerText = counter;
}

function increase() {
    counter++;
    updateCounter();
}

function decrease() {
    if (counter > 1) { // Ensure the counter doesn't go below 1
        counter--;
        updateCounter();
    }
  }




function signupData() {
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



    const name=document.getElementById("id_name").value
    const email=document.getElementById("id_email").value
    const phone_number=document.getElementById("id_phone_number").value
    const password=document.getElementById("id_password").value


    fetch('signup',{
         method: 'post',
        credentials: 'include',
        headers,
        body: JSON.stringify({
            email,name,phone_number,password
        })
    }).then(res=>{
       res.json().then(response=>{
           if (response.status === 'exist') {
                    Swal.fire({
                        text: response.message,
                        icon: "error"
                    });
                }
           if (response.status === 'user exist') {
                    Swal.fire({
                        text: response.message,
                        icon: "error"
                    });
                }
           if (response.status === 'send') {
                    Swal.fire({
                        text: response.message,
                        icon: "success"
                    });
                }
       })
    })

}