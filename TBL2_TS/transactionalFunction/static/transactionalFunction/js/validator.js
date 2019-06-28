var funcName = document.getElementById("id_functionalityName");
var funcType = document.getElementById("id_functionalityType");
var qttAlrs = document.getElementById("id_qtdALR");
var der = document.getElementById("id_qtdDER");
var serverCount = document.getElementById("id_countName");

var alrError = document.getElementById("alr-error");
var derError = document.getElementById("der-error");
var complexity = document.getElementById("id_complexity");
var points = document.getElementById("id_points");

funcType.addEventListener("change", fillComplexity);
qttAlrs.addEventListener("change", fillComplexity);
der.addEventListener("change", fillComplexity);

function validate(e, form){
  e.preventDefault();

  var error = false;
  var err = document.getElementById("error-message");

  fields = [funcName, funcType, qttAlrs, der, serverCount];

    //Insere erros de campos vazios
  for (i = 0; i < fields.length; i++){
    if(fields[i].value.length == 0){
      message = "Preencha todos os campos";
      fields[i].classList.add("error-field");
      error = true;
    }
    else{
      if(fields[i].classList.contains("error-field"))
        fields[i].classList.remove("error-field");
    }    
  }

  //insere erros se o valor do select for diferente do esperado
  if (!error && funcType.value != "EE" && funcType.value != "CE" && funcType.value != "SE"){
    funcType.classList.add("error-field");
    message = "Escolha um tipo entre EE, CE ou SE "
    error = true;
  }
  else if(!error){
    if(funcType.classList.contains("error-field"))
      funcType.remove("error-field");
  }

  if (!error && qttAlrs.value < 0){
    error = true;
    qttAlrs.classList.add("error-field");
    message = "Insira um valor maior ou igual a zero para a quantidade de ALR";
  }
  else if(!error){
    if (qttAlrs.classList.contains("error-field"))
      qttAlrs.classList.remove("error-field");
  }

  if (!error && der.value <= 0){
    error = true;
    der.classList.add("error-field");
    message = "Insira um valor maior que zero para a quantidade de DER";
  }
  else if(!error){
    if (der.classList.contains("error-field"))
      der.classList.remove("error-field");
  }

  if(error){
    err.innerHTML = message;    
  }
  else{
    var form = document.getElementById("form");
    form.submit();
  }
  
}

function fillPoints(){  
  if((complexity.value == "baixa" || complexity.value == "média" || complexity.value == "alta") && (funcType.value == "EE" || funcType.value == "CE" || funcType.value == "SE")) {
    points.value = calculatePoints(funcType.value, complexity.value);
  }
}

function fillComplexity(){  
  if(qttAlrs.value.length > 0 && qttAlrs.value < 0)
    alrError.innerHTML = "A quantidade mínima de ALR é 0";
  else
    alrError.innerHTML = "";  

  if(der.value.length > 0 && der.value <= 0)
    derError.innerHTML = "A quantidade mínima de DER é 1";  
  else
    derError.innerHTML = "";

  if(qttAlrs.value.length > 0 && der.value.length > 0 && funcType.value.length > 0 && qttAlrs.value >= 0 && der.value > 0){
    complexity.value = calculateComplexity(qttAlrs.value, der.value, funcType.value);
    fillPoints();
  }
  else{
    complexity.value = "";
    points.value = "";
  }
}

function calculatePoints(type, complexity){
  if (type == "EE" || type == "CE"){
    if(complexity == "baixa")
      return "3 PF";
    else if(complexity == "média")
      return "4 PF";
    else if(complexity == "alta")
      return "6 PF"
  }
  else if(type == "SE"){
    if(complexity == "baixa")
      return "4 PF";
    else if(complexity == "média")
      return "5 PF";
    else if(complexity == "alta")
      return "7 PF";
  }
}

function calculateComplexity(alr, der, functionality_type){
  var table = new Array(
    ["baixa", "baixa", "média"],
    ["baixa", "média", "alta"],
    ["média", "alta", "alta"]
  );  

  var qtd_der;
  var qtd_alr;

  if (functionality_type == "EE"){
    if (alr <= 1){
      qtd_alr = 0;
    }
    else if (alr == 2){
      qtd_alr = 1;
    }
    else if (alr >= 3){
      qtd_alr = 2;
    }

    console.log("DER: ." + der + ".");
    if (1 <= der && der <= 4){      
      qtd_der = 0;
    }
    else if (5 <= der && der <= 15){
      qtd_der = 1
    }
    else if (der >= 16){
      qtd_der = 2
    }

    console.log("Tipo: " + functionality_type + " qalr: " + qtd_alr + " qder: " + qtd_der + " : " + table[qtd_alr][qtd_der]);
  }

  else if (functionality_type == "CE"){
    if (alr <= 1){
      qtd_alr = 0
    }
    else if (2 <= alr && alr <= 3){
      qtd_alr = 1
    }
    else if (alr >= 4){
      qtd_alr = 2
    }

    if (1 <= der && der <= 4){
      qtd_der = 0
    }
    else if (5 <= der && der <= 19){
      qtd_der = 1
    }
    else if (der >= 20){
      qtd_der = 2
    }
  }
  else if (functionality_type == "SE"){
    if (alr <= 1){
      qtd_alr = 0
    }
    else if (2 <= alr && alr <= 3){
      qtd_alr = 1
    }
    else if (alr >= 4){
      qtd_alr = 2
    }

    if (1 <= der && der <= 5){
      qtd_der = 0
    }
    else if (6 <= der && der <= 19){
      qtd_der = 1
    }
    else if (der >= 20){
      qtd_der = 2
    }
  }

  

  return table[qtd_alr][qtd_der]
}