// submission
function firstsubmit() {
    let budget = document.getElementById('Budget').value;
    let purpose = document.getElementById('Purpose').value;
    console.log(budget);
    console.log(purpose);
    let xhr = new XMLHttpRequest();
    xhr.open("POST", "http://127.0.0.1:1111/first", true);
    xhr.setRequestHeader('Content-Type', 'application/json')
    let sendText = JSON.parse('{ "budget":"", "purpose":"" }');
    sendText.budget = budget;
    sendText.purpose = purpose;
    console.log(sendText);
    xhr.send(JSON.stringify(sendText));
    xhr.onload = function (e) {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
              console.log(JSON.parse(xhr.responseText));
              let data = JSON.parse(xhr.responseText).url;
              console.log(data);
              document.cookie = data.join('|');

              var list = document.createElement('ul');
              for(var i = 0; i < data.length; i++) {
                  var aTag = document.createElement('div');
                  var item = document.createElement('a');
                  item.appendChild(document.createTextNode(data[i]));
                  item.href = data[i];
                  aTag.appendChild(item);
                  list.appendChild(aTag);
              }
              document.getElementById("outText").appendChild(list);
              xhr.abort();
            } else {
              console.error(xhr.statusText);
              xhr.abort();
            }
        }
    };
}
function secondsubmit() {
    let budget = document.getElementById('Budget').value;
    let purpose = document.getElementById('Purpose').value;
    console.log(budget);
    console.log(purpose);
    let xhr = new XMLHttpRequest();
    xhr.open("POST", "http://127.0.0.1:1111/first", true);
    xhr.setRequestHeader('Content-Type', 'application/json')
    let sendText = JSON.parse('{ "budget":"", "purpose":"" }');
    sendText.budget = budget;
    sendText.purpose = purpose;
    console.log(sendText);
    xhr.send(JSON.stringify(sendText));
    xhr.onload = function (e) {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                console.log(JSON.parse(xhr.responseText));
                let data = JSON.parse(xhr.responseText).url;
                console.log(data);
                document.cookie = data.join('|');

                var list = document.createElement('ul');
                for(var i = 0; i < data.length; i++) {
                    var aTag = document.createElement('div');
                    var item = document.createElement('a');
                    item.appendChild(document.createTextNode(data[i]));
                    item.href = data[i];
                    aTag.appendChild(item);
                    list.appendChild(aTag);
                }
                document.getElementById("outText2").appendChild(list);
                xhr.abort();
            } else {
                console.error(xhr.statusText);
                xhr.abort();
            }
        }
    };
}
function thirdsubmit() {
    let budget = document.getElementById('Budget').value;
    let purpose = document.getElementById('Purpose').value;
    console.log(budget);
    console.log(purpose);
    let xhr = new XMLHttpRequest();
    xhr.open("POST", "http://127.0.0.1:1111/first", true);
    xhr.setRequestHeader('Content-Type', 'application/json')
    let sendText = JSON.parse('{ "budget":"", "purpose":"" }');
    sendText.budget = budget;
    sendText.purpose = purpose;
    console.log(sendText);
    xhr.send(JSON.stringify(sendText));
    xhr.onload = function (e) {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                console.log(JSON.parse(xhr.responseText));
                let data = JSON.parse(xhr.responseText).url;
                console.log(data);
                document.cookie = data.join('|');

                var list = document.createElement('ul');
                for(var i = 0; i < data.length; i++) {
                    var aTag = document.createElement('div');
                    var item = document.createElement('a');
                    item.appendChild(document.createTextNode(data[i]));
                    item.href = data[i];
                    aTag.appendChild(item);
                    list.appendChild(aTag);
                }
                document.getElementById("outText3").appendChild(list);
                xhr.abort();
            } else {
                console.error(xhr.statusText);
                xhr.abort();
            }
        }
    };
}
function forthsubmit() {
    let budget = document.getElementById('Budget').value;
    let purpose = document.getElementById('Purpose').value;
    console.log(budget);
    console.log(purpose);
    let xhr = new XMLHttpRequest();
    xhr.open("POST", "http://127.0.0.1:1111/first", true);
    xhr.setRequestHeader('Content-Type', 'application/json')
    let sendText = JSON.parse('{ "budget":"", "purpose":"" }');
    sendText.budget = budget;
    sendText.purpose = purpose;
    console.log(sendText);
    xhr.send(JSON.stringify(sendText));
    xhr.onload = function (e) {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                console.log(JSON.parse(xhr.responseText));
                let data = JSON.parse(xhr.responseText).url;
                console.log(data);
                document.cookie = data.join('|');

                var list = document.createElement('ul');
                for(var i = 0; i < data.length; i++) {
                    var aTag = document.createElement('div');
                    var item = document.createElement('a');
                    item.appendChild(document.createTextNode(data[i]));
                    item.href = data[i];
                    aTag.appendChild(item);
                    list.appendChild(aTag);
                }
                document.getElementById("outText4").appendChild(list);
                xhr.abort();
            } else {
                console.error(xhr.statusText);
                xhr.abort();
            }
        }
    };
}
function fifthsubmit() {
    let budget = document.getElementById('Budget').value;
    let purpose = document.getElementById('Purpose').value;
    console.log(budget);
    console.log(purpose);
    let xhr = new XMLHttpRequest();
    xhr.open("POST", "http://127.0.0.1:1111/first", true);
    xhr.setRequestHeader('Content-Type', 'application/json')
    let sendText = JSON.parse('{ "budget":"", "purpose":"" }');
    sendText.budget = budget;
    sendText.purpose = purpose;
    console.log(sendText);
    xhr.send(JSON.stringify(sendText));
    xhr.onload = function (e) {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                console.log(JSON.parse(xhr.responseText));
                let data = JSON.parse(xhr.responseText).url;
                console.log(data);
                document.cookie = data.join('|');

                var list = document.createElement('ul');
                for(var i = 0; i < data.length; i++) {
                    var aTag = document.createElement('div');
                    var item = document.createElement('a');
                    item.appendChild(document.createTextNode(data[i]));
                    item.href = data[i];
                    aTag.appendChild(item);
                    list.appendChild(aTag);
                }
                document.getElementById("outText5").appendChild(list);
                xhr.abort();
            } else {
                console.error(xhr.statusText);
                xhr.abort();
            }
        }
    };
}
function sixthsubmit() {
    let budget = document.getElementById('Budget').value;
    let purpose = document.getElementById('Purpose').value;
    console.log(budget);
    console.log(purpose);
    let xhr = new XMLHttpRequest();
    xhr.open("POST", "http://127.0.0.1:1111/first", true);
    xhr.setRequestHeader('Content-Type', 'application/json')
    let sendText = JSON.parse('{ "budget":"", "purpose":"" }');
    sendText.budget = budget;
    sendText.purpose = purpose;
    console.log(sendText);
    xhr.send(JSON.stringify(sendText));
    xhr.onload = function (e) {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                console.log(JSON.parse(xhr.responseText));
                let data = JSON.parse(xhr.responseText).url;
                console.log(data);
                document.cookie = data.join('|');

                var list = document.createElement('ul');
                for(var i = 0; i < data.length; i++) {
                    var aTag = document.createElement('div');
                    var item = document.createElement('a');
                    item.appendChild(document.createTextNode(data[i]));
                    item.href = data[i];
                    aTag.appendChild(item);
                    list.appendChild(aTag);
                }
                document.getElementById("outText6").appendChild(list);
                xhr.abort();
            } else {
                console.error(xhr.statusText);
                xhr.abort();
            }
        }
    };
}

function seventhsubmit() {
    let cpu_choice = parseInt(document.getElementById('cpu_select').value,10);
    console.log(cpu_choice);
    let xhr = new XMLHttpRequest();
    var json_str = document.cookie;
    var arr = json_str.split('|');
    console.log(arr);
    let url = document.arr[cpu_choice];
    console.log(url);

    xhr.open("POST", "http://127.0.0.1:1111/second", true);
    xhr.setRequestHeader('Content-Type', 'application/json')
    let sendText = JSON.parse('{ "url":""}');
    sendText.url = url;
    console.log(sendText);
    xhr.send(JSON.stringify(sendText));
    xhr.onload = function (e) {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
              console.log(JSON.parse(xhr.responseText));
              let data = JSON.parse(xhr.responseText).url;
              document.cookie = data;
              
              var list = document.createElement('ul');
              for(var i = 0; i < data.length; i++) {
                  var aTag = document.createElement('div');
                  var item = document.createElement('a');
                  item.appendChild(document.createTextNode(data[i]));
                  item.href = data[i];
                  aTag.appendChild(item);
                  list.appendChild(aTag);
              }
              document.getElementById("outText7").appendChild(list);
              xhr.abort();
            } else {
              console.error(xhr.statusText);
              xhr.abort();
            }
        }
    };
}


// // button
// var button_state = 0;
// window.onload = function () {
//     change_state();
//     document.getElementById("b1").addEventListener("click", function() {
//         button_state = 0;
//         change_state();
//     });
//     document.getElementById("b2").addEventListener("click", function() {
//         button_state = 1;
//         change_state();
//     });
//     document.getElementById("b3").addEventListener("click", function() {
//         button_state = 2;
//         change_state();
//     });

// };

// function change_state() {
//     let bs = document.getElementsByClassName("buttons");
//     for (let i = 0; i < bs.length; i++) {
//         if (button_state === i) {
//             bs[i].style.backgroundColor = "#F2F2F2";
//             document.getElementById("intro_title").innerHTML = bs[i].innerHTML;
//         } else {
//             bs[i].style.backgroundColor = "white";
//         }
//     }
// }
