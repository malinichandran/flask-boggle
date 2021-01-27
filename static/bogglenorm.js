function startgame(){
    let secs = 60;
let score = 0;
let words = new Set();

/*function showWord(word){
   let res= $(".words").append('<li>'+word+'</li>');
   return res;
}

function showScore(){
    return $(".score").text(score);
}

function showMessage(msg, cls){
   return $(".msg").text(msg).removeClass().addClass(`msg ${cls}`);
}

function showTimer(){
    return $(".timer").text(secs)
}



async function tick(){
 secs = secs-1
 showTimer();
 if(secs === 0){
     clearInterval(timer);
    await gameScore()
 }
}

let timer= setInterval(() => {
    tick()
}, 1000);

$(".add-word").on("submit", async function handleSubmit(evt){
    evt.preventDefault();
    let word = (".word").val()

    if(!word){
        return
    }
    if(words.has(word)){
        showMessage(`This ${word} already exists`, "err")
    }

    const resp = await axios.get("/check-word",{word:word})
    if(resp.data.result === "not-word"){
        showMessage(`${word} is not a valid english word`)
    } else if (resp.data.result === "not-on-board"){
        showMessage(`${word} does not exist on the board`)
    } else {
        showWord(word);
        score += word.length;
        showScore();
        words.add(word);
        showMessage(`${word} Added`,"ok")
    }
    $word.val("").focus();
})

async function gameScore() {
    $(".add-word").hide();
    const resp = await axios.post("/post-score", { score: score });
    if (resp.data.brokeRecord) {
      showMessage(`New record: ${score}`, "ok");
    } else {
      showMessage(`Final score: ${score}`, "ok");
    }
  
}*/
}
startgame();
