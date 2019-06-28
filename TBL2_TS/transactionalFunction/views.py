from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.db.models import Sum
from .models import TransactionalFunction
from .forms import TransactionFunctionForm

# Create your views here.
def getComplexity(functionality_type, qtd_alr, qtd_der):
    table = (['baixa', 'baixa', 'média'],
             ['baixa', 'média', 'alta'],
             ['média', 'alta', 'alta']
             )
    if functionality_type == 'EE':
        if qtd_alr <= 1:
            qtd_alr = 0
        elif qtd_alr == 2:
            qtd_alr = 1
        elif qtd_alr >= 3:
            qtd_alr = 2

        if 1 <= qtd_der <= 4:
            qtd_der = 0
        elif 5 <= qtd_der <= 15:
            qtd_der = 1
        elif qtd_der >= 16:
            qtd_der = 2

    elif functionality_type == 'CE':
        if qtd_alr <= 1:
            qtd_alr = 0
        elif 2 <= qtd_alr <= 3:
            qtd_alr = 1
        elif qtd_alr >= 4:
            qtd_alr = 2

        if 1 <= qtd_der <= 4:
            qtd_der = 0
        elif 5 <= qtd_der <= 19:
            qtd_der = 1
        elif qtd_der >= 20:
            qtd_der = 2

    elif functionality_type == 'SE':
        if qtd_alr <= 1:
            qtd_alr = 0
        elif 2 <= qtd_alr <= 3:
            qtd_alr = 1
        elif qtd_alr >= 4:
            qtd_alr = 2

        if 1 <= qtd_der <= 5:
            qtd_der = 0
        elif 6 <= qtd_der <= 19:
            qtd_der = 1
        elif qtd_der >= 20:
            qtd_der = 2

    return table[qtd_alr][qtd_der]


def getFunctionPoints(functionalityType, complexity):
    if functionalityType == 'EE' or functionalityType == 'CE':
        if complexity == 'baixa':
            pf = 3
        elif complexity == 'média':
            pf = 4
        elif complexity == 'alta':
            pf = 6
    elif functionalityType == 'SE':
        if complexity == 'baixa':
            pf = 4
        elif complexity == 'média':
            pf = 5
        elif complexity == 'alta':
            pf = 7
    return pf


class TransactionalFuncionCreate(View):
    def get(self, request):
        return render(request, 'create.html', {'form': TransactionFunctionForm()})

    def post(self, request):
        data = request.POST

        complexity = getComplexity(data['functionalityType'], int(data['qtdALR']), int(data['qtdDER']))
        function_points = getFunctionPoints(data['functionalityType'], complexity)

        tf = dict()
        tf['functionalityName'] = data['functionalityName']
        tf['functionalityType'] = data['functionalityType']
        tf['qtdALR'] = data['qtdALR']
        tf['qtdDER'] = data['qtdDER']
        tf['functionComplexity'] = complexity
        tf['qtdFunctionPts'] = function_points
        tf['countName'] = data['countName']
        form = TransactionFunctionForm(tf)
        if form.is_valid():
            form.save()
        return redirect('/')

class TransactionalFuncionList(View):
    def get(self, request):
        if (request.GET.get('type-filter') or request.GET.get('complexity-filter')):
            complexity_filter = request.GET.get('complexity-filter')
            type_filter = request.GET.get('type-filter')

            transactional_functions = TransactionalFunction.objects.all().order_by('functionalityType');

            if(type_filter != "todos"):
                transactional_functions = filter(lambda x: x.functionalityType == type_filter , transactional_functions)

            if(complexity_filter != "todas"):
                transactional_functions = filter(lambda x: x.functionComplexity == complexity_filter , transactional_functions)

        else:
            type_filter = " "
            complexity_filter = " "

            transactional_functions = TransactionalFunction.objects.all().order_by('functionalityType')


        sum_EE = 0
        sum_CE = 0
        sum_SE = 0
        for item in TransactionalFunction.objects.all():
            if(item.functionalityType == "EE"):
                sum_EE = sum_EE + item.qtdFunctionPts
            elif(item.functionalityType == "CE"):
                sum_CE = sum_CE + item.qtdFunctionPts
            elif(item.functionalityType == "SE"):
                sum_SE = sum_SE + item.qtdFunctionPts

        return render(request, 'list.html', dict(
            transactionalsFunctions = transactional_functions,
            typeFilter = type_filter,
            complexityFilter = complexity_filter,
            sumEE = sum_EE,
            sumCE = sum_CE,
            sumSE = sum_SE
        ))

class TransactionalFuncionShow(View):
    def get(self, request, pk):
        transactional_function = get_object_or_404(TransactionalFunction, pk = pk)
        return render(request, 'show.html', dict(transactionalFunction=transactional_function))
