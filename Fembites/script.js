/*global $*/
$(document).ready(function(){

    var carson1 = new Audio("audios/ben.mp3"); 
    var carson2 = new Audio("audios/Ben1.mp3");
    var obama = new Audio("audios/obamapig.mp3");
    var trump1 = new Audio("audios/trump1.mp3");
    var trump2 = new Audio("audios/trump.mp3"); 
    var trump3 = new Audio("audios/trump3.mp3");
    var trump4 = new Audio("audios/trump4.mp3");
    var kasich = new Audio("audios/kasich.mp3");
    var cruz1 = new Audio("audios/cruz.mp3");
    var cruz2 = new Audio("audios/cruz2.mp3");
    var huckabee1 = new Audio("audios/huckabee.mp3");
    var huckabee2 = new Audio("audios/Huckabee1.mp3");
   
    var tAudio= [trump1, trump2, trump3, trump4];
    var cAudio = [cruz1, cruz2];
    var hAudio = [huckabee1, huckabee2];
    var carAudio = [carson1, carson2];
    
    function rIndex(array){
        var min = 0;
        var max = array.length-1;
        var rindex = Math.floor(Math.random()*(max-min+1)+min);
        return rindex;
    }
    
    /*
    $("#button").on("click", function(){
    
    });     
    */
    
    $(".iBorder").click(function(){
        var idClicked = this.id;
        $("p").html(idClicked);
        
        if (idClicked == "teddy") {
            var cruz = cAudio[rIndex(cAudio)];
            
            if (cruz.paused)
                cruz.play();
            else
                cruz.pause();
        } 
        else if (idClicked =="amnesiac") {
            var carson = carAudio[rIndex(carAudio)];
            if (carson.paused)
                 carson.play();
            else
                carson.pause();
        } 
        else if (idClicked == "kasich") {
            if (kasich.paused)
                 kasich.play();
            else
                kasich.pause();
        } 
        else if (idClicked == "drumpf") {
           var trump = tAudio[rIndex(tAudio)];
            if (trump.paused)
                 trump.play();
            else
                trump.pause();
        } 
        else if (idClicked == "obama") {
            if (obama.paused)
                 obama.play();
            else
                obama.pause();
        }
        else if (idClicked == "huckabee"){
            var huckabee = hAudio[rIndex(hAudio)];
            if (huckabee.paused)
                huckabee.play();
            else 
                huckabee.pause();
    
        }
        
    });
    
    var horns = new Audio("audios/mlghorns.mp3");
    
    $("button").click(function(){
         horns.play();
         
         $(".angrytext").html("SILENCE MISOGYNY!!!");
         setTimeout(function() {
         $(".angrytext").fadeOut().empty();
        }, 4000);
    });


    
});
