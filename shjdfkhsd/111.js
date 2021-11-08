window.onload = function() {

    var times = document.querySelector(".times");
    var inner = times.getElementsByTagName("span");

    //设置定时器;
    var timer = null;

    function setTimer() {

        timer = setInterval(timesPlay, 1000);
    }
    setTimer();

    function cancleTimer() {

        clearInterval(timer);
    }

    //时间自动跳转函数;
    function timesPlay() {


        //结束时间;
        var endTime = new Date("2021/11/20 12:30:00");

        //现在时间;
        var now = new Date();

        //时间差:总的秒数(1000毫秒等于1秒);
        var lastTime = parseInt((endTime - now) / 1000);
        if (lastTime != 0) {

            //时间转换;
            var day = parseInt((lastTime / 60 / 60 / 24 % 24));
            var hour = parseInt((lastTime / 60 / 60 % 24));
            var min = parseInt((lastTime / 60 % 60));
            var sec = parseInt((lastTime % 60));
            //将获得的时分秒嵌入到相应的盒子中;
            inner[0].innerHTML = day;
            inner[1].innerHTML = hour;
            inner[2].innerHTML = min;
            inner[3].innerHTML = sec;
        } else {

            cancleTimer();
        }
    }
}