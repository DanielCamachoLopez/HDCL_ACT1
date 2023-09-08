{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMUVX+CO+2GrWifrk1cXlNm",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/DanielCamachoLopez/HDCL_ACT1/blob/main/HDCL_ACT4_README.md\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#ACTIVIDAD 4\n",
        "\n",
        "Nombre: Hector Daniel Camacho Lopez\n",
        "\n",
        "Matricula: 372239\n",
        "\n",
        "Grupo: 432\n",
        "\n",
        "Fecha: 04 de Septiembre del 2023"
      ],
      "metadata": {
        "id": "DbcgcR3DGyHs"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "1-Algoritmo que lee 3 calificaciones y calcula el promedio del alumno, desplegando un mensaje"
      ],
      "metadata": {
        "id": "s5tnH0QJI9Lp"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 279
        },
        "id": "zhYMEWDeGxJv",
        "outputId": "dc6c3b41-219b-49c3-c7df-13e415361375"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Cual es la primera calificacion del alumno? Calificacion entera del 1 al 100: -20\n",
            "ERROR, ingrese un numero entre el 0 y el 100\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "TypeError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-4-2f52ff3acbc3>\u001b[0m in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      2\u001b[0m     \u001b[0mcali1\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Cual es la primera calificacion del alumno? Calificacion entera del 1 al 100: \"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0mcali1\u001b[0m \u001b[0;34m<\u001b[0m \u001b[0;36m0\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0mcali1\u001b[0m \u001b[0;34m>\u001b[0m \u001b[0;36m100\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 4\u001b[0;31m       \u001b[0;32mraise\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"ERROR, ingrese un numero entre el 0 y el 100\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      5\u001b[0m     \u001b[0mcali2\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Cual es la segunda calificacion del alumno? Calificacion entera del 1 al 100: \"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      6\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0mcali2\u001b[0m \u001b[0;34m<\u001b[0m \u001b[0;36m0\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0mcali2\u001b[0m \u001b[0;34m>\u001b[0m \u001b[0;36m100\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mTypeError\u001b[0m: exceptions must derive from BaseException"
          ]
        }
      ],
      "source": [
        "try:\n",
        "    cali1 = int(input(\"Cual es la primera calificacion del alumno? Calificacion entera del 1 al 100: \"))\n",
        "    if cali1 < 0 or cali1 > 100:\n",
        "      raise print(\"ERROR, ingrese un numero entre el 0 y el 100\")\n",
        "    cali2 = int(input(\"Cual es la segunda calificacion del alumno? Calificacion entera del 1 al 100: \"))\n",
        "    if cali2 < 0 or cali2 > 100:\n",
        "      raise print(\"ERROR, ingrese un numero entre el 0 y el 100\")\n",
        "    cali3 = int(input(\"Cual es la tercera calificacion del alumno? Calificacion entera del 1 al 100: \"))\n",
        "    if cali3 < 0 or cali3 > 100:\n",
        "      raise print(\"ERROR, ingrese un numero entre el 0 y el 100\")\n",
        "    prom = (cali1 + cali2 + cali3) / 3\n",
        "except ValueError:\n",
        "    print(\"ERROR, los numeros ingresados deben ser ENTEROS, NO letras ni caracteres especiales\")\n",
        "\n",
        "else:\n",
        "    if prom < 30:\n",
        "        print(\"Repetir\")\n",
        "    elif prom < 60:\n",
        "        print(\"Extraordinario\")\n",
        "    elif prom < 70:\n",
        "        print(\"Suficiente\")\n",
        "    elif prom < 80:\n",
        "        print(\"Regular\")\n",
        "    elif prom < 90:\n",
        "        print(\"bien\")\n",
        "    elif prom <= 98:\n",
        "        print(\"Muy bien\")\n",
        "    elif prom <= 100:\n",
        "        print(\"Excelente\")\n",
        "    elif prom > 100:\n",
        "        print(\"ERRORR de promedio\")\n"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "2.Algoritmo que calcula el salario semanal de un trabajador dependiendo de las horas trabajadas y el salario por hora"
      ],
      "metadata": {
        "id": "NP0o4lXoQEp3"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "try:\n",
        "    hora = int(input(\"Cuantas horas trabajo en la semana?\"))\n",
        "    if hora < 0:\n",
        "        raise print(\"Solo numeros positivos\")\n",
        "    salhora = float(input(\"Cuanto gana por hora?\"))\n",
        "    if salhora < 0:\n",
        "        raise print(\"Solo numeros positivos\")\n",
        "    if hora <= 40:\n",
        "      salario = hora * salhora\n",
        "      print(f\"Salario por hora: {salhora}\")\n",
        "      print(f\"Salario normal: {salario}\")\n",
        "      print(\"Salario extra: Sin salario extra\")\n",
        "      print(f\"Salario Total: {salario}\")\n",
        "    elif hora <= 49:\n",
        "      salnorm = 40 * salhora\n",
        "      horaex = hora - 40\n",
        "      salext = salhora * horaex * 2\n",
        "      salario = salnorm + salext\n",
        "      print(f\"Salario por hora: {salhora}\")\n",
        "      print(f\"Salario normal: {salnorm}\")\n",
        "      print(f\"Salario extra: {salext}\")\n",
        "      print(f\"Salario Total: {salario}\")\n",
        "    elif hora > 49:\n",
        "      salnorm = 40 * salhora\n",
        "      salext = 9 * salhora * 2\n",
        "      horaext = hora - 49\n",
        "      salext3 = horaext * salhora * 3\n",
        "      salario = salnorm + salext + salext3\n",
        "      print(f\"Salario por hora: {salhora}\")\n",
        "      print(f\"Salario normal: {salnorm}\")\n",
        "      print(f\"Salario extra: {salext + salext3}\")\n",
        "      print(f\"Salario Total: {salario}\")\n",
        "except ValueError:\n",
        "    print(\"ERROR, digite numeros, no letras ni caracteres especiales\")"
      ],
      "metadata": {
        "id": "CBUVgXMuQLCn",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "e1b23662-cb6d-45a6-829c-245e37e36c58"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Cuantas horas trabajo en la semana?37\n",
            "Cuanto gana por hora?jwodj\n",
            "ERROR, digite numeros, no letras ni caracteres especiales\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "3.Algoritmo que calcula el total a pagar por consumo de agua dependiendo de los m3 de agua"
      ],
      "metadata": {
        "id": "eypJGi6RtOeS"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "try:\n",
        "    m3 = int(input(\"Cuantos m3 de agua se consumieron?\"))\n",
        "    if m3 < 0:\n",
        "        raise print(\"Solo numeros positivos\")\n",
        "\n",
        "    if m3 <= 4:\n",
        "      subt = 50 / 1.16\n",
        "      iva = subt * 0.16\n",
        "      print(f\"Subtotal: {subt} pesos\")\n",
        "      print(f\"Iva: {iva} pesos\")\n",
        "      print(f\"Total: 50 pesos\")\n",
        "    elif m3 <= 15:\n",
        "      subt = (m3 * 8) / 1.16\n",
        "      iva = subt * 0.16\n",
        "      total = subt + iva\n",
        "      print(f\"Subtotal: {subt} pesos\")\n",
        "      print(f\"Iva: {iva} pesos\")\n",
        "      print(f\"Total: {total} pesos\")\n",
        "    elif m3 <= 50:\n",
        "      subt = (m3 * 10) / 1.16\n",
        "      iva = subt * 0.16\n",
        "      total = subt + iva\n",
        "      print(f\"Subtotal: {subt} pesos\")\n",
        "      print(f\"Iva: {iva} pesos\")\n",
        "      print(f\"Total: {total} pesos\")\n",
        "    elif m3 > 50:\n",
        "      subt = (m3 * 11) / 1.16\n",
        "      iva = subt * 0.16\n",
        "      total = subt + iva\n",
        "      print(f\"Subtotal: {subt} pesos\")\n",
        "      print(f\"Iva: {iva} pesos\")\n",
        "      print(f\"Total: {total} pesos\")\n",
        "except:\n",
        "    print(\"ERROR, digite numeros, no letras ni caracteres especiales\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "G0dq3cM9tpv3",
        "outputId": "88eed452-b885-489a-b479-a0ca961860bd"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Cuantos m3 de agua se consumieron?-2\n",
            "Solo numeros positivos\n",
            "ERROR, digite numeros, no letras ni caracteres especiales\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "4.Algoritmo que calcula el promedio final de la materia en base a 5 examenes, de los cuales el mas bajo se anula y se promedia con los otros 4"
      ],
      "metadata": {
        "id": "Ud23bVGYw0pP"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "try:\n",
        "    cal1 = int(input(\"Dame la primera calificacion. Calificacion entera del 1 al 100:\"))\n",
        "    if cal1 < 0 or cal1 > 100:\n",
        "        raise print(\"ERROR, solo numeros entre el 0 y el 100\")\n",
        "    cal2 = int(input(\"Dame la segunda calificacion. Calificacion entera del 1 al 100: \"))\n",
        "    if cal2 < 0 or cal2 > 100:\n",
        "        raise print(\"ERROR, solo numeros entre el 0 y el 100\")\n",
        "    cal3 = int(input(\"Dame la tercera calificacion. Calificacion entera del 1 al 100: \"))\n",
        "    if cal3 < 0 or cal3 > 100:\n",
        "        raise print(\"ERROR, solo numeros entre el 0 y el 100\")\n",
        "    cal4 = int(input(\"Dame la cuarta calificacion. Calificacion entera del 1 al 100: \"))\n",
        "    if cal4 < 0 or cal4 > 100:\n",
        "        raise print(\"ERROR, solo numeros entre el 0 y el 100\")\n",
        "    cal5 = int(input(\"Dame la quinta calificacion: \"))\n",
        "    if cal5 < 0 or cal5 > 100:\n",
        "        raise print(\"ERROR, solo numeros entre el 0 y el 100\")\n",
        "    menor = cal1\n",
        "    if menor > cal2:\n",
        "        menor = cal2\n",
        "    if menor > cal3:\n",
        "        menor = cal3\n",
        "    if menor > cal4:\n",
        "        menor = cal4\n",
        "    if menor > cal5:\n",
        "        menor = cal5\n",
        "    prom = (cal1 + cal2 + cal3 + cal4 + cal5 - menor) / 4\n",
        "    print(f\"El promedio del alumno es: {prom}\")\n",
        "except:\n",
        "    print(\"ERROR, digite numeros ENTEROS, no letras ni caracteres especiales\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BBgCuQ6JxDOv",
        "outputId": "42bd4931-0144-4eb3-adf4-6fff14090dc9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Dame la primera calificacion: -1\n",
            "ERROR, solo numeros entre el 0 y el 100\n",
            "ERROR, digite numeros ENTEROS, no letras ni caracteres especiales\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "5.Algoritmo que sirve para jugar CHINCHAMPU (piedra, papel, tijera) para 1 jugador y la computadora"
      ],
      "metadata": {
        "id": "zXCupGuAzwCY"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "try:\n",
        "    import random\n",
        "    print(\"1)Piedra\")\n",
        "    print(\"2)Papel\")\n",
        "    print(\"3)Tijera\")\n",
        "    jug1 = int(input(\"Bienvenido jugador 1. Escoja piedra, papel o tijera ingresando el numero correspondiente: \"))\n",
        "    if jug1 <= 0 or jug1 > 3:\n",
        "      raise print(\"Solo numeros 1, 2 o 3... No es tan dificil\")\n",
        "\n",
        "    x = random.randint(1,3)\n",
        "    if jug1 == 1:\n",
        "      if x == 1:\n",
        "        print(\"EMPATE\")\n",
        "      else:\n",
        "        if x == 2:\n",
        "          print(\"Jugador 2 gana\")\n",
        "          print(\"Piedra pierde contra papel\")\n",
        "        else:\n",
        "          print(\"Jugador 1 gana\")\n",
        "          print(\"Piedra le gana a tijera\")\n",
        "    if jug1 == 2:\n",
        "      if x == 2:\n",
        "        print(\"EMPATE\")\n",
        "      else:\n",
        "        if x == 3:\n",
        "          print(\"Jugador 2 gana\")\n",
        "          print(\"Papel pierde contra tijera\")\n",
        "        else:\n",
        "          print(\"Jugador 1 gana\")\n",
        "          print(\"Papel le gana a piedra\")\n",
        "    if jug1 == 3:\n",
        "      if x == 3:\n",
        "        print(\"EMPATE\")\n",
        "      else:\n",
        "        if x == 1:\n",
        "          print(\"Jugador 2 gana\")\n",
        "          print(\"Tijera pierde contra piedra\")\n",
        "        else:\n",
        "          print(\"Jugador 1 gana\")\n",
        "          print(\"Tijera le gana a papel\")\n",
        "except:\n",
        "    print(\"ERROR, digite los numeros ENTEROS, no letras ni caracteres especiales\")\n"
      ],
      "metadata": {
        "id": "Rsp-mogi0iGn",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "b0a9eb7d-a410-4221-e7ce-8af4434bb795"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1)Piedra\n",
            "2)Papel\n",
            "3)Tijera\n",
            "Bienvenido jugador 1. Escoja piedra, papel o tijera ingresando el numero correspondiente: -1\n",
            "Solo numeros 1, 2 o 3... No es tan dificil\n",
            "ERROR, digite los numeros ENTEROS, no letras ni caracteres especiales\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "6.- Programa en Python que lea 4 números enteros desplegar cuales el menor, cual es mayor"
      ],
      "metadata": {
        "id": "wm_HWvKH2-Kx"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "try:\n",
        "    num1 = float(input(\"Dame el primer numero: \"))\n",
        "    num2 = float(input(\"Dame el segundo numero: \"))\n",
        "    num3 = float(input(\"Dame el tercer numero: \"))\n",
        "    num4 = float(input(\"Dame el cuarto numero: \"))\n",
        "    menor = num1\n",
        "    if menor > num2:\n",
        "      menor = num2\n",
        "    if menor > num3:\n",
        "      menor = num3\n",
        "    if menor > num4:\n",
        "      menor = num4\n",
        "    print(f\"El numero menor es: {menor}\")\n",
        "    mayor = num1\n",
        "    if mayor < num2:\n",
        "        mayor = num2\n",
        "    if mayor > num3:\n",
        "      mayor = num3\n",
        "    if mayor > num4:\n",
        "      mayor = num4\n",
        "    print(f\"El numero mayor es: {mayor}\")\n",
        "except:\n",
        "    print(\"ERROR, digite solo numeros, no letras ni caracteres especiales.\")\n"
      ],
      "metadata": {
        "id": "zh-RyOvX3CKn",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "75ac7a2f-660d-43b5-9dca-c47f001f9ec3"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Dame el primer numero: idhdew\n",
            "ERROR, digite solo numeros, no letras ni caracteres especiales.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "7.- Programa en Python que sirva para calcular el área de un triangulo, los datos de entrada deben ser forzosamente de tipo real"
      ],
      "metadata": {
        "id": "THPVcUHh6wdu"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "try:\n",
        "    base = input(\"Cual es la base del triangulo? Solo numeros con decimales: \")\n",
        "    altura = float(input(\"Cual es la altura del triangulo? Solo numeros con decimales: \"))\n",
        "    area = (base * altura) / 2\n",
        "except:\n",
        "    print(\"ERROR, digite numero, no letras ni caracteres especiales.\")\n",
        "else:\n",
        "    area = (base * altura) / 2\n",
        "    print(f\"La area del triangulo es de: {area}\")\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ai6pkdWT62Q8",
        "outputId": "a6731afe-d43e-461a-bb40-c3973d877a59"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Cual es la base del triangulo? Solo numeros con decimales: 3\n",
            "Cual es la altura del triangulo? Solo numeros con decimales: fhien\n",
            "ERROR, digite numero, no letras ni caracteres especiales.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "8.-Programa en Python que sirva para calcular el área de un circulo"
      ],
      "metadata": {
        "id": "fYONov20GqEi"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "try:\n",
        "  radio = float(input(\"Dame el radio del circulo\"))\n",
        "  if radio < 0:\n",
        "    raise print(\"ERROR, solo numeros positivos\")\n",
        "  area = 3.14 * pow(radio,2)\n",
        "  print(f\"El area del circulo es: {area}\")\n",
        "except:\n",
        "  print(\"ERROR, ingresa numeros, NO letras ni caracteres especiales\")"
      ],
      "metadata": {
        "id": "5bDBAYt8HmUO",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "19c21950-ba05-418d-c035-079681490980"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Dame el radio del circulo-34\n",
            "ERROR, solo numeros positivos\n",
            "ERROR, ingresa numeros, NO letras ni caracteres especiales\n"
          ]
        }
      ]
    }
  ]
}