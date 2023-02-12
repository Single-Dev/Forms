let requests = document.querySelectorAll('#requests')
let response = document.getElementById('response')
response.style.display = "none"
if (requests && response) {
    if (requests.length > 0) { 
        document.head.querySelector('title').innerHTML = `notifications (${requests.length})`
    }
    else if (requests.length <= 0) {
        response.style.display = "block"
    }
}
