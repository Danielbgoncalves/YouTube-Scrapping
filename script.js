const submitBtn = document.querySelector('#submit-btn');
let urlBox = document.querySelector('#playlist-url');
submitBtn.addEventListener('click', async ()=>{
    let url = urlBox.value;

    const response = await fetch('/api', {
        method: 'Post',
        headers: {
            'Content-Type':'application/json'
        },
        body:JSON.stringify({url:url})
    });

    if(response.ok){
        const result = await response.json();
        console.log(result);
    } else {
        const error = await response.json();
        console.error(error.message);
    }

});