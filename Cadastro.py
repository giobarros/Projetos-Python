{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/giobarros/Projetos-Python/blob/main/Cadastro.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from datetime import datetime\n",
        "cadastro = dict()\n",
        "cadastro['Nome'] = str(input('Nome: '))\n",
        "idade = int(input('Ano de nascimento: '))\n",
        "ano = datetime.now().year\n",
        "cadastro['Idade'] = ano - idade\n",
        "ctps = int(input('Carteira de trabalho (digite 0 se não tiver): '))\n",
        "if ctps != 0:\n",
        "  cadastro['CTPS'] = ctps\n",
        "  cadastro['Contratação'] = int(input('Ano de contratação: '))\n",
        "  cadastro['Salário'] = float(input('Salário: R$'))\n",
        "  aposentadoria = cadastro['Idade'] + ((cadastro['Contratação'] + 35) - ano)\n",
        "  cadastro['Idade que irá se aposentar'] = aposentadoria\n",
        "else:\n",
        "  cadastro['CTPS'] = 'Não possui carteira de trabalho'\n",
        "print('-=-' * 20)\n",
        "for k, v in cadastro.items():\n",
        "  print('- {} tem o valor: {}'.format(k, v))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kQiokTbgn_l5",
        "outputId": "9b78c3d5-c283-4c7c-b01e-76a1f7f91ff3"
      },
      "execution_count": 64,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Nome: Giovanna\n",
            "Ano de nascimento: 2002\n",
            "Carteira de trabalho (digite 0 se não tiver): 123\n",
            "Ano de contratação: 2015\n",
            "Salário: R$2500\n",
            "-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-\n",
            "- Nome tem o valor: Giovanna\n",
            "- Idade tem o valor: 20\n",
            "- CTPS tem o valor: 123\n",
            "- Contratação tem o valor: 2015\n",
            "- Salário tem o valor: 2500.0\n",
            "- Idade que irá se aposentar tem o valor: 48\n"
          ]
        }
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyOHoPrlWUDDwevOCypp8yo9",
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}