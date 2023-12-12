// add comments

function add_commentt(id){
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

    let headers={
        'Accept': 'application/json',
        'X-Requested-With': 'XMLHttpRequest', //Necessary to work with request.is_ajax()
        'X-CSRFToken': csrftoken,
}



    const email =document.getElementById('id_email').value
    const text =document.getElementById('id_text').value
    const frm =document.getElementById('frm')



    fetch('/add_comments',{
         method: 'post',
        credentials: 'include',
        headers ,
        body : JSON.stringify({
           email,text,id
        })
    }).then(response=>{
        frm.reset()
        response.json().then(res=>{
            if (res.status === 'ok'){
                Swal.fire({
                    text: res.message,
                    icon: "success"
});
            }
             if (res.status === 'no'){
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

    let headers={
        'Accept': 'application/json',
        'X-Requested-With': 'XMLHttpRequest', //Necessary to work with request.is_ajax()
        'X-CSRFToken': csrftoken,
}







    fetch('/addtocart',{
         method: 'post',
        credentials: 'include',
        headers ,
        body : JSON.stringify({
       pk
        })
    }).then(res=>{
        res.json().then(response=>{
            if (response.status === 'success'){
                Swal.fire({

                  text: response.message,
                  icon: "success"
                });
            }
            if (response.status === 'not_found'){
                Swal.fire({

                  text: response.message,
                  icon: "error"
                });
            }
            if (response.status === 'not_auth'){
                Swal.fire({

                  text: response.message,
                  icon: "error"
                });
            }

        })
    })
}