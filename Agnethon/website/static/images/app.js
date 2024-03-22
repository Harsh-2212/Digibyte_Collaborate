const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");
const sign_in_btn2 = document.querySelector("#sign-in-btn2");
const sign_up_btn2 = document.querySelector("#sign-up-btn2");
sign_up_btn.addEventListener("click", () => {
    container.classList.add("sign-up-mode");
});
sign_in_btn.addEventListener("click", () => {
    container.classList.remove("sign-up-mode");
});
sign_up_btn2.addEventListener("click", () => {
    container.classList.add("sign-up-mode2");
});
sign_in_btn2.addEventListener("click", () => {
    container.classList.remove("sign-up-mode2");
});

document.querySelectorAll('.btn').forEach(item => {
    item.addEventListener('click', event => {
        document.querySelector('.slider').style.transition = 'transform 0.3s';
        if (event.target.id === 'student-toggle') {
            document.querySelector('.slider').style.transform = 'translateX(100%)';
        } else {
            document.querySelector('.slider').style.transform = 'translateX(0%)';
        }
    });
});

function notify(type,message){
    (()=>{
        let n = document.createElement("div");
        let id = Math.random().toString(36).substring(2,10);
        n.setAttribute("id",id);
        n.classList.add("notification",type);
        document.getElementById("notification-area").appendChild(n);
        setTimeout(()=>{
            var notifications = document.getElementById("notification-area").getElementsByClassName("notify");
            for(let i = 0; i<notifications.length; i++){
                if(notifications[i].getAttribute("id")==id){
                    notifications[i].remove();
                    break;
                }
            }
        })
    })
}
