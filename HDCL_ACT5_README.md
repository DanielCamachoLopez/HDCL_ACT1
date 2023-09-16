{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO6biABiuT+M2VNWfwvjLQZ",
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
        "<a href=\"https://colab.research.google.com/github/DanielCamachoLopez/HDCL_ACT1/blob/main/HDCL_ACT5_README.md\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#ACTIVIDAD 5\n",
        "\n",
        "Nombre: Hector Daniel Camacho Lopez\n",
        "\n",
        "Matricula: 372239\n",
        "\n",
        "Grupo: 432\n",
        "\n",
        "Fecha: 11 de Septiembre del 2023"
      ],
      "metadata": {
        "id": "jVZvaAhsIuGd"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "1.- Programa en Python que genere 40 números aleatorios entre el 0 y 200, desplegar los números y la leyenda de cada número si es par o impar , la cantidad de los números pares e impares así como la suma de los números pares o impares.\n",
        "\n"
      ],
      "metadata": {
        "id": "b__HXLNEQ5th"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "#PARTE 1"
      ],
      "metadata": {
        "id": "qxSUCznXBW1x"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "_NCHWzSyItAZ"
      },
      "outputs": [],
      "source": [
        "\n",
        "import random\n",
        "par = 0\n",
        "impar = 0\n",
        "impares = 0\n",
        "pares = 0\n",
        "for i in range (0,40):\n",
        "  num = random.randint(0,200)\n",
        "  if num%2 == 0:\n",
        "    print(f\"{num} : Es par\")\n",
        "    pares = pares + num\n",
        "    par = par + 1\n",
        "  else:\n",
        "    print(f\"{num} : Es impar\")\n",
        "    impares = impares + num\n",
        "    impar = impar + 1\n",
        "\n",
        "print(f\"La suma de los numeros pares es de: {pares}\")\n",
        "print(f\"La suma de los numeros pares es de: {impares}\")\n",
        "\n"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "2.- Programa en Python que despliegue la tabla de multiplicar de un número dado (número entre el 1 y 20)."
      ],
      "metadata": {
        "id": "8sWIMR-zQ3PB"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from prompt_toolkit.shortcuts.progress_bar.base import E\n",
        "try:\n",
        "  num = int(input(\"Dame el numero de la tabla de multiplicar que deseas visualizar: (Solo numeros del 1 al 20)\"))\n",
        "  if num <= 20:\n",
        "      for i in range (1, 11):\n",
        "        mult = num * i\n",
        "        print(f\"{num} * {i} = {mult}\")\n",
        "  else:\n",
        "    print(\"SOLO numeros del 1 al 20\")\n",
        "except:\n",
        "  print(\"ERROR, digita numero ENTEROS, letras ni caracteres especiales\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "v9-cRmsTRFQ7",
        "outputId": "e8ef631d-6673-438b-fb02-5a30a99619d0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Dame el numero de la tabla de multiplicar que deseas visualizar: (Solo numeros del 1 al 20)20\n",
            "20 * 1 = 20\n",
            "20 * 2 = 40\n",
            "20 * 3 = 60\n",
            "20 * 4 = 80\n",
            "20 * 5 = 100\n",
            "20 * 6 = 120\n",
            "20 * 7 = 140\n",
            "20 * 8 = 160\n",
            "20 * 9 = 180\n",
            "20 * 10 = 200\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "3.- Programa en Python que lea una calificación, las calificación deberá estar en el rango de 0 a 100, si hay un error de captura, mostrar mensaje de error. con la calificación correcta mostrar msg de aprobado reprobado."
      ],
      "metadata": {
        "id": "jtNaqYpXSqjQ"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "try:\n",
        "  calif = int(input(\"Dame la calificacion: \"))\n",
        "  if calif < 0:\n",
        "    raise print(\"Solo numeros POSITIVOS\")\n",
        "  elif calif < 60:\n",
        "    print(f\"REPROBADO con {calif}\")\n",
        "  else:\n",
        "    print(f\"APROBADO con {calif}\")\n",
        "except:\n",
        "  print(\"SOLO numeros ENTEROS del 0 al 100, no letras ni caracteres especiales\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "aq4hj4tySt8J",
        "outputId": "6cf17aee-661e-46c3-b7f8-649520e5a0d7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Dame la calificacion: 60\n",
            "APROBADO con 60\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "4.- Programa en Python que lea n cantidad de números enteros dentro de un rango dado (> 0 ) , el programa deberá terminar cuando el usuario introduzca el número cero. Desplegar la suma de números y la media."
      ],
      "metadata": {
        "id": "n3aJn3xPVrQ7"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "try:\n",
        "\n",
        "  n = int(input(\"Cuantos numeros enteros deseas sumar? (Numero mayor a 0)\"))\n",
        "  print(\"En el proceso de digitar numeros enteros, digita 0 para terminar\")\n",
        "  suma = 0\n",
        "\n",
        "  for i in range (1,n+1):\n",
        "    if n == 0:\n",
        "      print(\"Elegiste terminar el proceso \")\n",
        "      break\n",
        "    else:\n",
        "      num = int(input(f\"Dame el numero {i}: \"))\n",
        "      if num == 0:\n",
        "          print(\"Elegiste terminar el proceso \")\n",
        "          break\n",
        "      suma = suma + num\n",
        "\n",
        "  media = suma / n\n",
        "\n",
        "  print(f\"La suma de todos los numeros enteros es de {suma}\")\n",
        "  print(f\"La media de todos los numeros enteros es de {media}\")\n",
        "\n",
        "except:\n",
        "  print(\"SOLO numeros ENTEROS mayores a 0, no letras ni caracteres especiales\")\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2YGndz73Vv41",
        "outputId": "874d3022-9b7f-4d64-bf81-33cc34eae815"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Cuantos numeros enteros deseas sumar? (Numero mayor a 0)5\n",
            "En el proceso de digitar numeros enteros, digita 0 para terminar\n",
            "Dame el numero 1: 0\n",
            "Elegiste terminar el proceso \n",
            "La suma de todos los numeros enteros es de 0\n",
            "La media de todos los numeros enteros es de 0.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "5.- Programa en Python que sirva para leer el promedio de una materia. donde el usuario tendrá un máximo de 3 oportunidades de cursar la materia, si el promedio es aprobado, felicitarlo y continuar el siguiente semestre, si promedio es reprobado deberá salir mensaje de repetir materia o es baja académica si ha reprobado 3 veces.\n",
        "\n"
      ],
      "metadata": {
        "id": "FZYfPhtP9g86"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "try:\n",
        "  for i in range (0, 3):\n",
        "      prom = int(input(\"Cual es tu promedio en este semestre? (Numeros ENTEROS del 1 al 100)\"))\n",
        "      if prom >= 60:\n",
        "        print(\"Felicidades, tu promedio es aprobatorio y por lo tanto pasas al sigueinte semestre\")\n",
        "        break\n",
        "      elif prom < 60 and i < 2:\n",
        "        print(\"Repetir materia, el promedio no es aprobatorio\")\n",
        "        continue\n",
        "      else:\n",
        "        print(\"Baja academica, has reprobado 3 veces\")\n",
        "except:\n",
        "  print(\"ERROR, digita numeros ENTEROS del 1 al 100, no letras ni carateres especiales\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vjHOL7Wo9juY",
        "outputId": "8168f461-7d47-400a-fd02-7f8ff030e064"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Cual es tu promedio en este semestre? (Numeros ENTEROS del 1 al 100)40\n",
            "Repetir materia, el promedio no es aprobatorio\n",
            "Cual es tu promedio en este semestre? (Numeros ENTEROS del 1 al 100)40\n",
            "Repetir materia, el promedio no es aprobatorio\n",
            "Cual es tu promedio en este semestre? (Numeros ENTEROS del 1 al 100)40\n",
            "Baja academica, has reprobado 3 veces\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#PARTE 2"
      ],
      "metadata": {
        "id": "Hg6mkmvuBRs7"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "1.- Función que lea n cantidad de números hasta que el usuario lo desee, desplegar la suma de los números, media y valor de los números mayores y menores."
      ],
      "metadata": {
        "id": "S44eVu5XBKco"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "try:\n",
        "  def nums ():\n",
        "    mayor = 0\n",
        "    suma = 0\n",
        "    menor = 0\n",
        "    num = int(input(\"Cuantos numeros deseas digitar? \"))\n",
        "    for i in range (1, num+1):\n",
        "      n = int(input(f\"Dame el numero {i}. Digita 0 si quieres terminar el proceso: \"))\n",
        "\n",
        "      if i == 1:\n",
        "        menor = n\n",
        "\n",
        "      if n == 0:\n",
        "         print(\"Elegiste terminar el proceso\")\n",
        "         break\n",
        "\n",
        "      if n > 0:\n",
        "         suma = suma + n\n",
        "\n",
        "      if n > mayor:\n",
        "           mayor = n\n",
        "      elif n < menor:\n",
        "           menor = n\n",
        "\n",
        "    media = suma / (num)\n",
        "    print(f\"El numero mayor es: {mayor} \")\n",
        "    print(f\"El numero menor es: {menor}\")\n",
        "    print(f\"La suma de todos los numeros es de: {suma}\")\n",
        "    print(f\"La media de los numeros es de: {media}\")\n",
        "\n",
        "  nums()\n",
        "\n",
        "except:\n",
        "     print(\"ERROR, solo digita numeros, no letras ni caracteres especiales\")\n",
        "\n"
      ],
      "metadata": {
        "id": "6ZGBWfWPBNu-",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "9ee449a2-0bc2-4d0c-f316-b3e9832d54cc"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Cuantos numeros deseas digitar? \n",
            "None4\n",
            "Dame el numero 1. Digita 0 si quieres terminar el proceso: 7\n",
            "Dame el numero 2. Digita 0 si quieres terminar el proceso: 8\n",
            "Dame el numero 3. Digita 0 si quieres terminar el proceso: 6\n",
            "Dame el numero 4. Digita 0 si quieres terminar el proceso: 2\n",
            "El numero mayor es: 8 \n",
            "El numero menor es: 2\n",
            "La suma de todos los numeros es de: 23\n",
            "La media de los numeros es de: 5.75\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "2.- Función que genere 15 números impares entre 10 y 60 o máximo de 25 números. desplegar la media de los pares y media de impares.\n",
        "\n"
      ],
      "metadata": {
        "id": "YFOueMU2-Csb"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "try:\n",
        "  def impares():\n",
        "\n",
        "    contpar = 0\n",
        "    contimpar = 0\n",
        "    impar = 0\n",
        "    par = 0\n",
        "    nums = int(input(\"De entre el 10 y 60, cuantos numeros impares deseas imprimir?: \"))\n",
        "    print(\"Digita un numero entre 10 y 60: \")\n",
        "\n",
        "    if nums < 10 or nums > 60:\n",
        "      print(\"ERROR, te dije que SOLO digites numeros entre 10 y 60 >:(\")\n",
        "\n",
        "    else:\n",
        "      for i in range (11, nums, 2):\n",
        "        print(i)\n",
        "        impar = impar + i\n",
        "        contimpar = contimpar + 1\n",
        "\n",
        "      for i in range (10, nums, 2):\n",
        "        par = par + i\n",
        "        contpar = contpar + 1\n",
        "\n",
        "      mediapar = par / contpar\n",
        "      mediaimpar = impar / contimpar\n",
        "      print(f\"La media de los numeros impares es de: {mediaimpar}\")\n",
        "      print(f\"La media de los numeros pares es de: {mediapar}\")\n",
        "\n",
        "\n",
        "  impares()\n",
        "\n",
        "except:\n",
        "  print(\"ERROR, digita solo numeros enteros, no letras ni caracteres especiales\")"
      ],
      "metadata": {
        "id": "AwY5mq6wMfbc",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "a251a8b2-f4e7-49e8-c2a5-8dfeb07783d9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "De entre el 10 y 60, cuantos numeros impares deseas imprimir?: \n",
            "None20\n",
            "Digita un numero entre 10 y 60: \n",
            "11\n",
            "13\n",
            "15\n",
            "17\n",
            "19\n",
            "La media de los numeros impares es de: 15.0\n",
            "La media de los numeros pares es de: 14.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "3.- Función que sirva para leer y validar un número dentro de un rango dado por el usuario. repetir esta acción hasta que el usuario lo desee, desplegar cantidad de números y promedio de los números."
      ],
      "metadata": {
        "id": "pf4lhgK2JMLG"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def numero(cadena):\n",
        "  try:\n",
        "    int(cadena)\n",
        "    return True\n",
        "  except ValueError:\n",
        "    return False\n",
        "\n",
        "\n",
        "\n",
        "try:\n",
        "  suma = 0\n",
        "  rangi = int(input(\"Desde que numero empieza el rango de numeros que deseas? \"))\n",
        "  rangf = int(input(\"Cual es el numero limite para el rango de numero que deseas? \"))\n",
        "  num = int(input(\"Cuantos numeros deseas validar? \"))\n",
        "  for i in range (1, num+1):\n",
        "      print(f\"Dame el numero {i} a validar \")\n",
        "      n = int(input(f\"El numero debe estar entre {rangi} y {rangf}: \"))\n",
        "\n",
        "      if n < rangi and n > rangf:\n",
        "        print(f\"ERROR, el numero debe estar entre {rangi} y {rangf}: \")\n",
        "\n",
        "      else:\n",
        "        print(n)\n",
        "        suma = suma + n\n",
        "\n",
        "      if numero(n):\n",
        "        print(\"Valor valido\")\n",
        "      else:\n",
        "        print(\"Valor NO valido\")\n",
        "\n",
        "\n",
        "  prom = suma / i\n",
        "  print(f\"El promedio por todos los numeros es de: {prom}\")\n",
        "\n",
        "except:\n",
        "  print(\"Numero no validado\")\n",
        "  prom = suma / (i-1)\n",
        "  print(f\"El promedio por todos los numeros es de: {prom}\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7InXWFtuKq_k",
        "outputId": "5f7e7064-649e-41fd-f2e1-7d44a6ed668f"
      },
      "execution_count": 55,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Desde que numero empieza el rango de numeros que deseas? 1\n",
            "Cual es el numero limite para el rango de numero que deseas? 100\n",
            "Cuantos numeros deseas validar? 3\n",
            "Dame el numero 1 a validar \n",
            "El numero debe estar entre 1 y 100: 3\n",
            "3\n",
            "Valor valido\n",
            "Dame el numero 2 a validar \n",
            "El numero debe estar entre 1 y 100: 3\n",
            "3\n",
            "Valor valido\n",
            "Dame el numero 3 a validar \n",
            "El numero debe estar entre 1 y 100: 3\n",
            "3\n",
            "Valor valido\n",
            "El promedio por todos los numeros es de: 3.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "4.- Función que reciba como parámetro los valores para el área de un triángulo y retorne su resultado"
      ],
      "metadata": {
        "id": "clxeM5cpYgg2"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def triangulo(b,h):\n",
        "    area = (b * h) / 2\n",
        "    print(f\"El area del triangulo es de: {area}\")\n",
        "triangulo(5, 40)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HP8IH2oXaHht",
        "outputId": "04891aa9-3bad-4b40-a110-fec57ba6dd61"
      },
      "execution_count": 56,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "El area del triangulo es de: 100.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "5.- Función que sirva para validar un número dentro de un rango dado."
      ],
      "metadata": {
        "id": "8RPIA64kb-IE"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def validar(cadena):\n",
        "  try:\n",
        "    int(cadena)\n",
        "    return True\n",
        "  except ValueError:\n",
        "    return False\n",
        "rangi = int(input(\"Dame el numero donde inicia tu rango de numeros:\"))\n",
        "rangf = int(input(\"Dame el numero donde termina tu rango de numeros: \"))\n",
        "numero = int(input(\"Dame un numero: \"))\n",
        "\n",
        "if numero >= rangi and numero <= rangf:\n",
        "    if validar(numero):\n",
        "      print(\"Has digitado un valor valido\")\n",
        "    else:\n",
        "      print(\"Has digitado un valor invalido\")\n",
        "else:\n",
        "  print(\"ERROR, SOLO numero que se encuentre en el rango establecido\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bII2S2ShcNc5",
        "outputId": "1cc03f0b-58b9-49e1-81fb-168f3a01992e"
      },
      "execution_count": 65,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Dame el numero donde inicia tu rango de numeros:1\n",
            "Dame el numero donde termina tu rango de numeros: 100\n",
            "Dame un numero: 67\n",
            "Has digitado un valor valido\n"
          ]
        }
      ]
    }
  ]
}