let datas;
var context = true;
var lessonContext = false;
var n = 0;

document.addEventListener('keypress', update)

function submit() {
    const number = document.getElementById("number").value;
    const theme = document.getElementById("theme").value;
    const explain = document.getElementById('status');

    explain.innerHTML = "Appuie sur 'Entrée' quand tu penses avoir trouvé"
    lessonContext = true
    lesson(number , theme);
}

async function lesson(number , theme) {
    promise = $.ajax({
        url: 'http://127.0.0.1:8080/get' + number + "&" + theme,
        type: 'GET',
        DataType: 'json',
        headers: {'Access-Control-Allow-Origin': '*'},
    });
    datas = await promise
    console.log(datas[0])
    update(13)
}

function update(event) {
    if (event.keyCode === 13 || event === 13 && lessonContext){
        const target = document.getElementById('word');
        if (n > datas.length) {
            lessonContext = false;
            n = 0;
            target.innerHTML = "Tu as finis la scéance d'entrainement"
        }

        if (context) {
            target.innerHTML = "Traduis: " + datas[n].word;
            context = false;
        } else {
            target.innerHTML = "La traduction est: " + datas[n].trad;
            context = true;
            n++;
        }
    }

}