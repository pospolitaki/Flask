
   'use strict';
   /* alert( 'Первый кролик!' );
    var s = prompt('hallo', 'kirill');
    prompt('hallo');
    alert(s);*/
    //var answer = (confirm('Are you here?')) ? 'glad to see you here' : 'it\'s a pitty';
    /*var answer = prompt('tell me a num','') ;
    var message = (answer<10) ? 'small one' : (answer<30) ? 'big enough' : 'huge!!!' ;
    alert(message)*/
    //var a = prompt('your number', 4);
    /*if(a == 'IE') {
        alert('О, да у вас IE!');
      } else if (browser == 'Chrome'
       || browser == 'Firefox'
       || browser == 'Safari'
       || browser == 'Opera') {
        alert('Да, и эти браузеры мы поддерживаем');
      } else {
        alert('Мы надеемся, что и в вашем браузере все ок!');
      }*/
    /*switch (+a) {
        case 0: 
            alert(0);
            break
        case 1:
            alert(1);
            break;
        case 2:
        case 3:
            alert('2,3');
            break;
    }*/
/*    function checkAge(age) {
    return (age > 18) ? true : confirm('Родители разрешили?');
    }
    checkAge(+a);   
    alert(checkAge(+a))
*/

function ask(question, yes, no) {
    if (confirm(question)) yes()
    else no()
}
var q = 'are you agree?'
function sayOk() {
    alert('Thats great!')
}
function sayNo(){
    alert('oho...')
}

var mult = new Function('a,b', 'return a+b');

ask(q, sayOk, sayNo);
alert(mult(1,2));

    /*switch (+a) {
        case 4:
          alert('Верно!');
          break;
      
        case 3:                    // (*)
        case 5:                    // (**)
          alert('Неверно!');
          alert('Немного ошиблись, бывает.');
          break;
      
        default:
          alert('Странный результат, очень странный');
      }*/
  