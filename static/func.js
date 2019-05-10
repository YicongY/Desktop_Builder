// submission
function submitCorpus() {
    document.getElementById("outputImg").style.display = "none";
    let intext = document.getElementById('inText').value;
    let selection = document.getElementById('selection').value;
    console.log(intext);
    console.log(selection);
    let xhr = new XMLHttpRequest();
    xhr.open("POST", "http://dmserv4.cs.illinois.edu:1111/remine", true);
    xhr.setRequestHeader('Content-Type', 'application/json')
    var sendText = JSON.parse('{ "text":"" }');
    sendText.text = intext;
    console.log(sendText);
    xhr.send(intext);
    xhr.onload = function (e) {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
              let data = JSON.parse(xhr.responseText).tuple;
              var list = document.createElement('ul');
              for(var i = 0; i < data.length; i++) {
                  var item = document.createElement('li');
                  item.appendChild(document.createTextNode(data[i]));
                  list.appendChild(item);
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


// button
var button_state = 0;
window.onload = function () {
    change_state();
    document.getElementById("b1").addEventListener("click", function() {
        button_state = 0;
        change_state();
    });
    document.getElementById("b2").addEventListener("click", function() {
        button_state = 1;
        change_state();
    });
    document.getElementById("b3").addEventListener("click", function() {
        button_state = 2;
        change_state();
    });

};

function change_state() {
    let bs = document.getElementsByClassName("buttons");
    for (let i = 0; i < bs.length; i++) {
        if (button_state === i) {
            bs[i].style.backgroundColor = "#F2F2F2";
            document.getElementById("intro_title").innerHTML = bs[i].innerHTML;
        } else {
            bs[i].style.backgroundColor = "white";
        }
    }
}

// JS for setting the "active" step class

// 'Next' buttons:
$(".next").click(function(){
  var oParent = $(this).closest(".step");
  setActiveStep(oParent.next());
});

// 'Back' buttons:
$(".back").click(function(){
  var oParent = $(this).closest(".step");
  setActiveStep(oParent.prev());
});


function setActiveStep(p_oDiv){
  
  // Set styles:  
  $(".step.active").removeClass("active");
 $(".step.inactive").removeClass("inactive");
  $(p_oDiv).addClass("active");
  $(p_oDiv).nextAll().addClass("inactive");

  // Scroll to active step:
    $('html, body').animate({
        scrollTop: $(p_oDiv).offset().top
    }, 500);
}

//Init the first step:
setActiveStep($(".step")[0]);