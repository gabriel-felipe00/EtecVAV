"""
Projeto: Diário de Classe com Pandas
Descrição:
Sistema simples para controle de alunos, notas e frequência.

Requisitos:
pip install pandas openpyxl
"""

import pandas as pd

class DiarioClasse:
    def __init__(self):
        self.alunos = pd.DataFrame(columns=[
            "Matricula",
            "Nome",
            "Turma",
            "Nota1",
            "Nota2",
            "Frequencia"
        ])

    # -----------------------------
    # Adicionar aluno
    # -----------------------------
    def adicionar_aluno(self, matricula, nome, turma,
                         nota1=0, nota2=0, frequencia=0):

        novo_aluno = {
            "Matricula": matricula,
            "Nome": nome,
            "Turma": turma,
            "Nota1": nota1,
            "Nota2": nota2,
            "Frequencia": frequencia
        }

        self.alunos = pd.concat(
            [self.alunos, pd.DataFrame([novo_aluno])],
            ignore_index=True
        )

        print(f"Aluno {nome} adicionado com sucesso!")

    # -----------------------------
    # Calcular média
    # -----------------------------
    def calcular_medias(self):
        self.alunos["Media"] = (
            self.alunos["Nota1"] +
            self.alunos["Nota2"]
        ) / 2

    # -----------------------------
    # Verificar situação
    # -----------------------------
    def verificar_situacao(self):

        self.calcular_medias()

        def situacao(linha):
            if linha["Frequencia"] < 75:
                return "Reprovado por Falta"

            elif linha["Media"] >= 7:
                return "Aprovado"

            elif linha["Media"] >= 5:
                return "Recuperação"

            else:
                return "Reprovado"

        self.alunos["Situacao"] = self.alunos.apply(
            situacao,
            axis=1
        )

    # -----------------------------
    # Mostrar diário
    # -----------------------------
    def mostrar_diario(self):

        self.verificar_situacao()

        print("\n===== DIÁRIO DE CLASSE =====\n")
        print(self.alunos)

    # -----------------------------
    # Buscar aluno
    # -----------------------------
    def buscar_aluno(self, nome):

        resultado = self.alunos[
            self.alunos["Nome"].str.contains(nome, case=False)
        ]

        return resultado

    # -----------------------------
    # Salvar Excel
    # -----------------------------
    def salvar_excel(self, arquivo="diario_classe.xlsx"):

        self.verificar_situacao()

        self.alunos.to_excel(arquivo, index=False)

        print(f"Arquivo salvo como {arquivo}")

    # -----------------------------
    # Estatísticas da turma
    # -----------------------------
    def estatisticas(self):

        self.verificar_situacao()

        print("\n===== ESTATÍSTICAS =====")

        print(f"Total de alunos: {len(self.alunos)}")

        print(
            f"Média geral: "
            f"{self.alunos['Media'].mean():.2f}"
        )

        print("\nSituações:")

        print(self.alunos["Situacao"].value_counts())


# ==================================================
# EXEMPLO DE USO
# ==================================================

if __name__ == "__main__":

    diario = DiarioClasse()

    # Adicionando alunos
    diario.adicionar_aluno(
        1,
        "João Silva",
        "1A",
        8,
        7,
        90
    )

    diario.adicionar_aluno(
        2,
        "Maria Souza",
        "1A",
        5,
        6,
        80
    )

    diario.adicionar_aluno(
        3,
        "Pedro Santos",
        "1A",
        3,
        4,
        60
    )

    # Mostrar diário
    diario.mostrar_diario()

    # Estatísticas
    diario.estatisticas()

    # Buscar aluno
    print("\n===== BUSCA =====")
    print(diario.buscar_aluno("Maria"))

    # Salvar Excel
    diario.salvar_excel()