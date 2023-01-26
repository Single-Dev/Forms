let requests = document.querySelectorAll('#requests')
let response = document.getElementById('response')
if (requests && response) {
    if (requests.length > 0) { 
        document.head.querySelector('title').innerHTML = `notifications (${requests.length})`
    }
    else if (requests.length <= 0) {
        response.innerHTML = "<h1>Asosiy jild top toza!</h1>"
    }
}
