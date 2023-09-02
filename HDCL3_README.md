{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM+ljekfCmM1pWEb7MsB7pD",
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
        "<a href=\"https://colab.research.google.com/github/DanielCamachoLopez/HDCL_ACT1/blob/main/HDCL3_README.md\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#ACTIVIDAD 3\n",
        "\n",
        "Nombre: Hector Daniel Camacho Lopez\n",
        "\n",
        "Matricula: 372239\n",
        "\n",
        "Grupo: 432\n",
        "\n",
        "Fecha: 28 de Agosto de 2023"
      ],
      "metadata": {
        "id": "bnfJ9EJJEKBS"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "1. Algoritmo que lee 3 calificaciones y calcula el promedio del alumno, desplegando un mensaje"
      ],
      "metadata": {
        "id": "fsXth30XEfzh"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GuKtPDxSD_So",
        "outputId": "76857499-ec02-443b-853a-0f1a9c0262a8"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Cual es la primera calificacion del alumno?98\n",
            "Cual es la segunda calificacion del alumno?98\n",
            "Cual es la tercera calificacion del alumno?98\n",
            "Muy bien\n"
          ]
        }
      ],
      "source": [
        "cali1 = int(input(\"Cual es la primera calificacion del alumno?\"))\n",
        "cali2 = int(input(\"Cual es la segunda calificacion del alumno?\"))\n",
        "cali3 = int(input(\"Cual es la tercera calificacion del alumno?\"))\n",
        "prom = (cali1 + cali2 + cali3) / 3\n",
        "if prom < 30:\n",
        "  print(\"Repetir\")\n",
        "elif prom < 60:\n",
        "  print(\"Extraordinario\")\n",
        "elif prom < 70:\n",
        "  print(\"Suficiente\")\n",
        "elif prom < 80:\n",
        "  print(\"Regular\")\n",
        "elif prom < 90:\n",
        "  print(\"bien\")\n",
        "elif prom <= 98:\n",
        "  print(\"Muy bien\")\n",
        "elif prom <= 100:\n",
        "  print(\"Excelente\")\n",
        "elif prom > 100:\n",
        "  print(\"ERRORR de promedio\")\n"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "2.Algoritmo que calcula el salario semanal de un trabajador dependiendo de las horas trabajadas y el salario por hora"
      ],
      "metadata": {
        "id": "cWhBmyq7EqGg"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "hora = int(input(\"Cuantas horas trabajo en la semana?\"))\n",
        "salhora = float(input(\"Cuanto gana por hora?\"))\n",
        "if hora <= 40:\n",
        "  salario = hora * salhora\n",
        "  print(f\"Salario por hora: {salhora}\")\n",
        "  print(f\"Salario normal: {salario}\")\n",
        "  print(\"Salario extra: Sin salario extra\")\n",
        "  print(f\"Salario Total: {salario}\")\n",
        "elif hora <= 49:\n",
        "  salnorm = 40 * salhora\n",
        "  horaex = hora - 40\n",
        "  salext = salhora * horaex * 2\n",
        "  salario = salnorm + salext\n",
        "  print(f\"Salario por hora: {salhora}\")\n",
        "  print(f\"Salario normal: {salnorm}\")\n",
        "  print(f\"Salario extra: {salext}\")\n",
        "  print(f\"Salario Total: {salario}\")\n",
        "elif hora > 49:\n",
        "  salnorm = 40 * salhora\n",
        "  salext = 9 * salhora * 2\n",
        "  horaext = hora - 49\n",
        "  salext3 = horaext * salhora * 3\n",
        "  salario = salnorm + salext + salext3\n",
        "  print(f\"Salario por hora: {salhora}\")\n",
        "  print(f\"Salario normal: {salnorm}\")\n",
        "  print(f\"Salario extra: {salext + salext3}\")\n",
        "  print(f\"Salario Total: {salario}\")\n"
      ],
      "metadata": {
        "id": "GctZA2doE2pR"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "3.Algoritmo que despliega el total de una llamada telefonica dependiendo de los minutos y el tipo de llamada"
      ],
      "metadata": {
        "id": "qqz-PIdSE3Mo"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"1) Llamada local\")\n",
        "print(\"2) Llamada nacional\")\n",
        "print(\"3) Llamada internacional\")\n",
        "tipo = int(input(\"Que tipo de llamada se realizara? Digita el numero correspondiente: \"))\n",
        "min = int(input(\"Cuantos minutos durara la llamada?\"))\n",
        "if tipo == 1:\n",
        "  subt = 3 / 1.16\n",
        "  iva = subt * 0.16\n",
        "  print(f\"Subtotal: {subt} pesos\")\n",
        "  print(f\"Iva:{iva} pesos\")\n",
        "  print(\"Total: 3 pesos\")\n",
        "elif tipo == 2:\n",
        "  minex = min - 3\n",
        "  extra = minex * 2\n",
        "  subt = (7 + extra) / 1.16\n",
        "  iva = subt * 0.16\n",
        "  total = subt + iva\n",
        "  print(f\"Subtotal: {subt} pesos\")\n",
        "  print(f\"Iva: {iva} pesos\")\n",
        "  print(f\"Total: {total} pesos\")\n",
        "elif tipo == 3:\n",
        "  minex = min - 2\n",
        "  extra = minex * 4\n",
        "  subt = (9 + extra) / 1.16\n",
        "  iva = subt * 0.16\n",
        "  total = subt + iva\n",
        "  print(f\"Subtotal: {subt} pesos\")\n",
        "  print(f\"Iva: {iva} pesos\")\n",
        "  print(f\"Total: {total} pesos\")\n"
      ],
      "metadata": {
        "id": "R-EXBt3UFEVo",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "29b5415d-ad4a-4628-a0fc-4b4d9ce31c9f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1) Llamada local\n",
            "2) Llamada nacional\n",
            "3) Llamada internacional\n",
            "Que tipo de llamada se realizara? Digita el numero correspondiente: 3\n",
            "Cuantos minutos durara la llamada?2\n",
            "Subtotal: 7.758620689655173 pesos\n",
            "Iva: 1.2413793103448276 pesos\n",
            "Total: 9.0 pesos\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "4.Algoritmo que calcula el total a pagar por consumo de agua dependiendo de los m3 de agua"
      ],
      "metadata": {
        "id": "rD8fORqrFFBh"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "m3 = int(input(\"Cuantos m3 de agua se consumieron?\"))\n",
        "if m3 <= 4:\n",
        "  subt = 50 / 1.16\n",
        "  iva = subt * 0.16\n",
        "  print(f\"Subtotal: {subt} pesos\")\n",
        "  print(f\"Iva: {iva} pesos\")\n",
        "  print(f\"Total: 50 pesos\")\n",
        "elif m3 <= 15:\n",
        "  subt = (m3 * 8) / 1.16\n",
        "  iva = subt * 0.16\n",
        "  total = subt + iva\n",
        "  print(f\"Subtotal: {subt} pesos\")\n",
        "  print(f\"Iva: {iva} pesos\")\n",
        "  print(f\"Total: {total} pesos\")\n",
        "elif m3 <= 50:\n",
        "  subt = (m3 * 10) / 1.16\n",
        "  iva = subt * 0.16\n",
        "  total = subt + iva\n",
        "  print(f\"Subtotal: {subt} pesos\")\n",
        "  print(f\"Iva: {iva} pesos\")\n",
        "  print(f\"Total: {total} pesos\")\n",
        "elif m3 > 50:\n",
        "  subt = (m3 * 11) / 1.16\n",
        "  iva = subt * 0.16\n",
        "  total = subt + iva\n",
        "  print(f\"Subtotal: {subt} pesos\")\n",
        "  print(f\"Iva: {iva} pesos\")\n",
        "  print(f\"Total: {total} pesos\")\n"
      ],
      "metadata": {
        "id": "SlZEGnnXFY14",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "21925257-1ae6-4bfd-95e2-241b2da5c49d"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Cuantos m3 de agua se consumieron?15\n",
            "Subtotal: 103.44827586206897 pesos\n",
            "Iva: 16.551724137931036 pesos\n",
            "Total: 120.0 pesos\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "5.Algoritmo que calcula el promedio final de la materia en base a 5 examenes, de los cuales el mas bajo se anula y se promedia con los otros 4"
      ],
      "metadata": {
        "id": "OLN-kGw2FZYo"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "cal1 = int(input(\"Dame la primera calificacion: \"))\n",
        "cal2 = int(input(\"Dame la segunda calificacion: \"))\n",
        "cal3 = int(input(\"Dame la tercera calificacion: \"))\n",
        "cal4 = int(input(\"Dame la cuarta calificacion: \"))\n",
        "cal5 = int(input(\"Dame la quinta calificacion: \"))\n",
        "menor = cal1\n",
        "if menor > cal2:\n",
        "  menor = cal2\n",
        "if menor > cal3:\n",
        "  menor = cal3\n",
        "if menor > cal4:\n",
        "  menor = cal4\n",
        "if menor > cal5:\n",
        "  menor = cal5\n",
        "prom = (cal1 + cal2 + cal3 + cal4 + cal5 - menor) / 4\n",
        "print(f\"El promedio del alumno es: {prom}\")\n"
      ],
      "metadata": {
        "id": "Xhy_3tSXFy2n",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "fcbc591e-5a57-4377-f622-e0b33e3148b6"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Dame la primera calificacion: 20\n",
            "Dame la segunda calificacion: 50\n",
            "Dame la tercera calificacion: 10\n",
            "Dame la cuarta calificacion: 30\n",
            "Dame la quinta calificacion: 40\n",
            "El promedio del alumno es: 35.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "6.Algoritmo que sirve para jugar CHINCHAMPU (piedra, papel, tijera) para 1 jugador y la computadora (usando condicion anidada)"
      ],
      "metadata": {
        "id": "Xi9G6rdWFzNg"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import random\n",
        "print(\"1)Piedra\")\n",
        "print(\"2)Papel\")\n",
        "print(\"3)Tijera\")\n",
        "jug1 = int(input(\"Bienvenido jugador 1. Escoja piedra, papel o tijera ingresando el numero correspondiente: \"))\n",
        "x = random.randint(1,3)\n",
        "if jug1 == 1:\n",
        "  if x == 1:\n",
        "    print(\"EMPATE\")\n",
        "  else:\n",
        "    if x == 2:\n",
        "      print(\"Jugador 2 gana\")\n",
        "      print(\"Piedra pierde contra papel\")\n",
        "    else:\n",
        "      print(\"Jugador 1 gana\")\n",
        "      print(\"Piedra le gana a tijera\")\n",
        "if jug1 == 2:\n",
        "  if x == 2:\n",
        "    print(\"EMPATE\")\n",
        "  else:\n",
        "    if x == 3:\n",
        "      print(\"Jugador 2 gana\")\n",
        "      print(\"Papel pierde contra tijera\")\n",
        "    else:\n",
        "      print(\"Jugador 1 gana\")\n",
        "      print(\"Papel le gana a piedra\")\n",
        "if jug1 == 3:\n",
        "  if x == 3:\n",
        "    print(\"EMPATE\")\n",
        "  else:\n",
        "    if x == 1:\n",
        "      print(\"Jugador 2 gana\")\n",
        "      print(\"Tijera pierde contra piedra\")\n",
        "    else:\n",
        "      print(\"Jugador 1 gana\")\n",
        "      print(\"Tijera le gana a papel\")\n"
      ],
      "metadata": {
        "id": "SN3PvCJYGGIv",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "fed02972-e471-49bf-d949-df62f91ed079"
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1)Piedra\n",
            "2)Papel\n",
            "3)Tijera\n",
            "Bienvenido jugador 1. Escoja piedra, papel o tijera ingresando el numero correspondiente: 2\n",
            "Jugador 2 gana\n",
            "Papel pierde contra tijera\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "7.Algoritmo que sirve para jugar CHINCHAMPU (piedra, papel, tijera) para 1 jugador y la computadora (usando seleccion multiple)"
      ],
      "metadata": {
        "id": "JrRbJzZ_GGwX"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import random\n",
        "print(\"1)Piedra\")\n",
        "print(\"2)Papel\")\n",
        "print(\"3)Tijera\")\n",
        "jug1 = int(input(\"Bienvenido jugador 1. Escoja piedra, papel o tijera ingresando el numero correspondiente: \"))\n",
        "x = random.randint(1,3)\n",
        "if jug1 == 1:\n",
        "  if x == 1:\n",
        "    print(\"EMPATE\")\n",
        "  elif x == 2:\n",
        "    print(\"Jugador 2 gana\")\n",
        "    print(\"Piedra pierde contra papel\")\n",
        "  elif x == 3:\n",
        "    print(\"Jugador 1 gana\")\n",
        "    print(\"Piedra le gana a tijera\")\n",
        "if jug1 == 2:\n",
        "  if x == 2:\n",
        "    print(\"EMPATE\")\n",
        "  elif x == 3:\n",
        "    print(\"Jugador 2 gana\")\n",
        "    print(\"Papel pierde contra tijera\")\n",
        "  elif x == 1:\n",
        "    print(\"Jugador 1 gana\")\n",
        "    print(\"Papel le gana a piedra\")\n",
        "if jug1 == 3:\n",
        "  if x == 3:\n",
        "    print(\"EMPATE\")\n",
        "  elif x == 1:\n",
        "      print(\"Jugador 2 gana\")\n",
        "      print(\"Tijera pierde contra piedra\")\n",
        "  elif x == 2:\n",
        "    print(\"Jugador 1 gana\")\n",
        "    print(\"Tijera le gana a papel\")\n"
      ],
      "metadata": {
        "id": "0PhjaEooGQMP",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "ebeb42d8-ca4b-44dc-854b-2b05ca11ac01"
      },
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1)Piedra\n",
            "2)Papel\n",
            "3)Tijera\n",
            "Bienvenido jugador 1. Escoja piedra, papel o tijera ingresando el numero correspondiente: 2\n",
            "Jugador 1 gana\n",
            "Papel le gana a piedra\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "8.Algoritmo que calcula el precio a pagar por un cliente en una tienda de electronica, tomando en cuenta los descuentos correspondientes"
      ],
      "metadata": {
        "id": "SzJ1-v0ZGQe_"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"1) Computadora\")\n",
        "print(\"2) Television\")\n",
        "print(\"3) Consola de videojuegos\")\n",
        "opc = int(input(\"Que desea comprar? Seleccione el numero correspondiente a su decision: \"))\n",
        "if opc == 1:\n",
        "  comp = float(input(\"Deme el precio de la computadora: \"))\n",
        "  adicion = int(input(\"Desea comprar tambien una impresosa? Escriba 1 si asi lo desea o 2 si no le interesa:\"))\n",
        "  if adicion == 1:\n",
        "    imp = float(input(\"Cual es el precio de la impresora? \"))\n",
        "    descomp = comp * .05\n",
        "    comptotal = comp - descomp\n",
        "    descimp = imp * .10\n",
        "    imptotal = imp - descimp\n",
        "    preciofin = comptotal + imptotal\n",
        "    print(f\"Total por computadora: {comptotal}\")\n",
        "    print(f\"Total de impresora: {imptotal}\")\n",
        "    print(f\"Total de la compra: {preciofin}\")\n",
        "  else:\n",
        "    descomp = comp * .05\n",
        "    comptotal = comp - descomp\n",
        "    print(f\"Total por computadora: {comptotal}\")\n",
        "    print(f\"Total de la compra: {comptotal}\")\n",
        "elif opc == 2:\n",
        "  tv = float(input(\"Deme el precio de la television: \"))\n",
        "  adicion = int(input(\"Desea comprar tambien una barra de sonido? Escriba 1 si asi lo desea o 2 si no le interesa: \"))\n",
        "  if adicion == 1:\n",
        "    barra = float(input(\"Cual es el precio de la barra de sonido?\"))\n",
        "    desctv = tv * .07\n",
        "    tvtotal = tv - desctv\n",
        "    descbarra = barra * .15\n",
        "    bartotal = barra - descbarra\n",
        "    preciofin = tvtotal + bartotal\n",
        "    print(f\"Total television: {tvtotal}\")\n",
        "    print(f\"Total de barra de sonido: {bartotal}\")\n",
        "    print(f\"Total de la compra: {preciofin}\")\n",
        "  else:\n",
        "    desctv = tv * .07\n",
        "    tvtotal = tv - desctv\n",
        "    print(f\"Total por television: {tvtotal}\")\n",
        "    print(f\"Total de la compra: {tvtotal}\")\n",
        "elif opc == 3:\n",
        "  cons = float(input(\"Deme el precio de la consola de videojuegos: \"))\n",
        "  adicion = int(input(\"Desea comprar tambien un juego? Escriba 1 si asi lo desea o 2 si no le interesa: \"))\n",
        "  if adicion == 1:\n",
        "    juego = float(input(\"Cual es el precio del juego? \"))\n",
        "    descons = cons * .10\n",
        "    constotal = cons - descons\n",
        "    desjuego = juego * .20\n",
        "    juegotot = juego - desjuego\n",
        "    preciofin = constotal + juegotot\n",
        "    print(f\"Total por la consola de videojuegos: {constotal}\")\n",
        "    print(f\"Total por el juego: {juegotot}\")\n",
        "    print(f\"Total de la compra: {preciofin}\")\n",
        "  else:\n",
        "    descons = cons * .10\n",
        "    constotal = cons - descons\n",
        "    print(f\"Total por la consola de videojuegos: {constotal}\")\n",
        "    print(f\"Total de la compra: {constotal}\")\n"
      ],
      "metadata": {
        "id": "hfUcWKnLGcBw",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "5c68c134-fec4-485c-b2fa-3df62050a867"
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1) Computadora\n",
            "2) Television\n",
            "3) Consola de videojuegos\n",
            "Que desea comprar? Seleccione el numero correspondiente a su decision: 1\n",
            "Deme el precio de la computadora: 20\n",
            "Desea comprar tambien una impresosa? Escriba 1 si asi lo desea o 2 si no le interesa:1\n",
            "Cual es el precio de la impresora? 30\n",
            "Total por computadora: 19.0\n",
            "Total de impresora: 27.0\n",
            "Total de la compra: 46.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "9.Algoritmo que calcula el precio a pagar por un cliente en una tienda de ropa, tomando en cuenta los descuentos correspondientes"
      ],
      "metadata": {
        "id": "tREpEDGUGcb2"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"1) Verano\")\n",
        "print(\"2) Invierno\")\n",
        "print(\"3) Primavera\")\n",
        "print(\"4) Otoño\")\n",
        "opci = int(input(\"En que temporada se encuentra? Ingrese un numero dependiendo de su eleccion:\"))\n",
        "if opci == 1:\n",
        "  precio = float(input(\"Deme el precio del articulo: \"))\n",
        "  desc = precio * .20\n",
        "  preciot = precio - desc\n",
        "  print(f\"El precio total es: {preciot}\")\n",
        "elif opci == 2:\n",
        "  precio = float(input(\"Deme el precio del articulo: \"))\n",
        "  print(\"1) Roja\")\n",
        "  print(\"2) Verde\")\n",
        "  print(\"3) No tiene/otra\")\n",
        "  etiq = int(input(\"De que color es la etiqueta del artuclo? Ingrese el numero correspondiente a su respuesta: \"))\n",
        "  if etiq == 1:\n",
        "    desc = precio * .30\n",
        "    preciot = precio - desc\n",
        "    print(f\"El precio total es: {preciot}\")\n",
        "  elif etiq == 2:\n",
        "    desc = precio * .15\n",
        "    preciot = precio - desc\n",
        "    print(f\"El precio total es: {preciot}\")\n",
        "  else:\n",
        "    print(f\"El precio total es: {precio}\")\n",
        "else:\n",
        "  precio = float(input(\"Deme el precio del articulo: \"))\n",
        "  print(\"1 )Amarilla\")\n",
        "  print(\"2) No tiene/otra\")\n",
        "  etiq = int(input(\"De que color es la etiqueta del artuclo? Ingrese el numero correspondiente a su respuesta: \"))\n",
        "  if etiq == 1:\n",
        "    desc = precio * .10\n",
        "    preciot = precio - desc\n",
        "    print(f\"El precio total es: {preciot}\")\n",
        "  else:\n",
        "    print(f\"El precio total es: {precio}\")\n",
        "\n"
      ],
      "metadata": {
        "id": "e9Pup2u9Gt2O",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "cc271d96-d2e4-417a-c5fd-2cd2c1a3b6b5"
      },
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1) Verano\n",
            "2) Invierno\n",
            "3) Primavera\n",
            "4) Otoño\n",
            "En que temporada se encuentra? Ingrese un numero dependiendo de su eleccion:2\n",
            "Deme el precio del articulo: 200\n",
            "1) Roja\n",
            "2) Verde\n",
            "3) No tiene/otra\n",
            "De que color es la etiqueta del artuclo? Ingrese el numero correspondiente a su respuesta: 1\n",
            "El precio total es: 140.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "10.Algoritmo que calcula el precio a pagar por un cliente en un restaurante, tomando en cuenta los descuentos correspondientes"
      ],
      "metadata": {
        "id": "CLyp7xlDGuIO"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"1) Lunes\")\n",
        "print(\"2) Martes\")\n",
        "print(\"3) Miercoles\")\n",
        "print(\"4) Jueves\")\n",
        "print(\"5) Viernes\")\n",
        "print(\"6) Sabado\")\n",
        "print(\"7) Domingo\")\n",
        "dia = int(input(\"Buen dia, en que dia de la semana de encuentra hoy? Ingrese el numero correspondiente: \"))\n",
        "print(\"1) Menu del dia\")\n",
        "print(\"2) Menu infantil\")\n",
        "print(\"3) Menu vegetariano\")\n",
        "print(\"4) Menu del chef\")\n",
        "print(\"5) Otro menu\")\n",
        "menu = int(input(\"Cual menu desea pedir hoy? Ingrese el numero correspondiente:  \"))\n",
        "menup = float(input(\"Cual es el precio de dicho menu? \"))\n",
        "if dia == 1:\n",
        "  if menu == 1:\n",
        "    descmenu = menup * .10\n",
        "    menupt = menup - descmenu\n",
        "    print(f\"El precio total es: {menupt}\")\n",
        "  else:\n",
        "    print(f\"El precio total es: {menup}\")\n",
        "elif dia == 2:\n",
        "  if menu == 2:\n",
        "    descmenu = menup * .20\n",
        "    menupt = menup - descmenu\n",
        "    print(f\"El precio total es: {menupt}\")\n",
        "  else:\n",
        "    print(f\"El precio total es: {menup}\")\n",
        "elif dia == 3:\n",
        "  if menu == 3:\n",
        "    descmenu = menup * .15\n",
        "    menupt = menup - descmenu\n",
        "    print(f\"El precio total es: {menupt}\")\n",
        "  else:\n",
        "    print(f\"El precio total es: {menup}\")\n",
        "elif dia == 4:\n",
        "  if menu == 4:\n",
        "    descmenu = menup * .05\n",
        "    menupt = menup - descmenu\n",
        "    print(f\"El precio total es: {menupt}\")\n",
        "  else:\n",
        "    print(f\"El precio total es: {menup}\")\n",
        "elif dia == 5:\n",
        "  if menu == 1:\n",
        "    descmenu = menup * .05\n",
        "    menupt = menup - descmenu\n",
        "    print(f\"El precio total es: {menupt}\")\n",
        "  else:\n",
        "    print(f\"El precio total es: {menup}\")\n",
        "else:\n",
        "  print(f\"El precio total es: {menup}\")\n",
        "\n",
        ""
      ],
      "metadata": {
        "id": "fcIWIrV-HB4e",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "cda6562a-d34d-42c4-f397-373d4f8ebcfe"
      },
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1) Lunes\n",
            "2) Martes\n",
            "3) Miercoles\n",
            "4) Jueves\n",
            "5) Viernes\n",
            "6) Sabado\n",
            "7) Domingo\n",
            "Buen dia, en que dia de la semana de encuentra hoy? Ingrese el numero correspondiente: 1\n",
            "1) Menu del dia\n",
            "2) Menu infantil\n",
            "3) Menu vegetariano\n",
            "4) Menu del chef\n",
            "5) Otro menu\n",
            "Cual menu desea pedir hoy? Ingrese el numero correspondiente:  1\n",
            "Cual es el precio de dicho menu? 200\n",
            "El precio total es: 180.0\n"
          ]
        }
      ]
    }
  ]
}