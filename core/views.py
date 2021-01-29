from django.shortcuts import render
from .models import Question
from django.core.paginator import Paginator, EmptyPage, InvalidPage

pag_total = 10  # total de paginas que vai ter o quizz,
question_global = Question.objects.get_queryset().order_by('id')[:pag_total]
# objetos aleatorio,provavelmente to errando porque atualiza a
# pagina e aleatorio tbm
resposta_jogador = []  # resposta jogador
list_correta = []  # resposta correta
for e in question_global.values():  # lista das respostas correta
    list_correta.append(e['correta'])


def showquizz(request):
    objeto = question_global  # pego o total de objetos que quero aleatoriamente
    paginator = Paginator(objeto, 1)  # comeco na primeira pagina

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        questions = paginator.page(page)
    except(EmptyPage, InvalidPage):
        questions = paginator.page(paginator.num_pages)

    context = {
        'objeto': objeto,
        'questions': questions,
        'count': pag_total
    }
    return render(request, 'showquizz.html', context)


def resultado(request):
    score = 0
    if len(resposta_jogador) <= (len(list_correta)):  # caso a quantidade de resposta for igual ou menor a de perguntas
        for i in range(len(resposta_jogador)):
            if resposta_jogador[i] == list_correta[i]:  # comparo a resposta do jogador com a lista de resposta certa
                score += 1

    context = {
        'score': score,
        'resposta_jogador': resposta_jogador,
        'questions': question_global,

    }
    return render(request, 'resultado.html', context)


def save_ans(request):
    # if aqui eu pegar a resposta do usuário e a resposta da questao simutaneamente?
    ans = request.GET['ans']
    print("salvou resposta", ans)
    resposta_jogador.append(ans)  # aqui que salvo as resposta do jogador
    return render(request, 'showquizz.html')  # passo para o request a lista atualizada


def index(request):
    resposta_jogador.clear()
    return render(request, 'index.html')
