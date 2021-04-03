
var contents = []

fetchData();

var contents = document.getElementById("contents")

function fetchData() {
  fetch('http://localhost:5000')
    .then(response => response.json())
    .then(data => displayContent(data))
    .catch( err => console.log(err))
}


function displayContent(data) {
  contents = data
  i=0
  for (var content of contents) {
    var button = document.createElement("button")
    button.id = i
    button.className = "content"
    button.innerText = content[1]
    button.addEventListener("click", copy)
    document.getElementById("contents").appendChild(button)
    i=i+1
  }
}

function copy() {
  var copyText = contents[this.id][1];
  var data = [new ClipboardItem({ "text/plain": new Blob([copyText], { type: "text/plain" }) })];
  navigator.clipboard.write(data).then(function() {
    console.log("Copied to clipboard successfully!");
    var x = document.getElementById("snackbar");
    x.className = "show";
    setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
  }, function() {
    console.error("Unable to write to clipboard. :-(");
    alert("error in copying")
  });
}
