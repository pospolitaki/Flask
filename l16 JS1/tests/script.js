/*var  a = prompt('enter first number');
var  b = prompt('enter second number');

function calcSum(a, b) {
    return (+a + +b);
};

alert( calcSum(a, b) )*/

/*var a = prompt('input number');
function getDecimal(number) {
    listOfIntegerAndDicimal = String(number).split('.');
    integer = listOfIntegerAndDicimal[0];
    decimal = parseFloat(listOfIntegerAndDicimal[1]);
    var result = 0;

    if (isFinite(decimal)) {
      result = '0.' + decimal;
    }

    return result;
  };
*/
  
/*    function ucFirst(word) {
        var upperChar = word.charAt(0).toUpperCase() 
        var result = ''
        if ( upperChar ) {
            result = upperChar + word.slice(1,) 
            }
            return result
    }
var word = prompt('type the word here')
alert( ucFirst(word) );

    function checkSpam(text) {
        var textToCheck = text.toLowerCase()
        return !!( ~textToCheck.indexOf('viagra') || ~textToCheck.indexOf('xxx') )
    }
*/

//Создайте функцию isEmpty(obj), которая возвращает true, если в объекте нет свойств и false – если хоть одно свойство есть.

/*function isEmpty(obj) {
    var counter = 0;
    for (i in obj) {
        counter++;
    }
    return (!counter)
}*/

//Есть объект salaries с зарплатами. Напишите код, который выведет сумму всех зарплат.

/*function summarizeSalary(salaries) {
    var result = 0;
    for (var persone in salaries) {
        result += salaries[persone];
    }
}*/

/*var obj = {
    className: 'open menu'
  }

function addClass(obj, cls) {
    var classes = obj.className ? obj.className.split(' ') : [];
    for ( var i = 0; i < classes.length; i++) {
        if ( classes[i] ==cls ) return;
    }
    classes.push(cls);
    obj.className = classes.join(' ');
} */

/*var arr = ["Есть", "жизнь", "на", "Марсе"];

var arrLength = arr.map(function(word) {
    return word.length;
})/*
//выведите 1, если первый аргумент есть, и 0 - если нет
 /*function checkFirsArg(x){
    if ( arguments[0] ) return console.log(1);
    return 0; 
 }

 function checkFirsArg1(x) {
     console.log(arguments.length ? 1 : 0)
 }*/

/*function summarizeArgs() {
    var sum = 0
    if (arguments.length) {
        for (var i = 0; i < arguments.length; i++) {
           sum += arguments[i] 
        }
    }
    console.log(sum)
}*/

/*function getWeekDay(date) {
    var days = ['vs', 'pn', 'vt', 'sr', 'cht', 'ptn', 'sb']
    return days[date.getDay()]
}

function getWeekDay1(date) {
    console.log(today.toLocaleString('ru', {weekday:'short'}))
}*/

/*function Calculator() {
    this.read = function() {
        this.firstNumber = prompt('Enter first number',0)
        this.secondNumber = prompt('Enter second number',0)
    };
    this.sum = function() {
        alert (+this.firstNumber + +this.secondNumber)
    }
}
var calculator = new Calculator;
calculator.read();
calculator.sum();
*/

/*function Calculator() {
    
    var methods = {
        '+' : function(a,b) {
            return a + b;
        },
        '-' : function(a,b) {
            return a - b; 
        }
    };
    this.calculate = function(str) {
        var elements = str.split(' ');
        var a = +elements[0];
        var op = elements[1];
        var b = +elements[2];

        if (!methods[op] || isNaN(a) || isNaN(b)) {
            return NaN;
        }
        alert(methods[op](a,b))
        return methods[op](a,b);
    }
    this.addMethod = function (op, func) {
        methods[op] = func;
        alert('Added! Thanks!');
    };

}
var clc = new Calculator();
clc.addMethod("*", function(a, b) {
    return a * b;
  });
clc.calculate(prompt('enter string'));*/
/*function User(fullName) {
    this.fullName = fullName;
    Object.defineProperties(this, {
        firstName: {get: function() {
            return this.fullName.split(' ')[0];
        },
        set: function(name){
            this.fullName = name + ' ' + this.lastName;
        }
    },
        lastName: {
            get: function(){
                return this.fullName.split(' ')[1];
            },
            set: function(name){
                this.fullName = this.firstName + ' ' + name;
            }
        }

    });
}
*/

/*function Article() {
    if (isFinite(Article.count)) {
        Article.count++;
    } else {
        Article.count = 1;
    }
    Article.created = new Date();
    //this.created = new Date();
    Article.showStats = function() {
        return 'Всего: ' + Article.count + ', Последняя: ' + Article.created;
    };
}*/
/*
function sum(arr) {
    return arr.reduce(function(a, b) {
      return a + b;
    });
  }

  function sumArgs() {
    arguments.reduce = [].reduce;
    return arguments.reduce(function(a,b){return a + b;});
}

function sumArgs() {
    return [].reduce.call(arguments,function(a,b){return a + b;});
}*/
/*function applyAll() {
    var args = [].slice.call(arguments,1);
    console.log(args);
    func = arguments[0];
    return func.apply(this, args);
}
function applyAll(func) {
    console.log(func);
    console.log(arguments);
    return arguments[0].apply(this, [].slice.call(arguments, 1));
  }*/

 /* function work(a) {
      console.log(a);
  }
  function makeLogging(f, log){
    function wrapper(a){
        log.push(a);
        return f.call(this, a);
      } 
    return wrapper;
  }*/

  /*function f(x) {
    return Math.random() * x; // random для удобства тестирования
  }

  function makeCaching(f) {
  var cache = {};

  return function(x) {
    if (!(x in cache)) {
      cache[x] = f.call(this, x);
    }
    return cache[x];
  };

  }*/

function FormatError(message) {
SyntaxError.apply(this, arguments);
this.name = 'FormatError';
this.message = message;
if (Error.captureStackTrace) {
    Error.captureStackTrace(this, this.constructor);
} else {
    this.stack = (new Error()).stack;
}
}

FormatError.prototype = Object.create(SyntaxError.prototype);
FormatError.prototype.constructor = FormatError;

