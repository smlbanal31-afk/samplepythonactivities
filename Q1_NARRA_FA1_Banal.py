{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "toc_visible": true,
      "authorship_tag": "ABX9TyN0m+TdPE4lyia+EQUFBK8g",
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
        "<a href=\"https://colab.research.google.com/github/smlbanal31-afk/samplepythonactivities/blob/main/Q1_NARRA_FA1_Banal.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "LPEK6kXESW_B",
        "outputId": "59fffd2c-e7aa-4c49-d777-d477d86e527e"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter x1: 2\n",
            "Enter y1: 3\n",
            "Enter x2: 7\n",
            "Enter y2: 8\n",
            "7.0710678118654755\n"
          ]
        }
      ],
      "source": [
        "import math\n",
        "\n",
        "#Ask the user for value of each coordinates\n",
        "x1 = float(input(\"Enter x1: \"))\n",
        "y1 = float(input(\"Enter y1: \"))\n",
        "x2 = float(input(\"Enter x2: \"))\n",
        "y2 = float(input(\"Enter y2: \"))\n",
        "\n",
        "diff_x = (x2 - x1)\n",
        "diff_y = (y2 - y1)\n",
        "\n",
        "\n",
        "distance = math.sqrt(pow(diff_x,2) + pow(diff_y,2))\n",
        "#calculates the distance between two points\n",
        "\n",
        "print(distance)\n",
        "#displays the distance\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "ycG7158cekXX"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "fQ26LAKIhGhd"
      }
    }
  ]
}