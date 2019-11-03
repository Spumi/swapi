let closeButtons = document.querySelector(".close-button").addEventListener("click", closeModal);

function closeModal(e){
    document.querySelector(".modal-bg").style.display = 'none';
}


function openModal(e){
    document.querySelector(".modal-bg").style.display = 'flex';
}


document.querySelector("#test").addEventListener("click", openModal)


function  setModalContent(response){
    document.querySelector("#modalConent").innerHTML = response;
    openModal();
}


 function sendForm(index){
        var xhr = new XMLHttpRequest();
        params = new FormData();
        params.append('index', index);

        xhr.onreadystatechange = function() {
            if (xhr.readyState == XMLHttpRequest.DONE) {
                setModalContent(xhr.response)
                // alert(xhr.response)
            }
        }
        xhr.open('POST', '/residents', true);
        xhr.send(params);
    };
