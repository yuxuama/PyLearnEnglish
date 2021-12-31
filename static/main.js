let datas;
var context = true;
var lessonContext = false;
var n = 0;

document.addEventListener('beforeinput', update);

function submit() {
    const number = document.getElementById("number").value;
    const theme = document.getElementById("theme").value;
    const explain = document.getElementById('status');

    if(n === '') {
        alert("Le paramètre du nombre d'élément n'est pas valide")
        return
    }

    if (!lessonContext) {
        explain.innerHTML = "Tu as choisit le thème: " + theme;
        lessonContext = true;
        lesson(number , theme);
    }
}

async function lesson(number , theme) {
    promise = $.ajax({
        url: 'http://127.0.0.1:8080/get' + number + "&" + theme,
        type: 'GET',
        DataType: 'json',
        headers: {'Access-Control-Allow-Origin': '*'},
    });
    datas = await promise;
    update(
        {target: {id: NaN}},
        true
    );
}

function update(event, initial=false) {
    // Update the container of the lesson whenever the enter key is pressed in the input context
    if (event.target.id === 'answer' && event.inputType === "insertLineBreak" && lessonContext && !initial){
        const target = document.getElementById('word');
        const counter = document.getElementById('counter');
        document.getElementById('answer').value = '';
        
        if (n >= datas.length) {
            document.getElementById('status').innerHTML = '';
            counter.innerHTML = ''
            lessonContext = false;
            n = 0;
            target.innerHTML = "Tu as finis la scéance d'entrainement";
            return;
        }

        if (context) {
            target.innerHTML = "Traduis: " + datas[n].word;
            counter.innerHTML = (n+1).toString() + '/' + datas.length;
            context = false;
        } else {
            target.innerHTML = "La traduction est: " + datas[n].trad;
            context = true;
            n++;
        }
    }

    else if (initial) {
        const target = document.getElementById('word');
        const counter = document.getElementById('counter');
        counter.innerHTML = (n+1).toString() + '/' + datas.length;
        target.innerHTML = "Traduis: " + datas[n].word;
        context = false;
    }
}