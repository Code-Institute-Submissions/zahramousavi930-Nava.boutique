function add_commentt(e) {
    let t = {
        Accept: "application/json",
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": (function (e) {
            let t = null;
            if (document.cookie && "" !== document.cookie) {
                const n = document.cookie.split(";");
                for (let o = 0; o < n.length; o++) {
                    const c = n[o].trim();
                    if (c.substring(0, e.length + 1) === e + "=") {
                        t = decodeURIComponent(c.substring(e.length + 1));
                        break;
                    }
                }
            }
            return t;
        })("csrftoken"),
    };
    const n = document.getElementById("id_email").value,
        o = document.getElementById("id_text").value,
        c = document.getElementById("rate").value,
        s = document.getElementById("frm");
    fetch("/add_comments", { method: "post", credentials: "include", headers: t, body: JSON.stringify({ email: n, text: o, id: e, rate: c }) }).then((e) => {
        s.reset(),
            e.json().then((e) => {
                "ok" === e.status && Swal.fire({ text: e.message, icon: "success" }), "no" === e.status && Swal.fire({ text: e.message, icon: "error" });
            });
    });
}
function add_to_cart(e) {
    let t = {
        Accept: "application/json",
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": (function (e) {
            let t = null;
            if (document.cookie && "" !== document.cookie) {
                const n = document.cookie.split(";");
                for (let o = 0; o < n.length; o++) {
                    const c = n[o].trim();
                    if (c.substring(0, e.length + 1) === e + "=") {
                        t = decodeURIComponent(c.substring(e.length + 1));
                        break;
                    }
                }
            }
            return t;
        })("csrftoken"),
    };
    const n = document.querySelector('input[name="options"]:checked').value,
        o = document.querySelector('input[name="color"]:checked').value,
        c = document.getElementById("counter").innerText;
    fetch("/order/addtocart", { method: "post", credentials: "include", headers: t, body: JSON.stringify({ pk: e, size: n, color: o, count: c }) }).then((e) => {
        e.json().then((e) => {
            "success" === e.status &&
                Swal.fire({ text: e.message, icon: "success" }).then(function () {
                    window.location = document.URL;
                }),
                "not_found" === e.status && Swal.fire({ text: e.message, icon: "error" }),
                "not_auth" === e.status && Swal.fire({ text: e.message, icon: "error" });
        });
    });
}
let counter = 1;
function updateCounter() {
    document.getElementById("counter").innerText = counter;
}
function increase() {
    counter++, updateCounter();
}
function decrease() {
    counter > 1 && (counter--, updateCounter());
}
function signupData() {
    const e = (function (e) {
        let t = null;
        if (document.cookie && "" !== document.cookie) {
            const n = document.cookie.split(";");
            for (let o = 0; o < n.length; o++) {
                const c = n[o].trim();
                if (c.substring(0, e.length + 1) === e + "=") {
                    t = decodeURIComponent(c.substring(e.length + 1));
                    break;
                }
            }
        }
        return t;
    })("csrftoken");
    let t = { Accept: "application/json", "X-Requested-With": "XMLHttpRequest", "X-CSRFToken": e };
    const n = document.getElementById("id_name").value,
        o = document.getElementById("id_email").value,
        c = document.getElementById("id_phone_number").value,
        s = document.getElementById("id_password").value;
    fetch("signup", { method: "post", credentials: "include", headers: t, body: JSON.stringify({ email: o, name: n, phone_number: c, password: s }) }).then((e) => {
        e.json().then((e) => {
            "exist" === e.status && Swal.fire({ text: e.message, icon: "error" }), "user exist" === e.status && Swal.fire({ text: e.message, icon: "error" }), "send" === e.status && Swal.fire({ text: e.message, icon: "success" });
        });
    });
}




function recovery_apssword(){
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

    let   headers={
        'Accept': 'application/json',
        'X-Requested-With': 'XMLHttpRequest', 
        'X-CSRFToken': csrftoken,
}


    const user_email =document.getElementById('id_email').value
     console.log(user_email)



    fetch('/user/forget-pass/', {
        method: 'post',
        credentials: 'include',
        headers ,
        body : JSON.stringify({
            user_email
        })
      }).then(response=>{
          response.json().then(res=>{

                  if(res.status === 'user_not_exist'){
                      const Toast = Swal.mixin({
                    toast: true,
                    position: 'top-end',
                    showConfirmButton: false,
                    timer: 5000,
                    timerProgressBar: true,
                    didOpen: (toast) => {
                        toast.addEventListener('mouseenter', Swal.stopTimer)
                        toast.addEventListener('mouseleave', Swal.resumeTimer)
                    }
                })

                        Toast.fire({
                    icon: 'error',
                    title: res.message
                })


                  }

                  if(res.status === 'error'){
                    const Toast = Swal.mixin({
                  toast: true,
                  position: 'top-end',
                  showConfirmButton: false,
                  timer: 5000,
                  timerProgressBar: true,
                  didOpen: (toast) => {
                      toast.addEventListener('mouseenter', Swal.stopTimer)
                      toast.addEventListener('mouseleave', Swal.resumeTimer)
                  }
              })

                      Toast.fire({
                  icon: 'error',
                  title: res.message
              })


                }

                  if(res.status ==='ok'){
                      const Toast = Swal.mixin({
                    toast: true,
                    position: 'top-end',
                    showConfirmButton: false,
                    timer: 5000,
                    timerProgressBar: true,
                    didOpen: (toast) => {
                        toast.addEventListener('mouseenter', Swal.stopTimer)
                        toast.addEventListener('mouseleave', Swal.resumeTimer)
                    }
                })

                        Toast.fire({
                    icon: 'success',
                    title: res.message
                })
                  }

              }) })
}
