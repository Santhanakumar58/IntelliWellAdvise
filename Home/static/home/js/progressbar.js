let file = document.getElementById("excel_upload");
let button = document.getElementsByTagName("button");
let progress = document.querySelector("progress");
let p_i = document.querySelector('.progress-indicator');
let load=0;
let process ="";
console.log(filename);

file.oninput = ()=>{
    let filename = file.files[0].name;
    let extension = filename.split('.').pop();
    let filesize=file.files[0].size;
    console.log ('hello');
    if (filesize <=1000000){
        filesize= (filesize/1000).toFixed(2) + 'kb';
    }
    if (filesize ==1000000 || filesize <= 1000000000){
        filesize= (filesize/1000000).toFixed(2) + 'mb';
    }
    if (filesize ==1000000000 || filesize <= 1000000000000){
        filesize= (filesize/1000000000).toFixed(2) + 'gb';
    }

    document.querySelector('label').innerText = filename;
    document.querySelector('.ex').innerText = extension;
    document.querySelector('.size').innerText = filesize;

    console.log ('.ex');
    console.log ('.size');
    }
